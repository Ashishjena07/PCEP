def sample():
    name = "ASHISH"

    def sample1():
        nonlocal name
        print(name)
        name = "LUCKY"
        print(name)

    sample1()
    print(name)
    
sample()

