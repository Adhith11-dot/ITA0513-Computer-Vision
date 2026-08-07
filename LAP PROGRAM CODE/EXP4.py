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
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(image, kernel, iterations=1)

cv2.imshow("Original", image)
cv2.imshow("Dilated", dilated)
cv2.imwrite("04_dilated.jpg", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
