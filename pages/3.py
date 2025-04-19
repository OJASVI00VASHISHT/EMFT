import streamlit as st
import numpy as np

# Constants
eps0 = 8.854e-12  # Vacuum permittivity
rho_L = 2e-9      # Line charge (C/m)
q = 8e-9          # Point charges (C)
r = np.array([2, 3, 4])  # Observation point

# --- Electric field due to line charge along x-axis ---
def E_line(r):
    y, z = r[1], r[2]
    E = (rho_L / (2 * np.pi * eps0)) * np.array([0, y, z]) / (y**2 + z**2)
    return E

# --- Electric field due to a single point charge ---
def E_point(q_pos):
    r_vec = r - q_pos
    R = np.linalg.norm(r_vec)
    E = (1 / (4 * np.pi * eps0)) * q * r_vec / R**3
    return E

# Total Electric Field
E_total = E_line(r) + E_point(np.array([0, 0, 1])) + E_point(np.array([0, 0, -1]))

# --- Streamlit Display ---
st.title("Electric Field Calculator")

st.markdown(
    "Q.3 - An infinite uniform linear charge density "
    r"$\rho_L = 2.0 \, \text{nC/m}$ lies along the x-axis in free space, "
    "while point charges of 8.0 nC each are located at (0, 0, 1) and (0, 0, -1). "
    "Find analytically the electric field **E** at point (2, 3, 4), "
    "and also write a MATLAB subroutine to verify your answer."
)

st.markdown("### Problem Setup")
st.latex(r"""\rho_L = 2.0\, \text{nC/m}, \quad q = 8.0\, \text{nC}, \quad r = (2,3,4)""")

st.markdown("### Formulas Used")
st.latex(r"""\vec{E}_{\text{line}} = \frac{\rho_L}{2\pi\varepsilon_0} \cdot \frac{(0, y, z)}{y^2 + z^2}""")
st.latex(r"""\vec{E}_{\text{point}} = \frac{1}{4\pi\varepsilon_0} \cdot \frac{q (\vec{r} - \vec{r}_q)}{|\vec{r} - \vec{r}_q|^3}""")

st.markdown("### Final Result")
st.write(f"Electric field at (2, 3, 4):")
st.latex(fr"\vec{{E}} = {E_total[0]:.2e}\,\hat i + {E_total[1]:.2e}\,\hat j + {E_total[2]:.2e}\,\hat k \;\text{{(N/C)}}")

# --- Display MATLAB Code ---
st.markdown("### Equivalent MATLAB Code")
st.code("""
function E = electric_field()
    eps0 = 8.854e-12;
    rho_L = 2e-9;
    q = 8e-9;
    r = [2, 3, 4];

    % Line charge contribution
    y = r(2); z = r(3);
    E_line = (rho_L / (2*pi*eps0)) * [0, y, z] / (y^2 + z^2);

    % Point charges
    E1 = (1/(4*pi*eps0)) * q * (r - [0, 0, 1]) / norm(r - [0, 0, 1])^3;
    E2 = (1/(4*pi*eps0)) * q * (r - [0, 0, -1]) / norm(r - [0, 0, -1])^3;

    E = E_line + E1 + E2;
end
""", language='matlab')