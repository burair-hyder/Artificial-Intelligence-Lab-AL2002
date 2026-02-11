# question 06
class Environment:
    def __init__(self):
        self.grid = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'j']
        ]
        self.room_status = {
            'a': 'safe', 'b': 'safe', 'c': 'fire',
            'd': 'safe', 'e': 'fire', 'f': 'safe',
            'g': 'safe', 'h': 'safe', 'j': 'fire'
        }

    def display(self):
        for row in self.grid:
            for room in row:
                if self.room_status[room] == 'fire':
                    print("F", end=" ")
                else:
                    print("S", end=" ")
            print()
        print("-" * 15)

    def has_fire(self, room):
        return self.room_status[room] == 'fire'

    def extinguish_fire(self, room):
        if self.has_fire(room):
            self.room_status[room] = 'safe'


class Robot:
    def __init__(self, environment, path):
        self.env = environment
        self.path = path
        self.position = path[0]

    def move_and_extinguish(self):
        for room in self.path:
            self.position = room
            print("Robot is at room '" + room + "'")
            if self.env.has_fire(room):
                print("Fire detected in room '" + room + "'! Extinguishing...")
                self.env.extinguish_fire(room)
            else:
                print("Room '" + room + "' is safe. Moving on.")
            self.env.display()


env = Environment()
robot_path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
robot = Robot(env, robot_path)

robot.move_and_extinguish()

print("All rooms have been checked and fires extinguished!")
env.display()
