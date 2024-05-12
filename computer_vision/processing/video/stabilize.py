import cv2
import numpy as np

def stabilize(video_path, output_path):
    """
    Stabilize an input video using optical flow.

    Args:
        video_path (str): Path to the input video file.
        output_path (str): Path to the output video file.

    Returns:
        None
    """
    video = cv2.VideoCapture(video_path)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = video.get(cv2.CAP_PROP_FPS)
    output_video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    prev_frame = None
    while True:
        ret, frame = video.read()
        if not ret:
            break
        if prev_frame is None:
            prev_frame = frame
            continue
        gray_prev = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
        gray_cur = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(gray_prev, gray_cur, None)
        mag, ang = cv2.cartToPolar(flow[:, :, 0], flow[:, :, 1])
        mag_thresh = 5
        ang_thresh = 20
        mask = (mag > mag_thresh) & (ang < ang_thresh)
        flow[mask == False] = 0
        flow_x, flow_y = flow[:, :, 0], flow[:, :, 1]
        flow_x = cv2.GaussianBlur(flow_x, (15, 15), 0)
        flow_y = cv2.GaussianBlur(flow_y, (15, 15), 0)
        flow_mag, flow_ang = cv2.cartToPolar(flow_x, flow_y)
        flow_mag_thresh = 5
        flow_ang_thresh = 20
        flow_mask = (flow_mag > flow_mag_thresh) & (flow_ang < flow_ang_thresh)
        flow[flow_mask == False] = 0
        flow_x[flow_mask == False] = 0
        flow_y[flow_mask == False] =0
        prev_frame = cv2.add(prev_frame, cv2.merge([flow_x, flow_y, np.zeros_like(flow_x)]))
        prev_frame = np.clip(prev_frame, 0, 255).astype(np.uint8)
        output_video.write(prev_frame)
    video.release()
    output_video.release()
