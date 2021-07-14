import pandas as pd
import plotly.express as px
import csv
import plotly.figure_factory as ff
import random
import statistics
import plotly.graph_objects as go

def randomSet(counter):
   dataset=[]
   for i in range(0,counter):
     index = random.randint(0,len(dataList)-1)
     value = dataList[index]
     dataset.append(value)
   mean = statistics.mean(dataset)  
   return mean

meanList=[]
for i in range(0,1000):
  setofmean = randomSet(100)
  meanList.append(setofmean)
  
df = pd.read_csv("Project111.csv")
dataList = df["reading_time"].tolist()

randomMean = randomSet(100)
print(randomMean)

mean = statistics.mean(meanList)
SD = statistics.stdev(meanList)


print("SD =", SD)
print("mean =", mean)

fig = ff.create_distplot([meanList],["reading_time"], show_hist=False )
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,.2], mode="lines"))

fig.show()