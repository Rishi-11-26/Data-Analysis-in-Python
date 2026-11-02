
import numpy as np

def calculate(values):
    # Convert input to a NumPy array
    arr = np.array(values)

    # Validate the number of elements
    if arr.size!=9:
        raise ValueError("List must contain nine numbers.")
    arr=arr.reshape(3,3)
    mean_axis0 = np.mean(arr, axis=0)
    mean_axis1 = np.mean(arr, axis=1)
    mean_matrix = np.mean(arr).item()

    variance_axis0 = np.var(arr,axis=0)
    variance_axis1 = np.var(arr,axis=1)
    variance_matrix = np.var(arr).item()

    std_axis0 = np.std(arr,axis=0)
    std_axis1 = np.std(arr,axis=1)
    std_matrix = np.std(arr).item()

    
    max_axis0 = np.max(arr,axis=0)
    max_axis1 = np.max(arr,axis=1)
    max_matrix = np.max(arr).item()

    min_axis0 = np.min(arr,axis=0)
    min_axis1 = np.min(arr,axis=1)
    min_matrix = np.min(arr).item()

    sum_axis0 = np.sum(arr,axis=0)
    sum_axis1 = np.sum(arr,axis=1)
    sum_matrix = np.sum(arr).item()

    return {
        'mean': [
            mean_axis0.tolist(),
            mean_axis1.tolist(),
            mean_matrix
        ],
        'variance': [
            variance_axis0.tolist(),
            variance_axis1.tolist(),
            variance_matrix
        ],
        'standard deviation': [
            std_axis0.tolist(),
            std_axis1.tolist(),
            std_matrix
        ],
        'max': [
            max_axis0.tolist(),
            max_axis1.tolist(),
            max_matrix
        ],
        'min': [
            min_axis0.tolist(),
            min_axis1.tolist(),
            min_matrix
        ],
        'sum': [
            sum_axis0.tolist(),
            sum_axis1.tolist(),
            sum_matrix
        ]
    }
