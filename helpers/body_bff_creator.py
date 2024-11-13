# helpers/body_bff_creator.py

from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

def create_bff_body(identity=None, sales_organization=None, payment_method=None, address_info=None):
    """
    Cria o payload para o pedido BFF com base nos dados de entrada.
    
    Parameters:
        - identity (str): Identidade do cliente (CNPJ ou CPF).
        - sales_organization (str): Código da organização de vendas.
        - payment_method (str): Método de pagamento.
        - address_info (dict): Informações do endereço obtidas do MongoDB.
        
    Returns:
        dict: Payload formatado para envio para a API BFF.
    """
    
    # Calcula a data de entrega, 2 dias a partir de hoje
    delivery_date = (datetime.utcnow() + timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # Gera um número de pedido aleatório começando com "EMECBFF"
    order_number = f"EMECBFF{fake.random_number(digits=4, fix_len=True)}"
    
    # Cria o payload com os dados padrão
    payload = {
        "delivery_date": delivery_date,
        "total": 43.60,
        "taxes": {},
        "customer": {
            "name": "TESTE EMERSON",
            "sales_organization": sales_organization,
            "identity": identity,
            "order_number": order_number,
            "payment_method": payment_method,
            "origin_distribution_center": "1625",
            "identity_type": "CNPJ",
            "email": "testeemerson@teste.com",
            "birth_date": "1992-12-22",
            "phone": "16996212196",
            "addresses": [
                {
                    "street": address_info.get("street", ""),
                    "number": address_info.get("number", ""),
                    "complement": address_info.get("complement", "N/A"),
                    "zip_code": address_info.get("zip_code", ""),
                    "city": address_info.get("city", ""),
                    "state": address_info.get("federative_unit", ""),
                    "country": address_info.get("country", ""),
                    "district": address_info.get("neighborhood", ""),
                    "type": "billing"
                },
                {
                    "street": address_info.get("street", ""),
                    "number": address_info.get("number", ""),
                    "complement": address_info.get("complement", "N/A"),
                    "zip_code": address_info.get("zip_code", ""),
                    "city": address_info.get("city", ""),
                    "state": address_info.get("federative_unit", ""),
                    "country": address_info.get("country", ""),
                    "district": address_info.get("neighborhood", ""),
                    "type": "delivery"
                }
            ]
        },
        "items": [
            {
                "description": "TESTE EMERSON",
                "sku": "000000000000759192",
                "quantity": 1,
                "fifo_category": "green",
                "price": {
                    "value": 110.50,
                    "unit": "KG",
                    "currency": "BRL",
                    "promotion": "teste"
                },
                "unit_of_measurement": "KG",
                "additional_info": None
            }
        ],
        "salesman": {
            "document_number": ""
        },
        "additional_info": None,
        "payment": {
            "type": "boleto",
            "method": "01",
            "amount": 43.60,
            "capture": True,
            "voucher": False,
            "external_authentication": None
        },
        "purchase_type": "app",
        "ip": "192.168.1.100"
    }
    
    return payload