import requests
from settings import success_status_codes

def get_currency_by_abbr(abbr_money):
	url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={abbr_money}&json"
	try:
		resp = requests.get(url)
		status_code = resp.status_code
		if status_code in success_status_codes:
			currency_info = resp.json()
		else:
			error_message = f'Request failed with status on {url} code {status_code}'
			print(error_message)
	except Exception as e:
		raise Exception(f"Request failed cross: {url} with Exception {e}")
#	print(currency_info, url)
		currency_info = currency_info[0]
		currency_name = currency_info["txt"]
		rate = currency_info["rate"]
		message = f"Курс {currency_name} сьогодні {rate} грн за 1 {abbr_money}."
		return message
		pass
