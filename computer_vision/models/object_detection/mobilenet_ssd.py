import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder

# Load the label map data (for translating label indices to product names)
label_map_path = 'path/to/label_map.pbtxt'
label_map = label_map_util.load_labelmap(label_map_path)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=100, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Load the model
model_path = 'path/to/model.pb'
model = model_builder.build(model_config=tf.compat.as_str(model_path), is_training=False)

# Restore the checkpoint
checkpoint = tf.compat.as_str(model_path)
restorer = tf.train.Saver()
restorer.restore(tf.compat.v1.global_variables_initializer(), checkpoint)

# Create a graph input tensor
image_tensor = tf.compat.v1.get_default_graph().get_tensor_by_name('image_tensor:0')

# Create a graph output tensor
detections_tensor = tf.compat.v1.get_default_graph().get_tensor_by_name('detection_boxes:0')

# Define a function for running inference
def run_inference_for_single_image(model, image):
    image = np.asarray(image)
    # The input needs to be a tensor
    image_tensor = tf.convert_to_tensor(image)
    # The model expects a batch of images, so add an axis with `tf.newaxis`.
    input_tensor = image_tensor[tf.newaxis,...]

    # Run inference
    output_dict = model(input_tensor)

    return output_dict['detection_boxes']

# Define a function for visualizing detections
def visualize_detections(image, detections):
    image = viz_utils.visualize_boxes_and_labels_on_image_array(
            image,
            detections['detection_boxes'][0].numpy(),
            detections['detection_classes'][0].numpy().astype(np.int32),
            detections['detection_scores'][0].numpy(),
            category_index,
            use_normalized_coordinates=True,
            max_boxes_to_draw=200,
            min_score_thresh=.30,
            agnostic_mode=False)

    return image

# Load an image
image_np = load_image_into_numpy_array('path/to/image.jpg')

# Run inference
detections = run_inference_for_single_image(model, image_np)

# Visualize detections
image_np_with_detections = visualize_detections(image_np, detections)

# Display the image
plt.figure()
plt.imshow(image_np_with_detections)
plt.show()
