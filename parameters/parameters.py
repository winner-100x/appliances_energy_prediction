import os

FILE_NAME = "energydata_complete.csv"
DATA_FOLDER = "data"

main_path = os.getcwd()

main_path

file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), FILE_NAME)