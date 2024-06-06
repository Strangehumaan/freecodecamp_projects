import numpy as np

def calculor(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        array = np.array(list).reshape(3,3)

    mean = [array.mean(axis=0,dtype=float).tolist(),array.mean(axis=1,dtype=float).tolist(),array.mean(dtype=float).tolist()]

    variance = [array.var(axis=0,dtype=float).tolist(),array.var(axis=1,dtype=float).tolist(),array.var(dtype=float).tolist()]

    standard_deviation = [array.std(axis=0,dtype=float).tolist(),array.std(axis=1,dtype=float).tolist(),array.std(dtype=float).tolist()]

    max = [array.max(axis=0).tolist(),array.max(axis=1).tolist(),array.max().tolist()]

    min = [array.min(axis=0).tolist(),array.min(axis=1).tolist(),array.min().tolist()]

    sum = [array.sum(axis=0).tolist(),array.sum(axis=1).tolist(),array.sum().tolist()]

    dic = {'Mean':mean,
            'Variance':variance,
            'Standard deviation':standard_deviation,
            'Max':max,
            'Min':min,
            'Sum':sum}
        
    return dic

