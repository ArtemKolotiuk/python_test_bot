from settings import token1
from fake import Bot


if __name__ == '__main__':
	bot = Bot(token1)
	bot.polling()