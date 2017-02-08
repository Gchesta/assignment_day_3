
def find_exchange_rate():
	"""This is a simple command line application to convert one currency into the other
	using the fixer.io API"""
	
	curr1 = input("Convert FROM (e.g USD, GBP):")
	curr1 = curr1upper()
	
	curr2 = input("Convert To (e.g GBP, USD)")
	curr2 = curr2.upper()
	
	amount = float(input("Please Enter the AMOUNT to be Converted:"))
	
	api_url = ("http://api.fixer.io/latest?symbols=%s,%s") % (curr1, curr2)
	exchange_rate = requests.get(api_url).json()["rates"][curr2]
	converted_amount = amount * exchange_rate
	
	return curr1 + str(amount) + " converts to " + curr1 + str(converted_amount)
	
	
	