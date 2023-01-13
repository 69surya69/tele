import telebot

bot = telebot.TeleBot("YOUR_TOKEN")

subjects = {"maths": ["link1", "link2"],
            "physics": ["link3", "link4"],
            "chemistry": ["link5", "link6"],
            "biology": ["link7", "link8"],
            "english": ["link9", "link10"],
            "history": ["link11", "link12"]}

def handle_subject(message):
    subject = message.text.lower()
    if subject in subjects:
        bot.send_message(message.chat.id, "Here are the links for {}:".format(subject))
        for link in subjects[subject]:
            bot.send_message(message.chat.id, link)
    else:
        bot.send_message(message.chat.id, "Invalid subject. Please choose one of the following subjects: {}".format(", ".join(subjects.keys())))

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome! Please select one of the following subjects: {}".format(", ".join(subjects.keys())))
    bot.register_next_step_handler(message, handle_subject)

bot.polling()
