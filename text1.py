#-*-coding:utf-8-*-
import numpy as np

a=np.arange((24),dtype=np.float32).reshape(2,3,4)
a[0,0,2]=66
print(a)
print(np.mean((a),axis=0))