def removeNreturnGC(dna):
 
    dna = dna.replace('N', '')
    gc = dna.count('G') + dna.count('C')
    return gc/float(len(dna))

print removeNreturnGC('AGCTGCNNNNNSCTG')



