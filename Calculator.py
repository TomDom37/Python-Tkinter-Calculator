from tkinter import *


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def EqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
    
    

root = Tk() #Creating the tk element
root.title("Calculator") #Title of window
operator=""
root.resizable(False, False)
text_Input = StringVar() #Input element for txtDisplay
root.configure(background="#85CDCA") #changing Frame settings

txtDisplay = Entry(root,font=("Arial bold", 20), textvariable=text_Input, bg="#65ADAA", bd=10, fg="black", justify="right").grid(columnspan=4)


#First Row:           
btn7= Button(root, padx=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="7", command=lambda:btnClick(7)).grid(row=1, column=0,)
btn8= Button(root, padx=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="8", command=lambda:btnClick(8)).grid(row=1, column=1)
btn9= Button(root, padx=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="9", command=lambda:btnClick(9)).grid(row=1, column=2)
Addition= Button(root, padx=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="+", command=lambda:btnClick("+")).grid(row=1, column=3)



#Second Row:
btn4=Button(root, padx=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="4", command=lambda:btnClick(4)).grid(row=2, column=0)
btn5= Button(root, padx=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="5", command=lambda:btnClick(5)).grid(row=2, column=1)
btn6= Button(root, padx=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="6", command=lambda:btnClick(6)).grid(row=2, column=2)
Subtraction= Button(root, padx=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="-", command=lambda:btnClick("-")).grid(row=2, column=3)

#Third Row:
btn1=Button(root, padx=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="1", command=lambda:btnClick(1)).grid(row=3, column=0)
btn2= Button(root, padx=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="2", command=lambda:btnClick(2)).grid(row=3, column=1)
btn3= Button(root, padx=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="3", command=lambda:btnClick(3)).grid(row=3, column=2)
Multipication= Button(root, padx=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="*", command=lambda:btnClick("*")).grid(row=3, column=3)

#Forth Row:
btn0= Button(root, padx=16, pady=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="0", command=lambda:btnClick(0)).grid(row=4, column=0)
btnClear= Button(root, padx=16,pady=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="C", command=btnClearDisplay).grid(row=4, column=1)
btnEquale= Button(root, padx=16,pady=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="=", command=EqualsInput).grid(row=4, column=2)
Division= Button(root, padx=16,pady=16, bd=8, bg="#7AC2BF" ,fg="black", font=("Arial bold", 20), text="/", command=lambda:btnClick("/")).grid(row=4, column=3)
###########################################################################

root.mainloop()
