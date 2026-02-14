from tkinter import *

root = Tk()

root.geometry("600x700")
root.title("CALCULATOR")
root.config(bg="antiquewhite")
label= Label(root,text="CALCULATOR",fg="darkcyan",font=("Arial",15,"bold","italic"),bg="antiquewhite")
label.pack(pady=(20,0),fill="both")

# heading 
outter_frame = Frame(root,bg="pink",relief="solid",borderwidth=2,height=70)
outter_frame.pack(padx=40,pady=20,expand=True,fill="both")




# screen layout
upper_frame = Frame(outter_frame ,bg="light grey",relief="sunken",borderwidth=2)
upper_frame.pack(fill="both",expand=True,padx=40,pady=20)


entry = Entry(upper_frame,bg="light grey",font=("Helvetica 20"))
entry.pack(fill="both",expand=True)



# bottom layout
bottom_frame = Frame(outter_frame,bg="lightseagreen",height=200,relief="solid",borderwidth=2)
bottom_frame.pack(fill="both",expand=True,padx=40,pady=(0,20))

# function for button 
def move(value):
    if value == "C":
        entry.delete(0,END)

    elif value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0,END)
            entry.insert(0,result)

        except Exception as e:
            entry.delete(0,END)
            entry.insert("ERROR")


    else :
        entry.insert(END,str(value))

        

    
# number button layout
number = Frame(bottom_frame,bg="silver",width=300,relief="solid",borderwidth=2)
number.pack(side="left",fill="both",expand=True,padx=20,pady=20)

arithmetic = Frame(bottom_frame,bg="silver",relief="solid",borderwidth=2)
arithmetic.pack(side="left",fill="both",expand=True,padx=20,pady=20)

btn9 = Button(number,text="9",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move(9))
btn9.grid(row=0,column=0,sticky="nsew",padx=30,pady=10)

btn8 = Button(number,text="8",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move(8))
btn8.grid(row=0,column=1,sticky="nsew",padx=30,pady=10)

btn7 = Button(number,text="7",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move(7))
btn7.grid(row=0,column=2,sticky="nsew",padx=30,pady=10)

btn6 = Button(number,text="6",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move(6))
btn6.grid(row=1,column=0,sticky="nsew",padx=30,pady=10)


btn5 = Button(number,text="5",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move(5))
btn5.grid(row=1,column=1,sticky="nsew",padx=30,pady=10)


btn4 = Button(number,text="4",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move(4))
btn4.grid(row=1,column=2,sticky="nsew",padx=30,pady=10)

btn3 = Button(number,text="3",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move(3))
btn3.grid(row=2,column=0,sticky="nsew",padx=30,pady=10)


btn2 = Button(number,text="2",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move(2))
btn2.grid(row=2,column=1,sticky="nsew",padx=30,pady=10)


btn1 = Button(number,text="1",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move(1))
btn1.grid(row=2,column=2,sticky="nsew",padx=30,pady=10)



btn10 = Button(number,text=".",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move("."))
btn10.grid(row=3,column=0,sticky="nsew",padx=30,pady=10)

btn11 = Button(number,text="0",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move(0))
btn11.grid(row=3,column=1,sticky="nsew",padx=30,pady=10)

btn12 = Button(number,text="C",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move("C"))
btn12.grid(row=3,column=2,sticky="nsew",padx=30,pady=10)





# arithmetic button layout
btn_add = Button(arithmetic,text="+",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move("+"))
btn_add.grid(row=0,column=0,sticky="nsew",padx=30,pady=10)

btn_sub = Button(arithmetic,text="-",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move("-"))
btn_sub.grid(row=0,column=1,sticky="nsew",padx=30,pady=10)

btn_divide = Button(arithmetic,text="%",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move("%"))
btn_divide.grid(row=0,column=2,sticky="nsew",padx=30,pady=10)

btn_multiply = Button(arithmetic,text="*",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move("*"))
btn_multiply.grid(row=1,column=0,sticky="nsew",padx=30,pady=10)

btn_modolus = Button(arithmetic,text="/",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move("/"))
btn_modolus.grid(row=1,column=1,sticky="nsew",padx=30,pady=10)

btn_square = Button(arithmetic,text="^",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move("^"))
btn_square.grid(row=1,column=2,sticky="nsew",padx=30,pady=10)

btn_equal = Button(arithmetic,text="=",bg="yellow",height=2,width=15,relief="solid",borderwidth=2,font=("Arial"),command=lambda:move("="))
btn_equal.grid(row=2,column=1,sticky="nsew",padx=30,pady=10)



# arithmetic row and column configuration
arithmetic.grid_rowconfigure(0,weight=1)
arithmetic.grid_rowconfigure(1,weight=1)
arithmetic.grid_rowconfigure(2,weight=1)
arithmetic.grid_rowconfigure(3,weight=1)

arithmetic.grid_columnconfigure(0,weight=1)
arithmetic.grid_columnconfigure(1,weight=1)
arithmetic.grid_columnconfigure(2,weight=1)
arithmetic.grid_columnconfigure(3,weight=1)



# number row and column configuration
number.grid_rowconfigure(0,weight=1)
number.grid_rowconfigure(1,weight=1)
number.grid_rowconfigure(2,weight=1)
number.grid_rowconfigure(3,weight=1)

number.grid_columnconfigure(0,weight=1)
number.grid_columnconfigure(1,weight=1)
number.grid_columnconfigure(2,weight=1)



root.mainloop()