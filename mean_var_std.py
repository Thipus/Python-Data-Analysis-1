import numpy as np
#list=[0,1,2,3,4,5,6,7,8]
list1=[2,6,2,8,4,0,1,5,7]
list2=[9,1,5,3,3,3,2,9,0]
list3=[2,6,2,8,4,0,1,]
def calculate(list):
    #list=list1
    #list=list2
    #list=list3
    if len(list)<9:
        raise ValueError("List must contain nine numbers.")
    the_Array=np.array(list)
    the_Array=the_Array.reshape(3,3)
    calculations={'mean':[],'variance':[],'standard deviation':[],'max':[],'min':[],'sum':[]}
    calculations["mean"]=[np.mean(the_Array,axis=0).tolist(),np.mean(the_Array,axis=1).tolist(),np.mean(the_Array)]
    calculations["variance"]=[np.var(the_Array,axis=0).tolist(),np.var(the_Array,axis=1).tolist(),np.var(the_Array)]
    calculations["standard deviation"]=[np.std(the_Array,axis=0).tolist(),np.std(the_Array,axis=1).tolist(),np.std(the_Array)]
    calculations["max"]=[np.max(the_Array,axis=0).tolist(),np.max(the_Array,axis=1).tolist(),np.max(the_Array)]
    calculations["min"]=[np.min(the_Array,axis=0).tolist(),np.min(the_Array,axis=1).tolist(),np.min(the_Array)]
    calculations["sum"]=[np.sum(the_Array,axis=0).tolist(),np.sum(the_Array,axis=1).tolist(),np.sum(the_Array)]
    return calculations