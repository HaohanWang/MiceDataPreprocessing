__author__ = 'Haohan Wang'

import numpy as np

def loadPhenotypes():
    text = [line.strip() for line in open('../data/PHENOTYPES/RESIDUALS/combinePheno.txt')]
    f = open('../final/phenoIDs.txt', 'w')
    for line in text[0].split()[1:]:
        f.writelines(line+'\n')
    f.close()
    pheno = {}
    for line in text[1:]:
        items = line.split()
        id = items[0]
        pheno[id] = '\t'.join(items[1:])
    return pheno

def loadGenotype():
    textIDs = [line.strip() for line in open('../preprocessedFile/miceIDs.txt')]
    snps = np.load('../preprocessedFile/miceSNPs.npy')
    genotype = {}
    for i in range(len(textIDs)):
        genotype[textIDs[i]] = snps[i,:]

    return genotype

def mergeFiles():
    pheno = loadPhenotypes()
    geno = loadGenotype()

    f1 = open('../final/IDs.txt', 'w')
    f3 = open('../preprocessedFile/mergePhenotypes.txt', 'w')
    data = []

    for mid in pheno:
        if mid in geno:
            f1.writelines(mid+'\n')
            f3.writelines(pheno[mid]+'\n')
            data.append(geno[mid])
    f1.close()
    f3.close()

    data = np.array(data)
    print data.shape
    np.save('../final/snps', data)


if __name__ == '__main__':
    mergeFiles()