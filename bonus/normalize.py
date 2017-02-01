import sys, os, re, argparse, struct
wt1 = sys.argv[1]
while not (re.match('[0-9A-F]{32}', wt1)):
    wt1 = input('Wave: ')
    wt1 = wt1.upper()
def convertwt(wt, list):
    for s in wt:
        i = int(s, 16)
        list.append(i)
def normalize(wtlist):
    old_min = min(wtlist)
    old_range = max(wtlist) - old_min
    new_min = 0
    new_range = 15.9999999999
    for s in range(0,len(wtlist)):
        wtlist[s] = int((wtlist[s] - old_min) / old_range * new_range + new_min)
wt1list = []
convertwt(wt1,wt1list)
normalize(wt1list)
wtstr=""
for s in wt1list:
    s = str(hex(int(round(s))))
    s = s.replace('0x','')
    wtstr = wtstr + s.upper()
print(wtstr)
os.system('echo ' + wtstr.strip() + '| clip')
print('Copied to clipboard')
