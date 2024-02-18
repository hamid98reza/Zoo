class Animal:
    def __init__(self,color:str, sound:str):
        self.color = color
        self.sound = sound

    def fly(self,type):
        print(f"a {self.color} {type} is {self.sound} and FLYING!!")

    def run(self,type):
        print(f"a {self.color} {type} is {self.sound} and RUNNING!!")