# token_manager.py

import requests
import time
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class TokenManager:
    def __init__(self):
        self.token = None
        self.token_expiry = 0

    def get_token(self):
        # Revalida o token se ele expirou ou está prestes a expirar
        if time.time() >= self.token_expiry:
            self.token = self._request_new_token()
            self.token_expiry = time.time() + 280  # Expira em 280 segundos
        return self.token

    def _request_new_token(self):
        url = os.getenv('TOKEN_API_URL')
        headers = {
            'client_id': os.getenv('TOKEN_CLIENT_ID'),
            'client_secret': os.getenv('TOKEN_CLIENT_SECRET'),
            'User-Agent': os.getenv('API_USER_AGENT'),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'client_id': 'operation',
            'grant_type': os.getenv('TOKEN_GRANT_TYPE'),
            'client_secret': os.getenv('BODY_CLIENT_SECRET'),
            'scope': os.getenv('TOKEN_SCOPE')
        }
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        return response.json()['access_token']