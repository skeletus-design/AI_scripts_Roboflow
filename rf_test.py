from roboflow import Roboflow
import supervision as sv
import cv2

rf = Roboflow(api_key="4vZMVNiftzxorjydoja6")
project = rf.workspace().project("rat-detection-3fcgx")
model = project.version(2).model

result = model.predict("cat.jpg", confidence=40, overlap=30).json()

labels = [item["class"] for item in result["predictions"]]

detections = sv.Detections.from_roboflow(result)

label_annotator = sv.LabelAnnotator()
bounding_box_annotator = sv.BoxAnnotator()

image = cv2.imread("cat.jpg")

annotated_image = bounding_box_annotator.annotate(scene=image, detections=detections)
annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections, labels=labels)

# Сохранение обработанного изображения
cv2.imwrite("annotated_cat.jpg", annotated_image)
