#!/usr/bin/env python

import cmath

jw = complex(0, 2.0 * cmath.pi * 13.56e6)
def ZR(R): return R
def ZL(L): return jw * L
def ZC(C): return 1.0 / (jw * C)


# die Werte
Zs = (ZR(100), ZR(25), ZC(220e-12))
Vs = (13.0, 6.56, 14.1)



def relation(v):
	"""relations between values"""
	relations = []
	for i in xrange(len(v)):
		for j in xrange(i+1, len(v)):
			relations.append(v[i]/v[j])
	return relations

def vload(Zload, Zi, V0=1.0):
	"""
		Source voltage Vload = abs( V0 * Zload / (Zload + Zi) )
	"""
	return abs((V0 * Zload) / (Zload + Zi))


VsRel = relation(Vs)
def error(r, x):
	"""
		calculates a "relative square error" sum
	"""
	# inner resistance is the value to search
	Zi = complex(r, x)

	results = []
	for v, z in zip(Vs, Zs):
		results.append ( vload(z, Zi) )

	error = 0.0
	for Vs1, Vs2 in zip(VsRel, relation(results)):
		# koennte eine division by zero ergeben...
		error += (1.0 - (Vs1 / Vs2)) ** 2
	return error


# try and error iterator

# start values and search windows
Rvals0 = 50
Rwindow = 50 # +/-
Xvals0 = 0
Xwindow = 100 # +/-
frac = 1.0

for loop in xrange(6):
	#~ print '--------------'
	Xvals = (Xvals0-Xwindow, Xvals0+Xwindow)
	Xvcnt = Xvals[1] - Xvals[0]
	Rvals = (max(0, Rvals0-Rwindow), Rvals0+Rwindow)
	#~ print 'R', Rvals
	#~ print 'X', Xvals

	deviants = []
	for r in xrange( *Rvals ):
		Zr = float(r) * frac
		for x in xrange( *Xvals ):
			Xr = float(x) * frac
			deviants.append( error(Zr, Xr) )

	# find best value
	min_dev = min(deviants)
	idx = deviants.index( min_dev )
	Rvals0 = (idx // Xvcnt + Rvals[0]) * 10
	Xvals0 = (idx % Xvcnt + Xvals[0]) * 10
	frac /= 10.0
	# can be set very small now
	Xwindow = 21
	Rwindow = 21


R = float(Rvals0) * frac
X = float(Xvals0) * frac
print 'Z = {:.5f}{:+.5f}j'.format(R, X)
print 'deviation:', min_dev

print 'Validation ...'
for Vload, Zload, in zip(Vs, Zs):
	print 'V0 is {:.6f}V @ {:.3f}Ohm'.format(Vload / vload(Zload, complex(R, X)), Zload)

