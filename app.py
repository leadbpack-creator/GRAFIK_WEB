import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Chainring Design")

# Buat 2 kolom untuk input x_min dan x_max
col1, col2, col3 = st.columns(3)

with col1:
    x_min = st.number_input("x minimum:", value=-10.0, step=0.1)

with col2:
    x_max = st.number_input("x maksimum:", value=10.0, step=0.1)

with col1:
    y_min = st.number_input("y minimum:", value=-10.0, step=0.1)

with col2:
    y_max = st.number_input("y maksimum:", value=10.0, step=0.1)

with col1:
    Nn = st.number_input("Teeth number:", value=40)

if st.button("Show Design"):
    try:
        # Buat sumbu x
        x = np.linspace(x_min, x_max, 400)

        # Definisi fungsi langsung di kode
        y = np.sin(x)  # <-- fungsi sudah ditentukan di sini

        # Plot
        fig, ax = plt.subplots()
        ax.plot(x, y, label="Chainring design")
        #ax.set_xlabel("x")
        #ax.set_ylabel("f(x)")
        #ax.legend()
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error: {e}")
