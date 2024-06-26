class Recipe:
    def __init__(self, name, cooking_time,rating):
        self.name = name
        self.cooking_time = cooking_time
        self.rating = rating
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Recipe:{self.name}, cooking time - {self.cooking_time} minutes, {self.rating}"