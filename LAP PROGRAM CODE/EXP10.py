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

matrix = np.float32([[1, 0, 100], [0, 1, 50]])
translated = cv2.warpAffine(image, matrix, (width, height))

cv2.imshow("Original", image)
cv2.imshow("Translated", translated)
cv2.imwrite("10_translated.jpg", translated)
cv2.waitKey(0)
cv2.destroyAllWindows()
