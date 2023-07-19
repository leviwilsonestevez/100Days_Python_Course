class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("new user has been created !!")

    def follow(self, user) -> None:
        user.followers += 1
        self.following += 1


user_1 = User(user_id="000", username="Angela")
print(user_1)
# not the best alternative in order to create variables. Better use contructor __init__
user_1.id = "001"
print(user_1.id)
user_constructor = User(user_id="001", username="Levis")
print(f"followers : {user_constructor.followers}")
user_1.follow(user_constructor)

print(f"followers user_1 : {user_1.followers}")
print(f"following user_1 : {user_1.following}")
