
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
plt.style.use('ggplot')


# In[ ]:


#kik- [mD] permeability for gas
#Swc- critical water saturation
#Sgc- critical gas saturation
#Swi- irreducible water saturation
#Sw- water saturation
#p, q- exponents in Corey equation
#krg- Relative gas permeability
#krw- Relative water permeability


# In[2]:


def Swc(kik): 
    Swc=0.16+0.053*np.log10(kik)
    if Swc < 0:
        return 0
    else:
        return Swc

def Sgc(kik): #
    Sgc=0.15-0.05*np.log10(kik)
    return Sgc

def krg_Corey(Sw,Swc,Sgc,p,q): #Relative permeability based on Corey equation
    krg=((1 - ((Sw - Swc) / (1 - Sgc - Swc))) ** p) * (1 - (((Sw - Swc) / (1 - Swc)) ** q))
    return krg


# In[3]:


def Swi(kik): #10
    Swi=10**(-0.187*np.log10(kik)+1.18)
    return Swi/100

def kw(kik): #6
    kw=kik**1.32
    return kw

def krw(Sw,Swc,r,kik): #7
    krw=((Sw-Swc)/(1-Swc))**r*(kw(kik)/kik)
    return krw

#6,7,10- equations from Cluff,Byrnes 2010- Permeability jail model


# In[4]:


kik = 0.1 #setting gas permeability


# In[5]:


Sw=np.linspace(0,1,100) #axis for water saturation
y1=krg_Corey(Sw, Swc(kik), Sgc(kik), 2.3, 2) #function based on kik
#parameters to create krg ((Sw, Swc(kik), Sgc(kik),p,q))
y2=krg_Corey(Sw, Swc(1), Sgc(1), 1.7, 2)
y3=krg_Corey(Sw, Swc(1), Sgc(1), 2.3, 2)
y4=krw(Sw,0.25,4,0.01)


# In[6]:


plt.plot(Sw,y1,Sw,y2,Sw,y3,Sw,y4) #relative permeability plot
plt.axis([0, 1, 0, 1]) #X and Y axis
plt.xlabel('Water Saturation (%)')
plt.ylabel('Gas Relative Permeability')


# In[19]:



plt.plot(Sw,y1,Sw,y2,Sw,y3,Sw,y4)
plt.xlabel('Water Saturation (%)')
plt.ylabel('Gas Relative Permeability')
plt.semilogy(1,0)


# In[8]:



df = pd.DataFrame([Sw,y1,y2,y4]).T
df.rename({0:"Sw",1:"kik=0.1",2:'kik=1',3:'krw'}, axis='columns') #ustawianie nazw kolumn tabeli

