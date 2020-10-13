# Simplified Silhouette Width (SSWC)

Implementation of Simplified Silhouette Width (SSWC) in Python 3.
Simplified Silhouette Width Criterion is a less expensive alternative than the original measure (Silhouette Width Criterion). 

## How to Run the code
1. Insert the path to your dataset in line 7
2. Run The Code
3. Insert the number of the column who contains the classes (First column is 0)
4. The program will create an archive 'silhouettes.txt' who contais the K-Means clustering execution (for k=2, k=3, k=4) and the SSWC values for each execution of the sklearn k-means algorithm


## Reference
[JASKOWIAK, Pablo Andretta. On the evaluation of clustering results: measures, ensembles, and gene expression data analysis](https://www.teses.usp.br/teses/disponiveis/55/55134/tde-23032016-111454/publico/VersaoRevisada_PabloAndrettaJaskowiak.pdf)