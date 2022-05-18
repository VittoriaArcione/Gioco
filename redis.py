import redis
from random import*

r = redis.StrictRedis(host= '93.145.175.242', port= 63213, password='1357642rVi0', db= 0)

f=[]
risultati_partita=str(f)

r.keys()

for i in range(10):
    partita=input('che partita hai fatto?')
    esito= input('hai vinto oppure hai perso?')
    r.set('partita', 'esito')
    value = r.get('NumeroPartita')
    f.append(value)
    print(value)
    
print(risultati_partita)



def insCanc():

    if(r.scard(risultati_partita)>0):
        for i in range(r.scard(risultati_partita)):  # per ogni riga del file vengono eseguite le righe di codice che seguono
                r.spop(risultati_partita)
                print(r.scard(risultati_partita))

    else:
        for line in f:  # per ogni riga del file vengono eseguite le righe di codice che seguono
            r.sadd(risultati_partita, line[:-1])
            print(line[:-1])
            print(r.scard(risultati_partita))

insCanc()