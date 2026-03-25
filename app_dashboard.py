import streamlit as st

st.title("Simple Sales Dashboard")
st.write("Track and visualize your monthly sales performance at a glance.")

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

months = list(sales.keys())
selected_month = st.selectbox("Select a month to view details:", months)

st.metric(label=f"Sales for {selected_month}", value=f"${sales[selected_month]}")

st.subheader("Sales Overview (Jan - Apr)")
st.bar_chart(list(sales.values()))
