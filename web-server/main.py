import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
  return [1, 2, 3, 4, 5]

@app.get("/html", response_class=HTMLResponse)
def get_list():
  return """
    <h1>Ejemplo con HTML</h1>
    <p>Un párrafo</p>
  """

@app.get("/perfil")
def get_list():
  return {"name" : "Platzi"}

def run():
  store.get_categories()

if __name__ == "__main__":
  run()