# TATARSKI BIFTEK
def izracun_tatarski(kolicina_mesa):
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
""".format(meso=kolicina_mesa, smjesa=round((omjer * 10), 1), zumanjci=round((omjer * 2), 1), \
           senf=round((omjer * 2), 1), limun=round((omjer), 1), ulje=int(omjer * 100), \
           kecap=round((omjer * 2), 1), zacin=round((omjer), 1))
    return tatarski_biftek


# BOLOGNESE
def izracun_bolognese(kolicina_mesa):
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
Poklopite i pirjajte na laganoj vatri oko 2 sata (original 4h) uz povremeno miješanje.

Napomena:
Ovo je originalni recept za umak bolognese koji je još 1982. potvrdila trgovačka komora Bologne. Želite li biti dosjedni originalu, umjesto spaghetta (špageta) treba koristiti tagliatelle.
""".format(meso=kolicina_mesa, ulje=round((omjer * 2), 1), panceta=round((omjer * 6), 1), kapula=round((omjer * 2), 1), \
           cesanj=round((omjer * 3), 1), mrkva=round((omjer * 2), 1), vino=round((omjer * 2), 1),
           pelati=int(omjer * 800), \
           lovor=round((omjer * 2), 1), pasta=int(omjer * 900))
    return bolognese


# HAMBURGER
def izracun_hamburger(kolicina_mesa):
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

okus bude pomalo leskovacki.""".format(meso=kolicina_mesa, svinja=int(omjer * 150), mast=round(omjer, 1), \
                                       bjelanjak=round((omjer * 2), 1), kapula=round(omjer, 1),
                                       cesanj=round((omjer * 2), 1), konzerva=round(omjer, 1))
    return hamburger


# FAZOL
def izracun_fazol(kolicina_mesa):
    omjer = kolicina_mesa / 100
    fazol = """Sastojci:
*********
Fažol: 	{fazol} g
Brašno tip800: 	{brasno} g
Kapula:	{kapula} g
Češanj:	{cesanj} g
Mrkva:	{mrkva} g
Konzerva 30%:	{konzerva} g
Govedina:         {meso} g
Mast:	{mast} g
Paprika:	{paprika} g
Papar:	{papar} g
Peršin:	{persin} g
Vegeta:	{vegeta} g
Lovor:	{lovor} g
Sol

Priprema:
*********
Prebran pasulj potopiti u odgovarajuću količinu hladne vode i držati ga na hladnom mestu
da se kvasi 1-3 ćasa. Zatim ocediti vodu u kojoj je pasulj potapan, pa pasulj staviti u pogodnu posudu,
naliti hladnom vodom da ogrezne i kuvati 10-15 minuta od prokljućavanja.

U međuvremenu na deo vrele masnoće dodati polovinu sitno seckanog crnog luka i mrkvu, sečenu na sitnije kockice
ili rendisanu, malo propržiti, pa dodati meso prethodno odvojeno od kostiju i isećeno na kocke. 
Sve zajedno dinstati dok ne ispari otpuštena tečnost, skinuti sa vatre | odložiti do upotrebe.

Iz prokuvanog pasulja ocediti vodu pa dodati polovinu sitno seckanog crnog luka, prodinstana meso sa ostalim artiklima,
po potrebi naliti toplom vodom ili fondom od kostiju da ogrezne i kuvati uz povremeno dolivanje tople vode
dok svi artikli omekšaju.

Preostalu masnoću zagrejati, dodati brašno i pržiti da blago porumeni. Kada brašno porumeni, isključiti toplotu
pa odmahdodati papriku u prahu i tucani i sitno seckani beli luk i sve dobro Izmešati.

Kada pasulj omekša dodati lovorov list, dodatak jelima, koncentrovani sok od paradajza, prethodno razmućen u toploj
vodi, posoliti i zapržiti uz stalno mešanje pasulja da se zaprška ne zgrudva.

Pasulj sa zaprškom kuvati istiha jo$ 20-30 minuta, posla ćega isključiti toplotu, dodati samleveni biber,
sitno seckani peršunov list. probati ukus i po potrebi dosoliti.

Napomena: ako nema uslova da ae meso, mrkva | luk crni prodinstaju, tada sa ovi artikh sitno iseckani 
(meso isečeno na kocke) dodaju u pasul u vreme predviđeno recepturom za prodinstane ove artikle pa se sve skupa
kuva dok svi artikli omekšaju i dalje produži tehnološki postupak predviđenom recepturom

Pasulj se pri kirvanju ne sme mešati sve do zapržavanja da ne bi došlo do lomljenja zrna i zegorevanja.
""".format(meso=kolicina_mesa, fazol=int(omjer * 120), brasno=round((omjer * 8), 1), kapula=round((omjer * 20), 1), \
           cesanj=round((omjer), 1), mrkva=round((omjer * 10), 1), konzerva=round((omjer * 3), 1), \
           mast=round((omjer * 20), 1), paprika=round((omjer * 0.3), 1), papar=round((omjer * 0.1), 1), \
           persin=round((omjer), 1), vegeta=round((omjer), 1), lovor=round((omjer * 0.01), 1))
    return fazol