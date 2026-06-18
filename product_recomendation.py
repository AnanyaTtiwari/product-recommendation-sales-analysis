import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# Preview
print(df.head())

#Understand Data
print(df.info())
print(df.describe())
print(df.columns)

#Clean Data
#error='coerce means “If any value is invalid or cannot be converted, don’t crash — just replace it with NaT”
df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed', errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='mixed', errors='coerce')

# Handling missing values
print(df.isnull().sum())

# Option (simple)
df['Sales'] = df['Sales'].fillna(0)
df['Profit'] = df['Profit'].fillna(0)


# Only drop if critical columns are missing
df = df.dropna(subset=['Product Name', 'Order ID'])

# Remove duplicates
df.drop_duplicates(inplace=True)

# EDA

# Top Selling Product
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_products)

#Top Categories
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(category_sales)

# Most Profitable Products
profit_products = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
print(profit_products)

# Top Product Vizualtization
top_products.plot(kind='bar')
plt.title("Top Selling Products")
plt.show()

# Build Recomendation system
#Basket = list of products bought together in one order
basket = df.groupby(['Order ID', 'Product Name'])['Quantity'].sum().unstack().fillna(0)

# Convert to binaary
basket = (basket > 0).astype(int)
#A correlation matrix shows how strongly things are related to each other
corr_matrix = basket.corr()

# Recommendation Function
def recommend(product_name):
    matches = [col for col in corr_matrix.columns if product_name.lower() in col.lower()]

    if not matches:
        return "Product not found"

    product = matches[0]

    return corr_matrix[product].drop(product).sort_values(ascending=False).head(10)



print(recommend("Bush Somerset Collection Bookcase"))

# Top Product-Recommendation
def top_recommendations(n=10):
    return df.groupby('Product Name')['Quantity'].sum().sort_values(ascending=False).head(n)

# Category-Based Recommendation
def recommend_by_category(product):
    category = df[df['Product Name'] == product]['Category'].iloc[0]
    return df[df['Category'] == category]['Product Name'].unique()

# Customer-Based Recommendation
def recommend_to_customer(customer_id):
    return df[df['Customer ID'] == customer_id]['Product Name'].unique()

# Save Clean Data
df.to_csv("cleaned_data_superstore.csv", index=False)

# connect Sql with python
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:root@localhost/sales")

df.to_sql("orders", engine, if_exists="replace", index=False)



