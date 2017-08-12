__author__ = 'Haohan Wang'

import numpy as np

def generateGoldenStandard():
    text = [line.strip() for line in open('../final/phenoIDs.txt')]
    ind2pheno = {}
    pheno2ind = {}
    for i in range(len(text)):
        line = text[i]
        ind2pheno[i] = line
        pheno2ind[line] = i


    phenos = np.load('../final/pheno.npy')
    inds = []
    gs = []

    text = [line.strip() for line in open('../data/extraInformation/phenosOfInterest')]
    names = []

    for line in text:
        if line.startswith('['):
            items = line[1:-1].split(',')
            idx = [int(j) for j in items]

            for i in range(len(gs)):
                if gs[i] is None:
                    gs[i] = idx
        else:
            inds.append(pheno2ind[line])
            gs.append(None)
            names.append(line)

    inds = np.array(inds)
    phenos = phenos[:, inds]

    print phenos.shape
    print len(gs)
    for g in gs:
        print g

    np.save('../finalWithGoldenStandard/pheno', phenos)
    np.save('../finalWithGoldenStandard/goldenStandard', gs)
    f = open('../finalWithGoldenStandard/phenoNames.txt', 'w')
    for n in names:
        f.writelines(n+'\n')
    f.close()

if __name__ == '__main__':
    generateGoldenStandard()