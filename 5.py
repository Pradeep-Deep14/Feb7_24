def sort_products_by_price(product_list):
    product_list.sort(key=lambda x:x[1])
    return tuple(product_list)

product=[('Laptop',1200),('Smartphone',800),('Headphones',150),('Camera',500)]
sorted_products=sort_products_by_price(product)
print(sorted_products)