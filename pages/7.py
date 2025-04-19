
import streamlit as st
import numpy as np

# --- Constants ---
eps0 = 8.854e-12  # Vacuum permittivity (F/m)
mu0 = 4 * np.pi * 1e-7  # Vacuum permeability (H/m)

# --- App Layout ---
st.set_page_config(page_title="Material Propagation Constants", layout="centered")
st.title("📡 Electromagnetic Material Analyzer")
st.markdown("Q.7 - Write a Matlab subroutine to computes the attenuation constant, dissipation factor and propagation constant for a material.")

st.markdown("Calculate **Attenuation Constant**, **Dissipation Factor**, and **Propagation Constant** from material properties.")

st.markdown("### 📥 Input Parameters")

# --- Inputs ---
sigma = st.number_input("Conductivity σ (S/m)", min_value=0.0, value=0.01)
eps_r = st.number_input("Relative Permittivity εᵣ", min_value=1.0, value=4.0)
mu_r = st.number_input("Relative Permeability μᵣ", min_value=1.0, value=1.0)
f = st.number_input("Frequency f (Hz)", min_value=1.0, value=1e9)

# --- Calculations ---
omega = 2 * np.pi * f
eps = eps_r * eps0
mu = mu_r * mu0
gamma = np.sqrt(1j * omega * mu * (sigma + 1j * omega * eps))
alpha = np.real(gamma)
beta = np.imag(gamma)
dissipation_factor = sigma / (omega * eps)

# --- Display Results ---
st.markdown("### 📊 Results")
st.latex(r"\omega = 2\pi f")
st.latex(fr"\omega = {omega:.2e} \ \text{{rad/s}}")
st.latex(fr"\tan\delta = \frac{{\sigma}}{{\omega \varepsilon}} = {dissipation_factor:.4f}")
st.latex(fr"\alpha = \text{{Re}}(\gamma) = {alpha:.4f} \ \text{{Np/m}}")
st.latex(fr"\gamma = \alpha + j\beta = {alpha:.4f} + j{beta:.4f} \ \text{{rad/m}}")

# --- MATLAB Code ---
st.markdown("### 💻 Equivalent MATLAB Subroutine")
st.code(f"""
function [alpha, beta, tan_delta, gamma] = compute_material_properties(sigma, eps_r, mu_r, f)
    % Constants
    eps0 = 8.854e-12;  % Vacuum permittivity (F/m)
    mu0 = 4 * pi * 1e-7;  % Vacuum permeability (H/m)

    % Compute angular frequency
    omega = 2 * pi * f;

    % Compute material properties
    eps = eps_r * eps0;  % Permittivity of the material
    mu = mu_r * mu0;     % Permeability of the material

    % Compute the propagation constant gamma
    gamma = sqrt(1j * omega * mu * (sigma + 1j * omega * eps));

    % Attenuation constant (Real part of gamma)
    alpha = real(gamma);

    % Phase constant (Imaginary part of gamma)
    beta = imag(gamma);

    % Dissipation factor (tan delta)
    tan_delta = sigma / (omega * eps);

    % Display the results
    disp(['Attenuation constant (alpha): ', num2str(alpha), ' Np/m']);
    disp(['Phase constant (beta): ', num2str(beta), ' rad/m']);
    disp(['Dissipation factor (tan delta): ', num2str(tan_delta)]);
    disp(['Propagation constant (gamma): ', num2str(alpha), ' + j', num2str(beta), ' rad/m']);
end

""", language='matlab')

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
