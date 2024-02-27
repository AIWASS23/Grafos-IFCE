import cv2
import csv
import matplotlib.pyplot
import numpy
import pandas

# Carregar a imagem
img = cv2.imread('img2.jpeg', 0)

# Aplicar thresholding na imagem
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Detectar pontos pretos na imagem thresholded
points = []
for y in range(thresh.shape[0]):
    for x in range(thresh.shape[1]):
        if thresh[y, x] == 0:
            points.append((x, y))

# Salvar a tabela de pontos em um arquivo CSV
with open('points.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y'])
    writer.writerows(points)

# Criar um gráfico de dispersão com os pontos
df = pandas.read_csv('points.csv')
matplotlib.pyplot.scatter(df['x'], df['y'], s=5)
matplotlib.pyplot.gca().invert_yaxis()
matplotlib.pyplot.show()

# Ler o arquivo CSV
df = pandas.read_csv('points.csv')

# Distância máxima permitida entre os pontos
max_distance = 0.5

# Listas para armazenar pontos médios e grupos
new_x = []
new_y = []
element_groups = {}

# Iterar sobre as linhas do DataFrame
for i, row in df.iterrows():
    x = row['x']
    y = row['y']
    
    # Encontrar pontos próximos
    near_points = []
    for j, other_row in df.iloc[i+1:].iterrows():
        other_x = other_row['x']
        other_y = other_row['y']
        distance = numpy.sqrt((x-other_x)**2 + (y-other_y)**2)
        if distance < max_distance:
            near_points.append([other_x, other_y])
    
    # Calcular o ponto médio se houver pontos próximos
    if len(near_points) > 0:
        near_points.append([x, y])
        avg_x = sum([p[0] for p in near_points]) / len(near_points)
        avg_y = sum([p[1] for p in near_points]) / len(near_points)
        new_x.append(avg_x)
        new_y.append(avg_y)
        
        # Adicionar pontos ao grupo correspondente
        if (avg_x, avg_y) not in element_groups:
            element_groups[(avg_x, avg_y)] = []
        element_groups[(avg_x, avg_y)].append((x, y))
    else:
        new_x.append(x)
        new_y.append(y)

# Plotar o novo conjunto de dados com os pontos médios
matplotlib.pyplot.scatter(new_x, new_y)
matplotlib.pyplot.show()

# Contar o número de elementos (grupos)
number_of_elements = len(element_groups)

print("Número de elementos:", number_of_elements)
