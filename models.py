#Pratyush
from facenet_models import FacenetModel

pic = "C:\Users\HP\Downloads\download (4).jpeg"
model = FacenetModel()
boxes, probabilities, landmarks = model.detect(pic)
print(boxes, probabilities, landmarks)