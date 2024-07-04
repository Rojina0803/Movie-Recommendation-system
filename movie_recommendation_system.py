import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt 

column_names=['user_id','item_id','rating','timestamp']
df=pd.read_csv('u.data',sep='\t',names=column_names) #SEPERSTOR:/t seperates data by TAB
# print(df.head())

movie_titles=pd.read_csv('Movie_Id_Titles')
# print(movie_titles.head())

df=pd.merge(df,movie_titles, on='item_id')
# print(df.head(3))

##EDA
# print(df.groupby('title')['rating'].mean().sort_values(ascending=False))
# print(df.groupby('title')['rating'].count().sort_values(ascending=False))

ratings=pd.DataFrame(df.groupby('title')['rating'].mean())
# print(ratings)

ratings['rate_count']=pd.DataFrame(df.groupby('title')['rating'].count())
# print(ratings)

# ratings['rate_count'].hist(bins=100)
plt.hist(x=ratings['rate_count'] ,bins=100)
# plt.show()

movie_mat=df.pivot_table(index='user_id',columns='title',values='rating')
# print(movie_mat)

starwars_rating=movie_mat['Star Wars (1977)']
# print(starwars_rating)

similar_to_starwars=movie_mat.corrwith(starwars_rating) #cosine similarity
# print(similar_to_starwars)

sorted=similar_to_starwars.sort_values(ascending=False)
# print(sorted)

corr_starwars=pd.DataFrame(similar_to_starwars,columns=['Corr'])
corr_starwars.dropna(inplace=True)
corr_starwars.sort_values('Corr',ascending=False)
corr_starwars=corr_starwars.join(ratings['rate_count'])
corr_starwars[corr_starwars['rate_count']>100].sort_values('Corr',ascending=True)
# print(corr_starwars)