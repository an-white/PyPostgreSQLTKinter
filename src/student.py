from tkinter import Button, Canvas, Entry, Frame, Label, Tk
from tkinter.constants import E, W
import psycopg2


def save_new_student(name, age):
    connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432",
    )
    cursor = connection.cursor()
    cursor
    print(name, age)


root = Tk()
root.title("hola")

# Canvas
canvas = Canvas(root, width=400, height=400)
canvas.pack()

frame = Frame()
# el espaciado relativo es respecto al ancho total de la ventana
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# un label usado como titulo de la seccion
label = Label(frame, text="add a student")
# como se posiciona cada cosa en la ventana con el grid row,column
label.grid(row=0, column=1)

# un label de identificacion
label = Label(frame, text="Name")
label.grid(row=1, column=0)
entry_name = Entry(frame)
entry_name.grid(row=1, column=1)


# un label de identificacion
label = Label(frame, text="Age")
label.grid(row=2, column=0)
entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

# con command mediante una funcion lambda puedo ejecutar una funcion
btn = Button(
    frame,
    text="Submit",
    command=lambda: save_new_student(entry_name.get(), entry_age.get()),
)

btn.grid(row=4, column=1, sticky=W + E)

root.mainloop()
