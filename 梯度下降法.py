import random
import matplotlib.pyplot as plt
_x = [i/100 for i in range(100)]
_y = [3*e+4+random.random() for e in _x]

# plt.plot(_x,_y,'.')
# plt.show()

w=random.random()
b=random.random()

plt.ion()
for _ in range(30): #总循环30次
    for x,y in zip(_x,_y):
        z = w*x+b   #感知机模型的前向过程
        o = z-y
        loss = o**2 #损失函数

        dw = -2*o*x   #梯度的反方向
        db = -2*o

        #梯度下降法
        w = w+0.1*dw
        b = b+0.1*db
        print('w=',w,'b=',b,'loss=',loss)
        v=[w*e+b for e in _x]
        plt.cla() #清屏
        plt.plot(_x,v) #描绘函数图像
        plt.plot(_x,_y,'.') #描绘数据
        plt.pause(0.1)

plt.ioff()
