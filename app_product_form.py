import streamlit as st

st.title("Inventory Management")

st.sidebar.header("Add New Product")

p_name = st.sidebar.text_input("Product Name")

p_category = st.sidebar.selectbox(
    "Category",
    ["Electronics", "Clothing", "Home & Kitchen", "Books", "Toys"]
)

p_price = st.sidebar.number_input("Price", min_value=0.0, step=0.01)

if st.sidebar.button("Add Product"):
    if p_name:
        st.success(f"Product '{p_name}' has been added successfully!")
        
        st.subheader("Product Details")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"Name: {p_name}")
            st.write(f"Category: {p_category}")
        
        with col2:
            st.write(f"Price: ${p_price:,.2f}")
    else:
        st.sidebar.error("Please enter a product name.")
