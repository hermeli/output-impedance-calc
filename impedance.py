#!/usr/bin/env python

import cmath

# complex function definiton
jw = complex(0, 2.0 * cmath.pi * 13.56e6)
def ZR(R): return R
def ZL(L): return jw * L
def ZC(C): return 1.0 / (jw * C)
def par(Z1,Z2): return Z1*Z2/(Z1+Z2)
def ser(Z1,Z2): return Z1+Z2

# sample circuit
#
#  o---Cs------------
#           |   |   |
#  (-> Zin) Cp  Lp  Rp
#           |   |   |
#  o----------------- 

# sample values
Cs = ZC(30e-12)
Cp = ZC(68e-12)
Lp = ZL(1e-6) 
Rp = ZR(5.6e3)

# calculate total
Zin = Cs + par(Cp,par(Lp,Rp))

print "Result Zin =",
print Zin
