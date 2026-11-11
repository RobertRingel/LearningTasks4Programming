"""
Moon Landing Simulation 
A Python program to simulate a lunar landing, teaching core programming and physics concepts.

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2026  
License: CC BY-SA 4.0
"""

print(">>> Retrorockets Moon landing <<< ")
print("    task 5")
print()

g = 1.622     
f = 1500.0
fbr = 10.0
h = 1000.0    
s = 0.0       
v = 0.0       
ds = 0.0      
v0 = v
b = 0.0       
t = 0.0       
dT = 1.0      

a = g
while h > 0.0:    
    print(f"Sec:{t:>5g} | {h:>6.1f}m | {v:>5.1f}m/s | Fuel:{f:>4.0f}l ", end=":")

    if f > 0.0:
        fb = input("Braking fuel (0–50): ")
        fb = float(fb)
    else:
        fb = 0.0
        print()

    f = f - fb    
    b = fb / (fbr*dT) 
    a = g - b     

    v0 = v        
    v = v + a*dT     
    ds = 0.5 * a * dT * dT + v0 * dT   
    h = h - ds                         

    t = t + dT

    if f < 0.0:
        print("Fuel exhausted!!!")
        f = 0.0

print("Touch down.")
v = 3.6 * v
print("    ... speed:", v, "km/h")