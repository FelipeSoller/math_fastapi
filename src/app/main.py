from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.app.controllers.api.v1.numbers_controller import NumbersController

app = FastAPI()
app.include_router(
  router=NumbersController().router,
  prefix="/api/v1/numbers"
)
    
@app.exception_handler(ValueError)
def value_error_exception_handler(_: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"message": str(exc)})

@app.exception_handler(Exception)
def generic_exception_handler(_: Request, exc: Exception):
    print(exc)
    return JSONResponse(status_code=500, content={"message": "Internal server error"})