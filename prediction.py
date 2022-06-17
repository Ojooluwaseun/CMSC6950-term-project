import pandas as pd
from geocoder import geocoder
from sklearn.ensemble import RandomForestRegressor
ran_forest = RandomForestRegressor()

class prediction:
    def __init__(self, data):
        self.data = data
        
    def transform(data):
        test_df = pd.DataFrame(data, index=[0])
        test_df['lat'] = test_df.apply(lambda x: geocoder.geocode(x.address)[0], axis=1)
        test_df['long'] = test_df.apply(lambda x: geocoder.geocode(x.address)[1], axis=1)
        test_df = test_df.drop(['address'], axis=1)
        
        test_df.to_hdf('test_data.h5', key='test_df') # save to hdf5
        
        return test_df