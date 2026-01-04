from pydantic import BaseModel
class LogQuery(BaseModel):
question: str
logs: str
