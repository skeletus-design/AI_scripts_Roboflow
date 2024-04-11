from roboflow import Roboflow
import supervision as sv
import cv2
import numpy as np
import tempfile

rf = Roboflow(api_key="4vZMVNiftzxorjydoja6")
project = rf.workspace().project("rat-detection-3fcgx")
model = project.version(2).model

# Открываем видеофайл
video_capture = cv2.VideoCapture("test_2.mp4")

# Получаем информацию о видеопотоке
fps = int(video_capture.get(cv2.CAP_PROP_FPS))
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Создаем объект для записи видео
output_video = cv2.VideoWriter("annotated_video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

label_annotator = sv.LabelAnnotator()
bounding_box_annotator = sv.BoxAnnotator()

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Создаем временный файл для сохранения кадра
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
        temp_filename = temp_file.name
        cv2.imwrite(temp_filename, frame)

        # Предсказываем на временном файле
        result = model.predict(temp_filename, confidence=40, overlap=30).json()
        labels = [item["class"] for item in result["predictions"]]
        detections = sv.Detections.from_roboflow(result)

        annotated_frame = bounding_box_annotator.annotate(scene=frame, detections=detections)
        annotated_frame = label_annotator.annotate(scene=annotated_frame, detections=detections, labels=labels)

        output_video.write(annotated_frame)

# Освобождаем ресурсы
video_capture.release()
output_video.release()
