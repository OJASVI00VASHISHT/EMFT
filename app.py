import streamlit as st
import numpy as np

def transform_point(point, rotation_deg, translation):
    theta = np.radians(rotation_deg)
    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    P = np.array(point)
    T = np.array(translation)
    P_transformed = R @ P + T
    return tuple(P_transformed)

st.title("Coordinate Transformation Tool")

x = st.number_input("Enter x coordinate of the point", value=0.0)
y = st.number_input("Enter y coordinate of the point", value=0.0)
angle = st.number_input("Enter rotation angle (in degrees)", value=0.0)
tx = st.number_input("Enter translation in x direction", value=0.0)
ty = st.number_input("Enter translation in y direction", value=0.0)

if st.button("Transform Point"):
    original_point = (x, y)
    translation_vector = (tx, ty)
    new_point = transform_point(original_point, angle, translation_vector)

    st.write(f"**Original Point:** {original_point}")
    st.write(f"**Transformed Point:** {new_point}")
