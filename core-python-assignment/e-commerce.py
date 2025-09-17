def cal_total(cart_items):
    if len(cart_items)==0:
        print("cart is empty")
        return
    total=0
    for price in cart_items.values():
        total=total+price
    if len(cart_items)>5:
        total =total* 0.9
    print("Total Price:",total)
cart_items={
    'Laptop': 50000,
    'Headphones': 2000,
    'Mouse': 500,
    'Keyboard': 1500
}
cal_total(cart_items)