import telebot



def is_subscriber(bot, chat_id:str, group:str):
    chat_member = bot.get_chat_member(f'{group}', chat_id)

    arr_members_types = ['creator', 'administrator', 'member']
    for i in arr_members_types:
        if i == str(chat_member.status):
            return True

    return False



def wikamp_task_comliter(message, bot):
    
    bot.send_message(message.chat.id, 'hi i am nextstephendlerr')
    
    

def download_photo_by_file_id(bot, message, file_id, save_folder:str, name=None):
    file_path = bot.get_file(file_id).file_path
    file = bot.download_file(file_path)
    if name == None:
        with open(f"{save_folder}/{message.chat.id}.png", "wb") as code:
            code.write(file)
        return
    else:
        with open(f"{save_folder}/{name}.png", "wb") as code:
            code.write(file)
        return
        