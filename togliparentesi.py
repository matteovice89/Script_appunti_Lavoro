#scaricato l'elenco di dispositivi da un server dhcp avevo necssità togliere le parentesi quadrate che racchiudevano l'ip.
#ricordasi di lanciare tutto dalla stessa directory

f = open('elenco.txt','r') #apertura file

for linea in f:
    nlinea=linea.replace('[','')
    nlinea=nlinea.replace(']','')
    with open('nuovoElenco.txt','a') as ff :
        ff.write(nlinea)
