class BookStore:
    def __init__(self, title,author_name):
        self.title = title
        self.author_name = author_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"{self.title} - {self.author_name}"
