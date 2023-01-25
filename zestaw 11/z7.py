class Student():
    
    last_album_num = 99999
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
        self.id = self.last_album_num + 1
        self.university = "UEK Kraków"
        
    def __str__(self):
        return f"id {self.id} {self.name} {self.surname}"
        
s1 = Student("Adam", "Kowalski")
Student.last_album_num += 1
s2 = Student("Adam", "Smith")

print(s2)