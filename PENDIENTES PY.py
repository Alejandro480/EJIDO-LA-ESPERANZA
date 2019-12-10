import openpyxl
import PIL

#ELE es abreviación de Ejido La Esperanza
doc = openpyxl.lod_workbook("ELE")

selecciom = hoja['B2':'D5']
for fials in seleccion:
    for columnas in filas:
        print (columnas.coordinate, columnas.valie)
    print ("---Final de Fila---")

#Si desea ver la imagen del area de estudio indique "y"
run = raw_input("Decea ver el Ejido de estudio y/n\n")

from PIL import Image

#Para que la imagen pudea ser mostradra debera de indicarse con el nombre de la imagen
def show(path_name):
    image = ()
image.open(path_name)=
    image.show()
show()
