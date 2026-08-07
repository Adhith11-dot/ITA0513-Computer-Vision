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

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

gradient = cv2.magnitude(sobel_x, sobel_y)
gradient = cv2.normalize(gradient, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

mask = cv2.GaussianBlur(gradient, (5, 5), 0)
sharpened = cv2.addWeighted(gray, 1.0, mask, 1.0, 0)

cv2.imshow("Original", image)
cv2.imshow("Gradient Masking", sharpened)
cv2.imwrite("25_gradient_masking.jpg", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
