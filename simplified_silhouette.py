import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import math


data = pd.read_csv('iris.csv', header=None)

n = int(input('Insira qual o atributo do dataset corresponde às classes: '))

# Dividindo os dados
X = np.array(data.drop(n, axis=1))
y = np.array(data[n])


def euclidean_distance(obj1, obj2):
    soma = 0
    colunas = len(X[0])
    for i in range(colunas):
        soma += (obj1[i] - obj2[i])**2
    
    distancia = math.sqrt(soma)
    return distancia


# Recebe um conjunto de dados
def simplified_silhouette(X):
    s = []

    for i in range(len(X)):
        # Distância aos centróides (sem contar o seu próprio centróide)
        dist = []
        
        # Calcula o a(i)
        ai = euclidean_distance(X[i], centroids[cluster_labels[i]])
        
        # Calcula a distancia aos outros centróides (sem contar o seu próprio)
        for j in range(len(centroids)):
            if j != cluster_labels[i]:
                d = euclidean_distance(X[i], centroids[j])
                dist.append(d)
        
        # Pega a lista de distancias e Calcula o b(i) -> centróide mais próximo
        bi = np.amin(dist)
        
        # Calcula o s(i)
        si = (bi - ai)/(max(bi, ai))
        s.append(si)
    # Retorna a Silhueta Simplificada (final)
    return np.mean(s)


# Execução solicitada -> k = 2, k = 3, k = 4

# lista que armazenará as silhuetas Simplificadas (finais)
list_sil = []

list_k = []

# Lista que vai armazenar as execuções do k-means
list_clusters = []

n_clusters = 2
for i in range(3):    
    kmeans = KMeans(n_clusters, max_iter=100)
    
    kmeans.fit(X)
    
    # Lista de clusters em que os objetos foram agrupados
    cluster_labels = kmeans.predict(X)
    
    list_clusters.append(cluster_labels)
    
    # Centróides da execução do KMeans
    centroids = kmeans.cluster_centers_
    
    # Obtém a silhueta simplificada da execução e adiciona na lista de silhuetas    
    result = simplified_silhouette(X)
    
    list_sil.append(result)
    list_k.append(n_clusters)
    
    n_clusters += 1


def write_txt():
    with open('silhouettes.txt', 'w') as fp:
        for i in range(3):
            fp.write(f'K = {list_k[i]} - Silhueta Simplificada (SSWC): {list_sil[i]}\n')
            fp.write(f'Execução do K-Means:\n{list_clusters[i]}\n\n')
    fp.close()


write_txt()

print('Programa Finalizado! Arquivo txt gerado.')
