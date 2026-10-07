import streamlit as st
import math

st.title("🔢 Advanced Calculator")

# Choose operation mode
mode = st.radio("Select Mode", ["Basic Operations", "Scientific / Advanced"])

st.divider()

if mode == "Basic Operations":
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number", value=0.0)

    operation = st.selectbox(
        "Choose operation",
        ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)", "Power (xʸ)", "Modulus (%)"]
    )

    if st.button("Calculate", type="primary"):
        result = None
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (×)":
            result = num1 * num2
        elif operation == "Division (÷)":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Cannot divide by zero!")
        elif operation == "Power (xʸ)":
            result = math.pow(num1, num2)
        elif operation == "Modulus (%)":
            result = num1 % num2

        if result is not None:
            st.success(f"**Result:** {result}")

else:  # Scientific / Advanced Mode
    num = st.number_input("Enter number", value=0.0)
    operation = st.selectbox(
        "Choose operation",
        ["Square Root (√x)", "Absolute Value (|x|)", "Logarithm (ln)", "Factorial (x!)", "Sin", "Cos", "Tan"]
    )

    if st.button("Calculate", type="primary"):
        result = None
        try:
            if operation == "Square Root (√x)":
                if num >= 0:
                    result = math.sqrt(num)
                else:
                    st.error("Cannot calculate square root of a negative number!")
            elif operation == "Absolute Value (|x|)":
                result = abs(num)
            elif operation == "Logarithm (ln)":
                if num > 0:
                    result = math.log(num)
                else:
                    st.error("Logarithm requires a positive number!")
            elif operation == "Factorial (x!)":
                if num >= 0 and num.is_integer():
                    result = math.factorial(int(num))
                else:
                    st.error("Factorial requires a non-negative integer!")
            elif operation == "Sin":
                result = math.sin(math.radians(num))
            elif operation == "Cos":
                result = math.cos(math.radians(num))
            elif operation == "Tan":
                result = math.tan(math.radians(num))

            if result is not None:
                st.success(f"**Result:** {result}")
        except Exception as e:
            st.error(f"Error performing calculation: {e}")
