#choose a data set, a variable to show the evolution through time, outputFilename to save output, monthly and yearly are boolean variables
#If both are passed as false, return daily graph
#if monthly or yearly is passed as true, return monthly or yearly graph respectively
#Both cannot be simultaneously true
import re
import pandas as pd
import numpy as np
import plotly.express as px

def timechart(data,var,cumulative,monthly=None,yearly=None):
#convert csv to pandas 
    if type(data)==str:
        data=pd.read_csv(data)
#Extract day from document     
    day=[]
    for i in range(0,len(data)):
        day.append(re.search('\d.*\d',data['Document'][i])[0])
    data['day']=day
#Extract month and year   
    month=[]
    year=[]
    for i in range(0,len(data)):
        month.append(data['day'][i][0:7])
        year.append(data['day'][i][0:4])
    data['month']=month
    data['year']=year
#Plot corresponding graph depending on the options 
    if cumulative==False:
        #monthly and yearly can't simultaneously be True
        if monthly==True and yearly==True:
            return "Choose one of the following: daily graph, monthly graph, yearly graph"

        elif monthly==True:#If monthly is True, return monthly non-cumulative graph
            data=data.sort_values('month')
            finalframe=pd.DataFrame()
            for i in sorted(set(data['month'])):
                tester=pd.DataFrame(data[data['month']==i][var].value_counts()).reset_index().rename(columns={'index':var,var:'Frequency'})
                for j in set(data[var]):
                    if j not in set(tester[var]):
                        temp=pd.DataFrame([j,0]).T.rename(columns={0:var}).rename(columns={0:var,1:'Frequency'})
                        tester=pd.concat([tester,temp])
                tester=tester.sort_values(var)
                tester
                date=np.repeat(i,len(tester))
                tester['date']=date
                tester=tester.reset_index(drop=True)
                finalframe=pd.concat([finalframe,tester])
            fig=px.bar(finalframe,var,'Frequency',animation_frame='date').update_xaxes(categoryorder='total ascending')

        elif yearly==True:#If yearly is True, return yearly non-cumulative graph
            data=data.sort_values('year')
            finalframe=pd.DataFrame()
            for i in sorted(set(data['year'])):
                tester=pd.DataFrame(data[data['year']==i][var].value_counts()).reset_index().rename(columns={'index':var,var:'Frequency'})
                for j in set(data[var]):
                    if j not in set(tester[var]):
                        temp=pd.DataFrame([j,0]).T.rename(columns={0:var}).rename(columns={0:var,1:'Frequency'})
                        tester=pd.concat([tester,temp])
                tester=tester.sort_values(var)
                tester
                date=np.repeat(i,len(tester))
                tester['date']=date
                tester=tester.reset_index(drop=True)
                finalframe=pd.concat([finalframe,tester])
            fig=px.bar(finalframe,var,'Frequency',animation_frame='date').update_xaxes(categoryorder='total ascending')
        else:#If neither is True, return daily non-cumulative graph
            data=data.sort_values('day')
            finalframe=pd.DataFrame()
            for i in sorted(set(data['day'])):
                tester=pd.DataFrame(data[data['day']==i][var].value_counts()).reset_index().rename(columns={'index':var,var:'Frequency'})
                for j in set(data[var]):
                    if j not in set(tester[var]):
                        temp=pd.DataFrame([j,0]).T.rename(columns={0:var}).rename(columns={0:var,1:'Frequency'})
                        tester=pd.concat([tester,temp])
                tester=tester.sort_values(var)
                tester
                date=np.repeat(i,len(tester))
                tester['date']=date
                tester=tester.reset_index(drop=True)
                finalframe=pd.concat([finalframe,tester])
            fig=px.bar(finalframe,var,'Frequency',animation_frame='date').update_xaxes(categoryorder='total ascending')
    else:
        if monthly==True and yearly==True:
            return "Choose one of the following: daily graph, monthly graph, yearly graph"
        elif yearly==True:#If yearly is True, return yearly cumulative graph
            data=data.sort_values('year')
            finalframe=pd.DataFrame()
            for i in sorted(set(data['year'])):
                tester=pd.DataFrame(data[data['year']<=i][var].value_counts()).reset_index().rename(columns={'index':var,var:'Frequency'})
                for j in set(data[var]):
                    if j not in set(tester[var]):
                        temp=pd.DataFrame([j,0]).T.rename(columns={0:var}).rename(columns={0:var,1:'Frequency'})
                        tester=pd.concat([tester,temp])
                tester=tester.sort_values(var)
                tester
                date=np.repeat(i,len(tester))
                tester['date']=date
                tester=tester.reset_index(drop=True)
                finalframe=pd.concat([finalframe,tester])
            fig=px.bar(finalframe,var,'Frequency',animation_frame='date').update_xaxes(categoryorder='total ascending')
        elif monthly==True:#If monthly is True, return monthly cumulative graph
            data=data.sort_values('month')
            finalframe=pd.DataFrame()
            for i in sorted(set(data['month'])):
                tester=pd.DataFrame(data[data['month']<=i][var].value_counts()).reset_index().rename(columns={'index':var,var:'Frequency'})
                for j in set(data[var]):
                    if j not in set(tester[var]):
                        temp=pd.DataFrame([j,0]).T.rename(columns={0:var}).rename(columns={0:var,1:'Frequency'})
                        tester=pd.concat([tester,temp])
                tester=tester.sort_values(var)
                tester
                date=np.repeat(i,len(tester))
                tester['date']=date
                tester=tester.reset_index(drop=True)
                finalframe=pd.concat([finalframe,tester])
            fig=px.bar(finalframe,var,'Frequency',var,animation_frame='date').update_xaxes(categoryorder='total ascending')
        else:#If neither is True, return daily cumulative graph
            data=data.sort_values('day')
            finalframe=pd.DataFrame()
            for i in sorted(set(data['day'])):
                tester=pd.DataFrame(data[data['day']<=i][var].value_counts()).reset_index().rename(columns={'index':var,var:'Frequency'})
                for j in set(data[var]):
                    if j not in set(tester[var]):
                        temp=pd.DataFrame([j,0]).T.rename(columns={0:var}).rename(columns={0:var,1:'Frequency'})
                        tester=pd.concat([tester,temp])
                tester=tester.sort_values(var)
                tester
                date=np.repeat(i,len(tester))
                tester['date']=date
                tester=tester.reset_index(drop=True)
                finalframe=pd.concat([finalframe,tester])
            fig=px.bar(finalframe,var,'Frequency',animation_frame='date').update_xaxes(categoryorder='total ascending')

    fig=fig.update_geos(projection_type="equirectangular", visible=True, resolution=110)
    return fig