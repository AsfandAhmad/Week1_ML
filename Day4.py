import numpy as np

sales_data = np.array([
    [200, 220, 250, 210, 180, 190],
    [230, 240, 260, 200, 195, 205],
    [210, 215, 255, 220, 185, 200],
    [205, 225, 270, 215, 190, 195],
    [215, 230, 265, 225, 200, 210],
    [225, 235, 275, 230, 205, 215],
    [235, 245, 280, 240, 210, 220],
    [245, 255, 290, 250, 215, 225],
    [255, 265, 300, 260, 220, 230],
    [265, 275, 310, 270, 225, 235]
])

total_sales_per_product = np.sum(sales_data, axis=0)
average_sales_per_product = np.mean(sales_data, axis=0)
commissioned_sales = sales_data * 1.05
sqrt_sales = np.sqrt(sales_data)

print(f"\nTotal Sales Per Product: {total_sales_per_product}")
print(f"Average Sales Per Product: {average_sales_per_product}")
print(f"Commissioned Sales (5% added): \n{commissioned_sales}")
print(f"Square Root of Sales: \n{sqrt_sales}")

bonus_array = np.array([10, 20, 15, 25, 30, 5])
sales_with_bonus = sales_data + bonus_array
sales_plus_50 = sales_data + 50

print(f"\nBonus Array: {bonus_array}")
print(f"Sales with Bonus: \n{sales_with_bonus}")
print(f"Sales + $50: \n{sales_plus_50}")

mean_sales = np.mean(sales_data)
median_sales = np.median(sales_data)
variance_sales = np.var(sales_data)
std_sales = np.std(sales_data)

print(f"\nMean Sales: {mean_sales}")
print(f"Median Sales: {median_sales}")
print(f"Variance of Sales: {variance_sales}")
print(f"Standard Deviation of Sales: {std_sales}")

max_sale = np.max(sales_data)
min_sale = np.min(sales_data)
range_sales = max_sale - min_sale

print(f"\nMaximum Sale: {max_sale}")
print(f"Minimum Sale: {min_sale}")
print(f"Range of Sales: {range_sales}")

q3 = np.percentile(sales_data, 75)
q1 = np.percentile(sales_data, 25)
iqr_sales = q3 - q1

print(f"\nIQR of Sales: {iqr_sales}")

sales_greater_250 = sales_data[sales_data > 250]
capped_sales = np.copy(sales_data)
capped_sales[capped_sales > 300] = 300
count_btw_200_250 = np.sum((sales_data >= 200) & (sales_data <= 250))
sales_below_mean = sales_data[sales_data < mean_sales]

print(f"\nSales greater than $250: {sales_greater_250}")
print(f"Capped Sales (max 300): \n{capped_sales}")
print(f"Count of Sales between $200 and $250: {count_btw_200_250}")
print(f"Sales below Mean: {sales_below_mean}")

day5_sorted = np.sort(sales_data[4])
total_sales_per_day = np.sum(sales_data, axis=1)
highest_sales_day_index = np.argmax(total_sales_per_day)

column_mean = np.mean(sales_data, axis=0)
row_mean = np.mean(sales_data, axis=1)
overall_avg_sales = np.mean(sales_data)

print(f"\nSorted Sales on Day 5: {day5_sorted}")
print(f"Total Sales Per Day: {total_sales_per_day}")
print(f"Day with Highest Total Sales :(Day {highest_sales_day_index + 1})")
print(f"Column Mean (Per Product): {column_mean}")
print(f"Row Mean (Per Day): {row_mean}")
print(f"Overall Average Sales: {overall_avg_sales}")

def highlight_outlier(data):
    mean_val = np.mean(data)
    std_val = np.std(data)
    threshold = mean_val + 2 * std_val
    return data[data > threshold]

outliers = highlight_outlier(sales_data)
print(f"\nOutliers : {outliers}")
