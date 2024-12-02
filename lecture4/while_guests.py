guest_command = input("Who to invite? Type <nobody> to stop.")
guest_list = []

while guest_command != "nobody":
    guest_list.append(guest_command)
    guest_command = input("Who to invite? Type <nobody> to stop.")

print(f"Got it. You invited {len(guest_list)} guests")