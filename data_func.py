import json
import os
import datetime



def create_user_data(message, folder_name:str):
    file_name = f"{message.from_user.id}"
    if os.path.exists(f'{folder_name}/{file_name}.json'):
        pass
    else:
        # User does not exist, create new data
        
        now = datetime.datetime.now()
        time_now = str(now.strftime("%d-%m-%Y %H:%M:%S"))

        user_info = {
            "id": message.from_user.id,
            "first-name": message.from_user.first_name,
            "last-name": message.from_user.last_name,
            "user-name": message.from_user.username,
            "languige": message.from_user.language_code,
            "info": {
                        "findings-count": 0,
                        "bot-start": time_now,
                },
            "subscribe": {
                        "count": 0,
                        "sub-date": 0,
                        "status": False
                    },
            "premium": {
                        "count-vip": 0
            },
            "photo-path": [],
            "chat-history": []
        }

        # Create new JSON file for user
        with open(f'{folder_name}/{file_name}.json', "w", encoding='utf-8') as f:
            json.dump(user_info, f, indent=4, ensure_ascii=False)



def add_user_data(path, data_update_path:str, new_data, data_update_path_in:str == None):
    with open(f"{path}.json", "r") as f:
        data = json.load(f)

    now = datetime.datetime.now()
    time_now = str(now.strftime("%d-%m-%Y %H:%M:%S"))


    if data_update_path_in == None:

        link_user_info = time_now, new_data

        data[f"{data_update_path}"].append(link_user_info)
        
    else:
        link_user_info = time_now, new_data

        data[f"{data_update_path}"][f"{data_update_path_in}"] = new_data


    with open(f"{path}.json", "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


