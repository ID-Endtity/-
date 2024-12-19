import telebot

global i
i=[]

token = "7790772322:AAHuc3-D8fpjXi__bMeZiz_O4OGInZd_38s"

var1 = ("https://imgur.com/6I9YG7g", "https://imgur.com/kUWap6L", "https://imgur.com/FeFZQOk","https://imgur.com/aBzxIGd",'https://imgur.com/CWMdXGs','https://imgur.com/Nyerscx', 'https://imgur.com/wftx5GX', 'https://imgur.com/UiJZTAZ', 'https://imgur.com/tDdGLb4',
		'https://imgur.com/Ph4Lj9e', 'https://imgur.com/ib4fGzH', 'https://imgur.com/OqCiAaD')

ans1 = ("2431",'123','4361',"237458",'2531',"235","4125",'верховногоглавнокомандующего','Деникин','девятнадцатом','орёл','125')
bot = telebot.TeleBot(token)
bot=telebot.TeleBot("7024147869:AAF27OqGFnVPndV1I47oKwN0AuyoKH150vI")

#@bot.message_handler(commands=['start'])
# def start_test(message):
# 	msg=message
# 	bot.send_message(,text="/start", )	


@bot.message_handler(commands=['test'])
def start_test(message):
	if len(i)==0:
		global count
		count=0
		bot.send_message(message.chat.id,
                     "Привет! 🎉 Добро пожаловать в викторину по ЕГЭ по истории!")
		global chat
		chat=message.chat.id
		global msg
		msg=message

	bot.send_photo(chat, var1[len(i)])
	bot.register_next_step_handler(msg, check_ans)
	


	
def continue_test():
	bot.send_photo(chat, var1[len(i)])
	bot.register_next_step_handler(msg, check_ans)
	if len(i)==12:
		bot.send_message(chat, f"Тест окончен. \nВы набрали {count} баллов.")

def check_ans(message):
	if message.text == ans1[len(i)]:
		bot.send_message(message.chat.id, "Верный ответ!")
		i.append(1)
		global count
		count+=1
		if len(i)<12:
			bot.register_next_step_handler(message,continue_test())

	else:
		bot.send_message(message.chat.id, "Неверный ответ!")
		m=bot.send_message(message.chat.id, f"Правильный ответ: {ans1[len(i)]}")
		i.append(1)
		if len(i)<12:
			bot.register_next_step_handler(message,continue_test())




bot.infinity_polling()