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

source = np.float64([
    [0, 0],
    [width - 1, 0],
    [width - 1, height - 1],
    [0, height - 1]
])

destination = np.float64([
    [80, 50],
    [width - 100, 30],
    [width - 50, height - 60],
    [40, height - 20]
])

A = []

for (x, y), (u, v) in zip(source, destination):
    A.append([-x, -y, -1, 0, 0, 0, x*u, y*u, u])
    A.append([0, 0, 0, -x, -y, -1, x*v, y*v, v])

A = np.array(A)
_, _, Vt = np.linalg.svd(A)
H = Vt[-1].reshape(3, 3)
H = H / H[2, 2]

transformed = cv2.warpPerspective(image, H, (width, height))

print("DLT Homography Matrix:")
print(H)

cv2.imshow("Original", image)
cv2.imshow("DLT Transformation", transformed)
cv2.imwrite("15_dlt.jpg", transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
