class Maquillar :
	def __init__(self,nombre,tipo,duracion,tonos) :
	     
	    self.nombre= nombre
	    self.tipo= tipo
	    self.duracion= duracion
	    self.tonos= tonos 

	def print_nombre(self):
	 	print (self.nombre)
	def print_tipo (self):
	 	print (self.tipo)
	def print_duracion(self):
	 	print (self.duracion)
	def print_tonos(self):
	 	print (self.tonos)

listaOjos= list()
listaRostro= list()
opc=0
while opc<4:
	opc=input()
	if opc==1: 
		print ('¿Cuantos productos desea registrar?')
    	Registro=int(input)
        if registro < 5:
        	print ('Nombre del producto')
     	    nombre=input()
            print ('tipo del producto; 1. Para ojos, 2. Para rostro')
            tipo=input()
            opci=0
            if opci==1:
             	print ('duracion del productos')
                duracion=input()
                print ('tonos del producto')
                tonos=input()
                ListaOjos.append(product)
            if opci==2:
             	print ('duracion del productos')
             	duracion=input()
             	print ('tonos del producto')
             	tonos=input ()
             	listaRostro.append(product)
    product= Maquillar(nombre,tipo,duracion,tonos)
        else:
        	print('La cantidad minima es de 5 productos')

    if opc==2:
       for product in listaOjos:
           product.print_nombre()
           product.print_tipo()
           product.print_duracion()
           product.print_tonos()

    if opc==3:
    	for product in listaRostro:
            product.print_nombre()
            product.print_tipo()
            product.print_duracion()
            product.print_tonos()
    if opc==4:
    	Print ('Hasta luego')
    	 



  