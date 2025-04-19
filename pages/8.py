import streamlit as st
import numpy as np

st.title("Inductance and Capacitance Calculator (Lossless Transmission Line)")

st.markdown("""
### Q.8 - Consider a transmission line where the insulating material is air and since \( \sigma = 0 \), the conductance parameter \( G = 0 \). 
The conductors have high conductivity such that \( R = 0 \).

For this transmission line with:
- A characteristic impedance \( Z_0 = 50 \, \Omega \)
- A phase constant \( \beta = 20 \, \text{rad/m} \) at 700 MHz

Find the line inductance and capacitance.

- First, obtain the results theoretically and then verify them using **MATLAB**.
""")


# Show formulas
st.latex(r"""
Z_0 = \sqrt{\frac{L}{C}}, \quad \beta = \omega \sqrt{L C}
""")
st.latex(r"""
LC = \left( \frac{\beta}{\omega} \right)^2, \quad L = Z_0 \cdot \sqrt{LC}, \quad C = \frac{1}{Z_0} \cdot \sqrt{LC}
""")

# Inputs
Z0 = st.number_input("Characteristic Impedance Z₀ (Ohms)", value=50.0, min_value=0.0)
beta = st.number_input("Phase Constant β (rad/m)", value=20.0, min_value=0.0)
frequency = st.number_input("Frequency (Hz)", value=700e6, min_value=1.0)

# Calculations
omega = 2 * np.pi * frequency
LC = (beta / omega) ** 2

L = Z0 * np.sqrt(LC)
C = np.sqrt(LC) / Z0

# Output
st.write(f"**Inductance per unit length (L)** = {L:.6e} H/m")
st.write(f"**Capacitance per unit length (C)** = {C:.6e} F/m")