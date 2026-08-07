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

kernel = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
], dtype=np.float32)

laplacian = cv2.filter2D(gray, cv2.CV_32F, kernel)
sharpened = cv2.convertScaleAbs(gray.astype(np.float32) - laplacian)

cv2.imshow("Original", image)
cv2.imshow("Sharpened", sharpened)
cv2.imwrite("20_laplacian_negative_center.jpg", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
