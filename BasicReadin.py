

#import plotly.plotly as py
#import plotly.tools as tls
import matplotlib as plt
#from plotly.graph_objs import Figure, Data, Layout
import pandas as pd

#tls.set_credentials_file(username="########", api_key="########")
                    
Dataset1 = pd.read_csv('DenverCOTemp.csv')
Dataset2 = pd.read_csv('ElizabethCOTemp.csv')

Dataset1.columns = ['Month','Denver_High_Temp_(C)','Denver_Low_Temp_(C)']
Dataset2.columns = ['Month','Elizabeth_High_Temp_(C)','Elizabeth_Low_Temp_(C)']

Merged_Data = pd.merge(Dataset1,Dataset2, how = 'inner')
X = range(1,13)
#List_Data = Merged_Data.to_dict()
#List_Data = Merged_Data.values.tolist()
fig = plt.pyplot.plot()
plt.pyplot.plot(X,Merged_Data['Denver_High_Temp_(C)'],label='Denver_High_Temp_(C)')
plt.pyplot.plot(X,Merged_Data['Denver_Low_Temp_(C)'],label='Denver_Low_Temp_(C)')
plt.pyplot.plot(X,Merged_Data['Elizabeth_High_Temp_(C)'],label='Elizabeth_High_Temp_(C)')
plt.pyplot.plot(X,Merged_Data['Elizabeth_Low_Temp_(C)'],label='Elizabeth_Low_Temp_(C)')
plt.pyplot.xticks(X,Merged_Data['Month'],rotation='vertical')
plt.pyplot.legend(loc='upper left',prop={'size':8})


#test = py.plot_mpl(fig)