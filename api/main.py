from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response
import boto3
import botocore.exceptions

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

# 🔢 Métrica personalizada
usuarios_criados_total = Counter("usuarios_criados_total", "Total de usuários criados")

# 🔗 Conexão com o DynamoDB via LocalStack
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url='http://localstack:4566',
    region_name='us-east-1',
    aws_access_key_id='test',
    aws_secret_access_key='test'
)

# 🧱 Criação da tabela (com verificação)
def create_table():
    try:
        existing_tables = dynamodb.meta.client.list_tables()['TableNames']
        if 'Users' not in existing_tables:
            dynamodb.create_table(
                TableName='Users',
                KeySchema=[{'AttributeName': 'email', 'KeyType': 'HASH'}],
                AttributeDefinitions=[{'AttributeName': 'email', 'AttributeType': 'S'}],
                ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
            )
    except botocore.exceptions.ClientError as e:
        print(f"Erro ao criar tabela: {e}")

create_table()

# 🚀 Endpoint para criar usuário
@app.post("/users")
def create_user(user: User):
    table = dynamodb.Table('Users')
    table.put_item(Item=user.dict())
    usuarios_criados_total.inc()  # Incrementa a métrica
    return {"message": f"Usuário {user.name} criado com sucesso!"}

# 📊 Endpoint para Prometheus coletar métricas
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")