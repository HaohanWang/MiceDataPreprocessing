__author__ = 'Haohan Wang'

import numpy as np

def sanityCheck(sanityIDs, miceIds):
    if len(sanityIDs) != len(miceIds):
        return False
    for i in range(len(sanityIDs)):
        if sanityIDs[i]!=miceIds[i]:
            return False
    return True

def extractGenomeInformation(i):
    text = [line.strip() for line in open('../data/GENOTYPES/chr'+str(i)+'.Build37.alleles')]
    ids = []
    for line in text:
        items = line.split()
        if items[0] == 'marker':
            ids.append(items[1])
    return ids

def snps2value(snps):
    p = len(snps[0])/2
    n = len(snps)
    result = np.zeros([n, p])
    for j in range(p):
        base = snps[0][j*2]
        baseCount = 0
        for i in range(n):
            for k in [j*2, j*2+1]:
                if snps[i][k] == base or snps[i][k] == 'NA':
                    baseCount += 1
        if baseCount > n:
            a = 0
            b = 2
        else:
            a = 2
            b = 0
        for i in range(n):
            if snps[i][j*2] == base:
                if snps[i][j*2+1] == base:
                    result[i,j] = a
                else:
                    result[i,j] = 1
            else:
                if snps[i][j*2+1] == base:
                    result[i,j] = 1
                else:
                    result[i,j] = b
    return result

def mergeGenotype():
    genomeInformation = []
    idSanityCheck = []
    data = []
    for i in range(1, 21):
        mice = []
        snps = []
        fileName = '../data/GENOTYPES/chr'+str(i)+'.Build37.data'
        text = [line.strip() for line in open(fileName)]
        genome = []
        for line in text:
            items = line.split()
            mouse = items[1]
            genome = items[6:]
            mice.append(mouse)
            snps.append(genome)
        genomeInformation.extend(extractGenomeInformation(i))
        if i == 1:
            idSanityCheck = [a for a in mice]
            result = snps2value(snps)
            data = result
        else:
            if sanityCheck(idSanityCheck, mice):
                result = snps2value(snps)
                data = np.append(data, result, 1)

    f1 = open('../final/snpID.txt', 'w')
    for a in genomeInformation:
        f1.writelines(str(a)+'\n')
    f1.close()

    f2 = open('../preprocessedFile/miceIDs.txt', 'w')
    for i in range(len(idSanityCheck)):
        if idSanityCheck[i].startswith('A0'):
            f2.writelines(idSanityCheck[i]+'\n')
    f2.close()

    print data.shape
    np.save('../preprocessedFile/miceSNPs', data)

if __name__ == '__main__':
    mergeGenotype()