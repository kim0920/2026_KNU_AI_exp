from pydantic import BaseModel, Field

class RestaurantProfile(BaseModel):
    saved_average_rating_score: float = Field(description="평점 평균")
    saved_positivity_score: float = Field(description="긍정 점수")
    #saved_reviews: list = Field(description="리뷰들")
    saved_reviews_score: list = Field(description="리뷰의 평점")
    saved_score_error: float = Field(description="평점과 리뷰의 오차")
    saved_advice:list = Field(description="리뷰 속 조언들")
