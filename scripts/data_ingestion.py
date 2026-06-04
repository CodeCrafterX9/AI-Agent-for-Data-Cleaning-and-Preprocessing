import pandas as pd
import os 

class DataIngestor:
    def __init__(self):
        print("Data Ingestion Process Started")

    def extract_from_csv(self,file_path :str) -> pd.DataFrame :
        #TO LOAD CSV DATA FROM FILE PATH 
        #RETURN PANDAS DATAFRAME

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ File nahi mili: {file_path}")

        print(f"LOADING FILE: {file_path}")
        df = pd.read_csv(file_path)
        print(f"CSV successfully loaded! Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        
        return df

stage_1 = DataIngestor()
sample_path = "../data/sample_data.csv"
df= stage_1.extract_from_csv(sample_path)
print(df.head())