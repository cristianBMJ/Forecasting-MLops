from pipelines.training_pipeline import train_pipeline
from zenml.client import Client


if __name__ == "__main__":
    # run the pipeline .
    # print( Client().active_stack.experiment_tracker.get_tracking_uri() )
    
    data_path = "/workspaces/Forecasting-MLops/data/extracted_data.json"
    print("Done")
    train_pipeline( data_path=data_path)

# mlflow ui --backend-store-uri "file:/home/codespace/.config/zenml/local_stores/29847686-a44a-4851-b931-78b37a6596ab/mlruns"