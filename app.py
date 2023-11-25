import streamlit as st
import pandas as pd


def apply_monthly_compound(annual_borrowing, interest_rate, compounding_periods, t):
    return annual_borrowing * ((1 + interest_rate/compounding_periods)**(compounding_periods*t)) 

# Function to calculate compound interest
def calculate_interest(principal, rate, years, compounding_periods):
        # Adjusting constants for monthly compounding
    #compounding_periods = 12 if compounding_periods == "Monthly" else 1

    interest_rate = rate

    total_years = years

    annual_borrowing = principal

    # Update the dataframe with the new calculations
    data_updated = {
        "Year": [],
        "Principal Borrowed ($)": [],
        "Total Compounded Amount ($)": [],
        "Interest Accumulated ($)": []
    }

    pre_calcs =[]
    for i in range(1, total_years + 1):
        total = 0
        for j in range(i):
            total += apply_monthly_compound(annual_borrowing, interest_rate, compounding_periods, j+1)

        pre_calcs.append(total)
            

    # Calculating the compounded amount and interest for each year with monthly compounding
    running_amount = 0
    for year in range(1, total_years + 1):

        principal = annual_borrowing * year
        compounded_amount = pre_calcs[year-1] 
        interest = compounded_amount - principal

        data_updated["Year"].append(year)
        data_updated["Principal Borrowed ($)"].append(principal)
        data_updated["Total Compounded Amount ($)"].append(compounded_amount)
        data_updated["Interest Accumulated ($)"].append(interest)

    # Convert the updated data to a DataFrame
    df_updated = pd.DataFrame(data_updated)

    # get the last row to get the total interest and total compounded amount
    total_borrowed = df_updated["Principal Borrowed ($)"].iloc[-1].round(0)
    total_interest_updated = df_updated["Interest Accumulated ($)"].iloc[-1].round(0)
    total_compounded_amount = df_updated["Total Compounded Amount ($)"].iloc[-1].round(0)

    df_updated["Total Compounded Amount ($)"] = df_updated["Total Compounded Amount ($)"].round(0)
    df_updated["Interest Accumulated ($)"] = df_updated["Interest Accumulated ($)"].round(0)

    return df_updated, total_interest_updated, total_compounded_amount, total_borrowed

# Streamlit UI components
st.title("John's Yearly Borrowing and Compound Interest Calculator")
principal = st.number_input("Yearly Loan Amount", min_value=0, value=150000)
rate = st.number_input("Annual Interest Rate (in %)", min_value=0.0, format="%.2f", value=6.0)
years = st.number_input("Duration (Years)", min_value=0, value=20)
compounding_periods = st.selectbox("Compounding Frequency", ["Annually", "Monthly"], index=1)

# Convert frequency to a number
compounding_periods = 12 if compounding_periods == "Monthly" else 1

# Button to perform calculation
if st.button("Calculate Interest"):
    df, total_interest, total_compounded_amount, total_borrowed = calculate_interest(principal, rate / 100, years, compounding_periods)

    # add a divider
    st.markdown("---")
    st.write(f"Total Interest: ${format(total_interest, ',')}")
    st.write(f"Total Compounded Amount: ${format(total_compounded_amount, ',')}")
    st.write(f"Total Borrowed: ${format(total_borrowed, ',')}")

    st.write(df)
    # format the numbers with commas
    
