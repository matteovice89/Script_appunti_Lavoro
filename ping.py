import subprocess

f = open('nuovoElenco.txt','r') #apertura file

for linea in f:
    destinazione=linea[:11]


    comando = ["ping", '-n', '1', destinazione]

    risultato = subprocess.run(comando, capture_output=True, text=True)
    with open('raggiungibili.txt','a') as ff :
        if risultato.returncode == 0:
            scrivi=(linea + " RAGGIUNGIBILE \n")
            ff.write(scrivi)
        else:
             scrivi=(linea + " NON RAGGIUNGIBILE \n")
             ff.write(scrivi)

f.close()

