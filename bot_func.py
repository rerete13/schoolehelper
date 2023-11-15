import telebot



def is_subscriber(bot, chat_id:str, group:str):
    chat_member = bot.get_chat_member(f'{group}', chat_id)

    arr_members_types = ['creator', 'administrator', 'member']
    for i in arr_members_types:
        if i == str(chat_member.status):
            return True

    return False
