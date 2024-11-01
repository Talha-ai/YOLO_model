from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.predict(source="airport.mp4", show=True, conf=0.4)  
