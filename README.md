# Forecasting-MLops
Forecasting streaming data under paradigm MLops. For this task, I used MLops framework **ZENML**. 

### ZENML
Install requirements:

```bash
pip install "zenml[server]"
```

Integration with scikit-learn

```bash
zenml integration install sklearn -y
```


Integration with MLflow

```bash
zenml integration install mlflow -y
```

Registred stack in MLflow

```bash
zenml experiment-tracker register mlflow_tracker --flavor=mlflow
zenml model-deployer register mlflow --flavor=mlflow
zenml stack register mlflow_stack -a default -o default -d mlflow -e mlflow_tracker --set
```

