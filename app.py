import streamlit as st
st.title("Division of Two Numbers")
st.header("Please Enter the Dividend and the Divisor below in the boxes provided")
number1=st.number_input("Dividend:")
number2=st.number_input("Divisor:")
if number2==0:
  st.write("Division by zero is not possible")
else:
  st.write('Quotient is =', number1/number2)
