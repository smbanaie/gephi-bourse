import pandas as pd
df = pd.read_csv("news_tags.csv")
tag = list(df['tags'])

my_list=[]
for i in range(0,len(tag)):
    if "بورس" in tag[i].replace(" ", "").split("^"):
        temp = tag[i].split("^")
        for j in temp:
            if j!="بورس":
                my_list.append(j)
        


weight = ['1' for i in range(len(my_list))]
temp_dframe = pd.DataFrame()
temp_dframe['target']=my_list
temp_dframe['weight'] = weight
gbtarget=temp_dframe.groupby(['target']).count()
target_it = dict(gbtarget['weight'])



main_df = pd.DataFrame()
main_df['source'] = ['بورس' for i in range(len(list(target_it.keys())))]
main_df['target']=list(target_it.keys())
main_df['weight']=list(target_it.values())
main_df2=main_df[['source','target','weight']]
main_df2.sort_values(by=['weight'],ascending=False,inplace=True)
main_df2.to_csv('stw1.csv', index=False)