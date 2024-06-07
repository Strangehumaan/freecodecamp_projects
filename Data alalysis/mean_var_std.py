# importing the library 
import numpy as np

#defining Function
def calculor(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        array = np.array(list).reshape(3,3)

    
    # Calculating mean
    mean = [array.mean(axis=0,dtype=float).tolist(),array.mean(axis=1,dtype=float).tolist(),array.mean(dtype=float).tolist()]

    # Calculating Variance
    variance = [array.var(axis=0,dtype=float).tolist(),array.var(axis=1,dtype=float).tolist(),array.var(dtype=float).tolist()]

    #Calculating Standard deviation
    standard_deviation = [array.std(axis=0,dtype=float).tolist(),array.std(axis=1,dtype=float).tolist(),array.std(dtype=float).tolist()]

    #Finding the max value
    max = [array.max(axis=0).tolist(),array.max(axis=1).tolist(),array.max().tolist()]

    #Finding the min value
    min = [array.min(axis=0).tolist(),array.min(axis=1).tolist(),array.min().tolist()]

    #Finding the sum
    sum = [array.sum(axis=0).tolist(),array.sum(axis=1).tolist(),array.sum().tolist()]

    #Gettting all values in the dictionary 
    dic = {'Mean':mean,
            'Variance':variance,
            'Standard deviation':standard_deviation,
            'Max':max,
            'Min':min,
            'Sum':sum}
        
    return dic

