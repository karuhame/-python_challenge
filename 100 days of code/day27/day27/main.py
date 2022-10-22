import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)


#label
my_label = tkinter.Label(text="son dep trai", font=("Arial", 25, "bold"))
my_label.pack(side="bottom")

#change label
my_label["text"] = "son"
my_label.config(text="son")


def button_clicked():
	print("I GOT CLICKED")
	new_test = info.get()
	my_label.config(text=new_test)
	print(new_test)


# create button
button = tkinter.Button(text="click me", command=button_clicked)  # command for function do not have "()"
button.pack()

# entry
info = tkinter.Entry(width=50)
info.pack()
print(info.get())




window.mainloop()
