import itertools
infile = open("movie_csv.csv","r")
newfile=open("genre_csv.csv","w")


for line in infile:
    line=line.split(",")
    genre=line[4]
    genre=genre.strip()
    genre=genre.rstrip(";")
    genre=genre.split(";")
    if len(genre) >= 2:
        com = itertools.combinations(genre, 2)
        comb = list(com)
        for i in range(len(comb)):
            newfile.write("%s,%s\n" %(comb[i][0],comb[i][1]))
infile.close()
newfile.close()