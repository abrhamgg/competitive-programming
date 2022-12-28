import math
"""
Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a × a.

What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.

"""
sizes = input()

sizes = sizes.split(' ')
n = int(sizes[0])
m = int(sizes[1])
a = int(sizes[2])

total = math.ceil(m / a) * math.ceil(n / a)

print(total)
