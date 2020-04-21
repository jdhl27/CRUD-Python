#-------------------------------------------------------------------------------
# Name:        funciones
#
# Author:      Juan David Hdez
#
# Proyecto:    CRUD con interfaz Tkinter
# Created:     14/10/2019
# Copyright:   (c) Juan 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Nodo:
    def __init__(self, codigo, nombre, edad, siguiente):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.siguiente = siguiente

class ListaLigada:
    def __init__(self):
        self.cabeza = None

    ## AGREGANDO NODO AL FINAL
    def agregarAlFinal(self, codigo, nombre, edad):
        if self.cabeza==None:
            self.cabeza = Nodo(codigo, nombre, edad,None)
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = Nodo(codigo, nombre, edad,None)

    ## CONTADOR CANTIDAD DE NODOS
    def contarNodos(self):
        contador = 0
        if self.cabeza==None:
            return contador
        else:
            actual = self.cabeza
            while actual != None:
                actual = actual.siguiente
                contador+=1
            return contador

    ## IMPRIMIR LISTA
    def mostrarLista(self):
        actual = self.cabeza
        while actual != None:
            print(actual.codigo, actual.nombre, actual.edad, end =" => ")
            actual = actual.siguiente

    ## MATRIZ CON NODOS DE LA LISTA
    def listar(self):
        mat=[]
        n = self.contarNodos()
        actual = self.cabeza
        for i in range(n):
            mat.append([])
            mat[i].append(actual.codigo)
            mat[i].append(actual.nombre)
            mat[i].append(actual.edad)
            actual = actual.siguiente
        return mat

    ## ELMINAR NODO
    def eliminar(self,cod):
        if self.cabeza != None:
            actual = self.cabeza
            anterior = actual
            ## ELIMINANDO PRIMER DATO
            if cod == actual.codigo:
                self.cabeza = actual.siguiente
                sw = True
                return sw
            else:
                sw = True
                while actual != None:
                    if cod == actual.codigo:
                        anterior.siguiente = actual.siguiente
                        sw = True
                        break
                    else:
                        sw = False
                    anterior = actual
                    actual = actual.siguiente
                return sw
        else:
            sw = False
            return sw


    ## BUSQUEDA
    def consultar(self,cod):
        if self.cabeza != None:
            n = self.contarNodos()
            n = int(n)
            actual = self.cabeza
            for i in range(n):
                if cod == actual.codigo:
                    sw = []
                    sw.append(actual.nombre)
                    sw.append(actual.edad)
                    break
                else:
                    sw = False
                actual = actual.siguiente
            return sw
        else:
            sw = False
            return sw

    ## MODIFICAR
    def modificar(self,cod, nombre, edad):
        if self.consultar(cod)!= False:
            actual = self.cabeza
            while cod != actual.codigo:
                actual = actual.siguiente
            actual.nombre = nombre
            actual.edad = edad
        else:
            sw = False
            return sw

    ## PROMEDIO EDAD
    def edadPromedio(self):
        if self.cabeza != None:
            edades = 0
            promedio = 0
            cantidad = self.contarNodos()
            cantidad = int(cantidad)
            actual = self.cabeza
            for i in range(cantidad):
                edades = edades + int(actual.edad)
                actual = actual.siguiente
            promedio = edades/cantidad
            promedio = int(promedio)
            return promedio
        else:
            promedio = 0
            return promedio

    def rangoEdades(self):
        if self.cabeza != None:
            cantEdades010 = 0
            cantEdades1020 = 0
            cantEdades2030 = 0
            cantEdades4050 = 0
            cantEdades6070 = 0
            cantEdades8090 = 0
            cantEdades90100 = 0
            cantidad = self.contarNodos()
            cantidad = int(cantidad)
            actual = self.cabeza
            while actual != None:
                edades = edades + int(actual.edad)
                actual = actual.siguiente
            promedio = edades/cantidad
            promedio = int(promedio)
            return promedio
        else:
            promedio = 0
            return promedio

