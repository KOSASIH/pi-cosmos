import cv2

def extract_frames(video_path, output_path, start_frame=0, end_frame=-1, step=1):
    """
    Extract frames from an input video and save them to an output directory.

    Args:
        video_path (str): Path to the input video file.
        output_path (str): Path to the output directory where the extracted frames will be saved.
        start_frame (int): Index of the first frame to be extracted. Default is 0.
        end_frame (int): Index of the last frame to be extracted. Default is -1 (extract all frames).
        step (int): Step size between frames to be extracted. Default is 1.

    Returns:
        None
    """
    video = cv2.VideoCapture(video_path)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    if end_frame == -1:
        end_frame = total_frames
    if end_frame > total_frames:
        end_frame = total_frames
    for i in range(start_frame, end_frame, step):
        video.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = video.read()
        if not ret:
            break
        output_frame_path = os.path.join(output_path, f"frame_{i:06d}.jpg")
        cv2.imwrite(output_frame_path, frame)
          video.release()
