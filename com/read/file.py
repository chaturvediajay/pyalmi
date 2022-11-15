import pandas as pd
import os


class FileRead:
    def __init__(self, name):
        self.name = name

    def fun(self):
        df = pd.read_csv('/Users/ajaychaturvedi/PycharmProjects/pyalmi/data/olist_customers_dataset.csv')
        print(df.to_string())
        print(self.name)


p = FileRead('Ajay Chaturvedi')
p.fun()
