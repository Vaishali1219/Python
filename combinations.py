from itertools import *
  
# Get all combinations of [1, 2, 3] and length 2 
comb = combinations_with_replacement(['A','A','A','S'], 4) 
  
# Print the obtained combinations 
for i in list(comb): 
    print (i) 
