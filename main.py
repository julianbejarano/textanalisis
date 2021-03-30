
import csv
import unicodedata
import re
import string

# 1 tener el diccionario ordenado
# 2 hacer dos columnas para el key y el valor
# 3 sacar el string del key y enviarlo a busca vecinos
# 4 alimentar la 3 columna con la cantidad de vecinos.
# 5 alimentar la 4 columna con el nombre de los vecinos
# 6 un for va bajando de fila
# 7 hacer un csv con los datos

file= str(input("digite el nombre del archivo a analizar: "))
rango = int(input("digite el numero de letras desde cuales hacer el analisis: "))

nom_Output = str(input("digite el nombre del archivo de salida: "))
datos = []
lista= []
general_dict = {}
dixio = []
listWords = []
# definimos una lista de caracteres que no deseamos
badChars = [';', ':', '!', "*","-","?","¿","¡","!",".",",",'"',"—","(",")","´","»","«","“","”"," ","ō","..."]

def Inicio (doc, rango):
    with open (doc, 'r', encoding="utf-8") as file:
        for lines in file:
            WordsPerLine = lines.lower().split()
            # imprimir el numero de palabras en las lineas
            # print (len(WordsPerLine))
            # imprimir el numero de palabras que hay en cada linea de palabras
            # print(WordsPerLine)
            # si hay mas de dos palabras en la linea
            if len(WordsPerLine) > 0:
                for word in WordsPerLine:

                    # si la palabra sin espacios tiene de mas de X caracteres o en cierto
                    # rango de caracteres o con un numero de caraceteres definido
                    if len(word.strip()) >= rango:
                    # if len(word.strip()) > 3:
                    # if len(word.strip()) in range (4,6):


                        # word = unicodedata.normalize('NFD', word)
                        # print ('numero de palabras: '+ str(count))
                        # imprimir cada un de las palabras que van apareciendo
                        # print (word)
                        # using join() + generator to
                        # remove bad_chars
                        test_string = ''.join(i for i in word if not i in badChars)
                        listWords.append(test_string)
        total = len(listWords)
    print("\nPalabras totales que contienen desde ", str(rango), " letras: ", str(total))
    return (listWords)

    # for x in range(len(listWords)):
    #     print (listWords[x])
    # creamos un diccionario que toma de la lista de palabras organizadas y les agrega el numero de veces que aparece
# listWords.sort()
# print(listWords[0:100])
# Check if the word is already in dictionary

def Dictado():
    for w in listWords:
        # preguntamos si la palabra está en el diccionario
        if w in general_dict:
            general_dict[w] = general_dict[w] + 1
        else:
            # Add the word to dictionary with count 1
            general_dict[w] = 1
            # comparamos las palabras vecinas de esta
            # Vecinos(w)
    return general_dict

def Vecinos (Palabra):
    total = len(listWords)
    lista.clear()
    for x in range(0, total - 1):
        # print(randomlist[x])
        if Palabra == listWords[x]:
            if x != 0:
                lista.append(listWords[x - 1])
            if x <= total:
                lista.append(listWords[x + 1])

    # print("los vecinos de '" + str(Palabra) + "' son:")
    #     podemos volver la lista un conjunto para que no
    #   se repitan las palabras vecinas
    return(sorted(list(set(lista))))


def Relevantes (x):
    # crear un dicccionario organizado segun el numero de apariciones de la palabra
    sorted_dict = sorted(general_dict.items(), key=lambda x: x[1], reverse=True)
    # imprimimos un rango del diccionario organizado por valores
    print("\nlas " + str(x) + " palabras mas relevantes son:\n\n", sorted_dict[0:x],"\n")


def Archivo ():
    # ir al diccionario sacar los datos de cada uno de los elementos
    sorted_dict = sorted(general_dict.items(), key=lambda x: x[1], reverse=True)
    dixio.clear()
    # hay que tener cuidado porque al organizar el diccionario y guardarlo en una variable
    # esta variable no es de tipo diccionario sino lista
    # print(type(general_dict))
    # print(type(sorted_dict))
    tam = len(sorted_dict)
    for i in range (0,tam):
        col_1 = str(sorted_dict[i][0])
        col_2 = str(sorted_dict[i][1])
        col_4 = Vecinos (col_1)
        col_3 = str(len(col_4))
        # print("Dato: ",i)
        # print(col_1,"\t", col_2,"\t", col_3,"\t", col_4)
        dixio.append([col_1,col_2,col_3,col_4])
        # dixio.append([col_1])
    EscribirCSV(dixio)



def EscribirCSV(uno):

    with open (nom_Output+".csv", 'w', newline='') as data:
        # hacemos una lista de los headers del archivo
        # saludo = ['text analizer by:', 'Julian Bejarano', 'juliabejaranog@gmail.com']
        header = ['Palabra','frecuencia','#veci', 'vecinos']
        # alistamos el archivo para escritura
        file = csv.writer(data, delimiter=',')
        # pasamos los headers como columnas independientes
        # file.writerow(saludo)
        file.writerow(header)
        # llenamos las columnas con los datos de las listas
        file.writerows(uno)

Inicio( file , rango)
Dictado()
print("\n\nTextAnalizer By: Julian Bejarano, julianbejaranog@gmail.com")
print("\nAnalizando...\n\n\n")
# Relevantes(10)
Archivo()
# print(dixio)
