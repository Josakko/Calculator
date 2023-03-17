import tkinter as tk


window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)
window.geometry("305x416")
window.iconbitmap("JK.ico")
window.config(bg="#10131c")


input_box = tk.Entry(window, width=15, bg="#333849", fg="#fff", font=("arial", 27)) 
input_box.grid(row=0, column=0, columnspan=5)

button_list = ['/', '*', '7', '8','9', '-', '4', '5','6', '+', '1', '2','3','.','(','0',')']

def button_click(number):
    current = input_box.get()
    input_box.delete(0, tk.END)
    input_box.insert(0, str(current) + str(number))

def button_clear():
    input_box.delete(0, tk.END)

def button_equal():
    try:
        result = eval(input_box.get())
        input_box.delete(0, tk.END)
        input_box.insert(0, str(result))
    except:
        input_box.delete(0, tk.END)
        input_box.insert(0, "Error")

def button_square_root():
    try:
        result = eval(input_box.get())**0.5
        input_box.delete(0, tk.END)
        input_box.insert(0, str(result))
    except:
        input_box.delete(0, tk.END)
        input_box.insert(0, "Error")

#def button_sign():
#    try:
#        if input_box.get()[0] == '-':
#            input_box.delete(0)
#        else:
#            input_box.insert(0, '-')
#    except:
#        pass

row = 1
col = 0

tk.Button(window, text="<-", width=3, font=("arial", 28),bg="#3c4359", fg="#fff", command=lambda:input_box.delete(len(input_box.get())-1)).grid(row=row, column=col)
col += 1
tk.Button(window, text="C", width=3, font=("arial", 28),bg="#3c4359", fg="#fff", command=button_clear).grid(row=row, column=col)
col += 1

for button in button_list:
    def cmd(temp=button):
        button_click(temp)
    tk.Button(window, text=button, width=3, font=("arial", 28),bg="#3c4359", fg="#fff", command=cmd).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(window, text="=", width=3, font=("arial", 28), bg="#5d68e2", fg="#fff", command=button_equal).grid(row=row, column=col)
col += 1

#tk.Button(window, text="+/-", width=3, font=("arial", 28), command=button_sign).grid(row=row, column=col)
#col += 1

#tk.Button(window, text="", width=3, font=("arial", 28), command=None, state="disabled").grid(row=row, column=col)
#col += 1


window.mainloop()