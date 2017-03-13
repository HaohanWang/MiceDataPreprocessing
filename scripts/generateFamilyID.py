__author__ = 'Haohan Wang'

def generateFamilyID():
    ids = [line.strip() for line in open('../final/IDs.txt')]
    text = [line.strip() for line in open('../data/gender.and.family')]

    id2family = {}
    familyUnique = {}
    c = 0
    for line in text:
        items = line.split('\t')
        fa = items[-1]
        if fa not in familyUnique:
            familyUnique[fa] = c
            c+=1
        id2family[items[0]] = familyUnique[fa]

    family = [id2family[s] for s in ids]

    f = open('../final/familyIDs.txt', 'w')
    for m in family:
        f.writelines(str(m)+'\n')
    f.close()

    print len(set(family))

if __name__ == '__main__':
    generateFamilyID()