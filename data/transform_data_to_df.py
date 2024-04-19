import pandas as pd 
#/workspaces/Forecasting-MLops/data/extracted_data.json
path = "data/extracted_data.json" 
data = pd.read_json(path)
# data/extracted_data.json
# /workspaces/Forecasting-MLops/data/extracted_data.json
data = data.drop(["Codigo", "Nombre", "Fecha"], axis=1)
data["time"] = data.index 
print( data.info(), "\n" )
X = data.drop( ["Valor"], axis=1) # time serie


print( X.head() )


