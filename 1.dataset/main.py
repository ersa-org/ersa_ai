
from torch.utils.data import  Dataset
import os
from PIL import Image


class MyData(Dataset):
  
	def __init__(self,root_dir,label_dir):
		self.root_dir = root_dir;
		self.label_dir = label_dir;
		self.path = os.path.join(self.root_dir,self.label_dir)
		self.img_path = os.listdir(self.path)

	def __getitem__(self, index):
		img_name = self.img_path[index]
		img_item_path = os.path.join(self.root_dir,self.label_dir,img_name)
		img= Image.open(img_item_path)
		label = self.label_dir
		img.show()
		return  img, label

	def __len__(self):
		return len(self.img_path)
	
root_dir = "data"
ants_label_dir = "ants"
ants_set = MyData(root_dir,ants_label_dir)
ants_set[1]

print("data")







 



























	

			
  

