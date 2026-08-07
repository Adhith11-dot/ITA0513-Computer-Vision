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
center = (width // 2, height // 2)

clockwise_matrix = cv2.getRotationMatrix2D(center, -45, 1.0)
counter_clockwise_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

clockwise = cv2.warpAffine(image, clockwise_matrix, (width, height))
counter_clockwise = cv2.warpAffine(image, counter_clockwise_matrix, (width, height))

cv2.imshow("Original", image)
cv2.imshow("Clockwise", clockwise)
cv2.imshow("Counter Clockwise", counter_clockwise)
cv2.imwrite("09_clockwise.jpg", clockwise)
cv2.imwrite("09_counter_clockwise.jpg", counter_clockwise)
cv2.waitKey(0)
cv2.destroyAllWindows()
