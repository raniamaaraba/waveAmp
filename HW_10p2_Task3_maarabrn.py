# Activity Python 1: Task 3
# File: ACT_Python_HeaderTemplate_Team355_maarabrn.py 
# Date:    29 10 2023
# By:      Rania Maaraba
# Section: 21
# Team:    355
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script is a header template that will be used for 
# all your python files the rest of the semester.

import math

E_0i = float(input('Enter the amplitude of the incident wave, E_oi ='))
n1 = float(input('Enter the refractive index of medium 1, n_1 ='))
n2 = float(input('Enter the refractive index of medium 2, n_2 ='))
η1 = float(input('Enter the intrinsic impedance of material 1, η_1 ='))
η2 = float(input('Enter the intrinsic impedance of material 2, η_2 ='))
θi = float(input('Enter the angle of incidence, θ_i ='))

θiii= θi*(math.pi/180)

θii= round(θiii,4)
print(θii)
SDL1 = (n1*math.sin(θii)/n2)
SDL2 = math.asin(SDL1)
SDL3 = SDL2*(180/math.pi)
SDL = round(SDL2,4)
print(SDL)


E0T1 = (2*(η2))*(math.cos(θii))
E0T2 = ((η2)*math.cos(SDL))+((η1)*math.cos(θii))
E0T = (E0T1/E0T2)*E_0i
EOR1 = ((η2)*math.cos(θii))-((η1)*math.cos(SDL))
EOR2 = ((η2)*math.cos(θii))+((η1)*math.cos(SDL))
EOR = (EOR1/EOR2)*E_0i
print("The angle of the transmitted wave is {0:.2f}º".format(SDL3))
print("The amplitude of the trasmitted wave is {0:.2f} V/m".format(E0T))
print("The amplitude of the reflected wave is {0:.2f} V/m".format(EOR))

