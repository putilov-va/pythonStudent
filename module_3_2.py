
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if not ("@" in sender and
            "@" in recipient and
            sender.endswith((".com", ".ru", ".net")) and
            recipient.endswith((".com", ".ru", ".net"))):
                # Метод endswith проверяет, заканчивается ли строка на указанную
                 # подстроку и возвращает значения True или False
        output = f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}"
    elif sender == recipient:
        output = ("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        output = f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}"
    else:
        output = (f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено"
              f" с адреса {sender} на адрес {recipient}.")
    print(output)
send_email('Это сообщение для проверки связи',
           'vasyok@1337gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание',
           'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре',
           'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')
#
#