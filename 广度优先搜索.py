from collections import deque

graphs = {}
graphs["you"] = ["alice", "bob", "claire"]
graphs["bob"] = ["anuj", "peggy"]
graphs["alice"] = ["peggy"]
graphs["claire"] = ["thom", "jonny"]
graphs["anuj"] = []
graphs["peggy"] = []
graphs["thom"] = []
graphs["jonny"] = []

def person_seller(name):
    return name[-1] == "m"
def check_banana(name):
    search_queue = deque()
    search_queue += graphs[name]
    searched =[]
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_seller(person):
                print(f"{person},you are a trader")
                return True
            else:
                search_queue += graphs[person]
                searched.append(person)
    return False
print(check_banana("you"))