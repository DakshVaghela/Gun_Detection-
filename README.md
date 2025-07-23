📌 Gun Detection using Haar Cascade and OpenCV
This project is a real-time gun detection system using OpenCV and a Haar Cascade classifier. It accesses the webcam, processes video frames, and detects the presence of guns using a pre-trained cascade model.

📷 Features
Real-time webcam feed

Haar Cascade-based gun detection

Visual alert overlay: GUNS DETECTED or No guns

Timestamp overlay

Frame resizing for performance

Console log when gun detection state changes

🛠️ Requirements
Python 3.x

OpenCV

imutils

Install dependencies:

bash
Copy
Edit
pip install opencv-python imutils
🚀 How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/gun-detector.git
cd gun-detector
Ensure the file cascade.xml (your trained gun cascade file) is present in the repo directory.

Run the script:

bash
Copy
Edit
python gun_detector.py
Press q to quit the webcam window.

🧠 Code Overview
cv2.CascadeClassifier: Loads the pre-trained classifier.

cv2.VideoCapture(0): Opens the webcam.

detectMultiScale: Detects objects in grayscale frames.

Alerts and rectangles are drawn when a gun is found.

📝 Notes
Make sure your cascade.xml file is well-trained and correctly detects guns (you can train your own with OpenCV if needed).

Accuracy depends on camera quality, lighting, and the model used.

For better performance, use a GPU-accelerated model like YOLOv5 or SSD in production systems.

