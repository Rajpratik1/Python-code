s=input("Enter any word:")
def shut_down(s):
    if s=="yes":
        return "Shutting Down"
    elif s=="no":
        return "Shutdown aborted"
    else:
        return "Sorry"
print(shut_down(s))