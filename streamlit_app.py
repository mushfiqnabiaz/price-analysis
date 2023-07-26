import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Bangladesh Product Price Analysis")


df = pd.read_csv('data/price-list-2015-2023.csv')
    
# Function to create the countplot 
def create_countplot(data, x):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=data, x=x)
    plt.xticks(rotation=90)
    plt.xlabel('Commodity')
    plt.ylabel('Count')
    plt.title('Count of Each Commodity')
    st.pyplot()
    
# Streamlit app
def main():
    st.title('Commodity Count Analysis')
    
    # Display the countplot
    st.subheader('Count of Each Commodity')
    create_countplot(df, 'Commodity')    

if __name__ == "__main__":
    main()
