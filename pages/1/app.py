import streamlit as st
import numpy as np

def cartesian_to_cylindrical(x, y, z):
    r = np.sqrt(x**2 + y**2)
    theta = np.degrees(np.arctan2(y, x))
    return np.array([["Radius (r)", f"{r} units"], ["Theta (θ)", f"{theta} degrees"], ["Z", f"{z} units"]])

def cartesian_to_circular(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.degrees(np.arctan2(y, x))
    phi = np.degrees(np.arccos(z / r)) if r != 0 else 0
    return np.array([["Radius (r)", f"{r} units"], ["Theta (θ)", f"{theta} degrees"], ["Phi (φ)", f"{phi} degrees"]])

st.title("Coordinate Transformation Tool")

# Ask the user to select the coordinate system
coordinate_system = st.selectbox(
    "Select the coordinate system to convert from:",
    ["Cartesian", "Cylindrical", "Circular"]
)

if coordinate_system == "Cartesian":
    x = st.number_input("Enter x coordinate", value=0.0)
    y = st.number_input("Enter y coordinate", value=0.0)
    z = st.number_input("Enter z coordinate", value=0.0)

    if st.button("Convert"):
        cylindrical_coords = cartesian_to_cylindrical(x, y, z)
        st.write("**Cylindrical Coordinates (Matrix Form):**")
        st.write(cylindrical_coords)

        circular_coords = cartesian_to_circular(x, y, z)
        st.write("**Circular Coordinates (Matrix Form):**")
        st.write(circular_coords)

elif coordinate_system == "Cylindrical":
    r = st.number_input("Enter radial distance (r)", value=0.0)
    theta = st.number_input("Enter angle θ (in degrees)", value=0.0)
    z = st.number_input("Enter z coordinate", value=0.0)

    if st.button("Convert"):
        x = r * np.cos(np.radians(theta))
        y = r * np.sin(np.radians(theta))
        st.write("**Cartesian Coordinates (Matrix Form):**")
        st.write(np.array([["X", f"{x} units"], ["Y", f"{y} units"], ["Z", f"{z} units"]]))

        circular_coords = cartesian_to_circular(x, y, z)
        st.write("**Circular Coordinates (Matrix Form):**")
        st.write(circular_coords)

elif coordinate_system == "Circular":
    r = st.number_input("Enter radial distance (r)", value=0.0)
    theta = st.number_input("Enter angle θ (in degrees)", value=0.0)
    phi = st.number_input("Enter angle φ (in degrees)", value=0.0)

    if st.button("Convert"):
        # Convert circular (spherical) to Cartesian
        x = r * np.sin(np.radians(phi)) * np.cos(np.radians(theta))
        y = r * np.sin(np.radians(phi)) * np.sin(np.radians(theta))
        z = r * np.cos(np.radians(phi))

        st.write("**Cartesian Coordinates (Matrix Form):**")
        st.write(np.array([["X", f"{x} units"], ["Y", f"{y} units"], ["Z", f"{z} units"]]))

        cylindrical_coords = cartesian_to_cylindrical(x, y, z)
        st.write("**Cylindrical Coordinates (Matrix Form):**")
        st.write(cylindrical_coords)
