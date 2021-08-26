import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))


def fileread(filename):
    name = []
    infile = open(filename, "r")
    infile.readline()
    for line in infile:
        line = line.rstrip('\n')
        word2 = line.split(" ; ")
        for i in range(len(word2)):
            name.append(word2[i])
    return name

#print(fileread("names.txt"))
