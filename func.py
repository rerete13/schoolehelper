import os


def download_telegram_photo(bot, message, save_directory:str, name=None):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    file_path = file_info.file_path
    downloaded_file = bot.download_file(file_path)


    os.makedirs(save_directory, exist_ok=True)

    if name == None:
        file_extension = file_path.split('.')[-1]
        unique_filename = os.path.join(save_directory, f'photo_{message.chat.id}_{photo.file_id}.{file_extension}')
        
    else:
        file_extension = file_path.split('.')[-1]
        name = name.replace(" ", "")
        unique_filename = os.path.join(save_directory, f'{name}.{file_extension}')
        

    with open(unique_filename, 'wb') as new_file:
        new_file.write(downloaded_file)
        
    return unique_filename