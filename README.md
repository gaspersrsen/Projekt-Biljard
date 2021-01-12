# Projekt-Biljard
Projekt v 2. letniku FMF pri Računalništvu.


## Wikipedija
Na osnovi principa ohranitve kinetične energije, ki je na slikah spodaj, se izvaja simulacija v polarnih koordinatah.<br/>
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_white&space;\begin{align}&space;\mathbf{v}'_1&=\mathbf{v}_1-\frac{2&space;m_2}{m_1&plus;m_2}&space;\&space;\frac{\langle&space;\mathbf{v}_1-\mathbf{v}_2,\,\mathbf{x}_1-\mathbf{x}_2\rangle}{\|\mathbf{x}_1-\mathbf{x}_2\|^2}&space;\&space;(\mathbf{x}_1-\mathbf{x}_2)&space;\\&space;\mathbf{v}'_2&=\mathbf{v}_2-\frac{2&space;m_1}{m_1&plus;m_2}&space;\&space;\frac{\langle&space;\mathbf{v}_2-\mathbf{v}_1,\,\mathbf{x}_2-\mathbf{x}_1\rangle}{\|\mathbf{x}_2-\mathbf{x}_1\|^2}&space;\&space;(\mathbf{x}_2-\mathbf{x}_1)&space;\end{align}" /><br/>
<img src="https://upload.wikimedia.org/wikipedia/commons/2/2c/Elastischer_sto%C3%9F_2D.gif"/><br/><br/>

## Zahteve za izvajanje simulacije:
* Python vsaj verzije 3.0 (napisano v 3.9.1) dosegljiv na:<br/>
https://docs.python.org/3/using/windows.html#launcher
* Modul Pygame (napisano v 2.0.1) za python doseglijiv na:<br/>
https://www.pygame.org/wiki/GettingStarted

##Izvajanje simulacije:
* poženemo datoteko Biljard.py - 200 naključnih različno pobarvanih delcev
* "WIP" - iz datoteke preberemo delce
* "Želja" - napišemo tekst in delce razporedimo v ta tekst, ki nato "disociira"

Ko teče simulacija jo lahko ustavimo/poženemo s preslednico. Spremenljivke okolja lahko nadziramo z drsniki. Pravtako pa lahko premikamo delce po polju.



## POZOR
Meddelčna gravitacija ni primerna za natančne simulacije,
ker popravek prekrivanja delcev pri odbojih
doda v simulacijo energijo.

## Viri:
* https://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/ <br/>
    Velik del kode sledi iz teh navodil, kako napisati program, ki simulira odboj kroglic.
* https://en.wikipedia.org/wiki/Elastic_collision
