from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Translator")
root.geometry("800x800")
root.configure(bg= "#F2CCC3")

l1 = Label(root, text = "LANGUAGE TRANSLATOR")
l1.place(relx= 0.5, rely= 0.1, anchor = CENTER)

l2 = Label(root, text = "Enter Text")
l2.place(relx= 0.2, rely= 0.3, anchor = CENTER)

ta = Text(root,height= 400, wrap= WORD, width=500, padx = 5, pady= 5, bd = 0)
ta.place(relx = 0.2, rely= 0.4, anchor = CENTER)

l3 = Label(root, text = "Output")
l3.place(relx= 0.8, rely= 0.3, anchor = CENTER)

ta1 = Text(root,height= 400, wrap= WORD, width=500, padx = 5, pady= 5, bd = 0)
ta1.place(relx = 0.8, rely= 0.4, anchor = CENTER)

language = list(LANGUAGE.values())

lan = ttk.Combobox( root, state= "readonly", values = language, width= 10)
lan.place(relx = 0.4, rely = 0.3, anchor = CENTER)

op = ttk.Combobox( root, state= "readonly", values = language, width= 10)
op.place(relx = 0.9, rely = 0.3, anchor = CENTER)

lan.set("english")
op.set("french")

class Translator:
    
    def translate(heading,source,destination):
        try:
            heading =ta.get(1,END)
            source = src_lang.get()
            destintion = dest_lang.get()
            op.delete(1.0, END)   
            op.insert(END, string)
        except:
            print("Try again")

Button(root, text="Translate", command= translate).place(relx = 0.5, rely = 0.7, anchor = CENTER)
obj1 = Translator()
root.mainloop()