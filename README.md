# EJIDO-LA-ESPERANZA
Muestra los datos obtenidos de obtención de las pendientes del Ejido la Esperanza y finalmente poder mostrar una imagen de dicho Ejido.

Alejandro Ramirez Serratos
   	 correo electronico: aserratos0809@gmail.com 
    
    "Facultad de Ingeniería Civil, PE-ITG..." Programa educativo Ingeniero Topografo Geomatico
    
# Pendientes-del-Ejido-la-Esperanza

![PalabrasdelTextoAlternativo](https://github.com/Alejandro480/EJIDO-LA-ESPERANZA/blob/master/IMAGENES/EJIDO.png)

# Resumen

En el presente proyecto se preverá in-formación sobre un ejido, específica-mente del ejido la esperanza, del cual se obtendrán características de las pendientes que tiene el ejido, esto se realiza con la finalidad de poder mostrar pendientes aptas para la agricultura.

Palabras clave: Agricultura, Cultivo, Pendientes.

# Abstract

In this project will provide for in-formation on an ejido, specific-minded of the ejido hope, from which will obtain characteristics of the slopes that the ejido has, this is done in order to be able to show slopes suitable for agricul-ture.

Keywords: Agriculture, Cultivation, Slopes

# Introducción

En el presente proyecto se mostrarán los resultados obtenidos de la elaboración de un raster de elevaciones, elaborado en un sis-tema de información geográfica, específi-camente ArcGis, el raster de elevaciones se obtiene mediante datos vectoriales propor-cionados por el INEGI mediante su página web.

La elaboración del presente trabajo tiene como objetivo poder mostrar las pendientes que son aptas para poder hacer practica de la agricultura, lo cual se realiza mediante daros vectoriales.

El proyecto esta compuesto principalmente por el desarrollo de un programa en Python, con el programa se pretende facilitar la ob-tención del conocimiento sobre las pendien-tes del ejido la esperanza, por lo que se sis-tematiza la obtención de la superficie de las diferentes pendientes que tiene el ejido la esperanza clasificándolos por colores para cada una de las pendientes que va desde 5° hasta los 64°, tomando en cuenta que las pendientes aptas para la agricultura son las menores de 5° y en algunos casos menores de 10°.

# Desarrollo 

Para desarrollar el programa que ten-dremos que elaborar en Python, prime-ramente tendremos que tener las libre-rías de “openpyxl” y otra librería llama “PIL”, la librería de openpyxl nos ayuda-ra a mostrar los datos alfanuméricos del Ejido la Esperanza obtenidos anterior-mente en ArcMap y almacenados en una hoja de cálculo de Excel con ex-tensión .csv, la librería de PIL nos ayu-dara a mostrar las imágenes del ejido, tanto como las de los rangos de eleva-ción, estas imágenes se invocaran den-tro del programa con el nombre con el que se han aguardado anteriormente 

1.	Como primer paso, tendremos que importar las librerías men-cionadas anteriormente, open-pyxl y PIL, si aún no las tienes instaladas instalas, instálalas e impórtalas posteriormente.

2.	Después tendremos que indicar el libro de trabajo de Excel con la librería de openpyxl, junto con las filas y columnas que desee que se muestren 

3.	Posteriormente se tendrá que agregar un apartado para que de la opción de poder mostrar las imágenes que se generaron del área de estudio, en este caso se tendrá que hacer de la siguiente forma: 
Si desea ver la imagen del area de es-tudio indique "y"
run = raw_input("Decea ver el Ejido de estudio y/n\n")

4.	Se tendrá que indicar que para la librería llama PIL se importe IMAGE, dentro de Python se in-dica de la siguiente forma

from PIL import Image

5.	Finalmente se tendrá que elabo-rar el código para mostrar las imágenes, dicho código queda elaborado de la siguiente forma:

def show(path_name):

    image = ()

image.open(path_name)=

    image.show()

show()

El código completo se anexa en el si-guiente párrafo


  	  import openpyxl
      import PIL
	  

	    #ELE es abreviación de Ejido La Esperanza
	    doc = open-pyxl.lod_workbook("ELE")
	

	    selecciom = hoja['B2':'D5']
  	  for fials in seleccion:
	    for columnas in filas:
	         print (colum-nas.coordinate, columnas.valie)
	    print ("---Final de Fila---")
	

	    #Si desea ver la imagen del area de estudio indique "y"
	    run = raw_input("Decea ver el Ejido de estudio y/n\n")
	

    	from PIL import Image
	

	    #Para que la imagen pudea ser mostradra debera de indicarse con el nombre de la imagen
	    def show(path_name):
	        image = ()
	    image.open(path_name)=
	       image.show()

# Manejo de Datos

El tipo de datos que se manejan en el programa son:
Datos vectoriales: estos datos son obligatoriamente necesarios debido a que con estos datos se creara el raster de elevaciones en ArcMap
Lenguaje de programación: para lo-grar crear el programa y este ejecute correctamente lo que se indica en el programa a elaborar
Sistemas de Información Geográfica: los SIG principalmente ArcGis (ArcMap) son importantes para el desarrollo de la localización de cada zona apta para la agricultura.
5.1. 	Sistema Operativo
El programa está diseñado dentro de un sistema operativo de Windows, especí-ficamente Windows 10, el programa se trabaja en Python 3.7.4.

5.2. 	Equipo de prueba
El equipo en el cual fue probado el pro-grama es una computadora portátil de la marca Hp Pavilion con las siguientes características:

![PalabrasdelTextoAlternativo](https://github.com/Alejandro480/EJIDO-LA-ESPERANZA/blob/master/IMAGENES/Especificaciones.png)

# Resultados

Lo que se logro obtener mediante la realización del código fue la demostra-ción de las imágenes que se anexaran posteriormente, al igual que la tabla donde se almacenan los datos obteni-dos de las pendientes del Ejido la Esperanza. 

Grafica de Pastel 

![PalabrasdelTextoAlternativo](https://github.com/Alejandro480/EJIDO-LA-ESPERANZA/blob/master/IMAGENES/Grafica.png)

Rangos de Elevacion 

![PalabrasdelTextoAlternativo](https://github.com/Alejandro480/EJIDO-LA-ESPERANZA/blob/master/IMAGENES/RANGOS.png)

Tabla de datos

![PalabrasdelTextoAlternativo](https://github.com/Alejandro480/EJIDO-LA-ESPERANZA/blob/master/IMAGENES/TABLA.png)

Ejido la Esperanza

![PalabrasdelTextoAlternativo](https://github.com/Alejandro480/EJIDO-LA-ESPERANZA/blob/master/IMAGENES/EJIDO.png)

# Conclusiones 

Durante la elaboración del proyecto se pudo observar que es bastante impor-tante la comprensión de las librerías dentro de Python tanto como la com-prensión de Python debido a que, si no se comprende bien alguno de estos temas, se tendrán dificultades para po-der trabajar dentro de ellos debido a que las librerías se dividen en diferentes partes.

Durante la elaboración del código se tuvieron algunos percances debido a que no se tenían contempladas la libre-rías que se utilizarían para poder elabo-rar correctamente el código del progra-ma, por lo que se tuvieron que analizar y comprender diferentes librerías para poder trabajar correctamente, por lo que se decidió trabajar con las librerías de openpyxl  y PIL.

# Referencias 

https://www.inegi.org.mx/app/mapas/
