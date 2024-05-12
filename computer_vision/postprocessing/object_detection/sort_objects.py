import cv2
import numpy as np
from object_detection.yolov5 import detect_objects

# Load image
image = cv2.imread('image.jpg')

# Detect objects in image
objects = detect_objects(image)

# Filter objects based on confidence score and area
filtered_objects = filter_objects(objects, min_confidence=0.7, min_area=500)

# Sort objects based on confidence score
sorted_objects = sort_objects(filtered_objects, sort_by='confidence', reverse=True)

# Display sorted objects
for obj in sorted_objects:
    x, y, w, h = obj['bbox']
    label = obj['class']
    confidence = obj['confidence']
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, f'{label} {confidence:.2f}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

# Display image
cv2.imshow('Objects', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
