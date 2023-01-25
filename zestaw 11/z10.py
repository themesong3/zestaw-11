class Phone():
    
    def __init__(self, make, model):
        
        self.phone_number = "000000000"
        self.is_on = False
        self.make = make
        self.model = model
        
    def change_phone_number(self, new_num):
        self.phone_number = new_num
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def make_call(self, number_to_call):
        print(f"Calling number {number_to_call}\n")
        
    def play_game(self, game_to_play):
        print(f"Now playing {game_to_play}\n")
    
    def __str__(self):
        text = "Phone information \n==================\n"
        text += f"Make: {self.make}     Model: {self.model}     Phone Number: {self.phone_number}"
        return text
        
        
p1 = Phone("Apple", "iphone6")
print(p1)