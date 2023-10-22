#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

# In[13]:


name = input("Enter you first name: ")

weight = input("Enter you weight in pounds: ")

height = input ("Enter you height in inches: ")

BMI = (weight * 703) / (height * height)


# In[14]:


type(height)


# In[41]:


name = input("Enter you first name: ")

weight = int(input("Enter you weight in pounds: "))

height = int(input ("Enter you height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI > 0:
    if (BMI < 18.5):
        print(name + ", You are underweight!")
    elif (BMI <= 24.9):
        print(name + ", You are normal weight!")
    elif (BMI <= 29.0):
        print(name + ", You are overweight!")
    elif (BMI <= 34.9):
        print(name + ", You are obese!")
    elif (BMI <= 39.9):
        print(name + ", You are severly obese!")
    else:
        print(name + ", You are morbidly obese!")
else:
        print("Enter valid inputs")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




