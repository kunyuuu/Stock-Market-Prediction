import datetime
import pandas_datareader.data as web

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2019, 12, 1)

df = web.DataReader("AAPL", 'yahoo', start, end)
bf = web.DataReader("ROKU",'yahoo', start, end)
af = web.DataReader("SNAP",'yahoo', start, end)
cf = web.DataReader("FB",'yahoo', start, end)
bf = web.DataReader("PYPL",'yahoo', start, end)

df.to_csv('PYPL.csv')
cf.to_csv('FB.csv')
af.to_csv('SNAP.csv')
df.to_csv('AAPL.csv')
bf.to_csv('ROKU.csv')