import sys,os,re,itertools
formulas = []
print('1-note formula')
print('0\n')
for x in range(1,12):
	formulas = itertools.combinations(['b2','2','b3','3','4','b5','5','b6','6','b7','7'],x)
	print(str(x+1) + "-note formulas")
	for f in formulas:
		print('1\t' + '\t'.join(f))
	print()