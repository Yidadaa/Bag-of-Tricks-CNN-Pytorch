'''Configure options for the repo.
'''
from os import path

# root directory of the repo
root_dir = path.abspath(__file__).replace(path.basename(__file__), '')

# root directory of the ImageNet dataset
imagenet_dataset_root_dir = path.join(root_dir, 'data')

# mean and std of ImageNet dataset, which is the same as Paper
imagenet_mean = [123.68, 116.779, 103.939]
imagenet_std = [58.393, 57.12, 57.375]


dataloader_config = {
    'num_workers': 4,
    'shuffle': True,
    'pin_memory': True
}