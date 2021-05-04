import pandas as pd
from getData import getData
from datetime import datetime

def dataAnaly():
    data = getData()
    dateToday = str(datetime.now().day)+", "+str(datetime.now().strftime('%B'))+" "+str(datetime.now().year)
    df = pd.DataFrame(data, index=list(data.keys()))
    df['Date'] = dateToday
    df.drop_duplicates(subset='Date', inplace=True)
    df.to_csv('COVID_Data_Master.csv',mode='a',header=False, index=False)
    print('Data Successfully added')