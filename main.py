from fastapi import FastApi

app = FasrAPI()

@app.get("/")
def read_root():
	return {"message": "Hello UFV from FastAPI"}

@app.get("/items/{id}")
def get_item(id: int):
	return {"id" : id, "name": "Laptop"}
