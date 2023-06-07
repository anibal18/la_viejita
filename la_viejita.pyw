from tkinter import *
from os import *



raiz=Tk()

frame1=Frame(raiz)
frame1.pack(anchor="center" , fill="both" , expand=1)
frame1.config(width=500, height=500)
frame1.config(bg="#998a8a")

titulo=Label(frame1 , text="La Viejita" , width=15, height=5 ,font="impact" ,bg="#000000" , fg="#ffffff")
titulo.place(relx=0.398, rely=0.1)

boton=Button(frame1 , text="Start",width=10, height=3 , bd=4 , fg="#005f61" , font="impact", relief="ridge")
boton.place(relx=0.4279, rely=0.5  )
boton.config(command=lambda:segunda_ventana())

barramenu=Menu(raiz)
raiz.config( menu=barramenu )


info_menu=Menu(barramenu ,background='#000099'  , fg="white" , activebackground="#00ff55" , activeforeground="#000000")
info_menu.add_command(label="Jugadores")
info_menu.add_command(label="Record")
info_menu.add_command(label="Acerca de")
barramenu.add_cascade(label="..." , menu=info_menu)

def segunda_ventana():
	raiz.destroy()
	consola=system("python la_viejita_funcionalidad.pyw")
	#lienzo=Canvas(consola , bg="red")


raiz.mainloop()
