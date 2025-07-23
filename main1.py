import cv2
import imutils
import datetime

CASCADE_PATH = 'cascade.xml'

# Load cascade and verify
Gun_cascade = cv2.CascadeClassifier(CASCADE_PATH)
if Gun_cascade.empty():
    raise IOError(f"Could not load cascade file: {CASCADE_PATH}")

# Open webcam (CAP_DSHOW can help on some Windows setups)
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not camera.isOpened():
    raise IOError("Could not access webcam (index 0).")

last_state = None  # track detection state so we don't spam prints

try:
    while True:
        ret, frame = camera.read()
        if not ret or frame is None:
            print("Failed to grab frame from camera; exiting.")
            break

        # Resize for speed/consistency
        frame = imutils.resize(frame, width=500)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        guns = Gun_cascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(100, 100)
        )

        gun_found = len(guns) > 0

        # Draw detections
        for (x, y, w, h) in guns:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Overlay status text + timestamp
        status_text = "GUNS DETECTED" if gun_found else "No guns"
        color = (0, 0, 255) if gun_found else (0, 255, 0)
        cv2.putText(frame, status_text, (10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame, timestamp, (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

        cv2.imshow("Security Feed", frame)

        # Print only when state changes
        if gun_found != last_state:
            print("GUNS DETECTED!" if gun_found else "guns don't")
            last_state = gun_found

        # Exit on 'q'
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break

finally:
    camera.release()
    cv2.destroyAllWindows()
