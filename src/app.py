import uvicorn
from src.router import router

create_db()

app = FastAPI()

app.include_router(router.router)


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
