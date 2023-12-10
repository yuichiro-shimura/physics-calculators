# This program calculates a table of air densities.
# Created by Yuichiro Shimura on 2023/12/09.

import pandas as pd
import plotly.express as px

# Universal gas constant and molecular weight of air
# R: Universal gas constant, approximately 8314.33 J/(kmol * K)
# M: Molecular weight of air, approximately 28.967 kg/mol
# This value is from "JSME Mechanical Engineers' Handbook A. Fundamentals A6:Thermal Engineering".
universal_gas_constant=8314.33
molecular_weight=28.967
gas_constant=universal_gas_constant/molecular_weight

# delta values
delta_pressure=5000
delta_temperature=10

# Initial values for pressure_abs
pressure_abs=5000

# Define table variable
temperature_array =[]
pressure_array =[]
density_array = []

# Calculates the density of a gas given the temperature and pressure.
while pressure_abs <= 100000:
    # Initial value for temperature.
    temperature=100
    
    # Calculate density of air.
    while temperature < 1000:
        density=pressure_abs/(gas_constant*temperature)
        temperature_array.append(temperature)
        density_array.append(density)
        pressure_array.append(pressure_abs)
        temperature = temperature + delta_temperature

    pressure_abs = pressure_abs + delta_pressure

table_header = ["temperature", "pressure", "density"]
density_table = [temperature_array, pressure_array, density_array]
density_table_df = pd.DataFrame(density_table)
density_table_df_transposed = density_table_df.transpose()
density_table_df_transposed.columns = table_header
print(density_table_df_transposed['temperature'])

# fig = px.scatter_3d(
#     density_table_df_transposed,
#     x=density_table_df_transposed['temperature'],
#     y=density_table_df_transposed['pressure'],
#     z=density_table_df_transposed['density'],
# )
# fig.show()