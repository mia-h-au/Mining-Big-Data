import argparse
import random
import sys
import time
from efficient_apriori import apriori, itemsets_from_transactions

parser = argparse.ArgumentParser(description="datasets")
parser.add_argument('-f', '--file', default="chess.dat")
parser.add_argument('-s', '--min_support', default = 0.8)
#verbosity: 1 to see number of frequent itemsets only. 2 to see detail
parser.add_argument('-v', '--verbosity', default = 1) 
parser.add_argument('-p', '--probability', default = 0.1)               
args = parser.parse_args()

sample = []

# pick some chunks at random to serve as the sample
# using probability and a random number
def pick_sample(probability):
    return random.random() < float(probability)

# Read the entire dataset, and for each basket, select that basket for the sample with some fixed probability p. 
# Suppose there are m baskets in the entire file. At the end, we shall have a sample whose size is very close to pm baskets.
def read_file():    
    global i 
    i = 1
    dataset = open(args.file, "r")    
    print("Read the file line by line and store it into an array.")
    # read the entire dataset
    for line in dataset:        
        line = line.rstrip()
        line_row = line.split()        
        # add random chunks to our sample
        if (pick_sample(args.probability)):
            sample.append(tuple(line_row))
        i += 1
    dataset.close()
    print (i, " lines read.")

def main():
    start_time = time.time()
    # read file and select sample
    read_file()
    print("Randomized algorithm with probability = ", args.probability, " on ", args.file)
    print("Support ratio = ", args.min_support, " . Support threshold = ", i*float(args.min_support))
    # use apriori algorithm on the sample    
    itemsets, rules = itemsets_from_transactions(sample, min_support=float(args.min_support),  max_length=3, verbosity=int(args.verbosity), output_transaction_ids=True)   
    print("Run time: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
    main()