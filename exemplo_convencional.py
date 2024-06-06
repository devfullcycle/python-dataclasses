
# exemplo convencional
class Order:

    __slots__ = ['order_id', 'product_id', 'quantity', 'price']

    # order_id: int
    # product_id: int
    # quantity: int
    # price: float

    def __init__(self, order_id, product_id, quantity, price): 
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
    
    def __init__(self, **data: Dict[str, Any]):
        self.order_id = data.get('order_id')
        self.product_id = data.get('product_id')
        self.quantity = data.get('quantity')
        self.price = data.get('price')

    def total(self):
        return self.quantity * self.price

    def __repr__(self):
        return f'Order(order_id={self.order_id}, product_id={self.product_id}, quantity={self.quantity}, price={self.price})'
    
    def __eq__(self, value: object) -> bool:
        return isinstance(value, Order) and self.order_id == value.order_id
