import pandas as pd 
#/workspaces/Forecasting-MLops/data/extracted_data.json
path = "data/extracted_data.json" 
data = pd.read_json(path)
# data/extracted_data.json
# /workspaces/Forecasting-MLops/data/extracted_data.json
data['Valor'] = pd.to_numeric(data['Valor'].str.replace(',', '.'))

print( data.info(), "\n" )


print( data.head() )

