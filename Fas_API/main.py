from typing import Union # Dùng để khai báo biến có thể có nhiều kiểu dữ liệu

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# {item_id} là một path parameter
#
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# http://localhost:8000/items/10
# http://localhost:8000/items/10?q=abc (?: Bắt đầu các tham số truy vấn)
# http://127.0.0.1:8000/docs