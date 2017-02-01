import sys, os, re, argparse, struct
parser = argparse.ArgumentParser(description='Normalize')
parser.add_argument('--normalize',
    action='store_true',
    help='normalize flag' )
args = parser.parse_args()
wt1 = ""
wt2 = ""
num = ""
while not (re.match('[0-9A-F]{32}', wt1)):
    wt1 = input('First wave: ')
    wt1 = wt1.upper()
while not (re.match('[0-9A-F]{32}', wt2)):
    wt2 = input('Last wave: ')
    wt2 = wt2.upper()
while not (num.isdigit()):
    num = input('Number of waveforms (blank for default=16): ')
    if num.isdigit():
        num = int(num)
        if num < 3:
            print("Sorry but we need at least 3, so we'll use 3 instead")
            num = 3
        if num > 16:
            print("Sorry but the max is 16 so we'll use 16 instead")
            num = 16
        break
    else:
        num = 16
        break
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
def interpolate(wtlist1, wtlist2, wtlist3, num):
    wtlist3.append(wtlist1)
    #magic happens
    for i in range(0,num-2):
        nextwt=[]
        for s in range(0,len(wtlist1)):
            sample = wtlist3[i][s]+((wtlist2[s]-wtlist1[s])/(num-1))
            nextwt.append(sample)
        wtlist3.append(nextwt)
    wtlist3.append(wtlist2)
def writebin(wtlist):
    bin = []
    for r in wtlist:
        for s in range(0,len(r),2):
            n = struct.pack('B', (int(round(r[s])) << 4) | (int(round(r[s+1]))))
            bin.append(n)
    if (len(wtlist) < 16):
        zeros = [136] * 16
        for i in range(0,16-len(wtlist)):
            for z in zeros:
                bin.append(struct.pack('B',z))
    with open('wavmorph.snt','wb') as newFile:
        for b in bin:
            newFile.write(b)
        print('\nwavmorph.snt written!')
def printerpolate(wtlist):
    print()
    for r in wtlist:
        wtstr = ""
        for s in r:
            s = str(hex(int(round(s))))
            s = s.replace('0x','')
            wtstr = wtstr + s.upper()
        print(wtstr)
    if (len(wtlist) < 16):
        strzeros = ['8'] * 32
        for i in range(0,16-len(wtlist)):
            print(''.join(strzeros))
wt1list = []
wt2list = []
wt3list = []
convertwt(wt1,wt1list)
convertwt(wt2,wt2list)
interpolate(wt1list,wt2list,wt3list,num)
if args.normalize:
    print('Normalizing waveforms...')
    for w in wt3list:
        normalize(w)
printerpolate(wt3list)
writebin(wt3list)
