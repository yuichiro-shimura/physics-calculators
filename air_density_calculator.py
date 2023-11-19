# This is an air property calculator that calculates density.
# Created by yuichiro shimura on 2023/11/19.

# Universal gas constant and molecular weight of air
# R: Universal gas constant, approximately 8314.33 J/(kmol * K)
# M: Molecular weight of air, approximately 28.967 kg/mol
# This value is from "JSME Mechanical Engineers' Handbook A. Fundamentals A6:Thermal Engineering".
universal_gas_constant=8314.33
molecular_weight=28.967
gas_constant=universal_gas_constant/molecular_weight

# variable
pressure_abs=float(input('pressure_abs[Pa]='))
temperature=float(input('temperature[K]='))

# Calculates the density of a gas given the temperature and pressure.
density=pressure_abs/(gas_constant*temperature)
print(density)