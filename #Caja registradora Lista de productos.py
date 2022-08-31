from multiprocessing import Value
from optparse import Values
import tkinter
from tkinter import END, Button, Entry, IntVar, Tk, ttk

class Interfaz:

    def __init__(self,ventana):
        self.ventana = ventana
        self.productos = ("Arroz-$3700", "Spaghetti-$4000", "Aceite-$7000", "Manzana-$1500", "Café-$3000", "Harina-$4200", "Gaseosa-$3800", "Pan-$1000", "Jugo-$2800", "Mantequilla-$1500", "Chocolate-$3600")
        self.cajaCantidad = IntVar()
        self.cajaTotal= IntVar()
        self.total=0
        self.dibujarComponentes()

    def dibujarComponentes (self):
        self.ventana.title("Caja Registradora")
        self.ventana.geometry("650x450")
        ttk.Label(self.ventana, text="Sellecciona el producto que deseas comprar: ").place(x=10, y=10)
        ttk.Label(self.ventana, text="Selecciona la cantidad del producto escogido: ").place(x=10, y=60)
        ttk.Label(self.ventana, text="El total es: ").place(x=450, y=400)
        self.combo = ttk.Combobox(self.ventana, state="readonly")
        self.combo.place(x=10, y=35)
        self.combo["values"]=self.productos
        self.combo.current(0)
        Entry(self.ventana, textvariable=self.cajaCantidad).place(x=10, y=85)
        Entry(self.ventana, textvariable=self.cajaTotal).place(x=520, y=400)
        Button(self.ventana, text="Agregar", command=self.agregarProducto).place(x=10, y=110)

        self.tabla= ttk.Treeview(self.ventana,columns=("Cantidad", "Subtotal"))
        self.tabla.heading("#0", text="Producto")
        self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.heading("Subtotal", text="Subtotal")
        self.tabla.place(x=10, y=150)
    
    def agregarProducto(self):
        texto=self.combo.get()
        datos=texto.split("-$")
        producto=datos[0]
        precio=datos[1]
        cantidad=self.cajaCantidad.get()
        subtotal=int(precio)*int(cantidad)
        self.tabla.insert("", END, text=producto, values=(cantidad,"$"+str(subtotal)))
        self.total=self.total+subtotal
        self.cajaTotal.set("$"+str(self.total))

obj=Interfaz(Tk())
obj.ventana.mainloop()