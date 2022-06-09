#Algoritmo A* per la ricerca della soluzione nel 15-puzzle
Il programma si articola in 8 file .py ciascuno con una diversa responsabilità. Il file **main.py** 
è quello che deve essere eseguito per ottenere i risultati mostrati nella relazione.
###FifteenPuzzleProblem.py
Contiene le strutture dati necessarie alla risoluzone del 15-puzzle.
####FifteenPuzzle
Definisce il problema vero e proprio mantenendo come attributi 
gli stati iniziali e finali e l'euristica prescelta per la ricerca della
soluzione. I suoi metodi principali sono:
1. **actions()** che restituisce la lista di operazioni possibili dato uno stato
2. **result()** che dato uno stato ed un azione restituisce lo stato ottenuto applicando 
l'azione allo stato in ingresso
3. **goal_test()** che riceve in ingresso uno stato e controlla se esso coincida con il goal
4. **check_solvability()** che controlla che dallo stato iniziale fornito si possa arrivare
alla soluzione
5. **h()** che sulla base dell'attributo heuristic definisce una diversa euristica per il problema

####Node
È la classe che mantiene le informazioni di uno stato: lo stato vero e proprio, il suo predecessore
e l'azione con cui si è ottenuto, ed infine il path_cost dallo stato iniziale al nodo dato.
1. **expand()** è il metodo che restituisce l'insieme dei possibili nodi raggiunti dato il problema
ed uno stato di partenza.
2. **child_node()** che restituisce un nuovo nodo ottenuto applicando l'azione data al nodo 
3. **path()** restituisce il percorso dalla radice al nodo dato

###ManhattanDistance.py
Contiene la funzione che calcola la distanza Manhattan dallo "state" al "goal" in input.

###LinearConflicts.py
Contiene le funzioni relative al calcolo dell'euristica Linear Conflicts per il 15-puzzle.
Il metodo **linearConflicts()** invoca i metodi LC_rows() ed LC_columns() che si occupano rispettivamente
di calcolare il numero di mosse da aggiungere alla distanza Manhattan a causa dei conflitti tra le celle.
I due metodi implementano l'algoritmo fornito in [(Hansson et al. 1992)](https://www.cse.sc.edu/~mgv/csce580sp15/gradPres/HanssonMayerYung1992.pdf)
servendosi dell'ausilio di **conflict_rows()** e **conflict_columns()** responsabili rispettivamente del calcolo
dei conflitti su righe e colonne.

###PriorityQueue.py
Contiene la classe PriorityQueue che implementa la coda con priorità (determinata dalla funzione f definita alla creazione della coda)
con cui verrà realizzata la frontiera di espansione dell'algoritmo di ricerca. La coda si serve di uno heap della libreria
heapq. I metodi principali sono **append()**, che inserisce nella coda nella corretta posizione sulla base di f, **pop()** 
che rimuove il primo elemento dalla coda e **top()** che lo restituisce senza rimuoverlo.

###Shuffle.py
Contiene la funzione per effettuare lo shuffle di uno stato in input di un numero dato di mosse.

###Astar.py
Contiene l'algoritmo A* nella sua forma unidirezionale. **astar_search()** riceve in input il 
problema, ne controlla la risolvibilità ed invoca il metodo **best_first_search()** fornenendo come
funzione di valutazione il path_cost + l'euristica del problema.

###BidirectionalAstar.py
Contiene l'algoritmo A* nella forma bidirezionale.
Come nel caso unidirezionale la funzione astar_bidirectional_search(), dopo aver controllato la risolvibilità
del problema invoca il metodo biBF_search() che implementa la ricerca bidirezionale. Dopo aver creato [...]

###testHeuristicsMonodirectionalAstar.py
Se eseguito, restituisce il grafico che analizza il numero di stati esplorati dall'algoritmo A* sfruttando 3 
differenti euristiche: numero di tessere mal poste, Distanza Manhattan e Distanza Manhattan + Conflitti Lineari.
Questo è ottenuto calcolando il numero medio di stati esplorati applicando l'algoritmo a input con un numero di shuffle 
variabile (da 20 a 29)

###testHeuristicsBidirectionalAstar.py
Fornisce lo stesso grafico di testHeuristicsMonodirectionalAstar.py utilizzando però l'algoritmo bidirezionale.

###testAstar.py
Se eseguito fornisce i grafici che rispettivamente mostrano il numero di stati analizzati dall'algoritmo A* unidirezionale
e bidirezionale e la lunghezza della soluzione a conferma l'ottimalità di entrambi.

###test.py
Se eseguito fornisce un grafico che compara i due algoritmi combinati con le diverse euristiche in termini di numero di
stati esplorati.
