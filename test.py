import pixellib
from pixellib.instance import custom_segmentation

segment_image = custom_segmentation()
segment_image.inferConfig(num_classes= 2, class_names= ["BG", "butterfly", "squirrel"])
segment_image.load_model("mask_rcnn_coco.h5")
segment_image.segmentImage("car.jpg", show_bboxes=True, output_image_name="sample_out.jpg")