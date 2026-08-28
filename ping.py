*** elenco estratto da dhcp server di windows server, prendo ip per ip testo se è raggiungibile ***
import platform
import subprocess
ip_list = []
with open('elenco.txt', 'r', encoding='utf-8') as f:
    for riga in f:
        inizio = riga.find('[')
        fine = riga.find(']')
        if inizio != -1 and fine != -1:
            ip = riga[inizio + 1 : fine]
            

    


            comando = ["ping", '-n', '1', ip]

            risultato = subprocess.run(comando, capture_output=True, text=True)
            with open('raggiungibili.txt','a') as ff :
                if risultato.returncode == 0:
                    scrivi=(riga + " RAGGIUNGIBILE \n")
                    ff.write(scrivi)
                else:
                     scrivi=(riga + " NON RAGGIUNGIBILE \n")
                     ff.write(scrivi)

f.close()

