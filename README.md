# NTRU-1998
Implementacja NTRU 1998 oraz analiza błędów deszyfracji

Analiza sytuacji gdy parametry __N, p, q, d__ kryptosystemu NTRU spełniają warunek ![equation](https://latex.codecogs.com/svg.latex?q%20%3E%20%286d&plus;1%29p) oraz jego wpływ na błedy w deszyfracji wiadomości.

# Założenia

## W celu przeprowadzenia doświadczenia przyjąłem następujące założenia:


* __N__ - liczba z przedziału _(100, 512)_, względnie pierwsza z __p__
* __p__ - losowa liczba z przedziału _(3, 200)_
* __q__ - losowa liczba pierwsza z przedziału _(4, 512)_, z założeniem, że: 
  ![equation](https://latex.codecogs.com/svg.latex?%5Cfrac%7BN%7D%7B2%7D%3C%20q%20%3C%20N%20-1)
oraz drugiego przypadku ![equation](https://latex.codecogs.com/svg.latex?q%20%3E%20%286d&plus;1%29p)
* __d__ - losowa liczba z zakresu z przedziału _(4, 12)_

Do przeprowadzonego badania zostało przyjęte wygenerowanie 10 iteracji losowych paramentów __N, p, q, d__, które następnie zostały poddane 100 próbom szyfrowania oraz deszyfrowania przy przyjętych obu przepadkach badawczych.
