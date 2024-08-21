from utils.helper import format_float_str_currency


class Product:
	counter: int = 1
	
	def __init__(self: object, name: str, price: float,) -> None:
		self.__code: int = Product.counter
		self.__name: str = name
		self.__price: float = price
		Product.counter += 1
		
	@property
	def code(self: object) -> int:
		return self.__code
	
	@property
	def name(self: object) -> str:
		return self.__name
	
	@property
	def price(self: object) -> float:
		return self.__price
	
	
	def __str__(self: object) -> str:
		return (f"Code: {self.code} \n"
			   f"Name: {self.name} \n"
			   f"Price: {format_float_str_currency(self.price)}")
		
		
		
	