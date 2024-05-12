import cv2
import numpy as np
from facial_recognition.models import FacialRecognitionModel

def recognize_faces(model_name, image_path, video_path=None, output_path=None):
    """
    Recognizefaces in an input image or video using a facial recognition model.

    Args:
        model_name (str): Name of the facial recognition model to be used.
        image_path (str): Path to the input image file.
        video_path (str): Path to the input video file. Default is None.
        output_path (str): Path to the output video file. Default is None.

    Returns:
        None
    """
    model = FacialRecognitionModel(model_name)
    if video_path is None:
        image = cv2.imread(image_path)
        faces = model.detect_faces(image)
        for face in faces:
            x, y, w, h = face['bbox']
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, face['identity'], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        cv2.imshow('Face Recognition', image)
        cv2.waitKey(0)
    else:
        video = cv2.VideoCapture(video_path)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        fps = video.get(cv2.CAP_PROP_FPS)
        if output_path is None:
            output_path = "output.mp4"
        output_video = cv2.VideoWriter(output_path, fourcc, fps, (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))))
        while True:
            ret, frame = video.read()
            if not ret:
                break
            faces = model.detect_faces(frame)
            for face in faces:
                x, y, w, h = face['bbox']
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, face['identity'], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            output_video.write(frame)
            cv2.imshow('Face Recognition', frame)
            cv2.waitKey(1)
        video.release()
        output_video.release()
