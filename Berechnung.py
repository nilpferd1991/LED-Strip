#!/usr/bin/env python

n = int(raw_input("Reihen: "))
m = int(raw_input("Spalten: "))
UGES = float(raw_input("U_ges: "))

ULED = 3.2
ILED = 15/1000.0

print("Anzahl Spalten:", n)
print("Anzahl Reihen:", m)
print("Anzahl LEDs:", n*m)
print("Gesamtleistungs:", m*ILED * UGES, "W")
print("Gesamtstrom:", m*ILED, "A")
print("Gesamtspannung:", UGES, "V")
print("Spannung am Widerstand:", UGES - n*ULED, "V")
print("Widerstandswert:", (UGES - n*ULED)/ILED, "Ohm")
print("Leistung am Widerstand:", (UGES - n*ULED)*ILED, "W")
