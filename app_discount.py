import streamlit as st

st.title("Price Calculator")

original_price = st.number_input("Enter Original Price:", min_value=0.0, value=1000.0, step=1.0)

discount_pct = st.slider("Select Discount Percentage:", min_value=0, max_value=50, value=10)

if st.button("Calculate Final Price"):
    discount_amount = original_price * (discount_pct / 100)
    final_price = original_price - discount_amount

    st.write(f"The final price after a {discount_pct}% discount is: {final_price}")

    st.write("### Price Summary")
    comparison_data = [
        ["Original Price", f"{original_price}"],
        ["Discount Applied", f"{discount_pct}%"],
        ["Final Price", f"{final_price}"]
    ]
    st.table(comparison_data)

