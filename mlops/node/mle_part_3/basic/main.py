from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Query Parameter
@app.get("/items")
def read_item(skip: int=0, limit: int = 10):
    return fake_items_db[skip:skip+limit]

# Muilti Parameter
from typing import Union

@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: str, q: Union[str, None], short: bool=False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item