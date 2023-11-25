import streamlit as st
import pandas as pd

# Function to calculate compound interest
def calculate_interest(principal, rate, years, compounding_periods):
        # Adjusting constants for monthly compounding
    compounding_periods = 12  # Monthly compounding

    interest_rate = 0.06

    total_years = 20
    annual_borrowing = 150_000

    # Update the dataframe with the new calculations
    data_updated = {
        "Year": [],
        "Principal Borrowed ($)": [],
        "Total Compounded Amount ($)": [],
        "Interest Accumulated ($)": []
    }

    # Calculating the compounded amount and interest for each year with monthly compounding
    for year in range(1, total_years + 1):
        principal = annual_borrowing * year
        compounded_amount = annual_borrowing * ((1 + interest_rate/compounding_periods)**(compounding_periods*year))
        interest = compounded_amount - annual_borrowing
        data_updated["Year"].append(year)
        data_updated["Principal Borrowed ($)"].append(principal)
        data_updated["Total Compounded Amount ($)"].append(compounded_amount)
        data_updated["Interest Accumulated ($)"].append(interest)

    # Convert the updated data to a DataFrame
    df_updated = pd.DataFrame(data_updated)

    # Calculate the total interest with monthly compounding
    total_borrowed = df_updated["Principal Borrowed ($)"].sum().round(0)
    total_interest_updated = df_updated["Interest Accumulated ($)"].sum().round(0)
    total_compounded_amount = df_updated["Total Compounded Amount ($)"].sum().round(0)

    df_updated["Total Compounded Amount ($)"] = df_updated["Total Compounded Amount ($)"].round(0)
    df_updated["Interest Accumulated ($)"] = df_updated["Interest Accumulated ($)"].round(0)

    return df_updated, total_interest_updated, total_compounded_amount, total_borrowed

# Streamlit UI components
st.title("John's Compound Interest Calculator")
principal = st.number_input("Loan Amount", min_value=0)
rate = st.number_input("Annual Interest Rate (in %)", min_value=0.0, format="%.2f")
years = st.number_input("Duration (Years)", min_value=0)
compounding_periods = st.selectbox("Compounding Frequency", ["Annually", "Monthly"], index=1)

# Convert frequency to a number
compounding_periods = 12 if compounding_periods == "Monthly" else 1

# Button to perform calculation
if st.button("Calculate Interest"):
    df, total_interest, total_compounded_amount, total_borrowed = calculate_interest(principal, rate / 100, years, compounding_periods)
    st.write(df)
    st.write(f"Total Interest: {total_interest}")
    st.write(f"Total Compounded Amount: {total_compounded_amount}")
    st.write(f"Total Borrowed: {total_borrowed}")
