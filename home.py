import streamlit as st

st.set_page_config(page_title="Engineering Tools Suite", page_icon="🛠️")

st.title("ELECTROMAGNETIC FIELD THEORY AND TRANSMISSION LINES-UEC307-2425EVESEM")

st.subheader("Microproject")

st.write("""
This app includes a collection of engineering calculators and visualizers including:
- Coordinate system transformation
- Standing wave & VSWR visualization
- And many more tools!

Use the sidebar to navigate between apps.
""")

st.subheader("Micro Project Details")
st.write("""
### Important Points:
1. Students will form project groups of 3-4 students from the same tutorial group.
2. Each project group can choose one project (without repetition in the tutorial group) that will be approved by the concerned tutorial faculty. If two groups have conflict on the same project, then the average CGPA of the group will be the criteria for project allotment.
3. Complete project selection process and notify it to the tutorial faculty by **18/04/2025 (Friday)**.
4. Final evaluation will be conducted by the tutorial faculty in the respective TUT classes during the **2nd last teaching weeks of the semester (12-16 May 2025)**.
5. Final evaluation will be of **10 marks**:
   - **5 marks**: Project outcome
   - **2 marks**: Report (@ 1 per group)
   - **3 marks**: Viva (evaluated individually, based on the allotted project)
6. Viva will be from the allotted project only.

---

### Annexure-A: List of Projects
1. **Coordinate System Transformation**  
   (i) Use MATLAB to convert coordinates of a point from one coordinate system to another.  
   (ii) Write a MATLAB routine to convert a vector in Cartesian components into spherical and cylindrical at a given point.

2. **Closed Surface Analysis**  
   The open surfaces ρ = 2.0 m and ρ = 4.0 m, z = 3.0 m and z = 5.0 m, and ϕ = 20° and ϕ = 60° form a closed surface.  
   (i) Find analytically the enclosed volume and total area of the enclosed surface.  
   (ii) Write a MATLAB program to verify your answers.

3. **Electric Field Calculation**  
   An infinite uniform linear charge ρL = 2.0 nC/m lies along the x-axis in free space, while point charges of 8.0 nC each are located at (0, 0, 1) and (0, 0, -1).  
   (i) Find analytically E at (2, 3, 4).  
   (ii) Write a MATLAB subroutine to verify your answer.

4. **Potential Difference Calculation**  
   A ring linear charge with a charge density ρL = 2.0 nC/m is located on the xy plane.  
   (i) Find the potential difference between point A (0, 0, 1.0) and point B (0, 0, 2.0).  
   (ii) Write a MATLAB program to verify your answer.

5. **Potential Distribution Between Spheres**  
   Write a MATLAB program to compute and plot the potential distribution between two spheres whose centers are coincident.

6. **Magnetic Field Calculation**  
   A current sheet A/m flows in the region -0.15 < x < 0.15 m.  
   (i) Calculate H at P(0, 0, 0.25).  
   (ii) Write a MATLAB program to verify your answer and plot the magnetic field in the x-y plane in the region -0.5 ≤ x ≤ 0.5 m and -0.5 ≤ z ≤ 0.5 m.

7. **Material Properties**  
   Write a MATLAB subroutine to compute the attenuation constant, dissipation factor, and propagation constant for a material.

8. **Transmission Line Analysis**  
   Consider a transmission line where the insulating material is air (σ = 0, G = 0) and the conductors have high conductivity (R = 0).  
   (i) For a characteristic impedance of 50 Ω and a phase constant of 20 rad/m at 700 MHz, find the line inductance and capacitance.  
   (ii) Verify the results using MATLAB.

""")