infile  = open('testfile.txt', 'r')       # opened for reading only
outfile = open('file.output.txt', 'w')    # opened for writing
for line in infile.readlines():
    outfile.write(line)
