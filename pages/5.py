import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Title & Inputs ---
st.title("Electric Potential Between Two Concentric Spheres")

st.markdown("Q.5 - Write a Matlab program to compute and plot the potential distribution between two spheres whose centres are coincident.")

R1 = st.number_input("Inner Sphere Radius R1 (m)", min_value=0.01, value=0.5)
R2 = st.number_input("Outer Sphere Radius R2 (m)", min_value=R1 + 0.01, value=R1+1.0)
V1 = st.number_input("Potential of Inner Sphere V1 (V)", value=100.0)
V2 = st.number_input("Potential of Outer Sphere V2 (V)", value=0.0)

# --- Compute Potential ---
r = np.linspace(R1, R2, 300)
V_r = V1 + ((V2 - V1)/(R2 - R1)) * (r - R1)
V_diff = V1 - V2

st.markdown("### Potential Difference")
st.latex(fr"\Delta V = V_1 - V_2 = {V_diff:.2f}\ \text{{V}}")

# --- Plot 1: Potential vs Radius ---
fig1, ax1 = plt.subplots()
ax1.plot(r, V_r, 'm', linewidth=2)
ax1.set_title("Electric Potential vs Radial Distance")
ax1.set_xlabel("Radial Distance r (m)")
ax1.set_ylabel("Potential V(r) (V)")
ax1.grid(True)
st.pyplot(fig1)

# --- Plot 2: Circle View with Potential Gradient ---
theta = np.linspace(0, 2*np.pi, 300)
x1 = R1 * np.cos(theta)
y1 = R1 * np.sin(theta)
x2 = R2 * np.cos(theta)
y2 = R2 * np.sin(theta)

fig2, ax2 = plt.subplots(figsize=(6, 6))
for i in range(len(r) - 1):
    color = plt.cm.plasma((V_r[i] - V2) / (V1 - V2))  # Normalize to [0, 1]
    circle = plt.Circle((0, 0), r[i], color=color, fill=True, alpha=0.03)
    ax2.add_artist(circle)

ax2.plot(x1, y1, 'b', label=f'Inner Sphere (R1={R1} m, V={V1} V)')
ax2.plot(x2, y2, 'r', label=f'Outer Sphere (R2={R2} m, V={V2} V)')
ax2.set_aspect('equal')
ax2.set_xlim([-R2 - 0.2, R2 + 0.2])
ax2.set_ylim([-R2 - 0.2, R2 + 0.2])
ax2.set_title("Cross-Section View of Spheres with Potential Field")
ax2.set_xlabel("x (m)")
ax2.set_ylabel("y (m)")
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)

# --- MATLAB Code ---
st.markdown("### Equivalent MATLAB Code")
st.code(f"""
function plot_potential_concentric_spheres()
    R1 = {R1};
    R2 = {R2};
    V1 = {V1};
    V2 = {V2};
    r = linspace(R1, R2, 300);
    V = V1 + ((V2 - V1)/(R2 - R1)) * (r - R1);

    % Plot 1: V(r) vs r
    figure;
    plot(r, V, 'm', 'LineWidth', 2);
    xlabel('r (m)');
    ylabel('V(r) (V)');
    title('Electric Potential vs Radial Distance');
    grid on;

    % Plot 2: Circular View
    theta = linspace(0, 2*pi, 300);
    x1 = R1 * cos(theta);
    y1 = R1 * sin(theta);
    x2 = R2 * cos(theta);
    y2 = R2 * sin(theta);

    figure; hold on;
    for i = 1:length(r)
        c = (V(i) - V2) / (V1 - V2); % normalized color
        fill_circle(0, 0, r(i), [1-c, 0, c], 0.05);
    end
    plot(x1, y1, 'b', 'DisplayName', 'Inner Sphere');
    plot(x2, y2, 'r', 'DisplayName', 'Outer Sphere');
    axis equal;
    legend;
    xlabel('x (m)');
    ylabel('y (m)');
    title('Electric Field Between Concentric Spheres');
    grid on;
end

function fill_circle(xc, yc, r, color, alpha_val)
    theta = linspace(0, 2*pi, 100);
    x = xc + r*cos(theta);
    y = yc + r*sin(theta);
    fill(x, y, color, 'FaceAlpha', alpha_val, 'EdgeColor', 'none');
end
""", language='matlab')