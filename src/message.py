from pydantic import BaseModel


class Message(BaseModel):
    id: int | None
    text: str 
    userId: str
   