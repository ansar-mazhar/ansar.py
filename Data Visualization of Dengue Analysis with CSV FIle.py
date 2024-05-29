"""
 Data Visualization of Dengue Analysis with CSV File

Created By:
    Rida Rafaqat           2023-EE-256
    Ansar                  2023-EE-268
    Rafay Nasir Khan       2023-EE-267
    Sofia Fiaz             2023-EE-262

Presented To:RR
    Dr. Haris Anwaar 

"""

#Importing Required Libraries:
    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Initialization Phase:

#Creating User Interface (UI):

print()
print()
print("         Data Visualization of Dengue Analysis with CSV File      ")


def UI():
    print()
    print("#1. For checking the data.")
    print("#2. Reading complete file without index.")
    print("===================")
    print()
    print("#3. Line Chart")
    print("    Press 1 to print the data for Confirmed cases as per District.")
    print("    Press 2 to print the data for Recovered cases as per District.")
    print("    Press 3 to print the data for Death cases as per District.")
    print("    Press 4 to print the data for Active cases as per District.")
    print("    Press 5 to print All data.")
    print()
    print("#4. Bar Graph")
    print("    Press 1 to print the data for Confirmed cases as per District.")
    print("    Press 2 to print the data for Recovered cases as per District.")
    print("    Press 3 to print the data for Death cases as per District.")
    print("    Press 4 to print the data for Active cases as per District.")
    print("    Press 5 to print the data in form of stack bar chart")
    print("    Press 6 to print the data in form of multi bar chart")
    print()
    print("#5. Scatter Chart")
    print()
    print("#6. For Exit")
    print("===============")

#Processing Phase:

#Defining Functions for Specific Forms of Analysis:

def Read_CSV():
    print()
    print()
    print("The Data")
    df=pd.read_csv("Disease_Data_Punjab.csv")
    print(df)

def No_Index():
    print()
    print()
    print("Reading the file without index")
    df=pd.read_csv("Disease_Data_Punjab.csv", index_col=0)
    print(df)


#FOR LINE CHART:

def line_plot():
    df=pd.read_csv("Disease_Data_Punjab.csv")
    df['Districts'] = ['LHR','GRW','SKT','FBD','MLN','IBD','DGK','SRG','GUJ','BWP','RYK','SWL','NWL','KWL']
    District=df["Districts"]
    Confirmed=df["Confirmed"]
    Recovered=df["Recovered"]
    Deaths=df["Deaths"]
    Active=df["Active"]
    plt.xlabel("Districts")

    
    YC = int(input("Enter the number representing your preferred line chart from the above choices: "))
    
    if YC == 1:
        plt.ylabel("Confirmed Cases")
        plt.title("District Wise Confirmed Cases")
        plt.plot(District, Confirmed, color='b')
        plt.show()
    elif YC == 2:
        plt.ylabel("Recovered Cases")
        plt.title("District Wise Recovered Cases")
        plt.plot(District, Recovered, color='g')
        plt.show()
    elif YC == 3:
        plt.ylabel("Death Cases")
        plt.title("District Wise Death Cases")
        plt.plot(District, Deaths, color='r')
        plt.show()
    elif YC == 4:
        plt.ylabel("Active Cases")
        plt.title("District Wise Active Cases")
        plt.plot(District, Active, color='c')
        plt.show()
    elif YC == 5:
        plt.ylabel("Number of cases")
        plt.plot(District, Confirmed, color='b', label = "District Wise Confirmed Cases")
        plt.plot(District, Recovered, color='g', label = "District Wise Recovered Cases")
        plt.plot(District, Deaths, color='r', label = "District Wise Death Cases")
        plt.plot(District, Active, color='c', label = "District Wise Active Cases")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")
        

#FOR BAR GRAPH:

def bar_plot():
    df = pd.read_csv("Disease_Data_Punjab.csv")
    df['Districts'] = ['LHR','GRW','SKT','FBD','MLN','IBD','DGK','SRG','GUJ','BWP','RYK','SWL','NWL','KWL']
    District = df["Districts"]
    Confirmed = df["Confirmed"]
    Recovered = df["Recovered"]
    Deaths = df["Deaths"]
    Active = df["Active"]
    plt.xlabel("Districts")


    YC = int(input("Enter the number representing your preferred bar graph from the above choices: "))
    
    if YC == 1:
        plt.ylabel("Confirmed Cases")
        plt.title("District Wise Confirmed Cases")
        plt.bar(District, Confirmed, color='b', width = 0.5)
        plt.show()
    elif YC == 2:
        plt.ylabel("Recovered Cases")
        plt.title("District Wise Recovered Cases")
        plt.bar(District, Recovered, color='g', width = 0.5)
        plt.show()
    elif YC == 3:
        plt.ylabel("Death Cases")
        plt.title("District Wise Death Cases")
        plt.bar(District, Deaths, color='r', width = 0.5)
        plt.show()
    elif YC == 4:
        plt.ylabel("Active Cases")
        plt.title("District Wise Active Cases")
        plt.bar(District, Active, color='c', width = 0.5)
        plt.show()
    elif YC == 5:
        plt.bar(District, Confirmed, color='b', width = 0.5, label = "District Wise Confirmed Cases")
        plt.bar(District, Recovered, color='g', width = 0.5, label = "District Wise Recovered Cases")
        plt.bar(District, Deaths, color='r', width = 0.5, label = "District Wise Death Cases")
        plt.bar(District, Active, color='c',width = 0.5, label = "District Wise Active Cases")
        plt.legend()
        plt.show()
    elif YC == 6:
        D=np.arange(len(District))
        width=0.25
        plt.bar(D,Confirmed, width, color='b', label = "District Wise Confirmed Cases")
        plt.bar(D+0.25, Recovered, width, color='g', label = "District Wise Recovered Cases")
        plt.bar(D+0.50, Deaths, width, color='r', label = "Districs Wise Death Cases")
        plt.bar(D+0.75, Active ,width, color='c', label = "District Wise Active Cases")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")
        
def scatter_chart():
    df=pd.read_csv("Disease_Data_Punjab.csv")
    df['Districts'] = ['LHR','GRW','SKT','FBD','MLN','IBD','DGK','SRG','GUJ','BWP','RYK','SWL','NWL','KWL']
    District = df["Districts"]
    Confirmed = df["Confirmed"]
    Recovered = df["Recovered"]
    Deaths = df["Deaths"]
    Active = df["Active"]
    
    SC=plt.gca()
    SC=plt.scatter(District, Confirmed, color="b", label="District Wise Confirmed Cases")
    SC=plt.scatter(District, Recovered, color="g", label="District Wise Recovered Cases")
    SC=plt.scatter(District, Deaths, color="r", label="District Wise Death Cases")
    SC=plt.scatter(District, Active, color="c", label="District Wise Active Cases")
    
    plt.xlabel("District")
    plt.title("Complete Scatter Chart")
    plt.legend()
    plt.show()
    
#Termination Phase:

UI()
YC = int(input("Enter Your Choice: "))

while YC == 1 or 2 or 3 or 4 or 5 or 6:

    if YC == 1:
        Read_CSV()
        break
    elif YC == 2:
        No_Index()
        break
    elif YC == 3:
        line_plot()
        break
    elif YC == 4:
        bar_plot()
        break
    elif YC == 5:
        scatter_chart()
        break
    elif YC == 6:
        print("Thank You for using...")
        break
    else: 
        print("Enter valid input")
        break


