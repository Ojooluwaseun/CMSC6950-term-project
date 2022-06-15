import numpy as np

class outliers:
    def __init__(self, data):
        self.data = data
        
    def remove_outliers(data, x):
        q25 = np.percentile(data[x], 25)
        q75 = np.percentile(data[x], 75)
        iqr = q75 - q25
        cut_off = iqr * 1.5
        lower, upper = 1, (q75 + cut_off)
        data = data[(data[x] < upper) & (data[x] > lower)]
        print(f"Outliers of {x} removed\n")
        return data
    
        
