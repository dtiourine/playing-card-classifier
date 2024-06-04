from torch.utils.data import Dataset, DataLoader
from torchvision.datasets import ImageFolder
class CardDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data = ImageFolder(data_dir, transform=transform)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

    @property
    def classes(self):
        return self.data.classes

def get_data_loaders(train_dir, valid_dir, test_dir, batch_size, transform=None):
    """
    Create data loaders for the training, validation, and testing datasets.

    Parameters:
        train_dir (str): Directory containing training data.
        valid_dir (str): Directory containing validation data.
        test_dir (str): Directory containing test data.
        batch_size (int): Number of samples per batch.
        transform (callable, optional): Optional transform to be applied on a sample.

    Returns:
        tuple: Contains three DataLoader instances for training, validation, and testing datasets,
               and a dictionary mapping from target indices to class labels.
    """
    # Create dataset objects for each type of data
    train_data = CardDataset(train_dir, transform=transform)
    valid_data = CardDataset(valid_dir, transform=transform)
    test_data = CardDataset(test_dir, transform=transform)

    # Create data loaders for each dataset
    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
    valid_loader = DataLoader(valid_data, batch_size=batch_size, shuffle=False)
    test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False)

    # Create a mapping from target indices to class labels
    target_to_class = {v: k for k, v in ImageFolder(train_dir).class_to_idx.items()}

    return train_loader, valid_loader, test_loader, target_to_class