
from MainWindow import *

## TATARSKI BIFTEK

def izracun_ispis(kolicina_mesa):
    kolicina_mesa = kolicina_mesa
    omjer = kolicina_mesa / 600
    tatarski_biftek = """Sastojci
        *************
        {meso} g juneće pisanice - skosati
    
        [nasjeckati]
        {smjesa}g slanih inćuna
        {smjesa}g kiselih krastavaca
        {smjesa}g kapara
        {smjesa}g svježeg peršinovog lista
        {smjesa}g luka
        
        [majoneza]
        {zumanjci} žumanjka
        {senf} žličice Dijon senfa
        {limun} limun (sok)
        {ulje} ml suncokretovog ulja
        {kecap} žličice kečapa
        
        [pomješati]
        [Začiniti]
        -Sol, Papar, Čili)
        
        [dodati u meso i miješati, dodavajući]
        {zacin} žličica Tabasco umaka
        {zacin} žličica Worcester umaka
        {zacin} žličica konjaka
        
        
        Priprema
        ***********
        -Za pripremu tatarskog bifteka, najbolje je uzeti rep i prvu polovicu srednjeg dijela junećeg bifteka. Meso dobro očistite od svih masnoća i žilica pa ga usitnite.
        Možete ga strugati ili sjeckati nožem sve dok se ne postane mazivo.
        
        – sitno nasjeckajte inćune, kisele krastavce, kapare, luk i peršinov list.
        
        - zamiješajte majonezu od žumanjaka, senfa i soka jednog limuna, postupno dodajući ulje u tankoj niti ili kap po kap.
        U dobivenu majonezu dodajte kečap, dobro promiješajte pa dodajte ostale sastojke koje ste prethodno nasjeckali.
        
        - Smjesu začinite solju, paprom i čilijem prema ukusu, a potom dodajte meso i miješajte tako da u jednu ruku uzmete žlicu, a u drugu vilicu.
        
        - Smjesu na kraju začinite Tabasco i Worcester umakom te konjakom, dobro promiješajte i ostavite u hladnjaku da se sastojci sjedine.
        """.format(meso = kolicina_mesa, smjesa = int(omjer * 10), zumanjci = int(omjer * 2), senf = int(omjer * 2), limun = int(omjer * 1), ulje = int(omjer * 100), kecap = int(omjer * 2), zacin = int(omjer))
    return tatarski_biftek

