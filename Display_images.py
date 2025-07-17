import matplotlib.pyplot as plt
import matplotlib.patches as patches
import torch
from facenet_pytorch import MTCNN, InceptionResnetV1
import numpy as np 
import skimage.io as io
from PIL import Image, ImageDraw, ImageFont


def display_labeled_faces(self, image_path):
    image = Image.open(image_path).convert('RGB') ##I think it needs to be in RGB
    boxes, probs = self.detector.detect(image)

    if boxes is None: 
        print("No faces detected.")
        return 
    
    faces = []
    for box in boxes: 
        x1, y1, x2, y2 = map(int, box) 
        face = image.crop((x1, y1, x2, y2)) ##crops face, then adds to list 
        faces.append(face) 
