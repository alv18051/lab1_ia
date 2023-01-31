from PIL import Image
def greyscale(imagen):
    ima=Image.open(imagen)
    ima_grey=ima.convert('L')
    ima_grey.save("gray_"+imagen)
    print("Se convirtio su imagen a escala de grises, se guardo en el archivo: ", "greyscale_"+imagen)

archivo = input("Ingrese el nombre del archivo con su extencion: ")
greyscale(archivo)
