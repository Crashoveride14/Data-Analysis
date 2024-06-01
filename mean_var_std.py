import numpy as np
# List of numbers 
lt = [0,1,2,3,4,5,6,7,8]
#Calculations for mean,standard deviation,varaince, max
def calculation():
    arr = np.array(lt).reshape(3,3)
    calc = {
        "mean": [[np.mean(arr,axis=0).tolist(), np.mean(arr,axis=1).tolist(), np.mean(arr).tolist()]],
        "var": [[np.var(arr,axis=0).tolist(), np.var(arr,axis=1).tolist(), np.var(arr).tolist()]],
        "standard deviation": [[np.std(arr,axis=0).tolist(), np.std(arr,axis=1).tolist(), np.std(arr).tolist()]],
        'max': [[np.max(arr,axis=0).tolist(), np.max(arr,axis=1).tolist(), np.max(arr).tolist()]],
        'min': [[np.min(arr,axis=0).tolist(), np.min(arr,axis=1).tolist(), np.min(arr).tolist()]],
    }
    return calc
calculation()

