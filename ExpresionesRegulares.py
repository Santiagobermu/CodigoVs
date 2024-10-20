#!/home/santiago/Descargas

import re

#1879-04-05,England,Scotland,5,4,Friendly,London,England,FALSE

pattern = re.compile(r'^([\d]{4,4})\-\d\d\-\d\d,(.+),(.+),(\d+),(\d+),.*$')

f = open ("/home/santiago/Descargas/Resultados_partidos.csv", "r")

for line in f:
    res = re.match(pattern, line)
    if res:
        total = int(res.group(4)) + int(res.group(5))
        if total > 10:
            print ("goles: %d, %s %s,%s [%d-%d]" %\
                   (total, res.group(1), res.group(2), \
                    res.group(3), int(res.group(4)), \
                   int(res.group(5))))

f.close()