from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularPredictor 


def perform_train_test_split(df):
    
    train_data, test_data = (
        train_test_split(df, test_size=0.33, random_state=42)

    )

    return train_data, test_data

def autogluon_model_build(df, autogluon_params):

    label = autogluon_params["label"]
    save_path = autogluon_params["save_path"]
    time_limit = autogluon_params["time_limit"]
    problem_type = autogluon_params["problem_type"]

    
    train_data, test_data = perform_train_test_split(df)
                                           
    predictor = ( 
        TabularPredictor(label=label, 
                         path=save_path, 
                         problem_type=problem_type)
        .fit(train_data, time_limit=time_limit)

    )

    return train_data, test_data, predictor 