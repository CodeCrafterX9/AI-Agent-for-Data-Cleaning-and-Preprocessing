import pandas as pd 
import numpy as np 

class DataCleaning:
    def handle_missing_values(self,df,strategy="mean",constant="Unkown"):
        #missing values ko handle karne ka tareeka 
        numeric_cols = df.select_dtypes(include="number").Columns
        for col in numeric_cols :
            
            mean = df[col].mean()
            median = df[col].median()
            mode = df[col].mode().iloc[0]

            if strategy == "mean":
                df[col]=df[col].fillna(mean)
            elif strategy == "mode":
                df[col]=df[col].fillna(mode)
            elif strategy == "median":
                df[col]=df[col].fillna(median)
            elif strategy == "drop":
                df.dropna(inplace=True)
            elif strategy == "forward-fill":
                df[col]=df[col].ffill()
            elif strategy == "backward-fill":
                df[col]=df[col].bfill()
            else:
                df[col]=df[col].fillna(0)
            
        for col in df.Columns:
            if col not in numeric_cols :
                if strategy == "mode":
                    df[col]=df[col].fillna(mode)
                elif strategy == "drop":
                    df.dropna(inplace=True)
                elif strategy == "forward-fill":
                    df[col]=df[col].ffill()
                elif strategy == "backward-fill":
                    df[col]=df[col].bfill()
                else:
                    df[col]=df[col].fillna(constant)
            
    def drop_duplicates(self,df,unique_entry_column_name=None,keep="first"):
        #removes duplicates rows
        #agar 2 rows hai , 1st wali ko ye duplicate nahi karega sirf extra row ko hi duplicate kahega & remove karega
        if unique_entry_column_name == None:
            df.drop_duplicates(inplace=True)
        elif unique_entry_column_name in df.Columns :
            df.drop_duplicates(inplace=True,subset=[unique_entry_column_name],keep=keep)
        #keep has 2 values first/last iska matlab hai 2 duplicates mei kisko pick karna hai 
        #unique column se hum primary ey define kar sakte hai df ka
    
    def show_datatypes(self,df):
        return df.dtypes

    def fix_datatypes(self,df,dict={}):
        for col in dict:
            try :
                df[col]=df[col].astype(dict[col])
            except:
                pass
        return df 
    
