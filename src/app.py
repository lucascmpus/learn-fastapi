import uvicorn
from src.routes import routes_product, routes_user

create_db()

app = FastAPI()

app.include_router(routes_product.router, prefix='/product')
app.include_router(routes_user.router, prefis='/user')


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
