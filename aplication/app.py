from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2

app = FastAPI()

# Configurações do banco de dados
# Deixar ativo quando for executar localmente
DB_HOST = 'localhost'
DB_NAME = 'dev-web'
DB_USER = 'admin'
DB_PASSWORD = '12341234'


# Modelo Pydantic para representar um produto
class Product(BaseModel):
    name: str
    describe: str
    price: str


# Função para conectar ao banco de dados
# Ativar para dockerizar
# DB_HOST = "meu-postgresdb"  # Nome do contêiner do PostgreSQL
DB_PORT = "5432"  # Porta padrão do PostgreSQL


def connect_db():
    conn = psycopg2.connect(host=DB_HOST,
                            port=DB_PORT,
                            dbname=DB_NAME,
                            user=DB_USER,
                            password=DB_PASSWORD)
    return conn


# Adicionando middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Rota para criar um novo produto
@app.post('/products/')
async def create_product(product: Product):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""INSERT INTO products (name, describe, price)
                VALUES (%s, %s, %s)""",
                (product.name, product.describe, product.price))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Product created successfully"}


# Rota para listar todos os produtos
@app.get('/products/')
async def get_products():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    products = [{'id': row[0], 'name': row[1],
                 'describe': row[2], 'price': row[3]} for row in rows]
    return products


# Rota para atualizar um produto
@app.put('/products/{product_id}')
async def update_product(product_id: int, product: Product):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""UPDATE products SET name = %s,
                describe = %s,
                price = %s
                WHERE id = %s""",
                (product.name, product.describe, product.price, product_id))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Product updated successfully"}


# Rota para excluir um produto
@app.delete('/products/{product_id}')
async def delete_product(product_id: int):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Product deleted successfully"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)
