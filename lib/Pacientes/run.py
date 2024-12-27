from fastapi import FastAPI, HTTPException

app = FastAPI()

app.title = "Proyecto Final Prt. 2"
app.version = "1.1.2"

@app.get("/", tags=["Bienvenido"])
def Bienvenida():
    return "Bienvenido My Lord"


