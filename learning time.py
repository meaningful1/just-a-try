import sys
import torch
import torchvision
print("torch version:",torch.__version__)
print("torchvision version:",torchvision.__version__)
print("python 版本:",sys.version)
x = torch.rand(3, 3)
print(x)