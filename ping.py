'''non è bello, bisognerebbe estrre l'ip in un altro modo ma per procaedere velocemente mi va bene così'''
import subprocess

f = open('nuovoElenco.txt','r') #apertura file

for linea in f:
    destinazione=linea[:11]


    comando = ["ping", '-n', '1', destinazione]

    risultato = subprocess.run(comando, capture_output=True, text=True)
    with open('raggiungibili.txt','a') as ff :
        if risultato.returncode == 0:
            ff.write(" " + linea + " RAGGIUNGIBILE")
        else:
             ff.write(" " + linea + " NON RAGGIUNGIBILE")
             print(risultato.stderr)

f.close()
