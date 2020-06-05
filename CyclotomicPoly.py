# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:07:35 2020

@author: Omar
"""

import numpy as np
import math

"""
Functions needed to create de nth-cyclotomic polynomial
"""
def nth_root_poly(n):
    """ Creates a polynomial of the form x^n - 1, to use on Mobius formula.
        Uses numpy polynomials
    """
    polyCoeffs = [0 for x in range(0,n - 1)]
    polyCoeffs.insert(0,1)
    polyCoeffs.append(-1)
    return np.poly1d(polyCoeffs) #returns polynomial x^n-1

def divisors_of(n):
    """Returns all divisors of n"""
    vector = [1]
    for x in range(2, n + 1):
        if n % x == 0:
            vector.append(x)
    return vector

def is_prime(n): 
    """Check if n is a prime"""
    if (n < 2): 
        return False
    for i in range(2,n + 1): 
        if (i * i <= n and n % i == 0): 
            return False
    return True

def euler_totient(n):
    "Euler's totient function"
    num_coprimes = 0        
    for k in range(1, n + 1):
        if math.gcd(n,k) == 1:
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
    """Mobius formula for cyclotomic polynomials, 
       returns the array of coefficients of the polynomial"""
    positive_powers = np.poly1d([1])
    negative_powers = np.poly1d([1])
    for d in divisors_of(n):
        if mobius_function(int(n / d)) == 1:
            positive_powers = np.polymul(positive_powers, nth_root_poly(d))
        elif mobius_function(int(n / d)) == -1:
            negative_powers = np.polymul(negative_powers, nth_root_poly(d))
        else:
            continue
    integer_coeff = [coeff for coeff in 
                     np.polydiv(positive_powers, negative_powers)[0]]
    return  integer_coeff
    

"""Some Cyclotomic Polynomials have a ton of zero coefficients, so I
    added the coeff_dict attribute, which returns a none-zero value dictionary 
    of the form {...,k:a_k,... }, where a_nx^n + ... + a_kx^k + ... + a_0""" 
        
class CycloPoly1d(np.poly1d):
    def __init__(self,n):
        super().__init__(mobius_cyclotomic(n))
        self.coeff_dict = {self.order - index: self.coef[index] 
                       for index in range(0,self.order+1) 
                       if self.coef[index] != 0}
        
class CycloPoly2d():
    def __init__(self,n):
        self.coeff = mobius_cyclotomic(n)
        self.order = euler_totient(n)
        self.coeff_dict = {self.order - index: self.coeff[index] 
                       for index in range(0,self.order+1) 
                       if self.coeff[index] != 0}
        
    def __str__(self):
        string = ''
        for power,coeff in self.coeff_dict.items():
            if coeff > 0:
                string += '+' + str(coeff) + 'x^' + str(power) + 'y^' + str(self.order - power) + ' '
            else:
                string += '-' + str(coeff) + 'x^' + str(power) + 'y^' + str(self.order - power) + ' '
        return string     
            
    def __call__(self,x,y):
        """Evaluates the polynomial on the coordinates (x,y)"""
        value = 0
        for i in range(0,self.order+1):  
            coef_i = int(self.coeff[i])
            x_i = int(math.pow(x,self.order-i))
            y_i = int(math.pow(y,i))
            value = value + int(coef_i*x_i*y_i)
        return value
        

        
            


        
        