import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
@st.cache
def load_data():
    df = pd.read_csv('/content/drive/MyDrive/Dataset/Price/price-list-2015-2023.csv')
    return df

df = load_data()

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
