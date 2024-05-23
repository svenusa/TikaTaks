from tkinter import*
from tkinter import messagebox #paziņojumi
Logs=Tk()
Logs.title("Tikataks")

playerX=True
count=0


def btnclick(button):
    global playerX,count
    if button["text"]==" " and playerX==True: #Spēlē x speletajs
        button["text"]="X"
        playerX=False
        count+=1
        checkWinner()
    elif button["text"]==" " and playerX==False: #Mainas speletaji
        button["text"]="O"
        playerX=True
        count+=1
        checkWinner()
    else:
        messagebox.showerror("TicTacToe", "Šeit kāds jau ir ieklikšķinājis")


def checkWinner():
    global winner

    if(btn1["text"]=="X" and btn2["text"]=="X" and btn3["text"]=="X" or 
    btn4["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X" or
    btn7["text"]=="X" and btn8["text"]=="X" and btn9["text"]=="X" or

    btn1["text"]=="X" and btn4["text"]=="X" and btn7["text"]=="X" or 
    btn2["text"]=="X" and btn5["text"]=="X" and btn8["text"]=="X" or
    btn3["text"]=="X" and btn6["text"]=="X" and btn9["text"]=="X" or

    btn1["text"]=="X" and btn5["text"]=="X" and btn9["text"]=="X" or 
    btn3["text"]=="X" and btn5["text"]=="X" and btn7["text"]=="X"):
        
        winner=True
        disableButtons()
        messagebox.showinfo("TicTacToe","Spēlētājs X ir uzvarējis")

    elif(btn1["text"]=="O" and btn2["text"]=="O" and btn3["text"]=="O" or 
    btn4["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O" or
    btn7["text"]=="O" and btn8["text"]=="O" and btn9["text"]=="O" or

    btn1["text"]=="O" and btn4["text"]=="O" and btn7["text"]=="O" or 
    btn2["text"]=="O" and btn5["text"]=="O" and btn8["text"]=="O" or
    btn3["text"]=="O" and btn6["text"]=="O" and btn9["text"]=="O" or

    btn1["text"]=="O" and btn5["text"]=="O" and btn9["text"]=="O" or 
    btn3["text"]=="O" and btn5["text"]=="O" and btn7["text"]=="O"):
        
        winner=True
        disableButtons()
        messagebox.showinfo("TicTacToe","Spēlētājs O ir uzvarējis")
    
    elif count==9:
        winner = False
        disableButtons()
        messagebox.showinfo("TicTacToe", "Neizšķirts")

def disableButtons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)


def reset():
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn1["text"]=" "
    btn2["text"]=" "
    btn3["text"]=" "
    btn4["text"]=" "
    btn5["text"]=" "
    btn6["text"]=" "
    btn7["text"]=" "
    btn8["text"]=" "
    btn9["text"]=" "


btn1=Button(Logs,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn1))
btn2=Button(Logs,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn2))
btn3=Button(Logs,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn3))
btn4=Button(Logs,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn4))
btn5=Button(Logs,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn5))
btn6=Button(Logs,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn6))
btn7=Button(Logs,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn7))
btn8=Button(Logs,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn8))
btn9=Button(Logs,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn9))

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)

btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)

btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

galvenaIzvelne=Menu(Logs)
Logs.config(menu=galvenaIzvelne)
opcijas=Menu(galvenaIzvelne,tearoff=False)
galvenaIzvelne.add_cascade(label="Opcijas", menu=opcijas)
opcijas.add_command(label="jauna spēle", command = reset)
opcijas.add_command(label="Iziet", command = Logs.quit)

Logs.mainloop()