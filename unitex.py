import os 

from os import path 
if path.exists("corpus-medical_snt") :
    os.system("rd /s corpus-medical_snt")
    
os.mkdir("corpus-medical_snt")
os.system("UnitexToolLogger Normalize corpus-medical.txt -r Norm.txt")

#-----using Aphabet.txt-------pour triee les tokens en ordre alphabetique et donner pour chaque lettres le nombre du substence dans corpus-medical.snt 
os.system("UnitexToolLogger Tokenize corpus-medical.snt -a Alphabet.txt")
#-----------------------------

os.system("UnitexToolLogger Compress subst.dic")

#-----using Aphabet.txt-------pour triee le contenue des dictionnaires(subst.bin) en ordre alphabetique donner pour chaque lettres le nombre du substence dans corpus-medical.snt 
os.system("UnitexToolLogger Dico -t corpus-medical.snt -a Alphabet.txt subst.bin  Dela_fr.bin")
#-----------------------------

os.system("UnitexToolLogger Grf2Fst2 posologie.grf")

#-----using Aphabet.txt-------pour triee les matches en ordre alphabetique et donner pour chaque lettres le nombre du substence dans corpus-medical.snt
os.system("UnitexToolLogger Locate -t corpus-medical.snt posologie.fst2 -a Alphabet.txt -L -I --all")
#-----------------------------

os.system("UnitexToolLogger Concord corpus-medical_snt/concord.ind -f \"Courrier new\" -s 12 -l 40 -r 55")



