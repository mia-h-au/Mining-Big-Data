INSTRUCTIONS TO RUN THE CODE (tested on Ubuntu virtual machine with Python 3):

In the console: cd to this folder containing randomized.py and datasets
python3 randomized.py -f [filename] -s [support ratio] -p [probability] -v [verbosity]
Default: [filename] = chess.dat, [support ratio] = 0.8, [probability] = 0.1, [verbosity] = 1 
(verbosity = 1: see the numbers of frequent itemsets only; = 2: see the frequent itemsets)

Frequent itemsets (singletons, pairs and triplets) will display on console. 