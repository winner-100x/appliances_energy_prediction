import os

ENERGY_FILE_NAME = "energydata_complete.csv"
DATA_FOLDER = "data"

main_path = os.getcwd()

main_path

#  This is a function that takes in file path and can be reused to avoid hardcoding and maintainablilty

energy_file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), ENERGY_FILE_NAME)

autogluon_params = {
    
    "save_path": 'artefacts/moodels_regression',
    "time_limit": 60,
    "label": "Appliances",
    "problem_type": "regression",
}