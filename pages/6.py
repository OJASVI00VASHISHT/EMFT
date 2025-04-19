import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Inputs ---
st.title("Magnetic Field due to a Current Sheet")

st.markdown("""
### Q.6 - A current sheet \( K \, \text{A/m} \) flows in the region \( -0.15 \leq x \leq 0.15 \, \text{m} \).  
Calculate the magnetic field \( \mathbf{H} \) at point \( P(0, 0, 0.25) \).

Write a **MATLAB program** to:
- Verify your answer.
- Plot the magnetic field \( \mathbf{H} \) in the x–z plane over the region  
  \( -0.5 \leq x \leq 0.5 \, \text{m} \),  
  \( -0.5 \leq z \leq 0.5 \, \text{m}.
""")

K = st.number_input("Surface Current Density K (A/m)", value=5.0)
a = 0.15  # Sheet region: -a < x < a
point_P = np.array([0, 0, 0.25])  # Observation point

# --- Magnetic Field at Point P ---
H_P = np.array([0, 0, K / 2]) if point_P[2] > 0 else np.array([0, 0, -K / 2])

st.markdown("### Magnetic Field at Point P(0, 0, 0.25)")
st.latex(r"\vec{H} = \frac{K}{2} \hat{z}")
st.latex(fr"\vec{{H}} = 0 \, \hat i + 0 \, \hat j + {H_P[2]:.2f} \, \hat k \; \text{{A/m}}")

# --- Magnetic Field in x-z plane for plotting ---
x = np.linspace(-0.5, 0.5, 40)
z = np.linspace(-0.5, 0.5, 40)
X, Z = np.meshgrid(x, z)

# Vector field: H points in +z above sheet, -z below sheet, 0 outside sheet region in x
H_x = np.zeros_like(X)
H_z = np.zeros_like(Z)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        x_val, z_val = X[i, j], Z[i, j]
        if -a <= x_val <= a:
            H_z[i, j] = K / 2 if z_val > 0 else -K / 2
        else:
            H_z[i, j] = 0

# --- Plot ---
fig, ax = plt.subplots()
ax.quiver(X, Z, H_x, H_z, color='purple', pivot='middle')
ax.set_title("Magnetic Field (H) in x-z Plane")
ax.set_xlabel("x (m)")
ax.set_ylabel("z (m)")
ax.set_aspect('equal')
ax.grid(True)
st.pyplot(fig)

# --- MATLAB Code ---
st.markdown("### Equivalent MATLAB Code")
st.code(f"""
function magnetic_field_sheet()
    K = {K};   % Current sheet density (A/m)
    a = {a};   % Sheet region: -a < x < a

    [x, z] = meshgrid(linspace(-0.5, 0.5, 40), linspace(-0.5, 0.5, 40));
    Hx = zeros(size(x));
    Hz = zeros(size(z));

    for i = 1:size(x,1)
        for j = 1:size(x,2)
            if abs(x(i,j)) <= a
                Hz(i,j) = K/2 * sign(z(i,j));
            else
                Hz(i,j) = 0;
            end
        end
    end

    quiver(x, z, Hx, Hz, 'Color', 'magenta');
    xlabel('x (m)');
    ylabel('z (m)');
    title('Magnetic Field (H) in x-z Plane');
    axis equal;
    grid on;
end
""", language='matlab')