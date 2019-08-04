from  tkinter import *
import requests
from bs4  import BeautifulSoup
import pandas


window=Tk()

def view_command():
	if item_listbox.get()=="lamps":
		listbox1.delete('0','end')
		r=requests.get("https://www.thehutcafe.com/products?category=the-hut-cafe-lamp-collection")
		c=r.content
		soup=BeautifulSoup(c,"html.parser")
		all=soup.find_all("div",{"class":"small-6 medium-4 large-3 xlarge-3 columns product-column"})
		l=[]
		r=0
		for item in all:

			d={}
			d["name"]=item.find("h2").text+""

			d["price"]=item.find("",{"class":"product-copy-price-current"}).text.replace("₹","").replace(" ","")
			l.append(d)
			listbox1.insert(END,l[r]['name']+"₹"+l[r]['price'])
			r=r+1
	elif item_listbox.get()=="chandlier":
		listbox1.delete('0','end')
		r=requests.get("https://www.thehutcafe.com/products?category=peacock-chandeliers")
		c=r.content
		soup=BeautifulSoup(c,"html.parser")
		all=soup.find_all("div",{"class":"small-6 medium-4 large-3 xlarge-3 columns product-column"})
		l=[]
		r=0
		for item in all:
			d={}
			d["name"]=item.find("h2").text+""
			d["price"]=item.find("",{"class":"product-copy-price-current"}).text.replace("₹","").replace(" ","")
			l.append(d)
			listbox1.insert(END,l[r]['name']+"₹"+l[r]['price'])
			r=r+1

	elif item_listbox.get()=="ships":
		listbox1.delete('0','end')
		r=requests.get("https://www.thehutcafe.com/products?category=ship-models")
		c=r.content
		soup=BeautifulSoup(c,"html.parser")
		all=soup.find_all("div",{"class":"small-6 medium-4 large-3 xlarge-3 columns product-column"})
		l=[]
		r=0
		for item in all:
			d={}
			d["name"]=item.find("h2").text+""
			d["price"]=item.find("",{"class":"product-copy-price-current"}).text.replace("₹","").replace(" ","")
			l.append(d)
			listbox1.insert(END,l[r]['name']+"₹"+l[r]['price'])
			r=r+1
	elif item_listbox.get()=="coffee table":
		listbox1.delete('0','end')
		r=requests.get("https://www.thehutcafe.com/products?category=ornate-coffee-table")
		c=r.content
		soup=BeautifulSoup(c,"html.parser")
		all=soup.find_all("div",{"class":"small-6 medium-4 large-3 xlarge-3 columns product-column"})
		l=[]
		r=0
		for item in all:
			d={}
			d["name"]=item.find("h2").text+""
			d["price"]=item.find("",{"class":"product-copy-price-current"}).text.replace("₹","").replace(" ","")
			l.append(d)
			listbox1.insert(END,l[r]['name']+"₹"+l[r]['price'])
			r=r+1
	elif item_listbox.get()=="animal lamps":
		listbox1.delete('0','end')
		r=requests.get("https://www.thehutcafe.com/products?category=coco-animal-lamps-1")
		c=r.content
		soup=BeautifulSoup(c,"html.parser")
		all=soup.find_all("div",{"class":"small-6 medium-4 large-3 xlarge-3 columns product-column"})
		l=[]
		r=0
		for item in all:
			d={}
			d["name"]=item.find("h2").text+""
			d["price"]=item.find("",{"class":"product-copy-price-current"}).text.replace("₹","").replace(" ","")
			l.append(d)
			listbox1.insert(END,l[r]['name']+"₹"+l[r]['price'])
			r=r+1
	elif item_listbox.get()=="all products":
		listbox1.delete('0','end')
		r=requests.get("https://www.thehutcafe.com/products")
		c=r.content
		soup=BeautifulSoup(c,"html.parser")
		all=soup.find_all("div",{"class":"small-6 medium-4 large-3 xlarge-3 columns product-column"})
		l=[]
		r=0
		for item in all:
			d={}
			d["name"]=item.find("h2").text+""
			d["price"]=item.find("",{"class":"product-copy-price-current"}).text.replace("₹","").replace(" ","")
			l.append(d)
			listbox1.insert(END,l[r]['name']+"₹"+l[r]['price'])
			r=r+1

window.geometry("550x400")

label1=Label(window,text="The hutcafe",font="times 24 bold")
label1.grid(row=0,column=4)

label2=Label(window,text="select the option",font="times 14 italic")
label2.grid(row=3,column=4)

items_list=["lamps","chandlier","ships","coffee table","animal lamps","all products"]
item_listbox=StringVar(window)
item_listbox.set("select product")
menu=OptionMenu(window,item_listbox,*items_list)
menu.grid(row=5,column=4)

listbox1=Listbox(window,height=15,width=80)
listbox1.grid(row=10,column=3,rowspan=6,columnspan=3,pady=10,padx=20)

sb1=Scrollbar(window)
sb1.grid(row=10,column=6,sticky='ns',rowspan=6)

listbox1.configure(yscrollcommand=sb1.set)
sb1.configure(command=listbox1.yview)

b1=Button(window,text="Search",command=view_command,width=12,bg='gray')
b1.grid(row=7,column=4)

window.mainloop()