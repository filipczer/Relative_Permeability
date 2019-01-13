# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
plt.style.use('ggplot')


# In[2]:


#kik- [mD] absolute permeability for gas
#Swc- critical water saturation
#Sgc- critical gas saturation
#Swi- irreducible water saturation
#Sw- water saturation
#p, q- exponents in Corey equation
#krg- Relative gas permeability
#krw- Relative water permeability


# In[3]:


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


# In[4]:


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


# In[5]:


kik = 0.1 #setting gas permeability [mD]


# In[6]:


Sw=np.linspace(0,1,100) #axis for water saturation
y1=krg_Corey(Sw, Swc(kik), Sgc(kik), 1.7, 2) #function based on kik
#parameters to create krg ((Sw, Swc(kik), Sgc(kik),p,q))
y2=krg_Corey(Sw, Swc(0.0001), Sgc(0.0001), 1.7, 2)#ultra tight sandstone
y3=krg_Corey(Sw, Swc(2), Sgc(2), 1.7, 2)
y4=krw(Sw,0.25,4,0.1)
y5=krw(Sw,0.25,4,0.0001)
y6=krw(Sw,0.25,4,2)
y7=krg_Corey(Sw, Swc(kik), Sgc(kik), 1.7, 2) 
y8=krg_Corey(Sw, Swc(kik), Sgc(kik), 4, 2) #change in exp p to check the influence
y9=krg_Corey(Sw, Swc(kik), Sgc(kik), 1.7, 4) #change in exp q to check the influence


# In[7]:


plt.plot(Sw,y1,label='krg, kik=0.1mD') #tight sandstone- upper bound 0.1mD
plt.plot(Sw,y2,label='krg, kik=0.0001mD') #ultratight sandstone 0.0001mD
plt.plot(Sw,y3,label='krg, kik=2mD') #conventional reservoir 2D
#relative permeability plot
plt.axis([0, 1, 0, 1]) #X and Y axis
plt.xlabel('Nasycenie wodą')
plt.ylabel('Przepuszczalność względna gazu')
plt.legend()
plt.savefig('gas1.pdf')


# In[8]:


plt.plot(Sw,y7,label='krg, p=1.7, q=2') #tight sandstone- upper bound 0.1mD
plt.plot(Sw,y8,label='krg, p=4, q=2') #ultratight sandstone 0.0001mD
plt.plot(Sw,y9,label='krg, p=1.7, q=4') #conventional reservoir 2D
#relative permeability plot
plt.axis([0, 1, 0, 1]) #X and Y axis
plt.xlabel('Nasycenie wodą')
plt.ylabel('Przepuszczalność względna gazu')
plt.legend()
plt.savefig('gas3.pdf')


# In[9]:


plt.plot(Sw,y1,label='krg, kik=0.1mD') #tight sandstone- upper bound 0.1mD
plt.plot(Sw,y2,label='krg, kik=0.0001mD') #ultratight sandstone 0.0001mD
plt.plot(Sw,y3,label='krg, kik=2mD') #conventional reservoir 2D
#relative permeability plot
plt.axis([0, 1, 0.01, 1]) #X and Y axis
plt.xlabel('Nasycenie wodą')
plt.ylabel('Przepuszczalność względna gazu')
plt.legend()
plt.semilogy()
plt.savefig('gas2.pdf')


# In[10]:


plt.plot(Sw,y4,label='krw, kik=0.1mD') #tight sandstone- upper bound 0.1mD
plt.plot(Sw,y5,label='krw, kik=0.0001mD') #ultratight sandstone 0.0001mD
plt.plot(Sw,y6,label='krw, kik=2mD') #conventional reservoir 2D
#relative permeability plot
plt.axis([0, 1, 0, 1]) #X and Y axis
plt.xlabel('Nasycenie wodą')
plt.ylabel('Przepuszczalność względna wody')
plt.legend()
plt.savefig('wat1.pdf')


# In[11]:


plt.plot(Sw,y4,label='krw, kik=0.1mD') #tight sandstone- upper bound 0.1mD
plt.plot(Sw,y5,label='krw, kik=0.0001mD') #ultratight sandstone 0.0001mD
plt.plot(Sw,y6,label='krw, kik=2mD') #conventional reservoir 2D
#relative permeability plot
plt.axis([0, 1, 0.01, 1]) #X and Y axis
plt.xlabel('water saturation')
plt.ylabel('relative permeability for water')
plt.legend()
plt.semilogy()
plt.savefig('wat2.pdf')


# In[12]:


plt.plot(Sw,y1,label='krg, kik=0.1mD') #tight sandstone- upper bound 0.1mD
plt.plot(Sw,y4,label='krw, kik=0.1mD') #krw with kik=0.1mD - correlated with y1
#relative permeability plot
plt.axis([0, 1, 0, 1]) #X and Y axis
plt.xlabel('water saturation') #nasycenie wodą
plt.ylabel('relative permeability') #przepuszczalność względna
plt.legend()
plt.savefig('un1.pdf')


# In[13]:


plt.plot(Sw,y1,label='krg, kik=0.1mD') #tight sandstone- upper bound 0.1mD
plt.plot(Sw,y4,label='krw, kik=0.1mD') #krw with kik=0.1mD - correlated with y1
plt.axis([0, 1, 0.01, 1]) #OY has to be >0!!!
plt.xlabel('water permeability')
plt.ylabel('relative permeability')
plt.semilogy(1,0)
plt.legend()
plt.savefig('un2.pdf')


# In[14]:


df = pd.DataFrame([Sw,y1,y2,y4]).T
df.rename({0:"Sw",1:"kik=y1",2:'kik=y2',3:'krw'}, axis='columns')
#setting up the table


# In[15]:


df.loc[np.nanargmin(np.absolute(y1-y4))] #Check a what saturation krw and krg meets, 1- kik, 3- krw


# In[16]:


df.info()

