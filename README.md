# CyclotomicPolynomial
A Python module for Cyclotomic Polynomials

### Description
This module can be considered as a small extension to the polynomial class in numpy, 
more exactly the poly1d class. I also added a class for a Cyclotomic Binary Form, which
is just a two variable version of a cyclotomic polynomial.

The heart of this module are the classes CycloPoly1d and CycloPoly2d. The first one inherits
from the poly1d class from numpy, so it has the same functionality and properties as the poly1d class.
CycloPoly2d doesn´t have that much functionality, but it can be used for basic stuff or you can use the `mobius_cyclotomic(n)`
function (which returns a list of coefficients of the nth-cyclotomic polynomial) to create your own 
cyclotomic polynomial class to your liking.

Due to the mathematical formula used to construct the cyclotomic polynomials this module also contains
some arithmetic functions from number theory, such as Euler's totient function, Möbius function, 
the divisor function and a function to determine if a number is a prime number.


### About the construction of the cyclotomic polynomials
The formula to obtain a cyclotomic polynomial is this one:

![equation](https://latex.codecogs.com/svg.latex?%5Cphi_n%28x%29%3D%5Cprod_%7Bd%7Cn%7D%28x%5Ed-1%29%5E%7B%5Cmu%28%5Cfrac%7Bn%7D%7Bd%7D%29%7D)

where ![](https://latex.codecogs.com/svg.latex?%5Cphi_n) denotes the nth cyclotomic polynomial, 
![](https://latex.codecogs.com/svg.latex?%5Cmu) 
is the Möbius function and 
![](https://latex.codecogs.com/svg.latex?%5Csmall%20%5Cprod_%7Bd%7Cn%7D) 
denotes the product over all the divisors of the natural number
![](https://latex.codecogs.com/svg.latex?%5Cinline%20n). This formula can be implemented in code very straightforward once you have the
needed arithmetic functions. 

For more information and examples about cyclotomic polynomials you can visit
this [wikipedia article on cyclotomic polynomials](https://en.wikipedia.org/wiki/Cyclotomic_polynomial) and 
I also recommend the book *Abstract Algebra* from Dummit and Foote, which contains a little section about this topic.
