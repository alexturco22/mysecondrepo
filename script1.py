#### PROBLEM 1 ####
# Correc the mistakes and produce the following output:
# Johnny, the total of your purchase is $1,688.70

def calcTotal(amt,tax,name):
    mytotal = amt * (1+tax)
    print(f"{myname}, the total of your purchase is ${mytotal:,.2f}")     #within the {} it should be mytotal and not total.

myname = 'Johnny'
price = 1560            #cant use a comma in 1,560
thetax = 0.0825          #has to be 0.0825 and not 8.25%
                                
                                 #1) name should be changed to myname
calcTotal(price,thetax,myname)     #2) when calling the function, the order of the arguments have to match line 5. 
                                        #- Instead of "thetax, price, name" it should be "price, thetax, name"





####  PROBLEM 2  ####
# print out ONLY the integers in the list below #
list1 = [1,'two',3.2,'four',5]

for i in list1:         
    if type(i) == int:                        #have to make an if statement here for the integers
        print(i)




#### PROBLEM 3 ####
# install the right library for the code below
# to work properly. The output will be a map.
# the filename is Baylor.html and it should
# open up in your browser. The library is Plotly.

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

lons = [-97.121041]
lats = [31.546872]
hover_texts = ['Baylor University<br>Enrollemt: 19,297<br>Male: 7,718<br>Female: 11,579']


data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'hovertext':hover_texts,
    'hoverinfo':"text",
    'marker': {'size':10,}
    }]

my_layout = Layout(title='Baylor University',geo_scope='usa')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='Baylor.html')
