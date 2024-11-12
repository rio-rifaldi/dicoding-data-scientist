import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

 
 

all_data = pd.read_csv('https://gist.githubusercontent.com/rio-rifaldi/5110201a2103b8a8cb23fd3640b40932/raw/ca8094eb456a7d7660ed7e2f3b1b9e32d9591c6a/main_data.csv') 
order_payments_df = pd.read_csv("https://gist.githubusercontent.com/rio-rifaldi/51927cf6ca9a2a251001a637be603150/raw/79f00245f25718e30b05cb8a642f1d1eeaf413b7/order_payments_dataset.csv")



product_price = all_data.groupby(["product_category_name","price"]).product_id.nunique().sort_index(ascending=False).reset_index()


product_price.drop(columns="product_id",inplace=True)
product_price.columns = ["product_category_name","mean_price"]

product_mean_price = product_price.groupby("product_category_name").mean().mean_price.to_dict()


st.title("Product Categories :orange[Mean Price]")
categories = list(product_mean_price.keys())
values = list(product_mean_price.values())
data = pd.DataFrame({'Category': categories, 'Value': values}).sort_values(by='Value', ascending=True)

plt.figure(figsize=(10, 48))  
plt.barh(data['Category'], data['Value'], color='skyblue')
plt.xlabel('Price in $')
plt.title('Product Categories Mean Price')

st.pyplot(plt)




customer_payment_list = order_payments_df.groupby(["payment_type"]).order_id.nunique().sort_values(ascending=False)

customer_payment_list_dict = customer_payment_list.to_dict()

fig, ax = plt.subplots()

st.title("Popular :red[Payment Types]")
payment_method = list(customer_payment_list_dict.keys())
data_payment_method = list(customer_payment_list_dict.values())
bar_colors = ['tab:green', 'tab:blue', 'tab:red', 'tab:orange','tab:blue']

ax.bar(payment_method, data_payment_method, color=bar_colors)

ax.set_ylabel('Customer Count')
ax.set_title('Most Popular Payment Types')


st.pyplot(fig)






data_list_dict = all_data.groupby(["product_category_name"]).product_id.nunique().sort_values(ascending=False).head(10).to_dict()


st.title("High Product Product :blue[Stock Categories]")
fig2, ax = plt.subplots()

data_product_categories = list(data_list_dict.keys())
data_product_values = list(data_list_dict.values())
y_pos = np.arange(len(data_product_categories))
error = np.random.rand(len(data_product_categories))


ax.barh(y_pos, data_product_values, xerr=error, align='center')
ax.set_yticks(y_pos, labels=data_product_categories)
ax.invert_yaxis()  
ax.set_xlabel('Product Stock')
ax.set_title('High Product Product Stock Categories')

st.pyplot(fig=fig2)



