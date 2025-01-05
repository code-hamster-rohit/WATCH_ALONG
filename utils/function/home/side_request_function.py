import requests
import os

class HomeRequestFunction:
    
    @staticmethod
    def get_user_details(url, query, entries):
        try:
            response = requests.get(url, params=query)
            if response.status_code == 200:
                user_instance = response.json()['data']
                for idx, entry in enumerate(entries):
                    entry.configure(state='normal')
                    entry.configure(text_color=os.getenv("BG_6"))
                    entry.delete(0, 'end')
                    entry.insert(0, user_instance[idx])
                    entry.configure(state='disabled')
            else:
                return response.status_code
        except requests.exceptions.RequestException as e:
            return 500
    
    @staticmethod
    def change_user_details(url, query, data, entries, get_url):
        try:
            response = requests.patch(url, params=query, json=data)
            if response.status_code == 200:
                HomeRequestFunction.get_user_details(get_url, query, entries)
            else:
                return response.status_code
        except requests.exceptions.RequestException as e:
            return 500