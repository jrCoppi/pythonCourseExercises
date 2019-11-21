#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Python Crash Course Exercises 
# 
# This is an optional exercise to test your understanding of Python Basics. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners, such as [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp/?couponCode=PY20)

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[3]:


7 ** 4


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[10]:


s = "Hi there Sam!"


# In[11]:


s.split(" ")


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[16]:


planet = "Earth"
diameter = 12742


# In[18]:


print("The diameter of {one} is {two} kilometers".format(one=planet,two=diameter))


# ** Given this nested list, use indexing to grab the word "hello" **

# In[21]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[23]:


print(lst[3][1][2])


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[24]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[28]:


d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# In[23]:


# Tuple is immutable


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[30]:


def domainGet(email):
    str = email.split("@")
    return str[1]


# In[31]:


domainGet('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[39]:


def findDog(text):
    text = text.lower()
    dogcatcher = text.split("dog")
    return len(dogcatcher) > 1


# In[40]:


findDog('Is there a dog here?')


# In[41]:


findDog('Is there a cat here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[56]:


def countDog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1
    return count


# In[57]:


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[86]:


seq = ['soup','dog','salad','cat','great']


# In[82]:


def excludeS(seq):
    wordsWiths = []
    count = 0
    for word in seq:
        if word[0] != 's':
            wordsWiths.append(word)
    return wordsWiths


# In[83]:


print(excludeS(seq))


# In[85]:


list(excludeS(seq))


# In[89]:


list(filter(lambda word: word[0] != 's',seq))


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[111]:


def caught_speeding(speed, is_birthday):
    ticket = "no ticket"
    if ((speed >= 66) or (is_birthday == False and speed >= 61)):
        ticket = "small ticket"
    if ((speed >= 86) or (is_birthday == False and speed >= 81)):
        ticket = "big ticket"
    return ticket


# In[114]:


caught_speeding(83,True)


# In[115]:


caught_speeding(83,False)


# # Great job!
