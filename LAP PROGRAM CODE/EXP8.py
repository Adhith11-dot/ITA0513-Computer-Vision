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
bigger = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow("Original", image)
cv2.imshow("Bigger", bigger)
cv2.imshow("Smaller", smaller)
cv2.imwrite("08_bigger.jpg", bigger)
cv2.imwrite("08_smaller.jpg", smaller)
cv2.waitKey(0)
cv2.destroyAllWindows()
