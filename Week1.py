# week-1-coursework-wmusi-spec
class Teams:
    def __init__(self,members):
        self.__myTeam=members
    #len interface implementation
    def __len__(self):
        return len(self.__myTeam)
    # contain interface inplemention
    def __contains__(self, member):
        #print("in is from here only")
        return member.upper() in (iu.upper() for iu in self.__myTeam) #return a boolean value
    #iter interface implementation
    def __iter__(self):
        #print("Iterator")
        return iter(self.__myTeam)
    #string interface implementation
    def __str__ (self):
        return '\n'.join(self.__myTeam) #generate a joined list of membersin string format
def main():
    classmates=Teams(['John','Steve','Tim'])
    print('Tim' in classmates)
    print('Sam' in classmates)
    iterator=iter(classmates)#we get iterable object reference
    for member in iterator:
        print(member)
    print("List of members in the team using print")
    print(classmates)
main()

