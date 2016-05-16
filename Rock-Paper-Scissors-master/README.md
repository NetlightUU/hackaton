# Sten Sax Påse Bottar #
Uppgiften här är att skriva en sten-sax-påse bot i Python.

Din bot får reda på din motspelares förra drag genom den globala variabeln `input`. Dragen representeras av bokstäverna `'R'`, `'P'` och `'S'` för sten, sax och påse (Rock, Paper, Scissors). Första rundan är strängen tom.
Din bot ska skriva sitt drag (en av bokstäverna) till den globala variabeln `output`.

Efterssom sten sax påse består av flera rundor så kan det vara bra att spara tidigare drag eller annan heurustisk information i globala variabler för att kunna dra slutsatser av det i senare versioner.

Det finns lite exempelprogram i gitrepot https://github.com/Netlight-KTH/Rock-Paper-Scissors/

## Körningen ##

Ni kan köra bottarna mot varandra genom att använda filen `rpsrunner.py` och ge den bottarnas filer som argument.

`python rpsrunner.py bot1.py bot2.py`

Ni kan också skicka in era bottar till alexander.viklund@netlight.com så kommer vi att köra alla bottar mot varandra. 
