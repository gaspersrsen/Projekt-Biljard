# Projekt-Biljard
Projekt v 2. letniku FMF pri Računalništvu.


## <b><u> Wikipedija </u></b>
Na osnovi principa ohranitve kinetične energije, ki je na slikah spodaj, se izvaja simulacija v polarnih koordinatah.<br/><br/>
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_white&space;\begin{align}&space;\mathbf{v}'_1&=\mathbf{v}_1-\frac{2&space;m_2}{m_1&plus;m_2}&space;\&space;\frac{\langle&space;\mathbf{v}_1-\mathbf{v}_2,\,\mathbf{x}_1-\mathbf{x}_2\rangle}{\|\mathbf{x}_1-\mathbf{x}_2\|^2}&space;\&space;(\mathbf{x}_1-\mathbf{x}_2)&space;\\&space;\mathbf{v}'_2&=\mathbf{v}_2-\frac{2&space;m_1}{m_1&plus;m_2}&space;\&space;\frac{\langle&space;\mathbf{v}_2-\mathbf{v}_1,\,\mathbf{x}_2-\mathbf{x}_1\rangle}{\|\mathbf{x}_2-\mathbf{x}_1\|^2}&space;\&space;(\mathbf{x}_2-\mathbf{x}_1)&space;\end{align}" /><br/>
<img src="https://upload.wikimedia.org/wikipedia/commons/2/2c/Elastischer_sto%C3%9F_2D.gif"/><br/><br/>

# 

## <b><u> Zahteve za izvajanje simulacije: </u></b>
* Python vsaj verzije 3.0 (napisano v 3.9.1) dosegljiv na:<br/>
https://docs.python.org/3/using/windows.html#launcher
* Modul Pygame (napisano v 2.0.1) za python doseglijiv na:<br/>
https://www.pygame.org/wiki/GettingStarted
<br/><br/>


## <b><u> Izvajanje simulacije: </u></b>
* Osnova: 100 naključnih delcev <br/>
poženemo datoteko Biljard.py<br/>
* Iz datoteke preberemo delce:<br/>
poženemo datoteko Biljard.py --File={lokacija datoteke}<br/>
v datoteki dodajamo delce s naslednjimi lastnosti:<br/>
masa, x, y, v, kot, radij, R, G, B, nakljucnaBarva<br/>

* <b> Dodatne nastavitve pri zagonu datoteke: </b> <br/>
* * gravitacija="{vrednost}"<br/>
        željena Zemeljska gravitacija navzdol (ponavadi manj od 0.5)<br/>
* * kTrenja="{vrednost}"<br/>
        željen koeficient trenja (ponavadi manj od 0.05)<br/>
* * kUpor="{vrednost}"<br/>
        željen koeficient zračnega upora (ponavadi manj od 0.001)<br/>
* * "gravKonst="{vrednost}"<br/>
        željen medsebojni privlak (ponavadi manj od 0.1)<br/>
        <b><u> POZOR: ta nastavitev občutno upočasi simulacijo <br/>
        POZOR: Meddelčna gravitacija ni primerna za natančne simulacije,ker popravek prekrivanja delcev pri odbojih
        doda v simulacijo energijo.</u></b>
* * "steviloDelcev="{vrednost}"<br/>
        Število novonastalih delcev<br/>
        <b><u> POZOR: --File povozi to nastavitev </u></b> <br/>
* * "mavrica"<br/>
        naključna barva delcev<br/>

*  "Želja" - napišemo tekst in delce razporedimo v ta tekst, ki nato "disociira"
<br/>

#
## <b><u> Interakcija z oknom </u></b>
* Ko teče simulacija jo lahko ustavimo/poženemo s preslednico.
* Spremenljivke okolja lahko nadziramo z drsniki.
* Pravtako pa lahko premikamo delce po polju.
<br/>

#
## <b><u> Viri: </u></b>
* https://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/ <br/>
    Velik del kode sledi iz teh navodil, kako napisati program, ki simulira odboj kroglic.
* https://en.wikipedia.org/wiki/Elastic_collision <br/>
* https://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/ <br/>
    Večina kode za uporabniško okno izhaja iz te strani.