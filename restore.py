import amino
client=amino.Client
a=input("your email: ")
b=input("your password: ")
try:
    client.restore(email=(a), password=(b))
    print("done")
except:
    print("something went wrong")

