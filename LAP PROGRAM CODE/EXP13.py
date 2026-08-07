import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]

    source = np.float32([
        [0, 0],
        [width - 1, 0],
        [width - 1, height - 1],
        [0, height - 1]
    ])

    destination = np.float32([
        [80, 50],
        [width - 100, 20],
        [width - 40, height - 50],
        [40, height - 20]
    ])

    matrix = cv2.getPerspectiveTransform(source, destination)
    transformed = cv2.warpPerspective(frame, matrix, (width, height))

    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Video", transformed)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
