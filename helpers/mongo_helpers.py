# helpers/mongo_helpers.py

from pymongo import MongoClient
import os
import pprint

# Conexão MongoDB
MONGO_CONNECTION_STRING = os.getenv("MONGO_CONNECTION_STRING")
DATABASE_NAME = "person"
COLLECTION_NAME = "customer"

def fetch_sales_info(identity):
    """
    Busca informações de vendas e endereço para o cliente com base no 'document_id' no campo 'documents'.
    """
    try:
        client = MongoClient(MONGO_CONNECTION_STRING)
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        print("Conexão com MongoDB estabelecida com sucesso.")
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return None, None, None

    try:
        result = collection.find_one({
            "documents": {
                "$elemMatch": {
                    "document_id": identity
                }
            }
        })

        if result:
            print("Documento encontrado:")
            pprint.pprint(result)

            # Extraindo informações de vendas
            sales_info = result.get("sales_informations", [])
            if sales_info:
                organization_code = sales_info[0].get("organization_code", None)
                payment_conditions = sales_info[0].get("payment_conditions", [])
                payment_method = payment_conditions[0].get("conditions", None) if payment_conditions else None
            else:
                organization_code = None
                payment_method = None

            # Extraindo informações de endereço
            addresses = result.get("addresses", [])
            if addresses:
                address_info = {
                    "street": addresses[0].get("street", None),
                    "number": addresses[0].get("number", None),
                    "zip_code": addresses[0].get("zip_code", None),
                    "city": addresses[0].get("city", None),
                    "state": addresses[0].get("federative_unit", None),
                    "country": addresses[0].get("country", None),
                    "district": addresses[0].get("neighborhood", None)
                }
            else:
                address_info = {key: None for key in ["street", "number", "zip_code", "city", "state", "country", "district"]}

            return organization_code, payment_method, address_info
        else:
            print(f"Nenhum documento encontrado para identity {identity}.")
            return None, None, None

    except Exception as e:
        print(f"Erro ao buscar documento no MongoDB: {e}")
        return None, None, None