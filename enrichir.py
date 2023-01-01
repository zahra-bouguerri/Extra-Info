import re, sys, urllib.request
from string import ascii_uppercase


corpus = open(sys.argv[1], 'r+', encoding='utf-8')
tmp = open('subst.dic', 'r+', encoding='utf-16')  
dic = open('subst.dic', 'a+', encoding='utf-16')
dicenri = open('subst_corpus.dic', 'w+', encoding='utf-16')

nb=0   #nombre de substances 
listCorpus = corpus.readlines()
errors = ["posologie","crp","intraveineuse","kt","kcl","eau","hémoglobine","nfs"] #mots erroné detecter par l'expression reguliere
for ligne in listCorpus:
    searchreg = re.search(r'''^[-*]?\s?(\w+)\s:?\s?(\d+|,|\d+.\d)+\s(mg|ml|µg|mcg|g|cp|amp|flacon).+''', ligne, re.I)     
    if searchreg:       
        if searchreg.group(1).lower() not in errors:
            dicenri.write(searchreg.group(1).lower()+',.N+subst\n')
            dic.write(searchreg.group(1).lower()+',.N+subst\n')     
            nb+=1
            print(str(nb)+" : "+searchreg.group(1))    
            
#suppression des doublons de subst.dic

dic = open('subst.dic', 'r+', encoding='utf-16')
tri = sorted(list(set(dic.readlines())))
dic = open('subst.dic', 'w+', encoding='utf-16')
for el in tri:
    dic.write(el)


# creation du  info3.txt

info3 = open('info3.txt', 'w+', encoding='utf-8')
dicenri = open('subst_corpus.dic', 'r+', encoding='utf-16')
list = tmp.readlines()
listDicEnri = dicenri.readlines()
nbLet = 0
for el in listDicEnri:
    if el not in list:   #verifier l'existence de medicament 
        nbLet+=1
        info3.write(el)
info3 = open('info3.txt', 'r+', encoding='utf-8')
list = info3.readlines()
info3 = open('info3.txt', 'w+', encoding='utf-8')
for letter in ascii_uppercase:       #le nombre de substances par lettre de l'alphabet
    nbLet=0
    for i in list:
        if letter == i[0].upper():
            nbLet+=1
            info3.write(i)
    info3.write('Number of  '+letter+': '+str(nbLet)+'\n')
    info3.write('_____________________________________\n')
info3.write('Total number: '+str(len(list(set(list)))))


# Creation du info2.txt

info2 = open('info2.txt', 'w+', encoding='utf-8')
dicenri = open('subst_corpus.dic', 'r+', encoding='utf-16')
listDicEnri = dicenri.readlines()
for letter in ascii_uppercase:       
    nbLet=0
    for el in list(set(listDicEnri)):
        if letter == el[0].upper():
            nbLet+=1
            info2.write(el)
    info2.write('Number of '+letter+': '+str(nbLet)+'\n')
    info2.write('_____________________________________\n')
info2.write('Total number: '+str(len(list(set(listDicEnri)))) + '\n')
