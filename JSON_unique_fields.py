#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''The task: create two JSON files with 3 people in each JSON file. 
A single person will occur in both JSON files. The others are unique to each file.
Each person has three properties (first name, last name and email address).
Ingest the JSON files and return a list of unique people - check that no other person has 
a combination of the same names or email address.'''


# In[ ]:


import json


# In[38]:


#Create the JSON files from scratch

# Data to be written
json3_dict = {
  "person1": {
    "firstname": "joe",
    "lastname": "smith",
    "email": "joesmith@email.com"
  },
  "person2": {
    "firstname": "jane",
    "lastname": "doe",
    "email": "janedoe@email.com"
  },
  "person3": {
    "firstname": "mike",
    "lastname": "matthews",
    "email": "mikematthews@email.com"
  }
}

json4_dict = {
  "person4": {
    "firstname": "joe",
    "lastname": "smith",
    "email": "joesmith@email.com"
  },
  "person5": {
    "firstname": "sarah",
    "lastname": "samuels",
    "email": "sarahsameuls@email.com"
  },
  "person6": {
    "firstname": "ben",
    "lastname": "banks",
    "email": "benbanks@email.com"
  }
}



# Serializing json
json_object3 = json.dumps(json3_dict, indent=4)
json_object4 = json.dumps(json4_dict, indent=4)
    
# Writing to file3.json
with open("file3.json", "w") as outfile:
    outfile.write(json_object3)
    
# Writing to file4.json
with open("file4.json", "w") as outfile:
    outfile.write(json_object4)    


# In[40]:


#read the JSON files


with open("file3.json") as json3_file:
    json_data3 = json.load(json3_file)
    
with open("file4.json") as json4_file:
    json_data4 = json.load(json4_file)    

#instatiate an empty dictionary which will store persons and a list of their [firstname, lastname and email]
new_dict = {}    
    
#make a combined dictionary from the two files (this won't exclude duplicates)
json_data3.update(json_data4)

#print the combined dictionary (no duplicates excluded)
print("Combined dict: ", json_data3, "\n")

print("Combined dict: ", json_data3.keys(), "\n")

for person in json_data1:
    properties_list = []
    #print(person, json_data1[person])
    
    for thing in json_data3[person]:
        properties_list.append(json_data3[person][thing])
    
    if properties_list not in new_dict.values():
        new_dict[person] = properties_list
        
print("New dict: ", new_dict, "\n")

print("New dict: ", new_dict.keys())


# In[ ]:





# In[ ]:





# In[ ]:




