import cv2
import numpy as np
import easyocr
import time

class Yolov5:
    def __init__(self, net_path, classes_path, source=0):
        self.net = self.load_model(net_path)
        self.classes = self.load_classes(classes_path)
        self.capture = self.load_capture(source)
        self.reader = self.load_ocr()
        # Constants.
        self.INPUT_WIDTH = 640
        self.INPUT_HEIGHT = 640
        self.SCORE_THRESHOLD = 0.2
        self.NMS_THRESHOLD = 0.45
        self.CONFIDENCE_THRESHOLD = 0.45
        # Text parameters.
        self.FONT_FACE = cv2.FONT_HERSHEY_SIMPLEX
        self.FONT_SCALE = 0.7
        self.THICKNESS = 1

        # Colors
        self.BLACK  = (0,0,0)
        self.BLUE   = (255,178,50)
        self.YELLOW = (0,255,255)
        self.RED = (0,0,255)

    def load_model(self, net_path):
        modelWeights = net_path
        net = cv2.dnn.readNet(modelWeights)
        return net
    
    def load_classes(self, classes_path):
        classesFile = classes_path
        classes = None
        with open(classesFile, 'rt') as f:
            classes = f.read().rstrip('\n').split('\n')
        return classes
    
    def load_capture(self, source):
        capture = cv2.VideoCapture(source)
        return capture
    
    def load_ocr(self):
        # OCR
        reader = easyocr.Reader(['en'], gpu=True)
        print("OCR loaded")
        return reader
    
    def draw_label(self, input_image, label, left, top):
        """Draw text onto image at location."""
        
        # Get text size.
        text_size = cv2.getTextSize(label, self.FONT_FACE, self.FONT_SCALE, self.THICKNESS)
        dim, baseline = text_size[0], text_size[1]
        # Use text size to create a BLACK rectangle. 
        cv2.rectangle(input_image, (left, top), (left + dim[0], top + dim[1] + baseline), self.BLACK, cv2.FILLED);
        # Display text inside the rectangle.
        cv2.putText(input_image, label, (left, top + dim[1]), self.FONT_FACE, self.FONT_SCALE, self.YELLOW, self.THICKNESS, cv2.LINE_AA)


    def pre_process(self, input_image, net):
        # Create a 4D blob from a frame.
        blob = cv2.dnn.blobFromImage(input_image, 1/255, (self.INPUT_WIDTH, self.INPUT_HEIGHT), [0,0,0], 1, crop=False)

        # Sets the input to the network.
        net.setInput(blob)

        # Runs the forward pass to get output of the output layers.
        output_layers = net.getUnconnectedOutLayersNames()
        outputs = net.forward(output_layers)
        #print(outputs[0].shape)

        return outputs

    def post_process(self, input_image, outputs):
        # Lists to hold respective values while unwrapping.
        class_ids = []
        confidences = []
        boxes = []

        # Rows.
        rows = outputs[0].shape[1]

        image_height, image_width = input_image.shape[:2]

        # Resizing factor.
        x_factor = image_width / self.INPUT_WIDTH
        y_factor =  image_height / self.INPUT_HEIGHT

        # Iterate through 25200 detections.
        for r in range(rows):
            row = outputs[0][0][r]
            confidence = row[4]

            # Discard bad detections and continue.
            if confidence >= self.CONFIDENCE_THRESHOLD:
                classes_scores = row[5:]

                # Get the index of max class score.
                class_id = np.argmax(classes_scores)

                #  Continue if the class score is above threshold.
                if (classes_scores[class_id] > self.SCORE_THRESHOLD):
                    confidences.append(confidence)
                    class_ids.append(class_id)

                    cx, cy, w, h = row[0], row[1], row[2], row[3]

                    left = int((cx - w/2) * x_factor)
                    top = int((cy - h/2) * y_factor)
                    width = int(w * x_factor)
                    height = int(h * y_factor)

                    box = np.array([left, top, width, height])
                    boxes.append(box)       
        # Perform non maximum suppression to eliminate redundant overlapping boxes with
        # lower confidences.
        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.CONFIDENCE_THRESHOLD, self.NMS_THRESHOLD)
        for i in indices:
            box = boxes[i]
            left = box[0]
            top = box[1]
            width = box[2]
            height = box[3]
            license_plate = input_image[top:top+height, left:left+width]

            # recognize characters from the license plate image
            characters = self.recognize_characters(license_plate)
            cv2.putText(input_image, characters, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            #cv2.rectangle(input_image, (left, top), (left + width, top + height), BLUE, 3*THICKNESS)
            #label = "{}:{:.2f}".format(classes[class_ids[i]], confidences[i])
            #draw_label(input_image, label, left, top)
        return input_image

    def recognize_characters(self, image):
        # preprocess the image
        # preprocessed = ocr_pre_process(image)
        
        # recognize characters using OCR reader
        result = self.reader.readtext(image, detail=0)
            
        return str(result)

yolo = Yolov5("weights\lp_v2.onnx", "config\lp_v2.txt", "data/Number Plate detection on Recorded Video.mp4")

frame = 0
# Obtain frame size information using get() method
frame_width = int(yolo.capture.get(3))
frame_height = int(yolo.capture.get(4))
frame_size = (frame_width,frame_height)
fps = 20

# Initialize video writer object
output = cv2.VideoWriter('data/output_video_from_file.avi', cv2.VideoWriter_fourcc(*'MJPG'), 20, frame_size)
while True:
    frame+=1
    _, frame = yolo.capture.read()
    if frame is None:
        print("End of stream")
        break
    #frame = cv2.rotate(frame, cv2.ROTATE_180)
    start = time.time()
    detections = yolo.pre_process(frame, yolo.net)
    img = yolo.post_process(frame.copy(), detections)
    end = time.time()
    total = end-start
    # Put efficiency information. The function getPerfProfile returns the overall time for inference(t) and the timings for each of the layers(in layersTimes)
    t, _ = yolo.net.getPerfProfile()
    label = 'FPS: %.2f' % (1000/(t * 1000.0 / cv2.getTickFrequency()))
    
    cv2.putText(img, label, (20, 40), yolo.FONT_FACE, yolo.FONT_SCALE, yolo.RED, yolo.THICKNESS, cv2.LINE_AA)
    output.write(img)
    cv2.imshow('Output', img)
    cv2.waitKey(5)

    if cv2.waitKey(1) > -1:
        print("finished by user")
        break