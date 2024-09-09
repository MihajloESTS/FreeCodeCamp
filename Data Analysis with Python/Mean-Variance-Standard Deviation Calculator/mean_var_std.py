import numpy as np

def calculate(param_list):
    if len(param_list) != 9:
        raise ValueError("List must contain nine numbers.")
    flattened = np.array(param_list)
    matrix = flattened.reshape(3,3)
    calculations = {
        "mean": [matrix.mean(axis=0).tolist(),matrix.mean(axis=1).tolist(), flattened.mean().item()],
        "variance": [matrix.var(axis=0).tolist(),matrix.var(axis=1).tolist(), flattened.var().item()],
        "standard deviation": [matrix.std(axis=0).tolist(),matrix.std(axis=1).tolist(), flattened.std().item()],
        "max": [matrix.max(axis=0).tolist(),matrix.max(axis=1).tolist(), flattened.max().item()],
        "min": [matrix.min(axis=0).tolist(),matrix.min(axis=1).tolist(), flattened.min().item()],
        "sum": [matrix.sum(axis=0).tolist(),matrix.sum(axis=1).tolist(), flattened.sum().item()]
    }

    return calculations