# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:17:32 2021

@author: tarun.chimnani`x
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]


creds = ServiceAccountCredentials.from_json_keyfile_name("august-creek-321105-71862a29a96c.json", scope)
client = gspread.authorize(creds)
sheet = client.open("color").sheet1  # Open the spreadhseet


#get the entire data of the sheet as a list

data = sheet.get_all_records()

    
for x in data:
    print(x)
print("\n")



# #get a specific row
# row = sheet.row_values(3)
# print(row)
# print("\n")

# #get a specific column

# column = sheet.col_values(2)
# print(column)

# #getting number of rows and columns in a sheet

# print("number of columns in sheet: ",sheet.col_count)
# print("number of rows in sheet: ",sheet.row_count)



# #update a value in sheet
# sheet.update_cell(2, 2, "green")# Update one cell


# #add row in sheet
# new = ["khyati","pink"]
# sheet.insert_row(new)

#delete rows in sheet

#sheet.delete_rows(2,4)




from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
window=Tk()
#window.resizable(False,False)

canva = Canvas(window,width=1100,height=500)
img = ImageTk.PhotoImage(Image.open("back.png"))

canva.create_image(0,0,anchor=NW,image=img)
canva.pack(fill=BOTH, expand=True)


def cost():
    days = int(text5.get(1.0,END))
    if(basic.get()==1):
       label7.config(text=500*days)
       c2.deselect()
       c3.deselect()
    if(delux.get()==1):
       label7.config(text=1000*days)      
       c1.deselect()
       c3.deselect()
    if(superdelux.get()==1):
       label7.config(text=1500*days)
       c1.deselect()
       c2.deselect()
    if(basic.get()==0 and delux.get()==0 and superdelux.get()==0):
         label7.config(text="0") 
        
        
        
       
def get_text():
    name = text2.get(1.0,END)
    address = text3.get(1.0,END)
    number = text4.get(1.0,END)
    days = int(text5.get(1.0,END))
    total = label7['text']
    new = [name,address,number,days,total]
    sheet.insert_row(new,len(data)+2)

label1 = Label(window,text="HOTEL",font="Verdana 50 bold",bg="#ff0000")
label1.place(x=100,y=20)

basic = IntVar();
delux = IntVar();
superdelux = IntVar();

c1 = Checkbutton(window, text='Basic', onvalue=1, offvalue=0,variable=basic,command=cost)
c1.place(x=50,y=120)

c2 = Checkbutton(window, text='Delux', onvalue=1, offvalue=0,variable=delux,command=cost)
c2.place(x=200,y=120)

c3 = Checkbutton(window, text='Super delux', onvalue=1, offvalue=0,variable=superdelux,command=cost)
c3.place(x=350,y=120)

label2 = Label(window,text="Name",font="Verdana 10 bold")
label2.place(x=100,y=180)
text2 = Text(window,height=1,width=20)
text2.place(x=300,y=180)


label3 = Label(window,text="Address",font="Verdana 10 bold")
label3.place(x=100,y=220)
text3 = Text(window,height=1,width=20)
text3.place(x=300,y=220)

label4 = Label(window,text="Phone number",font="Verdana 10 bold")
label4.place(x=100,y=260)
text4 = Text(window,height=1,width=20)
text4.place(x=300,y=260)


label5 = Label(window,text="Number of days",font="Verdana 10 bold")
label5.place(x=100,y=300)
text5 = Text(window,height=1,width=20)
text5.place(x=300,y=300)


label6 = Label(window,text="Total amount to be paid",font="Verdana 10 bold")
label6.place(x=100,y=340)
label7 = Label(window,text="0",font="Verdana 10 bold")
label7.place(x=300,y=340)
# text6 = Text(window,height=1,width=20)
# text6.place(x=300,y=340)

# enteries = Listbox(window,width=62,height=20)
# enteries.place(x=500,y=50)





b1 = Button(text="Add new entry",command = get_text)
b1.place(x=100,y=400)

# b2 = Button(text="Show all enteries",command = show_data)
# b2.place(x=200,y=400)

tree = ttk.Treeview(window)
tree.place(x=645,y=50)
tree["show"] = "headings"

tree["columns"] = ("name","Address","Contact number","Days","cost")

tree.column("name",width=100,anchor=NW)
tree.column("Address",width=100,anchor=NW)
tree.column("Contact number",width=100,anchor=NW)
tree.column("Days",width=40,anchor=NW)
tree.column("cost",width=100,anchor=NW)


tree.heading("name",text="name",anchor=NW)
tree.heading("Address",text="Address",anchor=NW)
tree.heading("Contact number",text="Contact number",anchor=NW)
tree.heading("Days",text="Days",anchor=NW) 
tree.heading("cost",text="cost",anchor=NW)


i=0
for ro in data:
    #tree.insert(parent='', index=0, iid=0, text='', )
    #tree.insert("", i,text="",values=('1','Vineet','Alpha','Alpha','Alpha'))
    tree.insert("", i,text="",values=(ro['name'],ro['Address'],ro['Contact number'],ro['Days'],ro['cost']))
    #i=i+1


# hsb = ttk.Scrollbar(window,orient="horizontal")
# hsb.configure(command=tree.xview)
# tree.configure(xscrollcommand=hsb.set)
# hsb.pack(fill=X,side=BOTTOM)

window.geometry("1100x500")
window.mainloop()
