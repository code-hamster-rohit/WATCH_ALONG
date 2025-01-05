from views.home.home import Home
import requests
import json
import os

class RequestFunction:
    
    @staticmethod
    def send_post_request(url, data, parent, buttons):
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                file_path = os.path.join(os.getcwd(), 'user_instance', 'user_instance.json')
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(response.json()['system_id'], f, indent=4, ensure_ascii=False)
                    f.close()
                Home(parent,  width=500, height=500, fg_color=os.getenv("BG_1")).put('grid', row=0, column=0, sticky='nsew')
            else:
                for button in buttons:
                    button.configure(text='CREATE')
                    button.configure(state='normal')
                return response.status_code
        except requests.exceptions.RequestException as e:
            for button in buttons:
                button.configure(text='CREATE')
                button.configure(state='normal')
            return 500