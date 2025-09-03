import streamlit as st

# Valor inicial del JUS
if "jus" not in st.session_state:
    st.session_state.jus = 74878

st.title("📊 Calculadora de Honorarios Profesionales")
st.write(f"Valor actual del JUS: **${st.session_state.jus:,.2f}**")

# Formulario para calcular
st.subheader("Calcular honorarios")
cantidad = st.number_input("Ingrese la cantidad de JUS:", min_value=0.0, step=0.5)

if st.button("Calcular"):
    total = cantidad * st.session_state.jus
    st.success(f"Honorarios: **${total:,.2f}**")

# Formulario para actualizar JUS
st.subheader("Actualizar valor del JUS")
nuevo_valor = st.number_input("Ingrese nuevo valor del JUS:", min_value=0.0, step=100.0)

if st.button("Actualizar JUS"):
    st.session_state.jus = nuevo_valor
    st.info(f"✅ Valor del JUS actualizado a **${st.session_state.jus:,.2f}**")
