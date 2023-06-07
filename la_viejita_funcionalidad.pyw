from random import *
from time import *
import sys
import os 
class Viejita():

	def __init__(self):
		#variable que almacena la letra escogida por el usuario
		self.letra_usuario=" "
		self.letra_pc=" "
		#varibale que almacena la letras en el lugar exacto del tablero.
		self.tablero=[" " for i in range(1,10)]
		#posicion escogida por el usuario
		self.numero_posicion=0
		self.n_aleatorio=0
	
	def dibuja_tablero(self):#dibuja el tablero

		print(
			" ___________\n"
			"|_"+ str(self.tablero[6])+"_|_"+ str(self.tablero[7])+"_|_"+ str(self.tablero[8])+"_|\n"
			"|_"+ str(self.tablero[3])+"_|_"+ str(self.tablero[4])+"_|_"+ str(self.tablero[5])+"_|\n"
			"|_"+ str(self.tablero[0])+"_|_"+ str(self.tablero[1])+"_|_"+ str(self.tablero[2])+"_|"
			)


	def escoger_letra(self):#pide al usuario una letra 
		self.n_aleatorio=randint(1,2)
		if self.n_aleatorio==1:
			self.letra_usuario=input("escoge entre X o O: ").upper()
			print("tu letra es: " + self.letra_usuario)
			if self.letra_usuario=="X":
				self.letra_pc="O"
			else:
				self.letra_pc="X"
			self.dibuja_tablero()
		else:
			print("escoge la computadora...")
			sleep(0.79)
			self.letra_pc=randint(1,2)
			if self.letra_pc==1:
				self.letra_usuario="O"
				self.letra_pc="X"
				self.dibuja_tablero()
			else:
				self.letra_usuario="X"
				self.letra_pc="O"
				self.dibuja_tablero()


	def escoger_tablero(self):#pide al usuario la posicion donde va a ir la letra 
		self.contador=1
		while True:
			if self.n_aleatorio==1:
				self.numero_posicion=int(input("escoge una posicion para jugar: "))
				for i in range(1 , 10):
					if i % 2==0 :
						self.tablero.pop(self.numero_posicion-1)#en esta parte se elimina un posicion para poder mantener las posiciones jugadas
						self.tablero.insert(self.numero_posicion-1 , self.letra_usuario)
						self.n_aleatorio=2
						self.dibuja_tablero()
						self.verificacion_ganador()
						
						break
			else:
				print("escoge la computadora...")
				sleep(0.79)
				while True:
					self.n_aleatorio_pc=randint(0,8)
					
					if self.tablero[self.n_aleatorio_pc]==" ":
						self.tablero.pop(self.n_aleatorio_pc)
						self.tablero.insert(self.n_aleatorio_pc, self.letra_pc)
						self.n_aleatorio=1
						self.dibuja_tablero()
						self.verificacion_ganador()

						break
			if self.contador==9:
				break
			self.contador+=1

	def verificacion_ganador(self):#este modulo se encarga de validar las posiciones ya jugadas y ver si existe un ganador.
		self.contador_verificacion2=0
		self.respuestas_ganadoras=[[0,4,8],[2,4,6],[0,3,6],[0,1,2],[1,4,7],[2,5,8],[6,7,8],[3,4,5]]
		self.contador_verificacion=0
		for i in self.tablero:
			for lista in self.respuestas_ganadoras:
				if self.letra_usuario=="X":
					if  self.tablero[lista[0]]=="X"and self.tablero[lista[1]]=="X"and self.tablero[lista[2]]=="X":
						print("ganaste")
						os.system("ganaste.pyw")
						sleep(1)
						sys.exit()
					if  self.tablero[lista[0]]=="O"and self.tablero[lista[1]]=="O"and self.tablero[lista[2]]=="O":
						print("gano la computadora")
						os.system("perdiste.pyw")
						sleep(1)
						sys.exit()
				if self.letra_usuario=="O":
					if  self.tablero[lista[0]]=="X"and self.tablero[lista[1]]=="X"and self.tablero[lista[2]]=="X":
						print("gano la computadora")
						os.system("perdiste.pyw")
						sleep(1)
						sys.exit()
					if  self.tablero[lista[0]]=="O"and self.tablero[lista[1]]=="O"and self.tablero[lista[2]]=="O":
						print("ganaste")
						os.system("ganaste.pyw")
						sleep(1)
						sys.exit()
	def crear_archivo(self):
		self.archivo=open(datos ,"while:")
		pass


lavieja=Viejita()
lavieja.escoger_letra()
lavieja.escoger_tablero()


									