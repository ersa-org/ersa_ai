
from torch.utils.data import Dataset
import os
from PIL import Image # pillow


class MyData(Dataset):

    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir  # data
        self.label_dir = label_dir  # ants
        self.path = os.path.join(self.root_dir, self.label_dir)  # data/ants
        self.img_path = os.listdir(self.path)

    def __getitem__(self, index):
        # return self.img_path[index]
        img_name = self.img_path[index]
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
				# self.root_dir+ self.label_dir+img_name
				# "data/" +"ants/" +"....jpa"
        img = Image.open(img_item_path)
        label = self.label_dir
        # img.show()
        return img, label

    def __len__(self):
        return len(self.img_path)


root_dir = "data"
ants_label_dir = "ants"
ants_set = MyData(root_dir, ants_label_dir)
print("数据集的第一个:",ants_set[1])
print("数据集的长度:",len(ants_set))



# class Aniaml:
#     def __init__(self):
#         self.type = None


# class Person(Aniaml):

#     def __init__(self, name, age, type):
#         self.name = name
#         self.age = age
#         self.type = type


# p1 = Person("robin", 33, 'human')

# print(p1.name)
# print(p1.age)
# print(p1.type)
