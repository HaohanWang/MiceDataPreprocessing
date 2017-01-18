__author__ = 'Haohan Wang'

import numpy as np

def cleanPhenotype():
    text = [line.strip() for line in open('../preprocessedFile/mergePhenotypes.txt')]
    n = len(text)
    p = len(text[0].split()) - 4
    data = np.zeros([n, p])
    phenos = []
    for line in text:
        phenos.append(line.split())
    for j in range(p):
        NAidx = []
        value = []
        for i in range(n):
            if phenos[i][j]!='NA':
                value.append(float(phenos[i][j]))
                data[i,j] = float(phenos[i][j])
            else:
                NAidx.append(i)
        m = np.mean(value)
        for i in NAidx:
            data[i,j] = m

    print data.shape
    np.save('../final/pheno', data)

if __name__ == '__main__':
    cleanPhenotype()