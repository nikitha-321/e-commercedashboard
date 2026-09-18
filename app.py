import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Ecommerce_Sales_Data_2024_2025.csv")


st.title("E-commerce Sales Dashboard 2024-2025")
Total_sales=df['Sales'].sum()
st.metric("Total Sales",f"Rs{Total_sales:,.0f}")
Total_profit=df['Profit'].sum()
st.metric("Total Profit",f"Rs{Total_sales:,.0f}")
st.header("Data Table")
st.dataframe(df, use_container_width=True)

st.header("Region wise sale area chart")
selected_region=st.selectbox("Select Region",df['Region'].unique())
region_sale = df.groupby('Region')['Sales'].sum()
st.area_chart(region_sale)

st.header("Category wise bar chart")
category_sale = df.groupby('Category')['Sales'].sum()
st.write("Category wise:", category_sale)
st.bar_chart(category_sale)

st.header("City wise sale")
city_sale = df.groupby('City')['Sales'].sum()
st.write("City wise:", city_sale)
st.line_chart(city_sale)

st.header("City wise Payment Mode")
city_payment = df.groupby(['City','Payment Mode']).size().unstack()
st.write(city_payment)
st.bar_chart(city_payment)

st.header("Which product sold more")
top_products = df.groupby('Product Name')['Quantity'].sum().sort_values(ascending=False).head(10)
st.write(top_products)
st.bar_chart(top_products)

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['year'] = df['Order Date'].dt.year
year_profit = df.groupby('year')['Profit'].sum().sort_values(ascending=False)

st.header("Year Wise Profit")
st.table(year_profit)
st.line_chart(year_profit)
top_year = year_profit.index[0]
top_profit = year_profit.values[0]
st.success(f"Top Profit year: {top_year} - Profit: {top_profit}")
