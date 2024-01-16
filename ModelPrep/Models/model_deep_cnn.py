#PyTorch stuff
import torch
import torchvision as torchv
import torch.nn as nn 
import torch.optim as optim
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, TensorDataset, random_split
from torchvision.datasets import ImageFolder

class DeepCNN(nn.Module):
    def __init__(self):
        super(DeepCNN, self).__init__()

        # Stem
        self.stem = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Conv2d(32, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )

        # Inception blocks (similar to Inception-ResNet)
        self.inception1 = InceptionBlock(64, 32, 64, 64, 64)  # Keep only one Inception block

        # Fully connected layers
        self.fc_model = nn.Sequential(
            nn.Linear(1005536, 512),  # Adjust the input size based on the modified model
            nn.ReLU(),
            #nn.Dropout(p=0.1),
            nn.Linear(512, 3)
        )

    def forward(self, x):
        x = self.stem(x)
        x = self.inception1(x)
        x = x.view(x.size(0), -1)
        x = self.fc_model(x)
        return x

class InceptionBlock(nn.Module):
    def __init__(self, in_channels, red_channels, mid1_channels, mid2_channels, out_channels):
        super(InceptionBlock, self).__init__()

        # 1x1 convolution branch
        self.branch1x1 = nn.Sequential(
            nn.Conv2d(in_channels, red_channels, 1),
            nn.ReLU()
        )

        # 1x1 convolution followed by 3x3 convolution branch
        self.branch3x3 = nn.Sequential(
            nn.Conv2d(in_channels, mid1_channels, 1),
            nn.ReLU(),
            nn.Conv2d(mid1_channels, mid2_channels, 3, padding=1),
            nn.ReLU()
        )

        # 1x1 convolution followed by 5x5 convolution branch
        self.branch5x5 = nn.Sequential(
            nn.Conv2d(in_channels, mid1_channels, 1),
            nn.ReLU(),
            nn.Conv2d(mid1_channels, mid2_channels, 5, padding=2),
            nn.ReLU()
        )

        # 3x3 max-pooling followed by 1x1 convolution branch
        self.branch_pool = nn.Sequential(
            nn.MaxPool2d(3, stride=1, padding=1),
            nn.Conv2d(in_channels, out_channels, 1),
            nn.ReLU()
        )

    def forward(self, x):
        branch1x1 = self.branch1x1(x)
        branch3x3 = self.branch3x3(x)
        branch5x5 = self.branch5x5(x)
        branch_pool = self.branch_pool(x)
        return torch.cat([branch1x1, branch3x3, branch5x5, branch_pool], 1)