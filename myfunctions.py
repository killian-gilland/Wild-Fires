import pandas as pd
import datetime as dt
import re

def fct1(chemin, i):
    df = pd.read_csv(chemin, skiprows = i, delimiter = ";")
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace("'", '_').astype(str)
    df["Année"] = df["Année"].astype("Int64")
    df["Numéro"] = df["Numéro"].astype("Int64")
    df["Type_de_feu"] = df["Type_de_feu"].astype("Int64")#*df["Année"].astype("Int64")
    df["Origine_de_l_alerte"] = df["Origine_de_l_alerte"].astype("Int64")
    df["Surface_parcourue_(m2)"] = df["Surface_parcourue_(m2)"].astype("Int64")
    #df = df.reindex(df["Numéro"])
    #df = df.rename(index=df['Numéro'])
    df["Commune"] = df["Commune"].fillna("No Commune")
    df["Lieu-dit"] = df["Lieu-dit"].fillna("No Lieu-dit")
    df["Commune"] = df["Commune"].str.title()
    df["Lieu-dit"] = df["Lieu-dit"].str.title()
    date = []
    heure = []
    x = []
    for i in range(len(df["Alerte"])):
        x.append(re.split("\s", str(df["Alerte"][i])))
    for i in range(len(x)):
        date.append(x[i][0])
        heure.append(x[i][1])
    df = df.assign(date = date)
    df = df.assign(heure = heure)
    df = df.rename(columns = {'Surface_parcourue_(m2)':'Surface_parcourue'})
    df["Surface_parcourue"] = df["Surface_parcourue"] / 10000
    df = df.drop("Alerte", axis=1)
    #df = df.drop("Numéro", axis=1)
    
    return df


df = fct1("C:/Users/33698/Documents/M2_EBDS/cours/data/liste_incendies_ du_12_08_2022.csv", 2)




import numpy as np

def function1():
    dep = input('Enter the department on which you wanna count the number of fires:')
    y = input('Enter the year associate:')
    dep = str(dep)
    y = int(y)
    if (dep == 'all'):
        return print('the total number of fires in France in the year', y, 'is :\n', np.count_nonzero(df["Année"] == y))
    else :
        return print('the total number of fires in France in the year', y, ' in the department ', dep, ' is :\n', np.count_nonzero((df["Département"] == dep) & (df["Année"] == y)))
    
    
    
    
    
    
    
    
def function2():
    dep = input('Enter the department on which you wanna sum the burnt area:')
    y = input('Enter the year associate:')
    dep = str(dep)
    y = int(y)
    if (dep == 'all'):
        return print('the burnt area total of the France in the year', y, 'is :\n', df.loc[(df['Année'] == y), 'Surface_parcourue'].sum(), 'ha')
    else:
        return print('the burnt area total of the department', dep,'in the year', y, 'is :\n', df.loc[(df['Année'] == y) & (df['Département'] == dep) , 'Surface_parcourue'].sum(), 'ha')
    
    
    
    
    
    
    
    
    
def function3():
    dep = input('Enter the department on which you wanna see some descriptive statistics of the burnt area:')
    y = input('Enter the year associate:')
    dep = str(dep)
    y = int(y)
    if (dep == 'all'):
        return print('The Q1, median, Q3 of the burnt area in France of the year', y, 'is :\n', df.loc[df['Année'] == y, 'Surface_parcourue'].quantile(q=[0.25, 0.5, 0.75]), '\n\nThe mean of the same year is :\n', df.loc[df['Année'] == y, 'Surface_parcourue'].mean(), 'ha')
    else:
        return print('The Q1, median, Q3 of the burnt area in the department', dep, 'of the year', y, 'is :\n', df.loc[(df['Année'] == y) & (df['Département']== dep), 'Surface_parcourue'].quantile(q=[0.25, 0.5, 0.75]),'\n\nThe mean of the same department and year is :\n', df.loc[(df['Année'] == y) & (df['Département']== dep), 'Surface_parcourue'].mean(), 'ha')
    
    
    
    
    
def function2b(dep, y):
    return df.loc[(df['Année'] == y) & (df['Département'] == dep) , 'Surface_parcourue'].sum()







import matplotlib
import matplotlib.pyplot as plt

def function22():
    dep = input('Enter the department on which you wanna sum the evolution of the burnt area:')
    dep = str(dep)
    for y in range(2000, 2023):
        plot = plt.scatter(y, function2b(dep, y), color = 'orange')
    plt.xlabel("year")
    plt.ylabel("area burnt in ha")
    chemin2 = print('C:/Users/33698/Documents/M2 EBDS/cours/data/',dep,'_graph_over_years.jpg')
    print(chemin2)
    #plt.savefig(str(chemin2))
    return plot










