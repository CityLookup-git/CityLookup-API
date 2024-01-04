import pandas as pd
import json
import glob

class DataLoader:
    def __init__(self, folder_path):
        self.dataframe = self.load_data(folder_path)

    def load_data(self, folder_path):
        df_list = []
        print("\n⏳ Loading data...\nThis may take a while. If the app crashes, you might be running out of RAM with your datasets.\n")
        for file_path in glob.glob(folder_path + '/*.geojson'):
            with open(file_path, 'r') as file:
                data = [json.loads(line) for line in file]
                df = pd.json_normalize(data)
                df_list.append(df)

        full_df = pd.concat(df_list, ignore_index=True)
        
        # Convert optimal columns to categories for performance
        if 'properties.city' in full_df.columns:
            full_df['properties.city'] = full_df['properties.city'].astype('category')
        if 'properties.street' in full_df.columns:
            full_df['properties.street'] = full_df['properties.street'].astype('category')

        print("✅ Load complete!\n")
        return full_df

    def get_streets_by_city(self, city):
        city_upper = city.upper()
        filtered_df = self.dataframe[self.dataframe['properties.city'].str.upper() == city_upper]
        streets = filtered_df['properties.street'].unique()
        return streets.tolist()
