#!/usr/bin/env python
# coding: utf-8

# In[3]:


myset={"Apple","Manago","Orange","Grapes"}
print (myset)


# In[10]:


myset={"Apple","Manago","Orange","Grapes"}
for x in myset:
 print (x)


# In[11]:


myset={"Apple","Manago","Orange","Grapes"}
myset.add("banana")
print(myset)


# In[12]:


myset={"Apple","Manago","Orange","Grapes"}
myset.update(["Pineapple","Watermelon"])
print(myset)


# In[13]:


myset={"Apple","Manago","Orange","Grapes"}
myset.add("banana","Peach")
print(myset)


# In[14]:


myset={"Apple","Manago","Orange","Grapes"}
print(len(myset))


# In[17]:


myset={"Apple","Manago","Orange","Grapes"}
myset=="Apple"


# In[28]:


my=["Apple","Manago","Orange","Grapes"]
"Manago" in myset


# In[29]:


mytuple=["Apple","Manago","Orange","Grapes"]
if("Manago" in mytuple):
    print ("yes")


# In[31]:


myset={"Apple","Manago","Orange","Grapes"}
myset.remove("Orange")
print(myset)


# In[32]:


myset={"Apple","Manago","Orange","Grapes"}
myset.clear()
print(myset)


# In[33]:


myset={"Apple","Manago","Orange","Grapes"}
del myset
print(myset)


# In[37]:


myset={"Apple","Manago","Orange","Grapes"}
Removed_item=myset.pop()
print(Removed_item)
Removed_item=myset.pop()
print(Removed_item)


# In[39]:


myset1={"Apple","Manago","Orange","Grapes"}
myset2={"Pineapple","Apple","Peach"}
myset1.difference_update(myset2)
print(myset1)


# In[40]:


myset1={"Apple","Manago","Orange","Grapes"}
myset2={"Pineapple","Apple","Peach"}
myset1.difference(myset2)
print(myset1)


# In[41]:


myset1={"Apple","Manago","Orange","Grapes"}
myset2={"Pineapple","Apple","Peach"}
a=myset1.difference(myset2)
print(myset1)
print(a)


# In[42]:


myset1={"Apple","Manago","Orange","Grapes"}
myset2={"Pineapple","Apple","Peach"}
a=myset1.difference_upate(myset2)
print(myset1)
print(a)


# In[ ]:


.

