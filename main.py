# main Entrypoint
from sklearn.model_selection import train_test_split
from parameters.parameters import (
    energy_file_path, autogluon_params
)
from data_ingestion.ingest import get_data
from model_building.build_model import autogluon_model_build
import time

# from data_ingestion.ingest import energy_data

# Stage 0 - Data Ingestion
print("Starting Data Ingestion")
start_time = time.time()
energy_data = get_data(energy_file_path)
end_time = time.time()
print(f"Execution time for Energy Data Ingestion is{end_time - start_time} seconds")
print(f"Size of Appliances Energy Data is{energy_data.shape}")
print(energy_data.head())

# Stage 1

# Stage 2 - Model Building
print("Starting Model Building...")
start_time = time.time()
train_data, test_data, predictor = ( 
autogluon_model_build(energy_data, autogluon_params)
)

end_time = time.time()
print(f"Execution time for Model Building is{end_time - start_time} seconds")
print(f"Size of Train Data is{train_data.shape}")
print(f"Size of Train Data is{test_data.shape}")

# Stage 3 - Model Evaluation - we want to evaluate the current data to see the result craeted

print("Starting Model Evaluation...")
start_time = time.time()
print(predictor.leaderboard(silent=True))
end_time = time.time()
print(f"Execution time for Model Evaluation (train) is{end_time - start_time} seconds")

start_time = time.time()
print(predictor.leaderboard(test_data, silent=True))
end_time = time.time()
print(f"Execution time for Model Evaluation(test) is{end_time - start_time} seconds")





