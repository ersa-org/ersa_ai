from torch.utils.tensorboard import SummaryWriter
import math


writer = SummaryWriter('logs')

x = 0.1

while x < math.pi:  # 3.14159
    writer.add_scalar("y=sin(x)", math.sin(x), x)
    x += 0.1

x1 = 0
while x1 < 10:
    writer.add_scalar("y=2x", 2*x1, x1)
    x1 += 1

writer.close()
