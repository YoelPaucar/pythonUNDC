# -*- coding: utf-8 -*-
# P(D)
p_diabetes=0.01
# P(-D)
p_no_diabetes=0.99
# Sensibilidad or P(Pos|D)
p_pos_diabetes=0.9
# Especificidad or P(Neg/-D)
p_neg_no_diabetes=0.9
# P(Pos)
p_pos=(p_diabetes*p_pos_diabetes)+(p_no_diabetes * (1-p_neg_no_diabetes))
p_diabetes_pos= (p_diabetes*p_pos_diabetes)/p_pos
print("La probabilidad de obtener un resultado positivo en la prueba P(pos) es: {}".format(p_pos))