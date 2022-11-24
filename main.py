import pandas as pd
import numpy as np
import openpyxl
import tabula


'''df = pd.read_csv('pokemon_data.csv')'''

df=pd.read_excel('KCET 2020 Eng 2nd Extended round Cutoff (1).xlsx',sheet_name='Table 1')
kc='KCET 2020 Eng 2nd Extended round Cutoff (1).xlsx'


#kcet= openpyxl.load_workbook(kc)
#kcet.active


'''print(df.head(2))
print(df[['Name','Speed']][0:5])'''
#print(df.columns + str(len(df.columns))) #only for header columns
#print(df.iloc[:,0])#printing a particular column by slicing

#df.isnull() is a function which takes in an obj i.e  row/s or column/s or a cell/s as input and prints True/false in
#place of of each element(cell) (true only if its non empty else false).

list_college=[]

#df.iloc[:,0].str.split().str.join(' ')


'''for i in range(len(df.axes[0])):
    print(str(i)+"  "+str(df.iloc[i,1])+" "+str(pd.isnull(df.iloc[i,1])))'''


'''df.iloc[:,0] = df.iloc[:,0].apply(lambda x: str(x).replace(u'\xa0', u' '))#very imp since spaces or breaks are stored as unicode '/xa0' when imported from excel to pandas
#but use this only if you need to actually print things.coz this affects the 'nan' values i.e empty cells and they wont be detected using isnull().So use this after using isnull()
to avoid the hinderance'''


df.insert(0,"College",[None]*len(df.axes[0]))   #Creates empty column at a specified position .Note here 3rd operand creates an empty list of size equal to number of rows.

#df.to_excel('kcet_rank.xlsx')
#df.axes[0]=rows and df.axes[1]=columns
# #df["College"]="" #Creates an empty column
#df[["College","Branch"]]  #use a list to show which column/rows you need to consider and then give that as input for dataframe incase of multiple row /& columns (nested)
#print(type(df[["College","Branch"]])) #since this has multiple row/column its like table and is of type dataframe
#print(type(df)) #df is a table and is of type data frame
#print(type(df["College"])#single row/column is of type series(pd series) which is similar to list
'''Basically dataframe functions (the ones operating on df)can be ony used for that data type i.e dataframe which is a table or a subset of it containing multiple row/column)
 So we cant use those function on a series or a single element.(Some exceptions are there)'''


k="UVCE"
del_row=[]
j=0
for i in df.iloc[:,1]:            #change the column index since we inserted college column at begining

    if pd.isnull(i)==False and i[0]=='E' and i[1].isdigit()==True:
        list_college.append(i)
        k=i
        del_row.append(j)#storing indices of rows to be deleted i.e the clg name row .

        #print("Hi"+str(k)+"titljis "+str(j))

    else:         #keep adding clg till none is encountered since begining of 0th column is null for every new clg.Note keep outside if condn since none doesnt occur here
        '''if pd.isnull(df.iloc[j,1])==True:
            del_row.append(j)'''#storing indices of all empty cells in branch(index 1) column i.e the row next to clg name which has categories and empty row in between for branches
                                #whose name is long and is assigned two rows and only one has ranks and other is empty.

        df["College"][j]=k    #csingle column is a series hence direct indexing/slicing can be done

        
        #print("Nooo"+str(k)+"jis"+str(j)+i)
    j=j+1

#print(list_college)
#print(del_row)
df.drop(labels=del_row, axis=0,inplace=True) #deleting rows(axis=0) whose indices are i del_row
                                      #note here indices of df dont change even after deleting rows.
df.dropna(inplace=True)#drop the row if it contains any null values.so this takes care of all the nulls after the clg names (containing categories) and the large branch names one(like IM )
                       #df.dropna() by default(without inplace=true)returns new dataset with nan containing rows deleted

df.reset_index(drop=True,inplace=True)#reset index creates a new column named index by default hence we have to specify drop as true to delete that extra column.inplace as we know
                                        #is for change directly to df rather than a copy

 #VVIMP You can only traverse any row/column once you reset all indices since few are missing due to deletion

print(len(df.axes[0]))
for i in range(len(df.axes[0])):
    if isinstance(df['GM'][i],str):
        df['GM'][i]=np.nan


'''def sorted_rank(rank):
    #if rank.isnull().any():
        #return rank
    if isinstance(rank,str):
        return int(400000)
    else:
        return rank'''

df.sort_values(by = "GM",inplace=True) # GM or GMH
#lambda x:np.nan if x.isnull()==False and x[0].isdigit==False else(int(x) if x.isnull==False else x)


fn='sorted.xlsx'
df.to_excel(fn) #close the file and try
#print(df.iloc[:26,0:2])
'''print(df.iloc[27,1])
series=pd.isnull(df["Branch"][0:28])
print(series)'''
print(df.head())
'''for i in range(len(df.axes[0])):
    print(str(i)+"  "+str(df.iloc[i,1])+" "+str(pd.isnull(df.iloc[i,1])))'''
'''for i in df["GM"]:
    print(str(type(i))+" "+str(i))'''

