import matplotlib.pyplot as plt

# 1. Definir los datos para las barras
categorias = ['Manzanas', 'Granadillas', 'Naranjas', 'Moras']
cantidades = [10, 15, 7, 12]

# 2. Crear la gráfica de barras
barras = plt.bar(categorias, cantidades, color=['red', 'yellow', 'orange', 'purple'])
plt.bar_label(barras)

# 3. Añadir títulos y etiquetas
plt.title('Venta de Frutas')
plt.xlabel('Frutas')
plt.ylabel('Cantidad')

# 4. Mostrar la gráfica
plt.show()
#prueba rama
print ("Esto lo hice en una rama jeje")

