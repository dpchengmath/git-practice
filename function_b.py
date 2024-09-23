# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    user_sum = 0
    
    while True:
        user_input = input()
        user_sum += user_input
        if user_input == 0 or user_sum >= 1000:
            return user_sum


if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
