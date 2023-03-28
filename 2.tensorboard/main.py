from torch.utils.tensorboard import  SummaryWriter
import math

writer = SummaryWriter('logs')

start = 0.1
while start < math.pi:
	writer.add_scalar("y=sin(x)", math.sin(start), start)
	start+=0.1
writer.close()