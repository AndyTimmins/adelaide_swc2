def dnaContent

passes = 0    
for (i, (seq, prefix, expected)) in enumerate(test):    
  if dna_Content(seq, prefix) == expected:    
    passes += 1    
else:    
  print('test %d failed' % i)    
    
print('%d/%d tests passed' % (passes, len(test)))




test = [	
['ACGTGT', {'A :1, 'C':1, 'G':2, 'T':2}, True],
['CAGGT', {'A :1, 'C':1, 'G':2, 'T':2}, True],

]




