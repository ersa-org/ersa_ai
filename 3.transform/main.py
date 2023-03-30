from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter

# tensor 数据类型
# transform.ToTensor
# Tensor 类型和普通数据类型的区别
# 为什么要用tensor类型


if __name__ == '__main__':
    img_path = "/Users/panzi/Desktop/git_pro/ersa_ai/1.dataset/F8DDCD9E-8CED-4ebe-BB5D-F884747880B5.png"
    img= Image.open(img_path)
    tensor = transforms.ToTensor()
    tensor_img = tensor(img)
    # print(tensor_img)
    writer = SummaryWriter("logs")
    writer.add_image("tensor image",tensor_img)

    t_n=transforms.Normalize([2,3,4],[3,4,3])
    normal_img =t_n(tensor_img)
    print("normal_image")
    print(normal_img)




    writer.close()


