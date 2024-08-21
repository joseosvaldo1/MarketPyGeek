from typing import List, Dict
from time import sleep

from models.product import Product
from utils.helper import format_float_str_currency

products: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
	menu()
	

def menu() -> None:
	print("################################")
	print("########### Welcome ############")
	print("########## Geek Shop ###########")
	print("################################")
	
	print("Select one of the options below: ")
	print("1. Register product(s);")
	print("2. List product(s);")
	print("3. Buy product(s);")
	print("4. Show shopping cart;")
	print("5. Close order;")
	print("6. Log out of the system.")
	
	option: int = int(input())
	
	if option == 1:
		register_product()
	elif option == 2:
		list_products()
	elif option == 3:
		buy_product()
	elif option == 4:
		show_cart()
	elif option == 5:
		close_order()
	elif option == 6:
		print("Come back often!")
		sleep(2)
		exit(0)
	else:
		print("Invalid option!")
		sleep(1)
		menu()
		
	
def register_product() -> None:
	print("################")
	print("Register Product")
	print("################")
	
	name: str = input("Enter the product name: ")
	price: float = float(input("Enter the product price: "))

	product: Product = Product(name, price)
	
	products.append(product)
	
	print(f"The product {product.name} was registered "
	      f"successfully!")
	
	sleep(2)
	
	menu()
	
	
def list_products() -> None:
	if len(products) > 0:
		print("################")
		print("List Products")
		print("################")
		print("----------------")
		for product in products:
			print("----------------")
			print(product)
			print("----------------")
			sleep(1)
			
	else:
		print("There are no registered products yet!")
	
	sleep(2)
	menu()


def buy_product() -> None:
	if len(products) > 0:
		print("##############################")
		print("Enter the code of the product to \n"
		      "be added to the shopping cart: ")
		print('--------------------------------')
		print("##### Available products #####")
		
		for product in products:
			print(product)
			print('--------------------------------')
			sleep(1)
		
		code: int = int(input())
		
		product: Product = get_product_by_code(code)
		
		if product:
			if len(cart) > 0:
				is_included_cart: bool = False
				for item in cart:
					quant: int = item.get(product)
					if quant:
						item[product] = quant + 1
						print(f"Product '{product.name}' now has "
						      f"'{quant + 1}' units in the cart")
						is_included_cart = True
				if not is_included_cart:
					prod = {product: 1}
					cart.append(prod)
					print(f"The product {product.name} has been"
					      f"added to the shopping cart.")
					sleep(2)
					menu()
			else:
				item = {product: 1}
				cart.append(item)
				print(f"The product '{product.name}' has"
				      f"been added to the shopping cart.")
		else:
			print(f"Product with code '{code}' was "
			      f"not found!")
		
		sleep(2)
		menu()
	else:
		print("There are no products for sale yet!")
	
	sleep(2)
	menu()


def show_cart() -> None:
	if len(cart) > 0:
		print("#####################################")
		print("### Products in the shopping cart ###")
		print("#####################################")
		
		for item in cart:
			for data in item.items():
				print('------------------')
				print(f"Product: {data[0]}")
				print(f"Quantity: {data[1]}")
				print('------------------')
				sleep(1)
	else:
		print(f"There are no products in the "
		      f"shopping cart yet")
	
	sleep(2)
	menu()


def close_order() -> None:
	if len(cart) > 0:
		total_value: float = 0
		
		print("##########################")
		print("Products in shopping cart:")
		print("##########################")
		
		for item in cart:
			for data in item.items():
				print('------------------')
				print(f"Product: {data[0]}")
				print(f"Quantity: {data[1]}")
				total_value += data[0].price*data[1]
				print('------------------')
				sleep(1)
		
		print(f"Your bill is "
		      f"{format_float_str_currency(total_value)}")
		print("Come back often!")
		cart.clear()
		sleep(5)
	else:
		print("There are no products in the shopping "
		      "cart yet")
	
	sleep(2)
	menu()
	
	
def get_product_by_code(code: int) -> Product:
	p: Product = None
	
	for product in products:
		if product.code == code:
			p = product
	
	return p


if __name__ == "__main__":
	main()
	