'''ImageNet Dataset Loader.
'''
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import ImageNet
from PIL import Image

import config

def setup_dataloader(batch_size:int)->(DataLoader, DataLoader):
    '''Setup dataloader for training and validation.
    '''
    train_set = ImageNet(config.imagenet_dataset_root_dir, split='train', download=True,
        transform=image_transforms)
    val_set = ImageNet(config.imagenet_dataset_root_dir, split='val', download=True,
        transform=image_transforms)
    train_loader = DataLoader(train_set, batch_size=batch_size, **config.dataloader_config)
    val_loader = DataLoader(val_set, batch_size=batch_size, **config.dataloader_config)
    return train_loader, val_loader

def image_transforms(img:Image.Image)->callable:
    '''Transforms for Image data.
    '''
    return transforms.Compose([])