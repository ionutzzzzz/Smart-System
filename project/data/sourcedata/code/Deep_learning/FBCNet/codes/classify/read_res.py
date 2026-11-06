import pandas
from os.path import join
import numpy as np

path=r'E:\rongfenqi\data_public\codebench\Deep_learning\FBCNet\output\shu\cv\2024-05-25--10-43-283'
# path=r'E:\rongfenqi\4_class\FBCNet\output\shu\cv\2022-06-11--17-17-740'

res=[]
for subj in range(156):
    load_path=join(path,'sub'+str(subj),'fold9','results.csv')
    dat=pandas.read_csv(load_path)
    aa=dat.values[1][1]
    # res.append(np.float(aa[aa.find(':')+1:aa.find(',')]))
    res.append(float(aa[aa.find(':') + 1:aa.find(',')]))


import scipy.io as sio

dat=sio.loadmat(r'E:\rongfenqi\data_public\codebench\Deep_learning\FBCNet\data\shu\rawMat\se001')

import pickle

with open(r'E:\rongfenqi\data_public\codebench\Deep_learning\FBCNet\output\shu\cv\2024-05-25--10-43-283\sub0\fold9\expResults0.dat', 'rb') as f:
    dat=pickle.load(f)

