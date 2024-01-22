import cv2
import os
from datetime import datetime

def canny_edge_detection(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    return blurred, edges

def save_edge_image(edges, folder):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    filename = os.path.join(folder, f"captured_image_{timestamp}.png")
    cv2.imwrite(filename, edges)
    print(f"Edge image saved: {filename}")

def main():
    cap = cv2.VideoCapture(0)

    # Create a folder to store edge images
    folder = "edge_images"
    os.makedirs(folder, exist_ok=True)

    while True:
        ret, frame = cap.read()
        if not ret:
            print('Image not captured')
            break

        blurred, edges = canny_edge_detection(frame)

        cv2.imshow("Original", frame)
        cv2.imshow("Blurred", blurred)
        cv2.imshow("Edges", edges)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord(' '):  # Press spacebar to capture and save the image
            save_edge_image(edges, folder)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
