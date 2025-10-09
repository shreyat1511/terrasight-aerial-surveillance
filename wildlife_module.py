import cv2
import numpy as np

# --- YOLO CONFIGURATION ---
CONFIDENCE_THRESHOLD = 0.1
NMS_THRESHOLD = 0.6
# These files must be downloaded and placed in your project directory
YOLO_CFG = 'yolov3-tiny.cfg'
YOLO_WEIGHTS = 'yolov3-tiny.weights'
COCO_NAMES = 'coco.names'

# Load the network model
net = cv2.dnn.readNetFromDarknet(YOLO_CFG, YOLO_WEIGHTS)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# Load class names
with open(COCO_NAMES, 'r') as f:
    classes = [line.strip() for line in f.readlines()]
COLORS = np.random.uniform(0, 255, size=(len(classes), 3),)

# Function to get the output layer names
def get_output_layers(net):
    layer_names = net.getLayerNames()
    return [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

def run_wildlife_detection(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Get frame dimensions
        height, width = frame.shape[:2]
        
        # Prepare the frame for the neural network (create a blob)
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        
        # Run the forward pass to get detections
        outs = net.forward(get_output_layers(net))

        class_ids = []
        confidences = []
        boxes = []

        # Process the raw output (detections)
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > CONFIDENCE_THRESHOLD:
                    # YOLO boxes are normalized to 0-1 and centered
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    
                    # Top left corner
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Apply Non-Max Suppression to remove overlapping boxes
        indices = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
        
        # Draw the final bounding boxes
        for i in indices:
            box = boxes[i]
            x, y, w, h = box
            
            label = str(classes[class_ids[i]])
            color = COLORS[class_ids[i]]
            
            # Draw box and label
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        cv2.imshow("Wildlife Detection (YOLO)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()