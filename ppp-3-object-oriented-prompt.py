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

pod1 = Podracer(500, 'perfect', 10000)
print(pod1.max_speed, pod1.condition, pod1.price)  # Output: 500 perfect 10000


# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)

  def boost(self):
    self.max_speed *= 2

anakin_pod = AnakinsPod(600, 'perfect', 15000)
print(anakin_pod.max_speed, anakin_pod.condition, anakin_pod.price)  # Output: 600 perfect 15000

anakin_pod.boost()
print(anakin_pod.max_speed)  # Output: 1200

# Define another class that inherits Podracer and call this one SebulbasPod.
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
#   def __init__(self, max_speed, condition, price):
#     super.init(max_speed, condition, price):

  def flame_jet(self,other):
    other.condition = "trashed"

sebulba_pod = SebulbasPod(550, 'perfect', 13000)
print(sebulba_pod.max_speed, sebulba_pod.condition, sebulba_pod.price)  # Output: 550 perfect 13000

sebulba_pod.flame_jet(pod1)
print(pod1.condition)  # Output: trashed


