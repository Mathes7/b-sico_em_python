from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
dados = datasets.load_iris()

df = dados.data

df = pd.DataFrame(df)
df.columns = dados.feature_names

df['target'] = dados.target

df_0 = df.loc[df['target']==0]
df_1 = df.loc[df['target']==1]
df_2 = df.loc[df['target']==2]

for i in df.columns[:4]:
    for j in df.columns[:4]:
        plt.figure(figsize=(8,4))
        plt.scatter(df_0[i],df_0[j],label=dados.target_names[0])
        plt.scatter(df_1[i],df_1[j],label=dados.target_names[1])
        plt.scatter(df_2[i],df_2[j],label=dados.target_names[2])
        plt.legend()
        plt.xlabel(i)
        plt.ylabel(j)
        plt.title(i+' x '+j)

for a in df.columns[:3]:
    for b in df.columns[:3]:
        plt.figure(figsize=(8,4))
        plt.scatter(df_0[a],df_0[b],label=dados.target_names[0])
        plt.scatter(df_1[a],df_1[b],label=dados.target_names[1])
        plt.scatter(df_2[a],df_2[b],label=dados.target_names[2])
        plt.legend()
        plt.xlabel(a)
        plt.ylabel(b)
        plt.title(a+' x '+b)

for c in df.columns[:2]:
    for d in df.columns[:2]:
        plt.figure(figsize=(8,4))
        plt.scatter(df_0[c],df_0[d],label=dados.target_names[0])
        plt.scatter(df_1[c],df_1[d],label=dados.target_names[1])
        plt.scatter(df_2[c],df_2[d],label=dados.target_names[2])
        plt.legend()
        plt.xlabel(c)
        plt.ylabel(d)
        plt.title(c+' x '+d)
        
for e in df.columns[:1]:
    for f in df.columns[:1]:
        plt.figure(figsize=(8,4))
        plt.scatter(df_0[e],df_0[f],label=dados.target_names[0])
        plt.scatter(df_1[e],df_1[f],label=dados.target_names[1])
        plt.scatter(df_2[e],df_2[f],label=dados.target_names[2])
        plt.legend()
        plt.xlabel(e)
        plt.ylabel(f)
        plt.title(e+' x '+f)

for i in df.columns[:4]:
    
    mean_0 = df_0[i].mean()
    mean_1 = df_1[i].mean()
    mean_2 = df_2[i].mean()
    
    median_0 = df_0[i].median()
    median_1 = df_1[i].median()
    median_2 = df_2[i].median()
    
    std_0 = df_0[i].std()
    std_1 = df_1[i].std()
    std_2 = df_2[i].std()
    
    count_0 = df_0[i].count()
    count_1 = df_1[i].count()
    count_2 = df_2[i].count()
    
    fig,axs = plt.subplots(2,2)
    fig.suptitle(i)
    axs[0,0].bar(dados.target_names,[mean_0,mean_1,mean_2])
    axs[0,0].set(ylabel = 'mean')
    axs[0,1].bar(dados.target_names,[median_0,median_1,median_2])
    axs[0,1].set(ylabel = 'median')
    axs[1,0].bar(dados.target_names,[std_0,std_1,std_2])
    axs[1,0].set(ylabel = 'std')
    axs[1,1].bar(dados.target_names,[count_0,count_1,count_2])
    axs[1,1].set(ylabel = 'count')



plt.figure()
plt.hist(df_0[a],bins=20,label=dados.target_names[0])
plt.hist(df_1[a],bins=20,label=dados.target_names[1])
plt.hist(df_2[a],bins=20,label=dados.target_names[2])
plt.legend()
plt.title('petal length de todas as plantas')

plt.figure()
plt.hist(df_0[e],bins=20,label=dados.target_names[0])
plt.hist(df_1[e],bins=20,label=dados.target_names[1])
plt.hist(df_2[e],bins=20,label=dados.target_names[2])
plt.legend()
plt.title('setal length de todas as plantas')

plt.figure()
plt.hist(df_0[c],bins=20,label=dados.target_names[0])
plt.hist(df_1[c],bins=20,label=dados.target_names[1])
plt.hist(df_2[c],bins=20,label=dados.target_names[2])
plt.legend()
plt.title('setal width de todas as plantas')

plt.figure()
df_0.hist(column='sepal length (cm)', bins=100)
plt.title('sepal lenght da planta 0')
plt.figure()
df_0.hist(column='sepal width (cm)', bins=100)
plt.title('sepal width da planta 0')
plt.figure()
df_0.hist(column='petal length (cm)', bins=100)
plt.title('petal length da planta 0')
plt.figure()
df_1.hist(column='sepal length (cm)', bins=100)
plt.title('sepal length da planta 1')
plt.figure()
df_1.hist(column='sepal width (cm)', bins=100)
plt.title('sepal width da planta 1')
plt.figure()
df_1.hist(column='petal length (cm)', bins=100)
plt.title('petal length da planta 1')
plt.figure()
df_2.hist(column='sepal length (cm)', bins=100)
plt.title('sepal length da planta 2')
plt.figure()
df_2.hist(column='sepal width (cm)', bins=100)
plt.title('sepal width da planta 2')
plt.figure()
df_2.hist(column='petal length (cm)', bins=100)
plt.title('petal length da planta 2')



plt.figure()
plt.boxplot(df[a])
plt.title('petal length de todas as plantas')
plt.figure()
plt.boxplot(df[e])
plt.title('sepal length de todas as plantas')
plt.figure()
plt.boxplot(df[c])
plt.title('sepal width de todas as plantas')

plt.figure()
plt.boxplot(df_0)
plt.title('informações gerais da planta 0')
plt.figure()
plt.boxplot(df_0[a])
plt.title('petal length da planta 0')
plt.figure()
plt.boxplot(df_0[e])
plt.title('sepal length da planta 0')
plt.figure()
plt.boxplot(df_0[c])
plt.title('sepal width da planta 0')

plt.figure()
plt.boxplot(df_1)
plt.title('informações gerais da planta 1')
plt.figure()
plt.boxplot(df_1[a])
plt.title('petal length da planta 1')
plt.figure()
plt.boxplot(df_1[e])
plt.title('sepal length da planta 1')
plt.figure()
plt.boxplot(df_1[c])
plt.title('sepal width da planta 1')

plt.figure()
plt.boxplot(df_2)
plt.title('informações gerais da planta 2')
plt.figure()
plt.boxplot(df_2[a])
plt.title('petal length da planta 2')
plt.figure()
plt.boxplot(df_2[e])
plt.title('sepal length da planta 2')
plt.figure()
plt.boxplot(df_2[c])
plt.title('sepal width da planta 2')

plt.figure()
plt.plot(df_0[c],label=dados.target_names[0])
plt.plot(df_1[c],label=dados.target_names[1])
plt.plot(df_2[c],label=dados.target_names[2])
plt.legend()
plt.title('setal width de todas as plantas')
plt.figure()
plt.plot(df_0[a],label=dados.target_names[0])
plt.plot(df_1[a],label=dados.target_names[1])
plt.plot(df_2[a],label=dados.target_names[2])
plt.legend()
plt.title('petal lenght de todas as plantas')
plt.figure()
plt.plot(df_0[e],label=dados.target_names[0])
plt.plot(df_1[e],label=dados.target_names[1])
plt.plot(df_2[e],label=dados.target_names[2])
plt.legend()
plt.title('setal lenght de todas as plantas')

plt.figure()
plt.plot(df_0[c],label=dados.target_names[0])
plt.legend()
plt.title('setal width da planta 0')
plt.figure()
plt.plot(df_1[c],label=dados.target_names[1])
plt.legend()
plt.title('setal width da planta 1')
plt.figure()
plt.plot(df_2[c],label=dados.target_names[2])
plt.legend()
plt.title('setal width da planta 2')

plt.figure()
plt.plot(df_0[e],label=dados.target_names[0])
plt.legend()
plt.title('setal lenght da planta 0')
plt.figure()
plt.plot(df_1[e],label=dados.target_names[1])
plt.legend()
plt.title('setal lenght da planta 1')
plt.figure()
plt.plot(df_2[e],label=dados.target_names[2])
plt.legend()
plt.title('setal lenght da planta 2')

plt.figure()
plt.plot(df_0[c],label=dados.target_names[0])
plt.legend()
plt.title('setal width da planta 0')
plt.figure()
plt.plot(df_1[c],label=dados.target_names[1])
plt.legend()
plt.title('setal width da planta 1')
plt.figure()
plt.plot(df_2[c],label=dados.target_names[2])
plt.legend()
plt.title('setal width da planta 2')

plt.figure()
plt.plot(df_0[a],label=dados.target_names[0])
plt.legend()
plt.title('petal lenght da planta 0')
plt.figure()
plt.plot(df_1[a],label=dados.target_names[1])
plt.legend()
plt.title('petal lenght da planta 1')
plt.figure()
plt.plot(df_2[a],label=dados.target_names[2])
plt.legend()
plt.title('petal lenght da planta 2')

from scipy import stats
import scipy as scipy 
import numpy as np


stats.shapiro(df[a])

stats.shapiro(df[c])

stats.shapiro(df[e])

stats.shapiro(df_0[a])

stats.shapiro(df_0[c])

stats.shapiro(df_0[e])

stats.shapiro(df_1[a])

stats.shapiro(df_1[c])

stats.shapiro(df_1[e])

stats.shapiro(df_2[a])

stats.shapiro(df_2[c])

stats.shapiro(df_2[e])


import seaborn as sns
media = df.groupby('target').mean()
cont = 0
for j in df.columns[:-1]:
    cont2 = 0
    resposta = {}
    for i in media.index:
        df2 = df.loc[df['target'] == i][j]
        cont = cont + 1
        shap = stats.shapiro(df2)
        shap = shap[1]
        shap = round(shap,2)
        if shap > 0.05:
            resp = 'Normal.'
        else:
            resp = 'Not normal.'
        print(f'Para a classe {i} e categoria {j}: ')
        print(f'p-value = {shap}. {resp}')
        resposta[i] = resp
    plt.figure()
    sns.histplot(data=df,x=j,hue='target',bins=50)
    plt.title(j)
    plt.xlabel(str(resposta))
    
media = df.groupby('target').mean()
cont = 0
for j in df.columns[:-1]:
    cont2 = 0
    resposta = {}
    for i in media.index:
        df2 = df.loc[df['target'] == i][j]
        cont = cont + 1
        shap = stats.shapiro(df2)
        shap = shap[1]
        shap = round(shap,2)
        if shap > 0.05:
            resp = 'Normal.'
        else:
            resp = 'Not normal.'
        print(f'Para a classe {i} e categoria {j}: ')
        print(f'p-value = {shap}. {resp}')
        resposta[i] = resp
    plt.figure()
    sns.histplot(data=df,x=j,hue='target',bins=50)
    plt.title(j)
    plt.xlabel(str(resposta))
    
#%% teste de hípoteses para tentar acertar as plantas

x =[]
for i in df['petal length (cm)']:
    if i <= 2:
        x .append(0)
    elif i > 2 and i <= 4.8:
        x.append(1)
    elif i > 4.81:
        x.append(2)
        
df.insert(loc = 5, column = 'tentativa de acertos', value = x)
df['tentativa de acertos'].value_counts()
df['target'].value_counts()

#%% comparando a coluna de tentativa de previsão com a coluna target
xt = (df['tentativa de acertos'] == df['target'])
       
xt.value_counts()

acertos = (143*100)/150

