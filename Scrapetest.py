#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())


# In[ ]:




