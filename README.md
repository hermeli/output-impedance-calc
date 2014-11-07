output-impedance-calc
=====================

Output Impedance Calculator (Thevenin)

This python script calculates the output impedance and source voltage from a given set 
of measurements of an unknown source. 

It works like this:

1) Connect a Resistor R1 (e.g. 100 Ohms) to the unknown source
2) Measure voltage V1 across resistor
3) Connect a Resistor R2 (e.g. 25 Ohms) to the unknown source
4) Measure voltage V2 across resistor
5) Connect a Capacitor C1 (e.g. 220pF) to the unknown source
6) Measure voltage V3 across capacitor

Input these values with a script editor and run the script. This is what you get:

$ python outputimp.py 
Z = 48.62478-1.24352j
deviation: 2.62646802837e-17
Validation ...
V0 is 19.321898V @ 100.000Ohm
V0 is 19.321898V @ 25.000Ohm
V0 is 19.321898V @ 0.000-53.350jOhm
