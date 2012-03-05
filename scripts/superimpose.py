import itertools
import sys


for x, y in zip(open(sys.argv[1]), open(sys.argv[2])): 
    for xc, yc in itertools.izip_longest(x.rstrip('\r\n'), y.rstrip('\r\n'), fillvalue=' '): 
        if yc == ' ': 
            sys.stdout.write(xc); 
        else: 
            sys.stdout.write(yc);
    sys.stdout.write('\n')
