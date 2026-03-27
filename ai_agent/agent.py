from pydantic import BaseModel, Field

class UserProfile(BaseModel):
    age: int = Field(description="user's age")
    height: int = Field(description="user's height")