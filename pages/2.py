import streamlit as st
import numpy as np

st.title("Volume and Surface Area Calculator (Cylindrical Coordinates)")

st.markdown(r"""
### Q.2  
The open surfaces ρ = 2.0 m and ρ = 4.0 m,  
z = 3.0 m and z = 5.0 m,  
ϕ = 20° and ϕ = 60° form a closed surface in cylindrical coordinates.  

Find analytically:  
**(i)** the enclosed volume  
**(ii)** the total area of the enclosed surface 
""")


st.markdown("### Given:")
rho1 = 2.0  # m
rho2 = 4.0  # m
z1 = 3.0    # m
z2 = 5.0    # m
phi1_deg = 20.0
phi2_deg = 60.0

# Convert degrees to radians
phi1 = np.deg2rad(phi1_deg)
phi2 = np.deg2rad(phi2_deg)

st.write(f"ρ from {rho1} m to {rho2} m")
st.write(f"z from {z1} m to {z2} m")
st.write(f"ϕ from {phi1_deg}° to {phi2_deg}°")

# Volume Calculation
volume = (phi2 - phi1) * (z2 - z1) * ((rho2**2 - rho1**2) / 2)

# Surface Areas
# 1. Two curved side surfaces (constant rho): A = Δϕ * Δz * ρ
A_rho1 = (phi2 - phi1) * (z2 - z1) * rho1
A_rho2 = (phi2 - phi1) * (z2 - z1) * rho2

# 2. Two top/bottom annular sectors (constant z): A = 0.5 * (ρ2^2 - ρ1^2) * Δϕ
A_z1 = 0.5 * (rho2**2 - rho1**2) * (phi2 - phi1)
A_z2 = A_z1

# 3. Two radial sides (constant φ): A = Δρ * Δz
A_phi1 = (rho2 - rho1) * (z2 - z1)
A_phi2 = A_phi1

# Total Surface Area
total_area = A_rho1 + A_rho2 + A_z1 + A_z2 + A_phi1 + A_phi2

st.markdown("### Results:")
st.success(f"Enclosed Volume: {volume:.4f} m³")
st.success(f"Total Surface Area: {total_area:.4f} m²")

# Show formulas
st.markdown("### Used Formulas:")
st.latex(r"V = (\phi_2 - \phi_1)(z_2 - z_1)\left[\frac{\rho_2^2 - \rho_1^2}{2}\right]")
st.latex(r"A_{\text{total}} = A_{\rho_1} + A_{\rho_2} + A_{z_1} + A_{z_2} + A_{\phi_1} + A_{\phi_2}")