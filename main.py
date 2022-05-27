from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score



    def change_name(self, change_name):
        self.change_name = change_name
        print(f'The student new name is: {self.change_name}')
        return self.change_name

    def change_age(self, change_age):
        self.change_age = change_age
        print(f'The student new age is: {self.change_age}')
        return self.change_age
    
    def add_track(self, add_track):
        self.add_track = add_track
        print(f'The student new track is: {self.add_track}')
        return self.add_track
    
    def get_score(self, score):
        self.score = score
        print(f'The student new score is : {self.score}')
        return self.get_score

# call class
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(27.50)
