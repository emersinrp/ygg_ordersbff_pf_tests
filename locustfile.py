# locustfile.py

from locust import HttpUser, task, between
from token_manager import TokenManager
from dotenv import load_dotenv
from helpers.body_bff_creator import create_bff_body
from helpers.mongo_helpers import fetch_sales_info
import os
import json
from faker import Faker

load_dotenv()
fake = Faker()

class BFFPerformanceTest(HttpUser):
    wait_time = between(1, 5)
    token_manager = TokenManager()
    
    host = os.getenv('BFF_API_HOST')
    orders_endpoint = "/external/bff/central/orders"

    def _get_headers(self, token):
        return {
            'User-Agent': os.getenv('API_USER_AGENT'),
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

    def _generate_identity(self):
        return fake.random_element(elements=[
            "04142833000148", "42968579000120", "06162976000147",
            "42126636000124", "56891046000100", "41558497000145",
            "57128927000129", "55664347000120", "56940660000107",
            "49865510000110"
        ])

    @task
    def create_order(self):
        token = self.token_manager.get_token()
        headers = self._get_headers(token)

        identity = self._generate_identity()
        organization_code, payment_method, address_info = fetch_sales_info(identity)

        # Cria o payload para o pedido
        payload = create_bff_body(
            identity=identity,
            sales_organization=organization_code or "DefaultOrgCode",
            payment_method=payment_method or "DefaultPaymentMethod",
            address_info=address_info
        )

        # Imprime o payload antes de enviá-lo
        print("Payload que está sendo enviado para a API:")
        print(json.dumps(payload, indent=4))

        try:
            response = self.client.post(
                self.orders_endpoint, 
                name="Orders BFF", 
                headers=headers, 
                data=json.dumps(payload)
            )
            response.raise_for_status()

            response_data = response.json()
            if response_data.get("success") == True:
                print(f"Order Number: {response_data.get('order_number')}")
            else:
                print("Erro na resposta: Pedido não foi bem-sucedido.")
                
        except Exception as e:
            print(f"Erro na requisição: {e}")
            if response:
                print("Detalhes da resposta:", response.text)