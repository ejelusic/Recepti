# TATARSKI BIFTEK

def izracun_tatarski(kolicina_mesa):
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
-Sol, Papar, Čili
      
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
""".format(meso = kolicina_mesa, smjesa = round((omjer*10),1), zumanjci = round((omjer*2),1), \
                   senf = round((omjer*2),1), limun = round((omjer),1), ulje = int(omjer*100), \
                   kecap = round((omjer*2),1), zacin = round((omjer),1))
    return tatarski_biftek

# BOLOGNESE
def izracun_bolognese(kolicina_mesa):
    kolicina_mesa = kolicina_mesa
    omjer = kolicina_mesa / 1000
    bolognese = """Sastojci:
*********
{ulje} žlice maslinovog ulja
{panceta} tankih feta pancete, sitno nasjeckane
{kapula} veća luka, usitnjena
{cesanj} česnja češnjaka, zdrobljena
{mrkva} mrkvice, nasjeckane
malo celera
{meso} kg nemasne mljevene govedine
{vino} velike čaše crnog vina, 
{pelati} g pelata,
{lovor} lista lovora, sol, svježe mljeveni papar
{pasta} kg tagliatella
svježe naribani parmezan za posluživanje

Priprema:
*********
Zagrijte ulje u posudi debela dna, 
prepržite pancetu, 
dodajte luk, češnjak i mrkvice
pirjajte dok ne omekšaju. 
Pojačajte vatru i dodajte mljevenu govedinu 
pirjajte dok ne posmeđi. 
Dolijte vino i kuhajte dok trećina ne ispari, 
posolite, popaprite. 
Smanjite temperaturu i 
umiješajte rajčicu i celer te dodajte lovorov list.
Poklopite i pirjajte na laganoj vatri sat, sat i pol, uz povremeno miješanje.

Napomena:
Ovo je originalni recept za umak bolognese koji je još 1982. potvrdila trgovačka komora Bologne. Želite li biti dosjedni originalu, umjesto spaghetta (špageta) treba koristiti tagliatelle.
""".format(meso = kolicina_mesa, ulje = round((omjer*2),1), panceta = round((omjer*6),1), kapula = round((omjer*2),1), \
           cesanj = round((omjer*3),1), mrkva = round((omjer*2),1), vino = round((omjer*2),1), pelati = int(omjer*800), \
           lovor = round((omjer*2),1), pasta = int(omjer*900))
    return bolognese

#HAMBURGER
def izracun_hamburger(kolicina_mesa):
    kolicina_mesa = kolicina_mesa
    omjer = kolicina_mesa / 350
    hamburger = """Sastojci:
*********
{meso}g govedjeg
{svinja}g svinjećeg (nevalja da je bas precisto meso)
{mast} Zlica masti
{bjelanjak} bjelanjka
persina, soli i papra
{kapula} velika kapula
{cesanj} cesnja cesnjaka
{konzerva} Zlica konzerve
par zlica vode
malo sode bikarbone

Priprema:
*********
sve dobro izmjesati i ostaviti bar jedan dan da odstoji, eventualno jos premjesitit ili oblikovati pljeskavice

ispeci pljeske i prepeci peciva na toj masti 
sloziti hamburgere po gustu..

okus bude pomalo leskovacki.""".format(meso = kolicina_mesa, svinja = int(omjer*150), mast = round(omjer,1), \
                                       bjelanjak = round((omjer*2),1), kapula = round(omjer,1), cesanj= round((omjer*2),1), konzerva = round(omjer,1))
    return hamburger