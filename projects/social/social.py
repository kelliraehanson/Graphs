import random #  To shuffle the list, `import random` to get shuffle.


class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self): # Returns the user object by name
        return self.name # Returns the user object by name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {} # Dictionary of users
        self.friendships = {} # Dictionary of friendships
         # User are nodes and frienships are edges

        # This is a Social Network:
        # {1: {8, 10, 5}}  this means that user 1 (vertices) is friends with user 8, 10 and 5.

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name): # Adding user
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set() # Friendships initialized to an empty set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        # number of users: numUsers and average number of friends: avgFrienships

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        # This means if you have 5 users AT MOST you can only have 4 friends.
        """
        # Reset graph
        self.lastID = 0 #lastId
        self.users = {} # Resetting our graph
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users 
        # Use a simple loop to add users
        for i in range(0, numUsers):
            self.addUser(f"User {i + 1}") # Use the addUser method from above (it takes in a name) won't be definded if you don't use self.addUser instead of just addUser
            # ^ Time Complexity: 0(n)
            # ^ Space Complexity: 0(n)
            # Add numUsers

        # Create friendships

        # avgFriendships = totalFriendships divided by numUsers
        # totalFriendships = avgFriendships * numUsers
        possible_friendships = [] # Empty array for 20 possible random friendships 
        # import math
        # math.floor(random.random() * 2)
        # ^ this will either give you 0 or 1 (basically just like a coin flip)
        # Remember if you flip a coin 100 times you won't get exactly 50 heads and 50 tails.
        # Some users might have more friends and some will have less friends. Not predictible. 

        for userID in self.users: # self.users is a dictionary that will give you all the keys
            for friendID in range(userID + 1, self.lastID + 1):
                possible_friendships.append((userID, friendID))
        # ^ Time Complexity: 0(n ^ 2)
        # ^ Space Complexity: 0(n ^ 2)

                print("\n")
                print(f"Possible Friendships:{possible_friendships}")
                print("\n")
        
        random.shuffle(possible_friendships) # Shuffle to create a list with all possible friendship combinations.
        # ^ Time Complexity of shuffle: 0(numUsers ^ 2) or 0(n ^ 2)
        # ^ Space Complexity of shuffle: 0(1) because you aren't using any extra space
        
        # print("\n")
        # print(possible_friendships)
        # print("\n")

        for friendship_index in range(avgFriendships * numUsers // 2): # Divided by two for two friendships. Double slash // so you don't get a float. This is the same as doing math.floor divided by 2
            friendship = possible_friendships[friendship_index]
            self.addFriendship(friendship[0], friendship[1])
            # ^ Time Complexity: 0(avgFriendships * numUsers // 2)
            # ^ Space Complexity: 0(avgFriendships * numUsers // 2)

     # Time Complexity of populateGraph: 0(n ^ 2) because it is the largest of them all
     # Space Complexity of populateGraph: 0(n ^ 2) same because it is the largest of them all



    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = Queue() # An empty Queue
        queue.enqueue([userID]) # Add userID
        
        while queue.size() > 0: # While nothing in queue
            path = queue.dequeue() # Dequeue first path
            node = path[-1] # While node is last in path
            
            if node not in visited: # If node not visited
                visited[node] = path
                
                for neighbor in self.friendships[node]: # Go through neighbor
                    new_path = path.copy()
                    new_path.append(neighbor) # Add neighbor to new_path
                    
                    queue.enqueue(new_path) # enqueue new_path
                   
        return visited

    
class Queue(): # imported from util.py
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack(): # imported from util.py
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2) # Here is shows you are doing this with 10 users
    print("\n")
    print(f"These are the users: {sg.users}") # sg stands for social graph
    print("\n")
    print(f"These are Social Graph Friendships: {sg.friendships}") # sg stands for social graph
    print("\n")
    connections = sg.getAllSocialPaths(1)
    print(f"These are all Social Paths (connections): {connections}")
    print("\n")
