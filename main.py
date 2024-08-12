from knight_travails import find_shortest_path

path = find_shortest_path((3,2), (7,7))
if path:
    print(f"=> You made it in {len(path) - 1} moves!  Here's your path:")
    for step in path:
        print(step)