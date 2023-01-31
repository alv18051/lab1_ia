from PIL import Image
import matplotlib.pyplot as plt

def discretizacion(imagen):
  
    ima=Image.open(imagen)
    height, width = ima.size
    i_size = (int(width/2), int(height/2))
    small_ima=ima.resize(i_size,Image.BILINEAR)
    resultado = small_ima.resize(ima.size, Image.NEAREST)
    filename="resultado_" + imagen 
    resultado.save(filename)
    print("Se discretizo su imagen, se guardo en el archivo: ", filename)
    