from fastapi import UploadFile
from PIL import Image
import torch
from torchvision import transforms
import io
from backend.util.dataloader import get_data_loaders
import json

async def make_prediction(model, file: UploadFile, device):

    transform = transforms.Compose([ transforms.Resize((128, 128)), transforms.ToTensor(),])
    with open('saved_model/target_to_class.json', 'r') as file:
        target_to_class = json.load(file)

    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))
    image_tensor = transform(image).unsqueeze(0)
    image_tensor = image_tensor.to(device)

    model.eval()
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted = torch.max(outputs, 1)

    label = target_to_class(predicted.item())

    return label.item()
