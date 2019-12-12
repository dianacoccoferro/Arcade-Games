
# room list
room_list = []
room = ["You are in Bedroom 2. There is a passage to the East.", 3, 1, None, None]
room_list.append(room)
room = ["You are in the South Hall. There is a passage to the East and North.", 4, 2, None, 0]
room_list.append(room)
room = ["You are in the Dinning Room. There is a passage to the North and West.", 5, None, None, 1]
room_list.append(room)
room = ["You are in Bedroom 1. There is a passage to the East and South.", None, 4, 0, None]
room_list.append(room)
room = ["You are in the North Hall. There is a passage to the North, East, South and West.", 6, 5, 1, 3]
room_list.append(room)
room = ["You are in the Kitchen. There is a passage to the South and West.", None, None, 2, 4]
room_list.append(room)
room = ["You are in the Balcony. There is a passage to the South.", None, None, None, 4]
room_list.append(room)

# current room
current_room = room_list[0]
print(current_room[0])
done = False


