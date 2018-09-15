# links


La documentazione relativa alla descrizione dei dati è disponibile a questo indirizzo: https://apidocs.wyscout.com/matches-wyid-events 

I dati relativi alla partita ed ai giocatori relativi sono scaricabili da questi link: 

Partita: https://bit.ly/2p3TcUY
Nomi giocatori: https://bit.ly/2Ndag9J


Esercizi
PROBLEMA 1
ESERCIZIO:
Calcolare la posizione media di ogni calciatore che abbia giocato almeno 45 minuti. Calcolare inoltre la distanza quadratica media di ogni giocatore rispetto alla sua posizione media. Calcolare, per ogni giocatore, il tempo medio che passa tra due eventi del giocatore (in secondi). 
Formato file da caricare:
- File csv (comma separated values) con il seguente header:
identificativo_calciatore,nome_calciatore,squadra_calciatore,posizione_media_x, posizione_media_y,distanza_quadratica_media,tempo_medio_tra_eventi
- Chiamare il file di output "problema_1.csv"
- Chiamare il file Python "problema_1.py"

Suggerimenti:
1. La distanza quadratica media di un giocatore rispetto alla sua posizione media è definita come la sommatoria, per ogni posizione p del calciatore, della distanza al quadrato tra la posizione p e la posizione media, fratto il numero totale di eventi del calciatore nella partita. 
2. L'attributo "positions" in ogni evento fornisce la posizione iniziale e finale dell'evento stesso sul campo (nota che la posizione finale non è presente per alcuni tipi di evento).
3. L'attributo "eventSec" fornisce il tempo in secondi dall'inizio della frazione di gioco corrente (ossia primo o secondo tempo) in cui accade l'evento.

Soluzioni problema 1
PROBLEMA 2
Risolvere gli esercizi seguenti:

ESERCIZIO (a):
Calcolare l'accuratezza media dei passaggi per ogni squadra e la sua standard deviation.

Formato file output:
- File csv (comma separated values) con il seguente header:
nome_squadra,accuratezza_media_dei_passaggi,standard_deviation_accuratezza_media_dei_passaggi
- Chiamare il file di output "problema_2_a.csv"
- Chiamare il file Python "problema_2_a.py"

Suggerimenti:
- Il tag "accurate" indica se un passaggio effettuato è accurato
- L'accuratezza media dei passaggi di una squadra è definita come la media delle accuratezze dei passaggi di ogni calciatore di quella squadra. La standard deviation dell'accuratezza dei passaggi di una squadra è definita come la deviazione standard delle accuratezze dei passaggi dei singoli calciatori di quella squadra. L'accuratezza dei passaggi per un calciatore è data dal numero di passaggi accurati del calciatore rispetto al suo numero totale di passaggi durante la partita. 


ESERCIZIO (b):
Fornire la lista dei calciatori che hanno fatto almeno due tackle e che si trovano nel quarto quartile della distribuzione dei tackle vinti. 

Formato file da caricare:
- File csv (comma separated values) con il seguente header: 
identificativo_calciatore,nome_calciatore,tackle_vinti
- Chiamare il file di output "problema_2_b.csv" 
- Chiamare il file Python "problema_2_b.py"

Suggerimenti:
- Un tackle è identificato dall'evento "ground defending duel". Il tag "won" indica che il tackle è stato vinto.

Soluzioni problema 2
PROBLEMA 3
Risolvere gli esercizi seguenti:
ESERCIZIO (a):
Dividere il campo di gioco in una griglia 5x5 (ossia in 25 celle di uguale dimensione). Per ogni cella e per ogni squadra calcolare:
i. Frequenza degli eventi effettuati (numero di eventi in quella cella sul totale degli eventi della squadra)
ii. Frequenza di passaggi accurati effettuati (numero di passaggi accurati in quella cella sul totale dei passaggi accurati)
iii. Frequenza di tiri effettuati 
iv. Frequenza di falli subiti 

Formato dei file da caricare:
- File csv (comma separated values) con il seguente header:
nome_squadra,numero_cella_x,numero_cella_y,frequenza_eventi,frequenza_passaggi_accurati,frequenza_tiri,frequenza_falli_subiti
- Chiamare il file di output "problema_3_a.csv"
- Chiamare il file Python "problema_3_a.py"

Suggerimenti:
- Le posizioni sul campo sono espresse in percentuali da 0 a 100. Esempio: (0, 50) indica il centro della propria porta per entrambe le squadre.
- Il tag "accurate" indica se un passaggio effettuato è accurato
- Se una cella non presenta eventi di un determinato tipo, la  sua frequenza per quel tipo di evento sarà 0.
- numero_cella_x indica la posizione della cella (tra 0 e 4) in cui 0 indicherà la cella più vicina alla propria porta e 4 quella più vicina alla porta avversaria.
- numero_cella_y indica la posizione della cella (tra 0 e 4) in cui 0 indicherà la cella più vicina al fallo laterale alla sinistra della propria porta, e 4 quella più vicina al fallo laterale a destra della propria porta.


ESERCIZIO (b):
Data la griglia costruita secondo l'esercizio (a)-i, calcolare la similarità tra le griglie delle due squadre. Per calcolare la similarità utilizzare la distanza coseno di similitudine (cosine similarity - https://it.wikipedia.org/wiki/Coseno_di_similitudine). Ripetere lo stesso esercizio per le griglie di cui ai punti (a)-ii, (a)-iii e (a)-iv.

Formato dei file da caricare:
- File csv (comma separated values) con il seguente header: 
tipo_griglia,similarity
- Chiamare il file di output "problema_3_b.csv"
- Chiamare il file Python "problema_3_b.py"

Suggerimenti:
- Il campo tipo_griglia può assumere valori da 1 a 4 e indica le griglie costruite secondo le quattro variabili indicate nei punti (a)-i, (a)-ii, (a)-iii, (a)-IV.


ESERCIZIO (c):
Calcolare la squadra "dominante" in ogni cella delle griglia costruita secondo il punto (a)-i. Una squadra è "dominante" in una cella se il suo valore di frequenza è maggiore di quello della squadra avversaria. Ripetere lo stesso esercizio per le griglie di cui ai punti (a)-ii, (a)-iii e (a)-iv.

Formato dei file da caricare:
- File csv (comma separated values) con il seguente  header: tipo_griglia,numero_cella_x,numero_cella_y,squadra_dominante,differenza_di_frequenza
- Chiamare il file di output "problema_3_c.csv"
- Chiamare il file Python "problema_3_c.py"

Suggerimenti:
- Il campo "differenza_di_frequenza" è la differenza in valore assoluto tra i valori di frequenza delle due squadre in una cella. 
