import pandas as pd
import random
import json

         
dataset = pd.read_csv('en_train.csv')

#dataset = dataset.iloc[:90000].values
#dataset = dataset.iloc[5000:10000].values
#dataset = dataset.iloc[5000:10000,:-1].values
sen_id = 0
data = []

input=["is","a","genius","of","plant","in","family","ads","."] # before column
output=["is","a","genius","of","plant","in","family","ads","."] # after column

for index in range(len(dataset)):

    idx =random.randint(0,10000000)
    
    if  (dataset[index][1]) != 0 : # test if we are in a specific sentence
      sen_id = dataset[index][0]
      input.append(dataset[index][3])
      output.append(dataset[index][4])
      
    if (dataset[index][1]) == 0 : # test if we are in out of sentence

      try:
      	      if (dataset[index][1]) >50:
      	      	       input=[]
		      output=[]
      	      else:
		      jason =	{"tid": idx, "index": sen_id, "output": output , "input": input} # create record of a sentence
		      data.append(jason)
		      input=[]
		      output=[]
      except:
      	continue
    
    prec_index = index

      	     
with open('data_train.json', 'w') as outfile:
    json.dump(data, outfile)

