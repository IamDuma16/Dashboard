import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración
st.set_page_config(
    page_title="Dashboard Morosidad Bancaria",
    layout="wide"
)

st.title("📊 Dashboard Analítico - Riesgo de Morosidad Bancaria")

# Cargar datos
df = pd.read_csv("dataset_personal.csv")

# =========================
# KPI
# =========================

total_clientes = len(df)

morosos = (df["Moroso"] == "Si").sum()

porcentaje = (morosos / total_clientes) * 100

c1, c2, c3 = st.columns(3)

c1.metric("Total Clientes", total_clientes)

c2.metric("Clientes Morosos", morosos)

c3.metric("Tasa de Morosidad", f"{porcentaje:.2f}%")

st.divider()

# =========================
# Gráfico de barras
# =========================

st.subheader("Clientes según Historial Crediticio")

fig, ax = plt.subplots(figsize=(7,4))

df["HistorialCrediticio"].value_counts().plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Historial")

ax.set_ylabel("Cantidad")

st.pyplot(fig)

# =========================
# Histograma
# =========================

st.subheader("Distribución del Ingreso Mensual")

fig, ax = plt.subplots(figsize=(7,4))

ax.hist(
    df["IngresoMensual"],
    bins=25
)

ax.set_xlabel("Ingreso")

ax.set_ylabel("Frecuencia")

st.pyplot(fig)

# =========================
# Heatmap
# =========================

st.subheader("Correlación entre Variables")

numericas = df.select_dtypes(include="number")

fig, ax = plt.subplots(figsize=(8,6))

sns.heatmap(
    numericas.corr(),
    annot=True,
    cmap="Blues",
    ax=ax
)

st.pyplot(fig)

# =========================
# Scatter Plot
# =========================

st.subheader("Ingreso vs Deuda")

fig, ax = plt.subplots(figsize=(7,5))

ax.scatter(
    df["IngresoMensual"],
    df["DeudaActual"]
)

ax.set_xlabel("Ingreso")

ax.set_ylabel("Deuda")

st.pyplot(fig)

# =========================
# Hallazgos
# =========================

st.header("Hallazgos Principales")

st.write("""
• Los clientes con historial crediticio malo presentan mayor probabilidad de morosidad.

• Existe una relación positiva entre el nivel de deuda y el riesgo de incumplimiento.

• Los clientes con ingresos más altos suelen mantener un menor ratio deuda/ingreso.
""")

# =========================
# Recomendaciones
# =========================

st.header("Recomendaciones")

st.write("""
✅ Fortalecer la evaluación crediticia antes de aprobar nuevos préstamos.

✅ Diseñar planes de refinanciamiento para clientes con alto riesgo.

✅ Implementar modelos predictivos como apoyo para la toma de decisiones.
""")