import requests
from settings import root_url, success_status_codes
from currency import get_currency_by_abbr

class Bot:
	updates_endpoint = '/getUpdates'
	send_message_endpoint = '/sendMessage'

	def __init__(self, token):
		self.token = token

	def get_updates(self):
		result = {'error': False, 'value': None}
		url = f'{root_url}{self.token}{self.updates_endpoint}'
		try:
			resp = requests.get(url)
			status_code = resp.status_code
			if status_code in success_status_codes:
				updates = resp.json().get('result')
				result['value'] = updates
				return result
			else:
				error_message = f'Request failed with status on {url} code {status_code}'
				print(error_message)
				result['error'] = True
				return result
		except Exception as e:
			raise Exception(f"Request failed cross: {url} with Exception {e}")

	# def get_updates_old(self):
	# 	url = f'{root_url}{self.token}{self.updates_endpoint}'
	# 	resp = requests.get(url)
	# 	status = resp.status_code
	# 	if status not in success_status_codes:
	# 		print(f'Request on URL {url} failed with status: {status}')
	# 	else:
	# 		updates = resp.json()['result']
	# 	return updates

	def send_message(self, chat_id, text):
		url = f'{root_url}{self.token}{self.send_message_endpoint}'
		try:
			response = requests.post(url, data={"chat_id":chat_id, "text":text})
			status = response.status_code
			if status not in success_status_codes:
				print(f'Request on URL {url} failed with status: {status}')
			else:
				status = response.status_code
				print(f'Status code: {status}')
		except Exception as e:
			raise Exception(f"Response failed with sending message, with {status}")

	def process_message(self, chat_id, text):
		print(text[0:10])
		print(text[-3:])
		try:
			if text == '/Hello':
				self.send_message(chat_id,'Getting started!')
			elif text == '/stop':
				self.send_message(chat_id, 'Stopped')
			elif text[0:5] == '/курс':
				if len(text) >= 9:
					currency_abbr = text[-3:]
					message = get_currency_by_abbr(currency_abbr)
					self.send_message(chat_id, message)
				else:
					self.send_message(chat_id, "Try again, please.")
			else:
				self.send_message(chat_id, "I don't  know...")
		except Exception as e:
			self.send_message(chat_id, f"Verify text message, it must consist of ('usd', 'eur', 'rub') be like: '/курс usd',   '{text[0:10]}' given")

	def polling(self):
		previous_message_id = 0
		while True:
			updates = self.get_updates()
			if not updates.get('error'):
				if updates.get('value'):
					last_message = updates.get('value')[-1]['message']
					last_message_id = last_message.get('message_id')
					if previous_message_id < last_message_id:
						chat_id = last_message.get('chat').get('id')
						last_message_text = last_message.get('text')
						self.process_message(chat_id, last_message_text)
						previous_message_id = last_message_id
























