import pandas as pd
from getData import getData
from datetime import datetime
import os


def dataAnaly(data):
    dateToday = str(datetime.now().strftime("%d"))+", " + \
        str(datetime.now().strftime('%B'))+" " + \
        str(datetime.now().strftime("%Y"))
    df = pd.DataFrame(data, index=list(data.keys()))
    df['Date'] = dateToday
    df.drop_duplicates(subset='Date', inplace=True)
    if os.path.exists('COVID_Data_Master.csv') == False:
        df.to_csv('COVID_Data_Master.csv', mode='a', index=False)
    else:
        df.to_csv('COVID_Data_Master.csv', mode='a', header=False, index=False)

    print('Data Successfully added')
