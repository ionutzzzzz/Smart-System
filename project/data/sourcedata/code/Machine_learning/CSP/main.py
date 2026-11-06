#SHU Dataset for CSP algorithm
# sub_id, input subject id 1 to 156

from ws import *
import os
import scipy.io as sio
import numpy as np

mne.set_log_level(verbose=0)



res=[]
for sub_id in range(1,157):

        data_path=r'WBCIC-SHU Motor Imagery Dataset'
        wst_accuracy=train_test(sub_id,data_path,k_fold=10)
        print('CSP acc is: ',wst_accuracy)
        res.append(wst_accuracy)


sio.savemat('results.mat',{'res':res})
with open ('results.txt' ,'w') as f:
        f.writelines(str(res))
print(np.average(res))




