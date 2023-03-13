import pandas as pd
# from parameters.parameters import file_path

def get_data(file_path):
    
    # This is a function that takes in file path and can be reused.
    
    df = pd.read_csv(file_path)

    return df

