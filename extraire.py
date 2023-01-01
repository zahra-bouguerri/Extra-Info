import urllib.request 
import re 
import codecs 
import string 
import sys 

args=True

if len(sys.argv)!=3:
	print("entrer l'intervalle d'extraction et le port du serveur en arguments")
	args=False

else:	
	if (not re.match("[A-Za-z]-[A-Za-z]",sys.argv[1])) or (sys.argv[1][2].upper()< sys.argv[1][0].upper()):
		print("premier argument est faux")
		args=False
	
	if re.search(r"\D",sys.argv[2]):
		print("Le format du port est incorrect")
		args=False

if args:
	
	Dinfo={}
	n=0
	
	dic=open("subst.dic",'w',encoding='utf-16-le')
	dic.write('\ufeff')
	
	alpha=string.ascii_uppercase
	
	for j in range(alpha.index(sys.argv[1].upper()[0]),alpha.index(sys.argv[1].upper()[2])+1):
		
		url= urllib.request.urlopen('http://localhost:'+sys.argv[2]+'/vidal/vidal-Sommaires-Substances-'+alpha[j]+'.htm')
		html=url.read().decode('utf8')
		
		medoc=re.findall("(<a href=\"Substance.+?>)(.+?)(</a>)",html)
		Dinfo[alpha[j]]=len(medoc)
		n=n+len(medoc)
		
		for i in medoc:
			dic.write(i[1]+",.N+subst\n")
		
		
	dic.close()
		
	infos=open("infos1.txt",'w')
	
	for i in Dinfo:
		infos.write("les medicaments qui commance par"+i+": "+str(Dinfo.get(i))+"\n")
	infos.write("\nTotal: "+str(n))
