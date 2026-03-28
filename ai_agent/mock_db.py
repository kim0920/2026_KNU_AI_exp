from model import RestaurantProfile

_store: dict = {}

def add_store(name:str, new_profile:RestaurantProfile):
    _store[name] = new_profile


def get_store():
    return _store