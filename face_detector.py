import os
import struct
from os import path
from bluetooth_widget import BluetootWidget
import cv2
from kivy import Logger


class FaceDetector:
    def __init__(self, path):
        self.path = path
        Logger.debug("FaceDetector.__init__()")
        self.scale_factor = 2
        self.detector = cv2.CascadeClassifier(os.path.join(self.path, "./data/haarcascade_frontalface_default.xml"))
        self.bluetooth = BluetootWidget("Essay")

    def detect_face_from_files(self, filename):
        image = cv2.imread(filename)
        return self.detect_faces(image)

    def detect_faces(self, image):
        image_copy = image.copy()
        gray = cv2.cvtColor(cv2.resize(image_copy, (0, 0), fx=1.0 / self.scale_factor, fy=1.0 / self.scale_factor), cv2.COLOR_RGB2GRAY)
        faces = self.detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3) * self.scale_factor
        data_tuple = faces[0]
        data = struct.pack('iiii', *data_tuple)
        self.bluetooth.send_stream.write(data)
        self.bluetooth.send_stream.flush()
        return faces
