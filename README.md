# Conquer The World

### Input:
La primera línea de entrada contiene un número entero n (1 ≤ n ≤ 250 000), el número de naciones. Esto es seguido
por n - 1 líneas, cada una con tres enteros u, v y c (1 ≤ u, v ≤ n, 1 ≤ c ≤ 106
), Indicando que
hay una ruta bidireccional que conecta las naciones u y v, que cuesta c por ejército para usar.
Finalmente, siguen otras n líneas, la i
th de los cuales contiene dos enteros no negativos xi y yi, indicando
que actualmente hay xi ejércitos en la nación i, y se necesitan al menos ejércitos yi para terminar en esa nación en
La configuración final. El número total de ejércitos (la suma de los valores de xi) es al menos la suma de los
valores de yi, y no más de 106.
### Salida
Muestre el costo mínimo para mover sus ejércitos de modo que haya al menos yi ejércitos en la nación i para todo i.

## Package

Instalar solo una libreria, o instalar Anaconda donde ya viene instalada la libreria https://www.anaconda.com/distribution/

```bash
pip install collections
```

## Usage

```python
agrega en cada combobox que aparece  linea  por linea y arroja el output
6
1 2 2
1 3 5
1 4 1
2 5 5
2 6 1
0 0
1 0
2 1
2 1
0 1
0 1

##code que permite esto
[n] = list(map(int, input().split()))
C = list(map(int, input().split()))

X = []
Y = []
```

## Requirements
Python 3.5>

## Bibliography

https://github.com/rafi-kamal/ACM-Solutions/tree/master/LightOj/Graph%20Theory
https://www.hackerrank.com/challenges/minimum-mst-graph/problem
https://www.hackerrank.com/challenges/deforestation-1/problem


## Metodos de Solución
-Este tipo de problema según mi punto de vista tiene que ver con teoria de Grafos y programación dinamica, donde se responde con encontrar  el costo minimo del flujo.
(def findMinFlow)

#####
Los algoritmos base que se baso la solución fue , primero 
Dado un gráfico conectado ponderado no dirigido, El Subárbol Realmente Especial se define como un subgráfico que consta de todos los nodos, Solo hay una ruta exclusiva desde un nodo a cualquier otro nodo.
El subgrafo tiene un peso total mínimo (suma de todos los bordes) entre todos los subgrafos. Para crear el Subárbol realmente especial, se elige siempre el borde con el menor peso, el algoritmo base en que se baso fue el de  KRUSKAL(G), 

### pseudocodigo:
### 1 A = ∅
### 2 foreach v ∈ G.V:
### 3    MAKE-SET(v)
### 4 foreach (u, v) in G.E ordered by weight(u, v), increasing:
### 5    if FIND-SET(u) ≠ FIND-SET(v):
### 6       A = A ∪ {(u, v)}
### 7       UNION(FIND-SET(u), FIND-SET(v))
### 8 return A
######

Segundo Breadth First Search o BFS para un gráfico (def bfs)
El primer recorrido transversal (o búsqueda) de un gráfico es similar al primer recorrido transversal de un árbol. El único problema aquí es que, a diferencia de los árboles, los gráficos pueden contener ciclos, por lo que podemos volver al mismo nodo nuevamente. Para evitar procesar un nodo más de una vez, utilizamos una matriz booleana visitada. Por simplicidad, se supone que todos los vértices son accesibles desde el vértice inicial.


Hagamos, sin pérdida de generalidad, los dos supuestos siguientes:
- No hay nada en los vértices internos de la entrada.
- El árbol es binario (para cada nodo interno con grado d 3, podemos hacer una cadena de
d    1 nodos internos conectados por bordes de costo 0).

Rootear el árbol arbitrariamente. Una idea natural es tratar de resolver esto mediante alguna  dinámica
programación en el árbol, moviéndose hacia arriba desde las hojas hasta llegar a la raíz donde
obtener la respuesta 
Primero describamos el estado a usar y cómo usarlo
Algunos problemas de programación dinámica tienen una recurrencia de esta forma:
dp (i, j) = mink≤j {dp (i − 1, k) + C (k, j)}
donde C (k, j) es alguna función de costo.

Digamos 1≤i≤n y 1≤j≤m, y evaluar C toma O (1) tiempo. La evaluación directa de la recurrencia anterior es O (nm2). Hay n × m estados ym transiciones para cada estado.

Deje que opt (i, j) sea el valor de k que minimiza la expresión anterior. Si opt (i, j) ≤opt (i, j + 1) para todo i, j, entonces podemos aplicar DP de divide y vencerás. Esto se conoce como la condición de monotonicidad. El "punto de división" óptimo para una i fija aumenta a medida que aumenta j.

Esto nos permite resolver todos los estados de manera más eficiente. Digamos que calculamos opt (i, j) para algunos i y j fijos. Entonces para cualquier j ′ <j sabemos que opt (i, j ′) ≤opt (i, j). Esto significa que al computar opt (i, j ′), ¡no tenemos que considerar tantos puntos de división!

Para minimizar el tiempo de ejecución, aplicamos la idea detrás de divide y vencerás. Primero, compute opt (i, n / 2). Luego, calcule opt (i, n / 4), sabiendo que es menor o igual que opt (i, n / 2) y opt (i, 3n / 4) sabiendo que es mayor o igual que opt (i , n / 2). Al hacer un seguimiento recursivo de los límites inferior y superior en opt, alcanzamos un tiempo de ejecución O (mnlogn). Cada posible valor de opt (i, j) solo aparece en logn diferentes nodos.
total nodes = 1sink + 1source + 2*N + sum_of_sizes_X + sum_of_size
