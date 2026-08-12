from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI(
    title="API de Ejemplo",
    description="API simple para demostración de FastAPI",
    version="1.0.0"
)

@app.get("/", tags=["General"])
def read_root():
    """
    Endpoint raíz que devuelve un mensaje de bienvenida.
    """
    return {"mensaje": "Hola mundo"}

@app.get("/suma", tags=["Operaciones"])
def suma(
    a: int = Query(..., description="Primer número entero"),
    b: int = Query(..., description="Segundo número entero")
):
    """
    Calcula la suma de dos números enteros.
    
    - **a**: Primer operando
    - **b**: Segundo operando
    """
    return {"resultado": a + b, "operacion": f"{a} + {b}"}