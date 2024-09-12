from typing import Dict
from fastapi import APIRouter

from src.app.schemas.numbers_schemas import AverageResponseSchema, NumbersRequestSchema, SumResponseSchema
from src.app.services.math_services import NumbersService

class NumbersController:
  def __init__(self):
    self.router = APIRouter()
    self.service = NumbersService()

    self.router.add_api_route(
      path="/sum",
      endpoint=self.sum,
      methods=["POST"],
      response_model=SumResponseSchema
    )

    self.router.add_api_route(
      path="/average",
      endpoint=self.average,
      methods=["POST"],
      response_model=AverageResponseSchema
    )

  def sum(self, params: NumbersRequestSchema) -> Dict[str, int]:
    result = self.service.sum(params.numbers)
    return {"sum": result}

  def average(self, params: NumbersRequestSchema) -> Dict[str, float]:
    result = self.service.average(params.numbers)
    return {"average": result}
