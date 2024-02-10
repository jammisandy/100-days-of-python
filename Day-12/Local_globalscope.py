# x = 5

# def func():
#     x=10
#     print(f"Value of x is {x}")

# func()

# print(f"Value of x is {x}")

#########################################
#global and local scope
player_health = 10 

def func():
    player_lives=2
    print(player_lives)
    print(player_health)

func()
print(player_health)