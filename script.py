# Page Visits Funnel
# Funnel for Cool T-Shirts Inc.

import pandas as pd

# load csv files
visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])

# inspect df using print and head
print(visits.head());
print(cart.head());
print(checkout.head());
print(purchase.head())

# inspect dfs size
print(visits.shape, cart.shape, checkout.shape, purchase.shape)

# combine visits and cart using a left merge
visits_cart = pd.merge(visits, cart, how='left')

# how long is the merged df?
print(visits_cart.shape)
# visit_cart_left has 2000 rows and 3 columns


# How many of the timestamps are null for the column cart_time?
cart_null = visits_cart[visits_cart['cart_time'].isnull()]
# print(visit_cart.cart_time.isna().sum())    # another way to count isnull or isna
# visit_cart_left[~visit_cart_left['cart_time'].isnull()]    # use ~ to return inverse count isnull=False
print(len(cart_null))
# 1652 users did not place in their cart on their visit
# null rows NaT means no data is stored


# What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
percent_cart_null = len(cart_null) / len(visits)
print(percent_cart_null)
# 82.6 % did not place a purchase in their cart on their visit

# combine cart and checkout using left merge and cout null values
cart_checkout = pd.merge(cart, checkout, how='left')
print(cart_checkout.shape)
checkout_null = cart_checkout[cart_checkout['checkout_time'].isnull()]
print(len(checkout_null))
# 122 users who did not checkout after they had added to cart
# What percentage of users put items in their cart, but did not proceed to checkout?
percent_checkout_null = len(checkout_null) / len(cart)
print(percent_checkout_null)
# 35.06 % did not checkout after placing in their cart

# Merge all four steps of the funnel, in order, using a series of left merges. Save the results to the variable all_data.
all_data = pd.merge(visits, cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
print(all_data.head())
print(all_data.shape)    # 2108 rows, 5 columns

# users made checkout
yes_checkout = all_data[~all_data['checkout_time'].isnull()]
# len(all_data[str_col_1]) - all_data[str_col_1].isna().sum()    # is another way!
n_checkout = len(yes_checkout)
print(n_checkout)
# 334 checkout has made
# users made checkout but not purchase item
yes_purchase = all_data[~all_data['purchase_time'].isnull()]
n_purchase = len(yes_purchase)
print(n_purchase)
# 252 purchase has made

# What percentage of users proceeded to checkout, but did not purchase a t-shirt?
# percentage of non-purchase after having checkout items
percent_purchase = (n_checkout - n_purchase) / n_checkout
print(percent_purchase)
# 24.55% did not made the purchase after checkout
print('-----------------------')

# Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)?
# import funnel_ratio function
from funnel import funnel_ratio

# test funnel_ratio function
print(funnel_ratio(1, all_data))
print(funnel_ratio(2, all_data))
print(funnel_ratio(3, all_data))
print(funnel_ratio(4, all_data))
print(funnel_ratio(5, all_data))
print(funnel_ratio('two'))

# Average Time to Purchase
# Task 10
# Using the giant merged DataFrame all_data that you created, let’s calculate the average time from initial visit to final purchase. Add a column that is the difference between purchase_time and visit_time.
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase)

avg_time_purch = all_data['time_to_purchase'].mean()
print(avg_time_purch)
# the average purchase time is 44 min




