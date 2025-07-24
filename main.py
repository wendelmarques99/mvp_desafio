from fastapi import FastAPI
import pandas as pd

planilha = pd.read_excel("./posicao_formatada.xlsx", sheet_name=None)
posicao = planilha["Sheet1"]
dicionario = planilha["Planilha1"]

posicao = posicao.to_dict(orient="records")

dicionario = dict(zip(dicionario["produto"], dicionario["classe"]))

app = FastAPI()

@app.get("/posicao")
def get_posicao():
    return posicao

@app.get("/dicionario")
def get_dicionario():
    return dicionario