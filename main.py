import json
from http.client import HTTPException

from fastapi import FastAPI

from data import get_producao_data, get_comercio_data, get_processa_data, get_importacao_data, get_exportacao_data

app = FastAPI()


@app.get("/api/producao/{year}")
def producao(year: str):

    data = get_producao_data(year)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found or table does not exist")
    return json.loads(data)


@app.get("/api/comercio/{year}")
def comercio(year: str):

    data = get_comercio_data(year)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found or table does not exist")
    return json.loads(data)


@app.get("/api/processa/{_type}/{year}")
def processa(_type: str, year: str):

    data = get_processa_data(_type, year)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found or table does not exist")
    return json.loads(data)


@app.get("/api/importacao/{_type}/{year}")
def importacao(_type: str, year: str):

    data = get_importacao_data(_type, year,)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found or table does not exist")
    return json.loads(data)


@app.get("/api/exportacao/{_type}/{year}")
def exportacao(_type: str, year: str):

    data = get_exportacao_data(_type, year)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found or table does not exist")
    return json.loads(data)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="info")
