import math
import random

def sestejVektorja(kot1, dolzina1, kot2, dolzina2): 
    """Seštevek dveh vekotjev"""
    x = math.sin(kot1) * dolzina1 + math.sin(kot2) * dolzina2
    y = math.cos(kot1) * dolzina1 + math.cos(kot2) * dolzina2
    kot  = 0.5 * math.pi - math.atan2(y, x) #Pazi ker je y definiran navzdol
    dolzina = math.sqrt(x ** 2 + y ** 2)
    return (kot, dolzina)

def skalarniProdukt(kot1, dolzina1, kot2, dolzina2):
     return math.sin(kot1) * dolzina1 * math.sin(kot2) * dolzina2 + math.cos(kot1) * dolzina1 * math.cos(kot2) * dolzina2

def odboj(d1, d2):
    """Elastičen odboj dveh delcev (ohranitev Energije)"""
    razx = d1.x - d2.x
    razy =  d1.y - d2.y
    sestm = d1.m + d2.m
    r2 = d2.radij + d1.radij
    odmik = math.sqrt(razx ** 2 + razy ** 2)
    
    if (odmik < r2):
        kotOdboja = math.atan2(razy, razx) + math.pi / 2
        #kinPred = d1.kineticnaEnergija() + d2.kineticnaEnergija()
        
        (k1, v1) = sestejVektorja(d1.kot, d1.v, d2.kot, -d2.v)
        (k2, v2) = sestejVektorja(d2.kot, d2.v, d1.kot, -d1.v )
        (d1.kot, d1.v) = sestejVektorja(d1.kot, d1.v, kotOdboja, (-2 * d2.m / sestm) * skalarniProdukt(k1, v1, kotOdboja, 1))
        (d2.kot, d2.v) = sestejVektorja(d2.kot, d2.v, kotOdboja +math.pi , (-2 * d1.m / sestm) * skalarniProdukt(k2, v2, kotOdboja, -1))
        
        """#Popravek zaradi računskih napak, ki so včasih tudi večje od 3%
        kinPo = d1.kineticnaEnergija() + d2.kineticnaEnergija()
        popravekKin = 1
        if(kinPo != 0):
            popravekKin = math.sqrt(kinPred / kinPo)
            if (abs(popravekKin - 1) > 0.01):
                print(popravekKin)
            d1.v *= popravekKin
            d2.v *= popravekKin"""

        prekrivanje = 0.5 * (r2 - odmik + 1)
        d1.x += math.sin(kotOdboja) * prekrivanje
        d1.y -= math.cos(kotOdboja) * prekrivanje
        d2.x -= math.sin(kotOdboja) * prekrivanje
        d2.y += math.cos(kotOdboja) * prekrivanje


#Konstruktor objektov
class Objekt:
    """Definicija objektov (krogov), ki jih simuliramo
    ter njihove funkcije"""
    def __init__(self, m, x, y, v, kot, radij, barva):
        self.m = m  #Masa
        self.x = x  #Pozicija
        self.y = y
        self.v = v  #Hitrost
        self.kot = kot  #Kot hitrosti
        self.radij = radij  #Radij
        self.barva = barva  #Barva
        self.debelina = self.radij  #Debelina

    def __repr__(self):
        return "Objekt(m={0.m}, x={0.x}, y={0.y}, v={0.v}, kot={0.kot}, r={0.radij})".format(self)

    def kineticnaEnergija(self):  #Kinetična energija delca
        return self.m *0.5 * (self.v * self.v)

    def potencialnaEnergija(self, other): #Potencialna energija delca
        return self.m * other.gravitacija * (other.visina - self.y) / other.casovniKorak

    def pospesek(self, vektor): #Pospešek delca
        (self.kot, self.v) = sestejVektorja(self.kot, self.v, vektor[0], vektor[1])

    def premik(self, other):  #Premik delca za nek čas dt
        self.x += self.v * other.casovniKorak * math.sin(self.kot)
        self.y -= self.v * other.casovniKorak * math.cos(self.kot)  #y je definiran navzdol

    def premikMiska(self, kazalec): #Prijem delca z miško, ter njegov premik
        razx = kazalec[0] - self.x
        razy =  kazalec[1] - self.y
        self.kot = math.pi / 2 + math.atan2(razy, razx)
        self.v = math.sqrt(razx **2 + razy ** 2) * 0.1


class Okolje:
    """Okolje simulacije, z njegovimi definicijami ter interakcijo z delci"""
    def __init__(self, sirina, visina, **kargs):
        self.sirina = sirina
        self.visina = visina
        self.delci = []
        self.barva = kargs.get("barva", (0,0,0))
        self.casovniKorak = kargs.get("casovniKorak", 0.1)
        self.gravitacija = kargs.get("gravitacija", 0.0) * self.casovniKorak  #0.99 * self.casovniKorak 
        self.kTrenja = kargs.get("kTrenja", 0.0) * self.casovniKorak  #0.0001 * self.casovniKorak
        self.kUpor = kargs.get("kUpor", 0.0) * self.casovniKorak  #0.0001 * self.casovniKorak
        self.gravKonst = kargs.get("gravKonst", 0.0) * self.casovniKorak

    def dodajDelec(self, n = 1, **kargs): 
        """Dodajanje delcev z možnimi atributi:(m, x, y, v, kot, radij, barva, mavrica)
        Mavrica povozi barvo"""
        for i in range(n):
            radij = kargs.get("radij", random.randint(10, 50))
            m = kargs.get("m", radij**2 * math.pi)
            x = kargs.get("x", random.randint(radij, int(self.sirina - radij)))
            y = kargs.get("y", random.randint(radij, int(self.visina - radij)))
            v = kargs.get("v", random.randint(-3, 3))
            kot = kargs.get("kot", random.uniform(-math.pi, math.pi))
            barva = kargs.get("barva", (200, 200, 200))
            if kargs.get("mavrica", False):
                barva = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self.delci.append(Objekt(m, x, y, v, kot, radij, barva))
    
    def odbojStena(self, other):  
        """Interakcija delca s steno"""
        if other.x >= self.sirina - other.radij:
            other.kot = -other.kot
            other.x = self.sirina - other.radij
        elif other.x <= other.radij:
            other.kot = -other.kot
            other.x = other.radij
        if other.y >= self.visina - other.radij:
            other.kot = math.pi - other.kot
            other.y = self.visina - other.radij
        elif other.y <= other.radij:
            other.kot = math.pi -other.kot
            other.y = other.radij

    def simuliraj(self): 
        """Pokliče vse potrebne funkcije, da se delci
        premaknejo v skladu s simulacijo"""
        for i, delec in enumerate(self.delci):
            vektorPosp = sestejVektorja(math.pi, self.gravitacija, delec.kot, -self.kTrenja - self.kUpor * delec.v **2)
            delec.pospesek(vektorPosp)
            #delec.pospesek((math.pi, self.gravitacija))
            #delec.pospesek((delec.kot, -self.kTrenja - self.kUpor * delec.v **2))
            delec.premik(self)
            self.odbojStena(delec)
            for delec2 in self.delci[i+1:]:
                odboj(delec, delec2)
                if (self.gravKonst !=0):
                    self.gravitacijaDelca(delec, delec2)

    def znotrajDelca(self, pozicija):  #Ali je dana znotraj kakšnega delca
        for d in self.delci:
            if math.sqrt((d.x - pozicija[0]) ** 2 + (d.y - pozicija[1]) ** 2) <= d.radij:
                return d

    def gravitacijaDelca(self, d1, d2): 
        """Gravitacijski privlak med dvema delcema"""
        razx = d1.x - d2.x
        razy =  d1.y - d2.y
        kotPrivlaka = math.atan2(razy, razx)
        mocPrivlaka = self.gravKonst / (razx ** 2 + razy ** 2)  #Brez mas
        vektor1 = (kotPrivlaka - 0.5 * math.pi, mocPrivlaka * d1.m)
        vektor2 = (kotPrivlaka + 0.5 * math.pi, mocPrivlaka * d2.m)
        d1.pospesek(vektor1)
        d2.pospesek(vektor2)
