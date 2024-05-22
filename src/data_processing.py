import pandas as pd

def import_data(file_path):
    data = pd.read_csv(file_path)
    data['latitude'] = data['latitude'].astype(float)
    data['longitude'] = data['longitude'].astype(float)
    return data
