#-----------------------------------ModifiedStarDataGraphPlotter.py-----------------------------------#

'''
Importing Modules:
-plotly.express (px)
-sys
-statistics (st)
-csv
-pandas (pd)
-time (tm)
'''

import plotly.express as px
import sys
import statistics as st
import csv
import pandas as pd
import time as tm

global_reader_list=None
headings=None


#Opening the file 'data.csv' to read the data
with open("data.csv",'r') as f:
  reader=csv.reader(f)
  reader_list=list(reader)
  headings=reader_list.pop(0)
  global_reader_list=reader_list


print("Welcome to ModifiedStarDataGraphPlotter.py")
print("Wel provide graph plotting of a modified dataset of stars.")

tm.sleep(2.3)
print("The units in ths version used are solar masses, solar gravities (1 unit= gravity of sun), lightyears, solar radii.")

tm.sleep(3.4)
print("Know more about these units through the folllowing links")
print("Solar Mass: 'https://en.wikipedia.org/wiki/Solar_mass'")
print("Solar Distance: 'https://en.wikipedia.org/wiki/Solar_radius'")
print("Lightyear: 'https://en.wikipedia.org/wiki/Light-year'")
tm.sleep(2.3)

print("Loading Data...")
tm.sleep(2.5)


#Running a for loop over the enumerated main dataset to eliminate datapoints that don not sataisfy the criteria
for row_index,row in enumerate(global_reader_list):
 
  #Verifying whether the distance values are lesser than 100 or not and the gravity values are between 150 and 350 or not
  #Case-1 
  if float(row[3])<100 or float(row[2])<150 or float(row[2])>350:
    global_reader_list.pop(row_index)
  

dataset=pd.DataFrame(global_reader_list,columns=headings)

names=dataset["Names"]

parameter_list=["Unusable_Element","Mass","Gravity","Distance","Radius"]

#Running a for loop over the enumerated list of parameters to display all the parameters to plot a graph or chart with
for parameter_index,parameter in enumerate(parameter_list):

  #Verifying whether the index of the paramteter is equal to zero or not to prevent displaying "Unusable_Element"
  #Case-1
  if parameter_index!=0:
    print("{}:{}".format(parameter_index,parameter))

parameter_input=int(input("Please enter the index of the parameter desired to plot with:"))

#Using a try-except block to check the validity  of the user's input
#Try block
try:

  #Verifying whether the user's input iequal to zero or not
  #Case-1
  if parameter_input!=0:
    user_choice=parameter_list[parameter_input]
  #Case-2  
  else:
    sys.exit("Invalid Input.")
#Except block
except:
  sys.exit("Invalid Input.")    


user_choice=parameter_list[parameter_input]

parameter_choice=dataset[user_choice].tolist()

new_parameter_choice=[]

#Running a for loop over the parameter of the user's choice
for parameter in parameter_choice:
  parameter=float(parameter)
  new_parameter_choice.append(parameter)

parameter_choice=new_parameter_choice


graph_list=["Unusable_Element","Scatter Graph","Bar Graph","Pie Chart"]

#Running a for loop over the enuemrated list of graphs or charts to display all graph choices possible to the user
for graph_index,graph in enumerate(graph_list):

  #Verifying whether the index of the paramteter is equal to zero or not to prevent displaying "Unusable_Element"
  #Case-1
  if graph_index!=0:
    print("{}:{}".format(graph_index,graph))

graph_input=int(input("Please enter the index of the type of graph to plot:"))   

#Using a try-except block to check the validity  of the user's input
#Try block
try:
   #Verifying whether the user's input iequal to zero or not
  #Case-1
  if graph_input!=0:
    user_choice=graph_list[graph_input]
  #Case-2  
  else:
    sys.exit("Invalid Input.")
#Except block    
except:
  sys.exit("Invalid Input.")  

graph_user_choice=graph_list[graph_input]

#Assessing the user's choice to plot the type of graph or chart to plot and  performing actions accordingly
#Case-1
if graph_input==1:
  scatter=px.scatter(x=names,y=parameter_choice,range_y=[0,(max(parameter_choice)/4)],width=6000,height=500)
  scatter.show()
#Case-2
elif graph_input==2:
  bar=px.bar(x=names,y=parameter_choice,range_y=[0,(max(parameter_choice)/4)],width=6000,height=500)
  bar.show()
#Case-3
elif graph_input==3:
  pie=px.pie(names=names,values=parameter_choice)
  pie.show()

#-----------------------------------ModifiedStarDataGraphPlotter.py-----------------------------------#