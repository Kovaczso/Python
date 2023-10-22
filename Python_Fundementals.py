#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World!")


# # Variables  

# In[3]:


x = 22

print (x)


# In[4]:


type (x)


# In[84]:


y = " Ice Cream "

print(y)


# In[86]:


type (y)


# In[87]:


y = "Chocolate"

y = " Ice Cream"

print (y)


# In[57]:


x,y,z = "Chocolate","Vanilla", "Rocky Road"

print (x)
print (y)
print (z)


# In[14]:


x = y = z = "Mint"

print (x)
print (y)
print (z)


# In[18]:


ice_cream = ['Chocolate', 'Vanilla', 'Rocky Road']

x,y,z = ice_cream

print (x)
print (y)
print (z)


# In[ ]:





# In[ ]:


# Camel case 

# Test Variable case <name>

testVariableCase = 'Vanilla Swirl'


# In[ ]:


# Pascal case 

# Test Variable case <name>

TestVariableCase = 'Vanilla Swirl'


# In[ ]:


# Snake case 

# Test Variable case <name>

test_variable_case = 'Vanilla Swirl'


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Data Types

# In[21]:


type (-12+100)


# In[22]:


type(12+10.25)


# In[24]:


type(12+3j)


# In[27]:


#Boolean

type(1>5)


# In[28]:


1>5


# In[29]:


1==1


# In[30]:


#Strings

'Single Quote'


# In[31]:


"Double Quote"


# In[32]:


"""Triple Quote"""


# In[41]:


multiline ="""
The ice cream vanquished
my longing for sweets,
upon this diet I look away,
it is no longer exists on this day,
"""


# In[42]:


print(multiline)


# In[53]:


a = "Hello World!"


# In[54]:


#Indexing in str

print(a[2:5])


# In[55]:


a*3


# In[58]:


#Lists 

[1,2,3]


# In[59]:


['Cookie Dough','Strawberry', 'Chocolate']


# In[60]:


['Vanilla',3,['Scoop','Spoon'],True]


# In[66]:


ice_cream = ['Cookie Dough','Strawberry', 'Chocolate']

ice_cream.append('Salted Caramel')

print(ice_cream)


# In[68]:


ice_cream[0]='Butter Pecan'

print(ice_cream)


# In[69]:


# Nested list 

nest_list=['Vanilla',3,['Scoop','Spoon'],True]


# In[75]:


nest_list[2]


# In[78]:


nest_list[2][1]


# In[79]:


# Tuple

tuple_scoops = (1,2,3,2,1)

type(tuple_scoops)


# In[81]:


tuple_scoops


# In[82]:


#Tuple data types cannot be altered after they are created!

tuple_scoops.append(3)


# In[83]:


#Sets

daily_pints = {1,2,3}


# In[84]:


type(daily_pints)


# In[85]:


print(daily_pints)


# In[88]:


daily_pints_log = {1,2,31,2,3,4,1,2,5,6,3,2}


# In[89]:


print (daily_pints_log)


# In[92]:


wifes_daily_pints_log = {1,3,5,7,3,24,5,7,3,2,0}


# In[96]:


# Combined unique values between two sets

print(daily_pints_log |wifes_daily_pints_log)


# In[97]:


# Matching values in two sets

print(daily_pints_log &wifes_daily_pints_log)


# In[98]:


# Not matching values between two sets
# This print() will display values that are not in "wifes_daily_pints_log" if you compare them with "daily_pints_log"
# If you want to know the values that are not in "daily_pints_log" => print(wifes_daily_pints_log - daily_pints_log)

print(daily_pints_log - wifes_daily_pints_log)


# In[99]:


print(wifes_daily_pints_log - daily_pints_log)


# In[100]:


# Combined unique values in both sets

print(wifes_daily_pints_log ^ daily_pints_log)


# In[102]:


# Dictionaries
# Key/Value Pair

dict_cream = {'name': 'Zsolt Kovac', 'Weekly intake' : 5,'Favorite ice creams':['Chocolate', 'Vanilla']}


# In[103]:


type(dict_cream)


# In[104]:


print(dict_cream)


# In[105]:


dict_cream.values()


# In[106]:


dict_cream.keys()


# In[107]:


dict_cream.items()


# In[111]:


dict_cream['name']


# In[113]:


dict_cream['name'] = 'Romana Kovacova'

print(dict_cream)


# In[119]:


dict_cream.update({'name': 'Romana Kovacova', 'Weekly intake': 10, 'Weight':300})

print(dict_cream)


# In[121]:


del dict_cream['Weight']


# In[122]:


print(dict_cream)


# # Comparison Operators

# In[ ]:


# == Equal
# != Not Equal
# > Greater than 
# < Less than
# >= Greater than or Equalto
# <= Less than or Equalto 


# In[125]:


10 == 50


# In[126]:


10 != 50


# In[127]:


'Vanilla' == 'Vanilla'


# In[129]:


x = 'Vanilla'
y = 'Chocolate'

x != y 


# In[132]:


10 <= 10


# In[133]:


10 >= 10


# Logical Operators

# In[ ]:


# and => Returns "True" if both statements are true
# or => Returns "True" if one of the statements are true
# not => Reverse result, returns "False" if the result is true


# In[134]:


(10>50) and (50>10)


# In[135]:


(10>50) or (50>10)


# In[137]:


# With str
# In this case both statements are true as initial letter of Vanilla is higher then the initial letter for Chocolate in the alphabetical order

('Vanilla' > 'Chocolate') and (50>10)


# In[138]:


not(50>10)


# Membership Operators

# In[143]:


ice_cream = 'I love Chocolate ice cream!'

'love' in ice_cream


# In[148]:


scoops = [1,2,3,4,5]
wanted_scoops = 8
wanted_scoops in scoops


# In[ ]:





# # If-Elif - Else Statements

# In[149]:


if 25 > 10:
    print('It worked!')


# In[152]:


# In this case the "if" statement not working as the "if" statement is not true and there is no else

if 25 < 10:
    print('It worked!')


# In[156]:


if 25 < 10:
    print('It worked!')
else: 
    print('It did not worked!')


# In[158]:


if 25 < 10:
    print('It worked!')
elif 25 < 30:
    print ('Elif worked!')
else: 
    print('It did not work!')


# In[159]:


if 25 < 10:
    print('It worked!')
elif 25 < 20:
    print ('Elif worked!')
elif 25 < 21:
    print ('Elif 2 worked!')
elif 25 < 40:
    print ('Elif 3 worked!')
elif 25 < 50:
    print ('Elif 4 worked!')
elif 25 < 20:
    print ('Elif 5 worked!')
else: 
    print('It did not work!')


# In[161]:


print('It worked!') if 10 >30 else print('It did not work!')


# In[166]:


if (25 < 10) or (1 < 3):
    print('It worked!')
    if 10 > 5 :
        print ('This nested if statement worked!')
elif 25 < 20:
    print ('Elif worked!')
elif 25 < 21:
    print ('Elif 2 worked!')
elif 25 < 40:
    print ('Elif 3 worked!')
elif 25 < 50:
    print ('Elif 4 worked!')
elif 25 < 20:
    print ('Elif 5 worked!')
else: 
    print('It did not work!')


# In[ ]:





# # For Loops

# In[171]:


integer = [1,2,3,4,5]


# In[173]:


for number in integer:
    print(number)


# In[174]:


for number in integer:
    print('Yep!')


# In[ ]:


integer = [1,2,3,4,5]


# In[175]:


for Jelly in integer:
    print(Jelly+Jelly)


# In[4]:


ice_cream_dict = {'name': 'Zsolt Kovac','Weekly': 5,'Favorite':['MCC','Chocolate']}


# In[5]:


for cream in ice_cream_dict.values():
    print(cream)


# In[6]:


for key, value in ice_cream_dict.items():
    print(key,'->',value)


# Nested For Loops

# In[7]:


flavors = ['Vanilla', 'Chocolate', 'Cookie Dough']
toppings = ['Fudges', 'Oreos','Marshmallows']


# In[9]:


for one in flavors:
    for two in toppings:
        print(one,'topped with', two)


# # While Loops

# In[11]:


# While Loops are going to be running until the conditions are met. 
# The instance that conditions are met Loop will break out.

number = 0

while number < 5:
    print(number)
    number = number + 1
    


# In[12]:


# In this case, the loops was checking if the variable (number) is equal to "3" starting from 0.
# If 0 is not equal to 3 it adds 1 to it to the next line and keeps going until it comes to 3 and it breaks out as the condition is met.

number = 0

while number < 5:
    print(number)
    if number == 3:
        break
    number = number + 1
    


# In[14]:


# In this case if the statement from line 6 - 8 is not true and loop will break out of it
# it will go to the else statement (line 12 - 13).
# The else statement is going to be triggered once the while loops is no longer is true


number = 0

while number < 5:
    print(number)
    if number == 6:
        break
    number = number + 1
else:
    print('No longer < 5')


# In[15]:


# Continue in line 10 will cause it to no longer running through the subsequent code but instead will go to the beging and restart the while loop
# This will then create an infinite loop



number = 0

while number < 5:
    print(number)
    if number == 3:
        continue
    number = number + 1
else:
    print('No longer < 5')


# In[24]:


number = 0

while number < 5:
    number = number + 1 
    if number == 3:
        continue
    print(number)
else:
        print('No longer < 5')


# # Functions

# In[25]:


def first_func():
    print('We did it!')
    


# In[26]:


first_func()


# In[28]:


def number_squared(number):
    print(number**2)
    


# In[29]:


number_squared(5)


# In[31]:


def number_squared_cust(number,power):
    print(number**power)
    


# In[32]:


number_squared_cust(5,3)


# In[42]:


def number_squared_cust(number,power):
    print(number**power)


# In[43]:


number_squared_cust(power = 5 ,number =3)


# In[ ]:





# In[37]:


args_tuple = (5,6,1,2,8)


def number_args(*number):
    print(number[0]*number[1])
    


# In[38]:


number_args(*args_tuple)


# In[52]:


def number_kwarg(**number):
    print('My number is: ' + number['intiger'] + ' My other number : ' +number['intiger2'])


# In[53]:


number_kwarg(intiger = '2309', intiger2 = '349')


# # Converting Data Types

# In[54]:


num_int  = 7

type(num_int)


# In[55]:


num_str = '7'

type(num_str)


# In[56]:


num_sum = num_int + num_str


# In[60]:


num_str_conv = int(num_str)

type(num_str_conv)


# In[62]:


num_sum = num_int + num_str_conv

print(num_sum)


# In[63]:


type(num_sum)


# In[64]:


list_type = [1,2,3]

type(list_type)


# In[67]:


list_type_to_tuple = tuple(list_type)


# In[68]:


type(list_type_to_tuple)


# In[70]:


list_type = [1,2,3,3,2,1,2,3,2,1]


# In[73]:


set(list_type)


# In[74]:


type(set(list_type))


# In[75]:


dict_type = {'name': 'Zsolt', 'age': 28, 'hair': 'No hair'}


# In[76]:


type(dict_type)


# In[77]:


dict_type.items()


# In[78]:


dict_type.values()


# In[79]:


dict_type.keys()


# In[80]:


list(dict_type.keys())


# In[81]:


type(list(dict_type.keys()))


# In[82]:


long_str = 'I like to party'


# In[83]:


list(long_str)


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




