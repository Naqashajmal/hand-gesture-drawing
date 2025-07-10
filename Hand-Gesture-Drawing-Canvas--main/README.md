# Gesture-Based Virtual Drawing Canvas 🎨  

A real-time **hand gesture-based drawing system** using **OpenCV and Mediapipe**. This project enables users to draw on a virtual canvas by tracking their **index finger** using a webcam.  

---

## 🚀 Features  

✅ **Real-time Hand Tracking** – Uses AI-powered Mediapipe Hands for precise finger detection.  
✅ **Virtual Drawing Canvas** – Draw using your index finger as a pen.  
✅ **Live Webcam Feed** – View your hand movements alongside the drawing.  
✅ **Smooth and Interactive** – Tracks finger motion seamlessly for fluid drawing.  
✅ **Simple & Lightweight** – Runs efficiently on standard webcams.  

---

## 🛠️ Technologies Used  

- **Python** 🐍  
- **OpenCV** 📷 (Computer Vision Library)  
- **Mediapipe** ✋ (Hand Tracking API)  
- **NumPy** 🔢 (Array Operations)  

---

## 📌 How It Works  

1️⃣ The webcam captures live video.  
2️⃣ **Mediapipe Hands** detects the landmarks of your hand.  
3️⃣ The tip of the **index finger (landmark 8)** is tracked.  
4️⃣ The movement of the index finger is stored as drawing points.  
5️⃣ The virtual canvas displays the drawings separately from the webcam feed.  

---

## 🖥️ Installation  

Make sure you have **Python 3.7+** installed. Then, install the required libraries:  

```bash
pip install opencv-python mediapipe numpy

Clone this repository and run the script:

git clone https://github.com/yourusername/Gesture-Drawing-Canvas.git
cd Gesture-Drawing-Canvas
python main.py

🖊️ Usage
Move your index finger to start drawing.
The system tracks your finger and creates strokes on the canvas.
Press 'Q' to exit.
🔮 Future Enhancements
✔️ Eraser Mode (Detect finger pinch to erase)
✔️ Color Selection (Change colors using gestures)
✔️ Line Thickness Control (Adjust line width dynamically)
✔️ Gesture-Based UI for Additional Controls

📢 Contributing
Feel free to fork this project, create a pull request, or suggest improvements!

🔗 LinkedIn: Muhammad Hassaan

This project is licensed under the MIT License.
