import os
from subprocess import call

path = os.getcwd()

inputs = sorted([path + "/input/" + file for file in os.listdir("input")])
solutions = sorted([path + "/solution/" +
                    file for file in os.listdir("solution") if "x" not in file])

print("======================================")
for day, (solution, input) in enumerate(zip(solutions, inputs)):
    print("Day {}".format(day + 1))
    call(["/usr/bin/env", "python3", solution, input])
    if day != len(solutions):
        print("--------------------------------------")
print("======================================")
