from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
    except IndexError:
        pass
    

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),director_text.get(),year_text.get(),genre_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),year_text.get(),director_text.get(),review_text.get(),genre_text.get())
    list1.delete(0,END)

def update_command():
    backend.delete(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4],selected_tuple[5])
    print(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4],selected_tuple[5])
def delete_command():
    backend.delete(selected_tuple[0])
def close_command():
	window.destroy()




window = Tk()
window.wm_title("FilmLog")
l1=Label(window,text="Title")
l1.grid(row= 0, column=0)

l2=Label(window,text="Year")
l2.grid(row= 1, column=0)

l3=Label(window,text="Director")
l3.grid(row= 0, column=3)

l5=Label(window,text='Genre')
l5.grid(row=0,column=5)

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
e4=Entry(window,textvariable=review_text)
e4.grid(row=1,column=4)

genre_text= StringVar()
e5=Entry(window,textvariable=genre_text)
e5.grid(row=0,column=6)

list1= Listbox(window,height=13,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=6)

sb1=Scrollbar(window)
sb1.grid(row=2,column=4)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View All",width=12,bg='grey',command=view_command)
b1.grid(row=2,column=5)

b2=Button(window,text="Search a Film",width=12,bg='grey',command=search_command)
b2.grid(row=3,column=5)

b3=Button(window,text="Add a Film",width=12,bg='grey',command=add_command)
b3.grid(row=4,column=5)

b4=Button(window,text="Update Selected",width=12,bg='grey',command=update_command)
b4.grid(row=5,column=5)

b5=Button(window,text="Delete Selected",width=12,bg='grey',command=delete_command)
b5.grid(row=6,column=5)

b6=Button(window,text="Close",width=12,bg='grey',command=close_command)
b6.grid(row=7,column=5)

window.mainloop()
