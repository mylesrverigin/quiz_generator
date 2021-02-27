import pandas as pd
import os 

class DataFetch():
    def __init__(self,path):
        self.path = path

    def get_file_names(self):
        self.files = os.listdir(self.path)
        return self.files

    def get_file(self,names):
        if isinstance(names,str):
            file_name = self.path + f'\{name}'
            try: 
                data = pd.read_csv(file_name)
                return data
            except: 
                return False
        else:
            if isinstance(names,list):
                temp_data = {}
                for i in names:
                    file_name = self.path + f'\{i}'
                    try: 
                        temp_data[i] = pd.read_csv(file_name)
                    except:
                        continue
                data = list(temp_data.values())
                while len(data) >= 2:
                    data[0] = data[0].append(data[1],ignore_index=True)
                    data.pop(1)
                return data[0]
                        
