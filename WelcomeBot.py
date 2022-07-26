import telebot
from telebot import *

bot = telebot.TeleBot("745648563:AAEyfePhXwBvjRLBwVLqHbybzGAeTynbItw")

tumbler = 0
chat_id = ''
name = '✖'
dateofbith = '✖'
interests = '✖'
number = '✖'

@bot.message_handler(commands=['start'])
def send_welcome(message):
	chat_id = message.from_user.id
	hello_text = "Привет, что-бы войти в чат города Умань нужно заполнить кое-какие данные...\n (Данные собираются только для того что-бы сортировать выгодные предложения по вашим предпочтениям)\n\nИмя и фамилия : " + name + "\n\n" + "Номер телефона : " + number + "\n\n" + "Зачем тебе этот чат? : " + interests
	if message.from_user.username == 'Dellay_k':
		bot.send_message(chat_id, 'Привет, сучечка :3')
		bot.send_sticker(chat_id, 'CAACAgIAAxkBAAImiF5Ef-WY8cYrbbfQgClWFYaW42fDAAJcAwACW4rCAz88eEHGDiF9GAQ')
	markup = types.InlineKeyboardMarkup()
	btn1 = types.InlineKeyboardButton(text = '😜Имя и фамилия😜', callback_data='name')
	btn2 = types.InlineKeyboardButton(text = '😏Номер телефона😏', callback_data='number')
	btn3 = types.InlineKeyboardButton(text = '😍Для чего тебе нужен этот чат?😍', callback_data = 'interests')
	markup.row(btn1)
	markup.row(btn2)
	markup.row(btn3)
	bot.send_message(chat_id, hello_text , reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.data == 'name':
		global tumbler
		back_markup = types.InlineKeyboardMarkup()
		btn_back = types.InlineKeyboardButton(text = '🔙Назад🔙', callback_data = 'back')
		back_markup.row(btn_back)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,
		text = 'Введите своё имя и фамилию :', reply_markup = back_markup)

		@bot.message_handler(func=lambda m: True)
		def name_handler(message):
			pass

	if call.data == 'number':
		back_markup = types.InlineKeyboardMarkup()
		btn_back = types.InlineKeyboardButton(text = '🔙Назад🔙', callback_data = 'back')
		back_markup.row(btn_back)
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id,
		text = 'Нажмите на троеточие справа сверху и \"Отправить свой телефон\".\n⭕🔴РАБОТАЕТ ТОЛЬКО С ТЕЛЕФОНА🔴⭕',
		reply_markup = back_markup
		)
		@bot.message_handler(content_types=['contact'])
		def get_phone_number(message):
			global tumbler
			global number
			if message.contact.phone_number == message.contact.phone_number and tumbler == 0:
				chat_id = message.from_user.id
				number = message.contact.phone_number
				print('+' + number)
				number = '+' + number + ' ✅'
				tumbler = 1
				markup = types.InlineKeyboardMarkup()
				btn1 = types.InlineKeyboardButton(text = '😜Имя и фамилия😜', callback_data='name')
				btn2 = types.InlineKeyboardButton(text = '😏Номер телефона😏', callback_data='number')
				btn3 = types.InlineKeyboardButton(text = '😍Для чего тебе нужен этот чат?😍', callback_data = 'interests')
				markup.row(btn1)
				markup.row(btn2)
				markup.row(btn3)
				bot.edit_message_text(chat_id = call.message.chat.id,
				message_id = call.message.message_id,
				text = 'Что-бы войти в чат города Умань нужно заполнить кое-какие данные...\n (Данные собираются только для того что-бы сортировать выгодные предложения по вашим предпочтениям)\n\nИмя и фамилия : ' + name + "\n\n" + "Номер телефона : " + number + "\n\n" + "Зачем тебе этот чат? : " + interests,
				reply_markup = markup
				)
				bot.delete_message(chat_id, message_id = message.message_id)

			bot.delete_message(chat_id, message_id = message.message_id)

	elif call.data == 'back':
		markup = types.InlineKeyboardMarkup()
		btn1 = types.InlineKeyboardButton(text = '😜Имя и фамилия😜', callback_data='name')
		btn2 = types.InlineKeyboardButton(text = '😏Номер телефона😏', callback_data='number')
		btn3 = types.InlineKeyboardButton(text = '😍Для чего тебе нужен этот чат?😍', callback_data = 'interests')
		markup.row(btn1)
		markup.row(btn2)
		markup.row(btn3)
		bot.edit_message_text(chat_id = call.message.chat.id,
		message_id = call.message.message_id,
		text = 'Что-бы войти в чат города Умань нужно заполнить кое-какие данные...\n (Данные собираются только для того что-бы сортировать выгодные предложения по вашим предпочтениям)\n\nИмя и фамилия : ' + name + "\n\n" + "Номер телефона : " + number + "\n\n" + "Зачем тебе этот чат? : " + interests,
		reply_markup = markup
		)

bot.polling(none_stop=True)
