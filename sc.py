from tkinter import *
window = Tk()
l1=Label(window,text="Title")
l1.grid(row= 0, column=0)

l2=Label(window,text="Year")
l2.grid(row= 1, column=0)

l3=Label(window,text="Director")
l3.grid(row= 0, column=3)

l4=Label(window,text="Review")
l4.grid(row= 1, column=3)

title_text= StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

year_text= StringVar()
e2=Entry(window,textvariable=year_text)
e2.grid(row=1,column=1)

director_text= StringVar()
e3=Entry(window,textvariable=director_text)
e3.grid(row=0,column=4)

review_text= StringVar()
e1=Entry(window,textvariable=review_text)
e1.grid(row=1,column=4)

list1= Listbox(window,height=13,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=6)

sb1=Scrollbar(window)
sb1.grid(row=2,column=4)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View All")
b1.grid(row=2,column=5)

b2=Button(window,text="Search a Film")
b2.grid(row=3,column=5)

b3=Button(window,text="Add a Film")
b3.grid(row=4,column=5)

b4=Button(window,text="Update Selected")
b4.grid(row=5,column=5)

b5=Button(window,text="Delete Selected")
b5.grid(row=6,column=5)

b6=Button(window,text="Close")
b6.grid(row=7,column=5)

window.mainloop()