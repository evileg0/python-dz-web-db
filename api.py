from fastapi  import FastAPI
import uvicorn
from db_actions import *

app = FastAPI()

@app.get("/test")
async def test():
    return "test"


@app.get("/list")
async def list():
    result = get_t_list()
    return result


uvicorn.run(app, host="0.0.0.0", port=8080)