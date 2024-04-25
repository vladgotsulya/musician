class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

class Musician(Person):
    def __init__(self, name, age, instrument):
        super().__init__(name, age)
        self.instrument = instrument
    
    def play_music(self):
        print(f"{self.name} играет {self.instrument}.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self):
        print(f"{self.name} изучает.")

class Guitarist(Musician):
    def __init__(self, name, age, instrument, guitar_type):
        super().__init__(name, age, instrument)
        self.guitar_type = guitar_type
    
    def play_guitar(self):
        print(f"{self.name} играет {self.guitar_type} гитара.")

class PrintPublication:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author

class Newspaper(PrintPublication):
    def __init__(self, title, author, date_published):
        super().__init__(title, author)
        self.date_published = date_published
    
    def publish(self):
        print(f"{self.title} был опубликован на {self.date_published}.")

class Book(PrintPublication):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre
    
    def read(self):
        print(f"{self.title} это {self.genre} книга.")

class Periodical(PrintPublication):
    def __init__(self, title, author, frequency):
        super().__init__(title, author)
        self.frequency = frequency
    
    def publish(self):
        print(f"{self.title} публикуется {self.frequency}.")