# Analiza performantelor algoritmilor de sortare

Acest proiect reprezinta un studiu experimental realizat in cadrul disciplinei Algoritmi si Structuri de Date si are ca scop compararea performantelor mai multor algoritmi de sortare utilizand implementari dezvoltate in Python.

Proiectul include:
- implementarea algoritmilor de sortare;
- generarea automata a seturilor de date;
- teste de performanta pentru diferite tipuri de input;
- generarea de grafice comparative;
- analiza scalabilitatii algoritmilor;
- interpretarea rezultatelor obtinute.

---

# Algoritmi analizati

## Algoritmi de complexitate patratica
- Bubble Sort
- Insertion Sort
- Selection Sort

## Algoritmi eficienti
- Merge Sort
- Quick Sort
- Heap Sort
- Shell Sort

## Algoritmi specializati
- Radix Sort
- TimSort

---

# Tipuri de date utilizate

Testele au fost realizate pe urmatoarele tipuri de seturi de date:
- Random
- Sorted
- Reversed
- Nearly Sorted

Dimensiunile utilizate variaza intre:
- 100
- 250
- 500
- 1000
- 2500
- 5000
- 7500
- 10000
- 15000
- 20000 elemente

---

# Structura proiectului

```text
sorting-study/
│
├── run_benchmark.py
├── graphs.py
├── results.csv
│
├── charts/
│   ├── scalability_chart.png
│   ├── bar_chart_log.png
│   ├── efficient_Random.png
│   ├── quadratic_Reversed.png
│   └── ...
│
├── ranking_table.csv
├── complexity_table.csv
│
└── latex/
    └── lucrare.tex
