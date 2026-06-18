class User:

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username


class Message:

    message_counter = 1

    def __init__(self, sender, content):

        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter+=1

    def __str__(self):

        return f"({self.id}) {self.sender.username}: {self.content}" 



class ChatRoom:

    def __init__(self):

        self.users =[]
        self.messages =[]

    def join(self, user):

        if user not in self.users:

            self.users.append(user)
            print(f"{user.username} joined the chatroom")

        else:
            print(f"{user.username} is already in the chatroom")


    def broadcast(self, sender, content):

        if sender in self.users:

            message = Message(sender, content)

            self.messages.append(message)

            print(message)

        else:
            print("You cannot send message because you have not joined the chatroom.")


    def leave(self, user):

        if user in self.users:

            self.users.remove(user)
            print(f"{user.username} left the Chatroom")

        else:
            print("User not found")


    def show_chat_history(self):

        print("Chat History:")
        for msg in self.messages:
            print(msg)

    
    def show_total_users(self):

        print(len(self.users))


    def show_active_users(self):

        for user in self.users:
            print(f"Active member:{user}")




room = ChatRoom()

u1 = User("Sarthak")
u2 = User("Ritika")
u3 = User("Krishna")

room.join(u1)
room.join(u2)

room.broadcast(u1, "Hello")
room.broadcast(u2, "Hii")

room.join(u3)

room.broadcast(u3, "Hey, What's up guys")

room.show_total_users()

room.show_chat_history()

room.leave(u1)

print(room.users)

room.show_active_users()