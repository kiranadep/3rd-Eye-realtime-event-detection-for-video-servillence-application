import cv2
import torch
from datetime import datetime
import time
import os
import pyttsx3
import json
from pushbullet import Pushbullet
import pathlib
pathlib.PosixPath = pathlib.WindowsPath

count = 0
recording = False
fps = 4  
desired_fps = 30

class Stream:
    def __init__(self):
        self.model = None 
        with open("D:/courses/main_project/flask/intents.json", 'r') as json_data:
            self.intents = json.load(json_data)
        self.load_model()
        self.processing()
    
    def say(self, text):
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 50)
        print("\nA.I:", text)
        engine.say(text=text)
        engine.runAndWait()
        print("\n")

    def load_model(self):
        if self.model is None:
            self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='D:\courses\web\\application\\third-eye-app\\best.pt')

    def processing(self,rtsp_url=None):
        global recording, count, fps

        cap = cv2.VideoCapture(0)



        if not cap.isOpened():
            print("Error: Failed to open camera")
            return

        ret, frame = cap.read()
        if ret:
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            print("FPS:", fps)
            cap.set(cv2.CAP_PROP_FPS, desired_fps)  

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        video_writer = None 
        output_file = None  

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame, (width, height))
            results = self.model(frame)
            cv2.putText(frame, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.6,
                        (0, 255, 0), 1)
            predictions = results.xyxy[0].cpu().numpy()

            for pred in predictions:
                x1, y1, x2, y2, confidence, class_index = pred
                class_label = self.model.names[int(class_index)]

                if (class_label == 'fire' or class_label == 'blast') and confidence > 0.5:

                    output = 'Fire has been Detected'
                    start_recording_time = time.time()
                    recording = True
                
                    API_KEY = "***********************" #add push bullet API
                    txt = "Fire Detected"
                    pb = Pushbullet(API_KEY)
                    push = pb.push_note('from 3RD EYE',txt)
                    try:
                        currentDate = datetime.now().strftime("%Y-%m-%d")
                        path = fr'D:/courses/main_project/saved_videos/{currentDate}'
                        os.makedirs(path, exist_ok=True)
                        if video_writer is None:
                            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                            output_file = f'{path}/{datetime.now().strftime("%H:%M:%S")}.mp4'
                            video_writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
                    except Exception as e:
                        print("Error:", e)
                        continue

                if class_label == 'smoke' and confidence > 0.5:
                    count += 1
                    if count == 5:

                        self.say("Smoke has been Detected")
                        start_recording_time = time.time()
                        recording = True

                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, f'{class_label}: {confidence:.2f}', (int(x1), int(y1) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            if recording and video_writer is not None: 
                video_writer.write(frame)

                if time.time() - start_recording_time >= 10:  
                    recording = False
                    video_writer.release()
                    print("Recording stopped.")
                    video_writer = None 
                    output_file = None  

            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

