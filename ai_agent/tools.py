from langchain_core.tools import tool
from model import RestaurantProfile
from mock_db import add_store, get_store

@tool
def save_restaurant(
    name: str,
    ratings: list,
    #ratings: list,
    pos: list,
    advice: list
)->None:
    '''음식점 정보를 저장하고 리뷰 리스트와 리뷰 평점의 평균, 모델이 판단한 긍정 점수의 평균과, 오차를 구해 저장합니다.
        Args:
            name: name of restaurant
            ratings: 음식점이 받은 리뷰 점수를 저장한 리스트. '점수'(int)으로 구성
            pos: 각 리뷰에 매겨진 긍정 점수
            advice: 리뷰별 조언

        Returns:
            None

        Note:
            "음식점이 받은 리뷰들을 저장한 튜플 리스트, ('점수'(int), '리뷰 내용'(str))으로 구성"
            튜플로 저장하니 너무 길어 오류 발생, 임시로 리뷰 점수만 저장하도록 변경
            
    '''
    
    # sum_val = 0
    # for i in ratings:
    #     sum_val+=int(ratings[i][0])

    #리뷰 리스트 생성
    #review = [ ratings[i][1] for i in range(len(ratings))  ]

    #리뷰 평점 리스트 생성, 오류 방지 위해 형변환
    #review_score = [ int(ratings[i][0]) for i in range(len(ratings))  ]

    #평점의 평균 계산
    #rating_avg = sum_val/len(ratings)

    #리뷰 전문을 저장하려다보니 오류가 발생, 리뷰 점수만 저장하는 방식으로 변경
    review_score = ratings

    rating_avg = sum(review_score)/len(ratings)

    #리뷰들의 긍정 점수를 나눠 평균 긍정점수 계산
    pos_score = sum(pos)/len(pos)

    score_error = abs(rating_avg-pos_score*5)

    profile = RestaurantProfile(
        saved_average_rating_score= rating_avg,
        saved_positivity_score= pos_score,
       # saved_reviews=review,
        saved_reviews_score=review_score,
        saved_score_error= score_error,
        saved_advice = advice
    )

    add_store(name, profile)


@tool
def get_rating_score(res_name:str)->tuple:
    '''리뷰 평점의 평균과 모델이 판단한 긍정 점수, 오차를 반환합니다.
        Args:
            res_name: name of restaurant
        Returns:
            rating_avg:리뷰 평점의 평균
            pos_score:긍정 점수의 평균
            score_error:리뷰와 긍정 점수간의 오차
        Raises:
            ValueError: 음식점에 대한 정보가 저장되지 않았을 때 발생
    '''

    store = get_store()

    rating_avg = store[res_name].saved_average_rating_score

    if not rating_avg:
        raise ValueError("저장된 값을 찾을 수 없습니다.")
    
    pos_score = store[res_name].saved_positivity_score

    score_error = store[res_name].saved_score_error

    return rating_avg, pos_score, score_error



@tool
def get_advice_inreview(res_name:str)->list:
    '''"res_name"음식점에 대한 리뷰 속 조언들을 list로 반환합니다.
        Args:
            res_name: name of restaurant
        Returns:
            advice: list of advice in the reviews for "res_name"
    '''

    store = get_store()
    
    return store[res_name].saved_advice