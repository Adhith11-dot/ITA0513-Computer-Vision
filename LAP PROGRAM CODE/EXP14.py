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
    [width - 100, 30],
    [width - 50, height - 60],
    [40, height - 20]
])

homography, status = cv2.findHomography(source, destination)
transformed = cv2.warpPerspective(image, homography, (width, height))

print("Homography Matrix:")
print(homography)

cv2.imshow("Original", image)
cv2.imshow("Homography Transformation", transformed)
cv2.imwrite("14_homography.jpg", transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
