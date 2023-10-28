import uvicorn
from app import get_app

app = get_app()

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)