from fastapi import FastAPI,UploadFile,File
from PIL import Image
from io import BytesIO
import torch
import torch.nn as nn
from torchvision.models import efficientnet_b0
import torchvision.transforms as transforms


app=FastAPI()

def load_model():
    model=efficientnet_b0()

    model.classifier=nn.Linear(1280,2)
    state_dict = torch.load('backend/models/efficient_net_finetuned.pth',map_location=torch.device('cpu'))
    model.load_state_dict(state_dict)
    return model

def preprocess():
    transformed=transforms.Compose(
    [transforms.ToTensor(),
    transforms.Resize((224,224))
    ]
)
    return transformed

@app.post('/predict')
async def predict(file:UploadFile=File(...)):
    class_names={0:'Eczema',1:'Scabies'}
    content=await file.read()
    img=Image.open(BytesIO(content)).convert('RGB')
    model=load_model()
    transform=preprocess()
    img_tensor=transform(img).unsqueeze(0)
    model.eval()
    with torch.no_grad():
      results=model(img_tensor)
      _,predicted=torch.max(results,1)
      predicted_class = class_names[predicted.item()]
    return predicted_class






