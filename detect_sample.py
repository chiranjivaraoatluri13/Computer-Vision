from ultralytics import YOLO
model = YOLO('yolov8s.pt')
results = model('your_image.jpg')
results[0].show()
results[0].save('output')
