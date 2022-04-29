import pandas as pd
import random
import os

# Read the source 
df = pd.read_csv('../data/processed/author-parse-articles.csv')

donelist = pd.read_csv('./donelist.csv')
donelist_list = donelist['0'].to_list()
# print(donelist.columns)

# Getting Domains From News Websites 
m = df['art_article_url'].str.extract('(?<=http://)(.*?)(?=/)|(?<=https://)(.*?)(?=/)')
m = m[0].fillna(m[1]).fillna(df['art_article_url'])
df['art_extracted_domain'] = m


df.groupby('art_extracted_domain')['art_extracted_domain'].count().sort_values(ascending=False)


most_scraped = list(df.groupby('art_extracted_domain')['art_extracted_domain'].count().sort_values(ascending=False)[:50].index)

df_filtered = df[~df['art_extracted_domain'].isin(most_scraped)]

# Adding a column for cleaning indentation
df_filtered['art_processed'] = 0

# Index for columns that are processed 
done = [] 


df_filtered = df_filtered.reset_index()

import time
random_seed = random.randint(0,90000)
while True : 
    
    os.system("clear")
    
    index = random.randint(0, len(df_filtered))
    print(f'Reading Index {index}')
    if index in donelist_list :
        print('Already in list, Skipping')
        continue
    else:
        ref = df_filtered.loc[index]['ref_title']
        art = df_filtered.loc[index]['art_article_text']
        
        print(f'REF:\n {ref}')
        print(f'ART:\n {art}')
        
        
        flag = int(input('-1: removed\n1: good \n2: sumary\n0: end'))
        
        if flag == 0 :
            break 

        time.sleep(5)
        print(f'appending index {index}')
        df_filtered.iat[index, df_filtered.columns.get_loc('art_processed')] = flag
        df_filtered.to_csv(f'../data/processed/manual-parse-articles-{random_seed}.csv')
        donelist_list.append(index)
        donelist.append(pd.Series(index),ignore_index=True )
        donelist.to_csv('./donelist.csv')
    
    