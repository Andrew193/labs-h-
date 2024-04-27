def calculate_total_price(product_prices, discount):
    return _calculate_total_price(product_prices, discount)

def calculate_total_price_with_tax(product_prices, discount, tax_rate):
    total_price = _calculate_total_price(product_prices, discount)
    total_price *= (1 + tax_rate)
    return total_price

def _calculate_total_price(product_prices, discount):
    total_price = 0
    for price in product_prices:
        if discount:
            total_price += price * 0.9
        else:
            total_price += price
    return total_price