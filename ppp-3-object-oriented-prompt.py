# Watto needs a new system for organizing his inventory of podracers.
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"

pod = Podracer(500, 'trashed', 10000)
pod.repair()
print(pod.condition)  # Output: "repaired"


# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
    # Method to boost the speed
    def boost(self):
        self.max_speed *= 2

# Example usage
new_pod = AnakinsPod(2, 'perfect', 15000)
new_pod.boost()
print(new_pod.max_speed)  # Output: 4


# Define another class that inherits Podracer and call this one SebulbasPod.
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
    # Method to trash another podracer's condition
    def flame_jet(self, other):
        other.condition = "trashed"

# Example usage
third_pod = SebulbasPod(550, 'perfect', 13000)
another_pod = Podracer(400, 'perfect', 12000)
third_pod.flame_jet(another_pod)
print(another_pod.condition)  # Output: "trashed"

