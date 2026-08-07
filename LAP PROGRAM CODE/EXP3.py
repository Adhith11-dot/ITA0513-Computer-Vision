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
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
outline = cv2.Canny(gray, 100, 200)

cv2.imshow("Original", image)
cv2.imshow("Outline", outline)
cv2.imwrite("03_canny_outline.jpg", outline)
cv2.waitKey(0)
cv2.destroyAllWindows()
