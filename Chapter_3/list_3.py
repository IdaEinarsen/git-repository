#3.4 Guest list

guest_list = ['gaben', 'harleen', 'megan']
invite = "You have been invited to a dinner party! "
print(f'Dear, {guest_list[0].title()}! {invite}')
print(f'Dear, {guest_list[1].title()}! {invite}')
print(f'Dear, {guest_list[2].title()}! {invite}')
# I invited 2 acresses and also the co creator of valve corporation.

#3.5 Changing Guest List 
print(f"{guest_list[2].title()} can't make it to the dinner.")
del guest_list[2]
guest_list.append('liza koshy')
guest_list.append('stig larsson')
print(guest_list)
print(f'Dear, {guest_list[0].title()}! {invite}')
print(f'Dear, {guest_list[1].title()}! {invite}')
print(f'Dear, {guest_list[2].title()}! {invite}')
print(f'Dear, {guest_list[3].title()}! {invite}')
# I removed megan from the list and added Liza (a youtuber) and Stig (my grandpa) and sent out new invites

#3.6 More Guests
print("I have found a bigger table and will invite more people!")
guest_list.insert(0, 'carina')
guest_list.insert(3, 'jesus')
guest_list.insert(6, 'tarzan')
print(guest_list)
print(f'Dear, {guest_list[0].title()}! {invite}')
print(f'Dear, {guest_list[1].title()}! {invite}')
print(f'Dear, {guest_list[2].title()}! {invite}')
print(f'Dear, {guest_list[3].title()}! {invite}')
print(f'Dear, {guest_list[4].title()}! {invite}')
print(f'Dear, {guest_list[5].title()}! {invite}')
print(f'Dear, {guest_list[6].title()}! {invite}')
# I added 3 more people to the list by using insert instead of append.  carina(my grandma) and then i couldn't come up with anymore names so jesus and tarzan was the outcome.

#3.7 Shrinking Guest List

print("Someone stole the dinner table so now there isnt enough space for more then two guests")
popped_guests = guest_list.pop()
print(f"{popped_guests.title()}, i'm sorry but you're invitation has been taken back.")
popped_guests = guest_list.pop()
print(f"{popped_guests.title()}, i'm sorry but you're invitation has been taken back.")
popped_guests = guest_list.pop()
print(f"{popped_guests.title()}, i'm sorry but you're invitation has been taken back.")
popped_guests = guest_list.pop()
print(f"{popped_guests.title()}, i'm sorry but you're invitation has been taken back.")
popped_guests = guest_list.pop()
print(f"{popped_guests.title()}, i'm sorry but you're invitation has been taken back.")
print(guest_list)
print(f'Dear, {guest_list[0].title()}! {invite}')
print(f'Dear, {guest_list[1].title()}! {invite}')
del guest_list[0]
del guest_list[0]
print(guest_list)
# I told them that the table have been stolen and that i only have 2 seats. i then used the pop method and popped out five people and sent a message to them telling them there invitation has been taken back.
#i then sent 2 more invites , deleted guests using del and printed guest list



