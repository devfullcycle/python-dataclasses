from dataclasses import dataclass, field, asdict, astuple
from typing import Optional, List
from datetime import datetime

@dataclass(slots=True, kw_only=True)
class Product:
    product_id: int
    name: str
    price: float
    description: Optional[str] = None

@dataclass(slots=True, kw_only=True)
class Order:
    order_id: int
    client_id: int
    total: float = field(init=False, default=0.0)
    products: List[Product] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        self.__calculate_total()
    
    def __calculate_total(self):
        self.total = sum([product.price for product in self.products])


product1 = Product(product_id=1, name='Product 1', price=20)
order1 = Order(order_id=1, client_id=1, products=[product1])
print(order1)

print(asdict(order1))
print(astuple(order1))