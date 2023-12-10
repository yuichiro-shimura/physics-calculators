import plotly.graph_objs as go
import numpy as np
import pandas as pd

# Define temperature and pressure ranges
temp_range = np.arange(100, 2001, 20)
pressure_range = np.arange(5000, 500001, 10000)

# Create 2D arrays for temperature and pressure
temp, pressure = np.meshgrid(temp_range, pressure_range)

# Calculate air density based on temperature and pressure
air_density = pressure / (287.058 * temp)

# Create 3D surface plot
fig = go.Figure(data=[go.Surface(z=air_density, x=temp, y=pressure, colorscale='jet')])
fig.update_layout(title='3D Surface Graph of Air Density', scene=dict(xaxis_title='Temperature (K)', yaxis_title='Pressure (Pa)', zaxis_title='Air Density (kg/m^3)'))
fig.show()