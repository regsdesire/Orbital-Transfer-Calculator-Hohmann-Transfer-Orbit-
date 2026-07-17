# main.py
import ctypes
import os
import subprocess

#0 clear the terminal before execution
subprocess.run("cls", shell=True)

#1 Load the compiled C library
# Note: On Windows, use .dll. On Mac/Linux, use .so or .dylib
lib_path = os.path.abspath("math_engine.dll") 
lib = ctypes.CDLL(lib_path)

# 2. Define the argument and return types
lib.vis_viva.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.vis_viva.restype = ctypes.c_double

#3 Handle the user input
print("|||- - - Orbital Velocity Calculator - - -|||")
m1 = float(input("Enter the larger mass, m1 (kg): "))
m2 = float(input("Enter the smaller mass, m2 (kg): "))

#4 Set the parameters
r = 1.496e11
a = 1.49598e11

#4 Call the C function
result = lib.vis_viva(r, a, m1, m2)

#5 Print the answer
print(f"Vis-viva via the engine gives v = {result} m/s")