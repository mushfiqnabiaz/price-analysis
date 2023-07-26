import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data

df = pd.read_csv('/data/price-list-2015-2023.csv')
@st.cache


# Set Seaborn theme
sns.set_theme(color_codes=True)

# Sidebar to filter data if required
st.sidebar.header('Data Filters')
selected_price_type = st.sidebar.selectbox('Select Price Type', df['Price Type'].unique())

# Filter the data based on selected price type
filtered_data = df[df['Price Type'] == selected_price_type]

# Visualize count of each commodity
st.header('Count of Each Commodity')
plt.figure(figsize=(12, 6))
sns.countplot(data=filtered_data, x='Commodity')
plt.xticks(rotation=90)
plt.xlabel('Commodity')
plt.ylabel('Count')
plt.title('Count of Each Commodity')
st.pyplot()

# Visualize count of each year
st.header('Count of Each Year')
plt.figure(figsize=(8, 6))
sns.countplot(data=filtered_data, x='Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Count of Each Year')
st.pyplot()

# Visualize count of each price type
st.header('Count of Each Price Type')
plt.figure(figsize=(8, 6))
sns.countplot(data=filtered_data, x='Price Type')
plt.xlabel('Price Type')
plt.ylabel('Count')
plt.title('Count of Each Price Type')
st.pyplot()

# Convert the Average Price column to numeric, ignoring non-convertible values
filtered_data['Average Price'] = pd.to_numeric(filtered_data['Average Price'].str.replace(',', ''), errors='coerce')

# Aggregate duplicate entries by taking the average price
aggregated_data = filtered_data.groupby(['Year', 'Commodity'])['Average Price'].mean().reset_index()

# Visualize commodity-wise retail prices over time
st.header('Commodity-wise Prices Over Time')
plt.figure(figsize=(12, 8))
for commodity in aggregated_data['Commodity'].unique():
    data_by_commodity = aggregated_data[aggregated_data['Commodity'] == commodity]
    plt.plot(data_by_commodity['Year'], data_by_commodity['Average Price'], label=commodity)

plt.xlabel('Year')
plt.ylabel('Average Price')
plt.title('Commodity-wise Prices Over Time')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
st.pyplot()

# Visualize price ranges by commodity using boxplots
st.header('Price Ranges by Commodity')
plt.figure(figsize=(10, 6))
sns.boxplot(x='Commodity', y='Average Price', data=filtered_data)
plt.xlabel('Commodity')
plt.ylabel('Average Price')
plt.title('Price Ranges by Commodity')
plt.xticks(rotation=90)
plt.grid(True)
st.pyplot()

# Calculate the correlation matrix
correlation_matrix = filtered_data.corr()

# Visualize the correlation matrix as a heatmap
st.header('Correlation Matrix')
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Matrix')
st.pyplot()

# Calculate percentage change in prices year-on-year
st.header('Percentage Change in Prices Year-on-Year')
retail_data = df[df['Price Type'] == 'Retail']
retail_data['Average Price'] = pd.to_numeric(retail_data['Average Price'].str.replace(',', ''), errors='coerce')
retail_price_percentage_change = retail_data.groupby('Year')['Average Price'].pct_change() * 100

wholesale_data = df[df['Price Type'] == 'Wholesale']
wholesale_data['Average Price'] = pd.to_numeric(wholesale_data['Average Price'].str.replace(',', ''), errors='coerce')
wholesale_price_percentage_change = wholesale_data.groupby('Year')['Average Price'].pct_change() * 100

# Create plots for percentage change in retail and wholesale prices
plt.figure(figsize=(10, 6))
plt.plot(retail_data['Year'], retail_price_percentage_change, marker='o', linestyle='-', label='Retail')
plt.plot(wholesale_data['Year'], wholesale_price_percentage_change, marker='o', linestyle='-', label='Wholesale')
plt.xlabel('Year')
plt.ylabel('Percentage Change')
plt.title('Percentage Change in Prices Year-on-Year')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
st.pyplot()

# Show the raw data table
st.header('Raw Data Table')
st.write(df)

# Show the filtered data table
st.header('Filtered Data Table')
st.write(filtered_data)
