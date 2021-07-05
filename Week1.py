# week-1-coursework-wmusi-spec
class Teams:
    def __init__(self,members):
            self.__myTeam=members
    def __len__(self):
        return len(self.__myTeam)
    def __contains__(self, member):
        #print("in is from here only")
        return member in self.__myTeam
    def __iter__(self):
        #print("Iterator")
        return iter(self.__myTeam)
def main():
    classmates=Teams(['John','Steve','Tim'])
    print('Tim' in classmates)
    print('Sam' in classmates)
    iterator=iter(classmates)#we get iterable object reference
    for member in iterator:
        print(member,end=" ")
main()

