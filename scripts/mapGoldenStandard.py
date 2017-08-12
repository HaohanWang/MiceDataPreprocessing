__author__ = 'Haohan Wang'
import numpy as np

def getSNPPositions():
    text = [line.strip() for line in open('../final/snpID.txt')]
    i = -1
    idx2snp = {}
    snp2idx = {}
    for line in text:
        i += 1
        idx2snp[i] = line
        snp2idx[line] = i

    text = [line.strip() for line in open('../data/extraInformation/mapfile.txt')][1:]

    position = {}
    for line in text:
        items = line.split()
        if items[1] == 'X':
            c = 20
        else:
            c = int(items[1])
        position[items[0]] = (c, int(items[2]))

    for k in position:
        if k in snp2idx:
            ind = snp2idx[k]
            idx2snp[ind] = position[k]

    return idx2snp

def getGoldenStandard(fileName, outfile, idx2snp):
    text = [line.strip() for line in open('../data/extraInformation/'+fileName)]
    inds = []
    for line in text:
        items = line.split('\t')
        if items[3] == 'X':
            c = 20
        else:
            c = int(items[3])
        positions = items[4].split('- ')
        l = int(positions[0])
        u = int(positions[1])
        for k in idx2snp:
            ci, pi = idx2snp[k]
            if ci == c:
                if l <= pi <= u:
                    inds.append(k)
    print inds
    np.save('../preprocessedFile/idx_'+outfile, inds)

if __name__ == '__main__':
    idx2snp = getSNPPositions()
    for fn in ['anxiety', 'asthma', 'CD3', 'CD4', 'CD8', 'diabetes']:
        print fn
        getGoldenStandard(fn, fn, idx2snp)

