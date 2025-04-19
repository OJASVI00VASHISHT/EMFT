import streamlit as st
import numpy as np

# Constants
eps0 = 8.854e-12
rho_L = 2e-9  # Linear charge density (C/m)
R = 1.0       # Assume radius of ring = 1 m
zA = 1.0
zB = 2.0

# --- Electric potential on z-axis due to ring ---
def V_ring(z):
    return (rho_L * R) / (2 * eps0 * np.sqrt(R**2 + z**2))

V_A = V_ring(zA)
V_B = V_ring(zB)
V_AB = V_A - V_B

# --- Streamlit Display ---
st.title("Potential Difference due to a Ring Charge")

st.markdown(
    "Q.4 - A ring-shaped linear charge with charge density "
    r"$\rho_L = 2.0 \, \text{nC/m}$ lies on the x-y plane. "
    "Find the **potential difference** between point A (0, 0, 1.0) and point B (0, 0, 2.0). "
    "Also, write a **MATLAB program** to verify your answer."
)

st.markdown("### Problem Setup")
st.latex(r"""\rho_L = 2.0\, \text{nC/m}, \quad R = 1.0\, \text{m}""")
st.latex(r"""\text{Point A: } (0, 0, 1.0), \quad \text{Point B: } (0, 0, 2.0)""")

st.markdown("### Formula Used")
st.latex(r"""V(z) = \frac{\rho_L R}{2 \varepsilon_0 \sqrt{R^2 + z^2}}""")

st.markdown("### Final Result")
st.latex(fr"V_A = {V_A:.2f} \, \text{{V}}, \quad V_B = {V_B:.2f} \, \text{{V}}")
st.latex(fr"V_{{AB}} = V_A - V_B = {V_AB:.2f} \, \text{{V}}")

# --- Display MATLAB Code ---
st.markdown("### Equivalent MATLAB Code")
st.code("""
function V_AB = ring_potential_diff()
    eps0 = 8.854e-12;
    rho_L = 2e-9;
    R = 1.0; % radius of ring in meters
    zA = 1.0;
    zB = 2.0;

    V = @(z) (rho_L * R) / (2 * eps0 * sqrt(R^2 + z^2));

    V_A = V(zA);
    V_B = V(zB);
    V_AB = V_A - V_B;
end
""", language='matlab')