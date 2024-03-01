def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]
    """
    badges = []
    for name in names:
        badge = f"Hello, my name is {name}."
        badges.append(badge)
    return badges
    
print(batch_badge_creator(["Arel", "Carol"]))
    """

def assign_rooms(names):
    rooms = [1, 2, 3, 4, 5, 6, 7, 8]
    return [f"Hello, {name}! You'll be assigned to room {room}!" for name, room in zip(names, rooms)]
"""
    rooms = [1, 2, 3, 4, 5, 6, 7, 8]
    assignments = []
    for name, room in zip(names, rooms):
            assignment = f"Hello, {name}! You'll be assigned to room {room}!"
            assignments.append(assignment)
    return assignments
    

print(assign_rooms(["Arel", "Carol"]))
"""


def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    
    assignments = assign_rooms(names)
    for assignment in assignments:
        print(assignment)
