from fastapi import UploadFile
from PIL import Image
import torch
from torchvision import transforms
import io
from backend.util.dataloader import get_data_loaders
import json
from backend.model.model import CardClassifier


def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = CardClassifier()
    model.load_state_dict(torch.load("backend/model/saved_model/model_card_classifier.pth", map_location=device))
    model.eval()
    model = model.to(device)
    model.device = device  # Storing device in the model for easy reference
    return model

def load_index_to_label_map():
    with open('backend/model/saved_model/target_to_class.json', 'r') as file:
        index_to_label = json.load(file)

    return index_to_label

def predict_image(image, model, index_to_label):
    try:
        transform = transforms.Compose([
            transforms.Resize((128, 128)),
            transforms.ToTensor(),
        ])
        image = transform(image).unsqueeze(0)
        image = image.to(model.device)
        output = model(image)
        _, predicted = torch.max(output, 1)
        predicted_index = predicted.item()
        predicted_class = index_to_label[str(predicted_index)]

    except Exception as e:
        raise e
    return predicted_class
