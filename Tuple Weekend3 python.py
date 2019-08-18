#!/usr/bin/env python
# coding: utf-8

# In[2]:


tuples=("India",pakistan,"Australia","canada")
print (tuples)


# In[3]:


tuples=("India",'pakistan',"Australia","canada")
print (tuples[3])


# In[8]:


tuples=("India","pakistan","Australia","canada")
print(tuples)
a=("India","pakistan","Australia","canada")
print(a)


# In[7]:


tuples=("India",'pakistan',"Australia","canada")
print(tuples[1:])


# In[10]:


mylist=["Modi","Trump","Imran"]
mytuple=tuple(mylist)
print(mytuple)
print(mylist)


# In[11]:


mylist=["Modi","Trump","Imran"]
mytuple=tuple(mylist)
print(mytuple)
print(mylist)
mytuple[2]="morrison"
print(mytuple)


# In[13]:


tuples=("India",'pakistan',"Australia","canada")
myminituple=("Modi","Trump","Imran")
newtuple=tuples+myminituple
print(newtuple)


# In[19]:


mytuple=("Hello",)*2
print(mytuple)
tuples=("India",'pakistan',"Australia","canada")*2
print(tuples)


# In[27]:


tuples=("India",'pakistan',"Australia","canada")
for y in tuples:
 print(y)


# In[29]:


tuples=("India",'pakistan',"Australia","canada")
if "canada" in tuples:
    print ("yes, it is present")


# In[31]:


tuples=("India",'pakistan',"Australia","canada","India")
Occurence=tuples.count("India")
print(Occurence)


# In[32]:


lists=["India",'pakistan',"Australia","canada","India"]
Occurence=lists.count("India")
print(Occurence)


# In[37]:


tuples=("India",'pakistan',"Australia","canada","India")
Occurence=tuples.count("i")
print(Occurence)


# In[38]:


tuples=(            "India",'pakistan',"Australia","canada","India")
tuples.strip()
print(tuples)


# In[ ]:




