import pandas as pd 
from sqlalchemy import create_engine

df = pd.read_excel("Sample.xls")

engine = create_engine('mysql://root:123321mm@localhost/project8')
df.to_sql('managestore_data', con=engine)
print(df)