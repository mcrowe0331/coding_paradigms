# Functional Prompt (Keep variables immutable, only pure functions)
def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
            return sorted(arr)






#Watta needs a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
# Object Oriented Prompt
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
  # Define a repair() method that will update the condition of the podracer to "repaired".      
        def repair(self):
            self.condition = "repaired"
            
# Define a new class, AnakinsPod that inherits the Podracer, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
        
    def boost(self):
        self.max_speed *= 2
        
# Define another class that inherits Podracer and call thisone SebulbasPod.
# Class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
