from fastapi import FastAPI

app = FastAPI()

# base route
@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/bot/{difficulty}/get_move")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}