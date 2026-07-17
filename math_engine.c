// math_engine.c
// Simple function to demonstrate the Python-to-C bridge
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double vis_viva(double r, double a, double m1, double m2) {
double G = 6.6743e-11;
double mu = G*(m1 + m2);
double v = sqrt(mu*((2.0/r)-(1.0/a)));
return v;
}