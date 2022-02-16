import random
import plotly.express as px
import plotly.figure_factory as pff
import pandas as pd
import statistics as s
import plotly.graph_objects as go

df=pd.read_csv("StudentsPerformance.csv")
diceResult=df["reading score"].tolist()

mean=sum(diceResult)/len(diceResult)
print("mean=",mean)

median=s.median(diceResult)
print("Median=",median)

mode=s.mode(diceResult)
print("mode=",mode)

sd=s.stdev(diceResult)
print("Standard Deviation=",sd)

sd1start,sd1end=mean-sd,mean+sd
sd2start,sd2end=mean-(sd*2),mean+(sd*2)
sd3start,sd3end=mean-(sd*3),mean+(sd*3)



figure=pff.create_distplot([diceResult],["result"],show_hist=False)
figure.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
figure.add_trace(go.Scatter(x=[sd1start,sd1start],y=[0,0.17],mode="lines",name="sd1"))
figure.add_trace(go.Scatter(x=[sd1end,sd1end],y=[0,0.17],mode="lines",name="sd1"))

figure.add_trace(go.Scatter(x=[sd2start,sd2start],y=[0,0.17],mode="lines",name="sd2"))
figure.add_trace(go.Scatter(x=[sd2end,sd2end],y=[0,0.17],mode="lines",name="sd2"))

figure.show()

list1=[result for result in diceResult if result>sd1start and result<sd1end]
list2=[result for result in diceResult if result>sd2start and result<sd2end]
list3=[result for result in diceResult if result>sd3start and result<sd3end]


print("{}% of data lies within first standard deviation".format(len(list1)*100/len(diceResult)))
print("{}% of data lies within second standard deviation".format(len(list2)*100/len(diceResult)))
print("{}% of data lies within third standard deviation".format(len(list3)*100/len(diceResult)))
