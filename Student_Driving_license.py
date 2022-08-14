# Plantilla básica tkinteR
from tkinter import *
root=Tk()
root.title("fibonacci")
root.geometry("400x400")

root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Permiso de conducir", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Nombre :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Fecha de nacimiento :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="No.pin :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Dirección :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Autorización para conducir los siguientes vehículos :")

# Crea todas las etiquetas requeridas para ser mostradas
label_id=Label(root)
label_name=Label(root)
label_dob=Label(root)
label_pin=Label(root)
label_address=Label(root)
label_vehicle_type=Label(root)

# Define la función
def v():
    id_licencia=6795894532
    label_id["text"]=id_licencia
    nombre="francisco-gomes"
    label_name["text"]=nombre
    fecha="10/08/2022"
    label_dob["text"]=fecha
    pin=162534
    label_pin["text"]=pin
    direccion="miguel hidalogo 654"
    label_address["text"]=direccion
    tipos=["bicicleta", "moto", "avioneta", "camion"]
    label_vehicle_type["text"]=tipos
    
label_id.pack()    
label_name.pack()
label_dob.pack()
label_pin.pack()
label_address.pack()
label_vehicle_type.pack()
    
# Crea un botón
button1=Button(root, text="agregar", command=v)
button1.pack()

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()

# Plantilla básica tkinter fin de la declaración
root.mainloop()