from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

# Configurações do banco de dados
DB_HOST = 'localhost'
DB_NAME = 'dev-web'
DB_USER = 'admin'
DB_PASSWORD = '12341234'


# Modelo Pydantic para representar um produto
class Product(BaseModel):
    id: int
    name: str
    describe: str
    price: float


# Função para conectar ao banco de dados
def connect_db():
    conn = psycopg2.connect(host=DB_HOST,
                            dbname=DB_NAME,
                            user=DB_USER,
                            password=DB_PASSWORD)
    return conn

# Rota para criar um novo produto
@app.post('/products/')
async def create_product(product: Product):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, describe, price) VALUES (%s, %s, %s)",
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
    cur.execute("UPDATE products SET name = %s, describe = %s, price = %s WHERE id = %s",
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
