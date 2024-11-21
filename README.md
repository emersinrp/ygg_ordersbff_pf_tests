# BFF Payload Generator

Este projeto é um gerador de payloads para integração com a API BFF de pedidos. Ele utiliza dados dinâmicos extraídos do MongoDB e preenche automaticamente os campos do payload conforme as necessidades do sistema.

---

## 📚 Índice

- [Descrição do Projeto](#-descrição-do-projeto)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Como Executar](#-como-executar)
- [Funcionalidades](#-funcionalidades)
- [Exemplo de Uso](#-exemplo-de-uso)
- [Contribuições](#-contribuições)
- [Licença](#-licença)

---

## 📝 Descrição do Projeto

Este projeto gera um payload dinâmico para criação de pedidos na API BFF. Ele suporta:

- Dados do cliente, incluindo endereços, identidade e métodos de pagamento.
- Itens do pedido com informações detalhadas como preço, quantidade e categoria FIFO.
- Endereços (billing e delivery) preenchidos automaticamente a partir do MongoDB.

Além disso, o projeto inclui uma lógica para gerar números de pedido, calcular datas de entrega e personalizar os payloads com base nos parâmetros recebidos.

---

## 📂 Estrutura do Projeto

```plaintext
helpers/
├── body_bff_creator.py   # Módulo principal que gera o payload do pedido
README.md                 # Documentação do projeto

body_bff_creator.py

Este arquivo contém a função create_bff_body, que é responsável por gerar o payload do pedido. Ele aceita parâmetros para personalizar o payload, incluindo:
	•	identity: Identidade do cliente (CNPJ/CPF).
	•	sales_organization: Organização de vendas.
	•	payment_method: Método de pagamento.
	•	address_info: Informações do endereço extraídas do MongoDB.
```
---
✅ Pré-requisitos

Antes de executar este projeto, certifique-se de ter:
	1.	Python 3.8+ instalado.
	2.	Dependências listadas no arquivo requirements.txt (se aplicável):
	•	Faker para geração de dados aleatórios.
	3.	Um banco de dados MongoDB configurado com os dados necessários.

---
🚀 Como Executar

	1.	Configurar o MongoDB:
Certifique-se de que seu banco de dados MongoDB contém os dados esperados para o cliente (nome, endereço, identidade, etc.).
	
    2.	Executar a Função:
No terminal, execute o seguinte comando:
from helpers.body_bff_creator import create_bff_body

# Dados de exemplo
identity = "0009319663"
sales_organization = "1625"
payment_method = "boleto"
address_info = {
    "street": "Rua Teste",
    "number": "551",
    "complement": "Apto 101",
    "zip_code": "14095020",
    "city": "Ribeirão Preto",
    "federative_unit": "SP",
    "country": "Brasil",
    "neighborhood": "Centro"
}

payload = create_bff_body(
    identity=identity,
    sales_organization=sales_organization,
    payment_method=payment_method,
    address_info=address_info
)

print(payload)

# Execução Locust

```plaintext
locust -f locustfile.py
locust --headless -f locustfile.py --users 1 --spawn-rate 1
locust --headless -f locustfile.py --tags test1 --users 1 --spawn-rate 1
locust -f ./locustfiles/locustfile.py
locust -f locustfiles/ --users 10 --spawn-rate 1

-u 10: Define o número de usuários simultâneos.
-r 2: Define a taxa de criação de novos usuários (2 usuários por segundo).
--run-time 1m: Define a duração do teste (1 minuto).
```

---
✨ Funcionalidades

	•	Geração Automática de Payloads:
	•	Endereços (billing e delivery) preenchidos automaticamente.
	•	Informações detalhadas de cliente e itens do pedido.
	•	Integração com MongoDB:
	•	Recupera informações de clientes diretamente do banco de dados.
	•	Dados Dinâmicos:
	•	Gera números de pedido únicos e calcula a data de entrega automaticamente.
---
🧰 Exemplo de Uso

Input

Parâmetros fornecidos:
identity = "0009319663"
sales_organization = "1625"
payment_method = "boleto"
address_info = {
    "street": "Rua Teste",
    "number": "551",
    "complement": "Apto 101",
    "zip_code": "14095020",
    "city": "Ribeirão Preto",
    "federative_unit": "SP",
    "country": "Brasil",
    "neighborhood": "Centro"
}

---

🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:
	1.	Faça um fork do repositório.
	2.	Crie um branch para a sua funcionalidade: git checkout -b minha-feature.
	3.	Faça as alterações e envie um pull request.

---

### Próximos Passos:
**a.** Crie um arquivo `requirements.txt` se necessário, para listar as dependências do projeto.  
**b.** Adicione uma seção com testes unitários no `README.md`.