import math
import re
import sys
import os

class Vec3:
    def __init__(self, point_string=None, x=0, y=0, z=0):
        if point_string:
            match = re.search(r'\((-?[0-9]+), (-?[0-9]+), (-?[0-9]+)\)', point_string)
            self.x = int(match.group(1))
            self.y = int(match.group(2))
            self.z = int(match.group(3))
        else:
            self.x = x
            self.y = y
            self.z = z

    def distance_from(self, point):
        return math.sqrt(math.pow(point.x - self.x, 2) +
               math.pow(point.y - self.y, 2) +
               math.pow(point.z - self.z, 2) * 1.0)

    def __eq__(self, point):
        if isinstance(point, Vec3):
            return ((self.x == point.x) and (self.y == point.y) and (self.z == point.z))
        else:
            return False

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__repr__())


with open(os.path.join("spawn_lists", "spawnlist_nocollapse.txt")) as file:
    spawns = file.readlines()
    spawns = set([Vec3(point_string=spawn.strip()) for spawn in spawns])

# EDIT THESE
x = -881
y = 4600
z = -1700
# ----------

# Take the output and search for them in the Angle Warp SRM
# tab of the OoT SRM / GIM Tables Google spreadsheet
# https://docs.google.com/spreadsheets/d/1SLJzamokLb7wDOaJh5x8DsxmMBy9oIYawyDN3dAWppw/edit#gid=125184608

spawn_point = Vec3(x=x, y=y, z=z)

distances = []
for spawn in spawns:
    distances.append({
        'spawn': spawn,
        'distance': spawn_point.distance_from(spawn)
    })
distances = sorted(distances, key=lambda distance: distance['distance'], reverse=True) 

for distance in distances:
    print(f"{distance['spawn']} is {distance['distance']} away")