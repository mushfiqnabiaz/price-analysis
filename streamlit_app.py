import streamlit as st
import pandas as pd
import numpy as np
st.title("Bangladesh Product Price Analysis")

def main():
    st.title("Read CSV File in Streamlit")

    # Load the CSV file from the "data" directory
    df = pd.read_csv('data/price-list-2015-2023.csv')

    # Display the DataFrame
    st.dataframe(df)

if __name__ == "__main__":
    main()
