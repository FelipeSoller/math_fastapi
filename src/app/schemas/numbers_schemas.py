from pydantic import BaseModel

class NumbersRequestSchema(BaseModel):
    numbers: list[int]

class SumResponseSchema(BaseModel):
    sum: int

class AverageResponseSchema(BaseModel):
    average: float