#advent of code 2021 day2  part1  Johan g
import os
path = "C:\\Users\jocke\OneDrive\Dokument\Knacka_kod\Phyton\Datateknik\\advent_of_code\\advent-of-code-2021\python\johan_g\day2\commands.txt"

try:
    commands = []
    with open(path, "r") as file:
        for line in file:
            commands.append(line.strip())
except IOError as io:
    print(f"Error: {io}")


horzP = 0
depth = 0
for command in commands:
  direction = int(command[(len(command)-1)])

  if "up" in command:
      depth -= direction
  elif "down" in command:
      depth += direction
  elif "forward" in command:
      horzP += direction        


print(f"Hirozontal position: {horzP}  \nDepth:  {depth}")
print(f"Multiplied:  {depth*horzP}")