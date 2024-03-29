import tkinter
 
window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

##Entry

input = tkinter.Entry(width=10)
input.pack()
input.get()
# import turtle

# tim = turtle.Turtle()
# tim.write()










window.mainloop()