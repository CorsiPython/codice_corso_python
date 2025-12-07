from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Mount the `static` directory at /static
app.mount("/static", StaticFiles(directory="static"), name="static")


class Prodotto(BaseModel):
    nome: str
    prezzo: float
    disponibile: bool = True


prodotti: List[Prodotto] = []


@app.get("/prodotti", response_model=List[Prodotto])
def lista_prodotti(categoria: Optional[str] = None, limite: int = 10):
    return prodotti[:limite]


@app.post("/prodotti", response_model=Prodotto, status_code=201)
def crea_prodotto(prodotto: Prodotto):
    prodotti.append(prodotto)
    return prodotto


@app.get("/")
def root():
    # Serve the static SPA entrypoint
    return FileResponse("static/index.html")
