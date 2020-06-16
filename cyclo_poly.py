import numpy as np
import math

#-------------------------------------------------------------------------------
def nth_root_poly(n):
    """Creates a polynomial of the form x^n - 1.

    Args:
        n: A natural number.

    Returns:
        An instance of the class numpy.poly1d
    """
    polyCoef = [0 for x in range(0, n - 1)]
    polyCoef.insert(0, 1)
    polyCoef.append(-1)
    return np.poly1d(polyCoef)


def divisors_of(n):
    """Returns list with all the divisors of the natural number n"""
    vector = [1]
    for x in range(2, n + 1):
        if n % x == 0:
            vector.append(x)
    return vector


def is_prime(n):
    """Checks if n is a prime"""
    if (n < 2):
        return False
    for i in range(2, n + 1):
        if (i * i <= n and n % i == 0):
            return False
    return True


def euler_totient(n):
    "Euler's totient function"
    num_coprimes = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            num_coprimes += 1
    return num_coprimes


def mobius_function(n):
    """Mobius function (Number Theory)"""
    if (n == 1):
        return 1
    p = 0
    for i in range(1, n + 1):
        if (n % i == 0 and is_prime(i)):
            if (n % (i * i) == 0):
                return 0
            else:
                p += 1
    if (p % 2 != 0):
        return -1
    else:
        return 1


def mobius_cyclotomic(n):
    """Mobius formula for cyclotomic polynomials.
    
    Args: A naural number n.

    Returns: List of coefficients of the nth-cyclotomic
        polynomial
    """
    positive_powers = np.poly1d([1])
    negative_powers = np.poly1d([1])
    for d in divisors_of(n):
        if mobius_function(int(n / d)) == 1:
            positive_powers = np.polymul(positive_powers, nth_root_poly(d))
        elif mobius_function(int(n / d)) == -1:
            negative_powers = np.polymul(negative_powers, nth_root_poly(d))
        else:
            continue
    integer_coef = [coef for coef in
                     np.polydiv(positive_powers, negative_powers)[0]]
    return  integer_coef


class CycloPoly1d(np.poly1d):
    """Class for the 1 variable cyclotomic polynomial.

    This class inherits from the poly1d class in numpy. The only difference is
    in the coeff_dict method, which returns a dictionary of non-zero
    coefficients.

    Methods:
        coef_dict(self): Returns dictionary of none-zero coefficients.

    """
    def __init__(self,n):
        super().__init__(mobius_cyclotomic(n))

    def coef_dict(self):
    """ Returns dictionary of none-zero coefficients."""
        coef_dict = {}
        for index in range(0, self.order + 1):
            if self.coef[index] != 0:
                coef_dict[self.order - index] = self.coef[index]
        return coef_dict


class CycloPoly2d():
    """Class for the 2 variable cyclotomic polynomial

    Methods:
        coef_dict(self): Returns dictionary of none-zero coefficients.
        __str__(self): Returns a string version of the polynomial for printing.
        __call__(self,x,y): Evaluates the polynomial on (x,y) coordinates.
    """


    def __init__(self,n):
        self.coef = mobius_cyclotomic(n)
        self.order = euler_totient(n)
        
    def coef_dict(self):
    """ Returns dictionary of none-zero coefficients."""
        coef_dict = {}
        for index in range(0, self.order + 1):
            if self.coef[index] != 0:
                coef_dict[self.order - index] = self.coef[index]
        return coef_dict

    def __str__(self):
    """Returns a string version of the polynomial for printing"""
        string = ''
        for power,coef in self.coef_dict.items():
            if coef > 0:
                string += '+' + str(int(coef)) + 'x^' + str(power) + 'y^' + str(self.order - power) + ' '
            else:
                string += '-' + str(int(coef)) + 'x^' + str(power) + 'y^' + str(self.order - power) + ' '
        return string

    def __call__(self,x,y):
        """Returns the result of evaluating the polynomial 
        on the coordinates (x,y)"""
        value = 0
        for i in range(0,self.order+1):
            coef_i = int(self.coef[i])
            x_i = int(math.pow(x,self.order-i))
            y_i = int(math.pow(y,i))
            value = value + int(coef_i*x_i*y_i)
        return value