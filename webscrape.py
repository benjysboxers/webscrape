import matplotlib.pyplot as plt
import requests
import bs4
import pandas as pd
import os 


 
 
# Make requests from webpage
url = 'https://www.worldometers.info/coronavirus/country/canada/'
result = requests.get(url)
 
 
 
# Creating soap object
soup = bs4.BeautifulSoup(result.text,'lxml')
 
 
 
# Searching div tags having maincounter-number class
cases = soup.find_all('div' ,class_= 'maincounter-number')
 

class Corona:
    data =[]
    cases = '10'
    def __init__(self):
        
        for i in cases:
            span = i.find('span')
            self.data.append(span.string)

#        print(self.data)

    def __repr__(self):
        return(self.data)


print(repr(Corona))

newCases = Corona()
   
# Creating dataframe

df = pd.DataFrame({"Corona Virus Infection Cases in Canada": newCases.data})
df.head(0).style.format({"Corona Cases in Canada": "{:20,.0f}"})

 
# Naming the columns
df.index = ['TotalCases', ' Death', 'Recovered']


# Exporting data into Excel
df.to_csv('Corona_Data.csv')


#Opening Excel File
File = os.path.abspath("Corona_Data.csv")
os.startfile(File)




var = pd.read_csv(os.path.abspath("Corona_Data.csv"))
df = pd.DataFrame(var)
  
X = list(df.iloc[:,0])

Y = list(df.iloc[:,1])

#Line Graph Representation of Statistics
plt.plot(X, Y, color='red', linestyle='dashed')
plt.gca().invert_xaxis() 
plt.gca().invert_yaxis() 
# setting x and y axis range
# naming the x axis
plt.grid(color = 'green', alpha = 0.3, linestyle = '-', linewidth = 2)
plt.xlabel('Situation')
# naming the y axis
plt.ylabel('figures')
 
# giving a title to my graph
plt.title('Most Recent Canada Covid 19 Records')
 
# function to show the plot
plt.show()

