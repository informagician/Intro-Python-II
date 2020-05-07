# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, loc):
        self.loc = loc
        self.items = []

    def inventory(self):
        if len(self.items) == 0:
            print('You are not holding anything')
        else:
            print("You are holding:")
            for i in self.items:
                print(i)
    
    def take(self,item):
        self.items.append(item)
        print(f'You picked up a {item}')

    def drop(self,item):
        self.items.remove(item)