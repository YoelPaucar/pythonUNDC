# -*- coding: utf-8 -*-
# P(D)
p_diabetes=0.01
# P(-D)
p_no_diabetes=0.99
# Sensibilidad or P(Pos|D)
p_pos_diabetes=0.9
# Especificidad or P(Neg/-D)
p_neg_no_diabetes=0.9
#P(Pos/-D)
p_pos_no_diabetes=0.1
# P(Pos)
p_pos=(p_diabetes*p_pos_diabetes)+(p_no_diabetes * (1-p_neg_no_diabetes))

p_no_diabetes_pos=(p_no_diabetes * p_pos_no_diabetes)/ p_pos
print("Probalidad de que un individuo no tenga diabetes,\n\
      dado que ese individuo obtuvo un resultado positivo de la prueba es: {}".format(p_no_diabetes_pos))