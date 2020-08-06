from tkinter import *
import requests as r
from bs4 import BeautifulSoup as bsp
w=Tk()
w.title("corona update")
w.geometry("700x500")
def covd():
    if(e.get()=="world"):
        url="https://www.worldometers.info/coronavirus/"
    else:
        url="https://www.worldometers.info/coronavirus/country/"+e.get()
    page=r.get(url)
    soup=bsp(page.content,"html.parser")
    #print(soup)
    info=soup.find_all(class_="maincounter-number")
    l=[]
    for item in info:
        l.append(item.get_text())
    l1=Label(w,text="Coronavirus Cases in "+e.get()+":"+l[0]).pack()
    #l1.config(w,text="Coronavirus Cases in "+e.get()+":"+l[0]).pack()
    l2=Label(w,text="Deaths in "+e.get()+":"+l[1]).pack()
    l3=Label(w,text="Recovered in "+e.get()+":"+l[2]).pack()
e=Entry(w,width=60)
e.pack()
b=Button(w,text="submit",command=covd).pack()
w.mainloop()
