import sys, os, re, argparse, struct
wt1 = sys.argv[1:]
while not (len(wt1) == 32):
    wt = input('Wave: ')
    wt1 = wt.split()
for i in wt1:
    while not (re.match('\d\d?', i.strip())):
        wt = input('Wave: ')
        wt1 = wt.split()
def convertwt(wt, list):
    wtlist = wt.split()
    print(wtlist)
    for s in wt:
        i = int(s, 10)
        list.append(i)
def towav(wtlist):
    strs = ""
    for s in wtlist:
        s = str(hex(int(s)))
        s = s.replace('0x','')
        #print(s)
        strs = strs + str(s.upper())
    print(strs)
    os.system('echo ' + strs.strip() + '| clip')
    print('Copied to clipboard')
#wt1list = []
#convertwt(wt1,wt1list)
towav(wt1)
