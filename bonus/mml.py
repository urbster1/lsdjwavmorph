import sys, os, re, argparse, struct
wt1 = sys.argv[1]
while not (re.match('[0-9A-F]{32}', wt1)):
    wt1 = input('Wave: ')
    wt1 = wt1.upper()
def convertwt(wt, list):
    for s in wt:
        i = int(s, 16)
        list.append(i)
def tomml(wtlist):
    strs = ""
    for s in wtlist:
        #print(s)
        strs = strs + str(s) + ' '
    print(strs)
    os.system('echo ' + strs.strip() + '| clip')
    print('Copied to clipboard')
wt1list = []
convertwt(wt1,wt1list)
tomml(wt1list)
