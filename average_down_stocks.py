import math
# Check how much you need to spend to average down a previously bought stock price

# Set the current price of the stocks
current_price_stocks = 24.6

# Set the amount of stocks you would buy
amount_stocks_to_buy = 4

# Set the current average of your already purchased stocks
stock_current_average = 30.9773

# Set the current amount of stocks you have
current_amount_stocks = 15

# Set the total positive amount paid for the stocks you currently own
total_paid_before = 74.57

# Set the current loss or profit amount
current_loss_profit = 134.98

# Set the price of the fee you must pay: 
# add + 8 if you are not buying finnish stocks or today is not an Equity Savings Day
fee = current_price_stocks*amount_stocks_to_buy*0.01 #+8

########################################## MATH ################################################################
new_average_stock_price = (stock_current_average*current_amount_stocks + current_price_stocks*amount_stocks_to_buy)/(current_amount_stocks + amount_stocks_to_buy)
you_pay = fee + current_price_stocks*amount_stocks_to_buy

you_pay_in_total = total_paid_before + current_loss_profit + you_pay
new_value = new_average_stock_price*(current_amount_stocks+amount_stocks_to_buy)
updated_profit_loss = you_pay_in_total - new_value

########################################## RESULTS ################################################################
print(f"If you buy {amount_stocks_to_buy} stocks, the new average stock price will be {new_average_stock_price}, and you must pay {you_pay} euros")