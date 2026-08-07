import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp")]
)
root.destroy()

if not path:
    raise SystemExit("No image selected.")

image = cv2.imread(path)
if image is None:
    raise SystemExit("Unable to read the selected image.")

image = cv2.imread("input.jpg")
height, width = image.shape[:2]

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
transformed = cv2.warpPerspective(image, matrix, (width, height))

cv2.imshow("Original", image)
cv2.imshow("Perspective Transformation", transformed)
cv2.imwrite("12_perspective.jpg", transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
