# Gioco

## Scopo del gioco

Bisogna prendere 10 monete senza essere colpiti dagli ostacoli

## Traiettorie degli ostacoli

Ogni tre secondi tre ostacoli si muoveranno verso il personaggio (da destra verso sinistra) seguendo traiettorie rettilinee e paraboliche casuali alternandosi(ex. al secondo 3 seguiranno traiettorie rettilinee, al secondo 6 seguiranno traiettorie paraboliche etc...)

## Svolgimento

Un personaggio su un aeroplano deve raccogliere monete durante il tragitto evitando gli ostacoli che si muovono verso di lui in modo imprevedibile.

## Comandi

Tasti direzionali (freccette) per muovere il personaggio.

## funzionamento blocchi: 
blocco 1: vengono disegnati sfondo, personaggio, timer econtatore in alto a destra dello schermo, la prima moneta (in una posizione casuale dello schermo)

blocco 2: viene richiesto il segnale per far partire il gioco (bisogna premere il tasto 'invio')

blocco 3: ogni cinque secondi vengono disegnate sullo schermo tre monete in posizioni casuali

blocco 4: ogni tre secondi, da destra verso sinistra vengono disegnati tre ostacoli che si muoveranno lungo traiettorie rettilinee e paraboliche alternandosi. 
Per esempio al secondo 3, tutti e tre i nemici disegnati si muovono lungo traiettorie rettilinee.
Al secondo 6 si muoveranno lungo traiettorie paraboliche casuali, al secondo 9 nuovamente rettilinee etc..

blocco 5: la posizione del personaggio coincide con uno dei punti appartenenti delle tre parabole o rette casuali? 

blocco 6: la posizione di una moneta e la posizione del personaggio coincidono?

blocco 7: lo schermo viene aggiornato, ciò significa che quando il personaggio incontra la moneta quest'ultima non sarà più visibile

![diagramma di flusso 3](https://user-images.githubusercontent.com/73583881/160933027-dc0ed9df-0c72-4576-a744-725e1e889bed.jpg)

blocco 8: il valore del contatore viene incrementato di +1

blocco 9: se il contatore raggiunge il valore 10, il gioco termina con esito positivo

blocco 10: indica la fine del gioco. 
Collegato al blocco 5 significa che la partita è stata persa.
Collegato al blocco 9 significa che la partita è stata vinta.
