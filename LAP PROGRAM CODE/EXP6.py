import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
path = filedialog.askopenfilename(
    title="Select a video",
    filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv *.wmv")]
)
root.destroy()

if not path:
    raise SystemExit("No video selected.")

cap = cv2.VideoCapture(path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(frame, (7, 7), 0)
    edges = cv2.Canny(gray, 100, 200)

    cv2.imshow("Original", frame)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("Blurred", blur)
    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
