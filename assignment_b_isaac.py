# UTORid: abdull68
import sys

class SocialNetwork(object):

##    _graph = {}
    
    def __init__(self):
        self._graph = {}   


    def load_from_file(self, f) -> None:
        '''
        Reads a file and populates self._graph with contents
        '''

        file = open(f, "r")
        
        for line in file:
            other_list = []
            school_list = []
            e_mail_list = []
            other = ''

            lineLen = len(line)
            
            index_1 = line.index('<') + 1
            index_2 = line.index('>')

            e_mail = line[index_1:index_2]
            name = line[0:index_1 - 1]
            other = name + line[index_2 + 1:] 
            
            index_1 = line.index('(') + 1
            index_2 = line.index(')')
            
            other_list.append(name) 
            e_mail_list.append(line[index_2 + 2:-1])
            print(e_mail_list)
            other_list.append(line[index_1:index_2].split(','))
            other_list.append(e_mail_list[0].split(','))
            self._graph[e_mail] = other_list

        # Makes friendship mutual     
        for person in self._graph:
            pFriends = self._graph[person][2]
            if len(pFriends) > 1:
                for friend in pFriends:
                    if not self._graph[friend][2] == '':
                        fFriends = self._graph[friend][2]
                        if person not in fFriends:
                            if fFriends == ['']:
                                self._graph[friend][2] = [person]
                            else:
                                self._graph[friend][2].append(person)

        print(self._graph.keys())
        for key in self._graph.keys():
            print(self._graph[key])
                
                

    def friends(self, email:'str') -> str:
        '''
        List all friends of person x (where x is an e-mail address). Output this list on its own line, separated by spaces.
        The list should be sorted in alphabetical order. Do not add any other output. For example,
        >>> friends harold@alias.me
        
        >>> friends hl@imaeatchu.com
        Annie Dr. Evil
        >>> friends andy@toronto.edu
        Brian Law
        '''
        friends = []

        if self._graph[email][2][0] == '':
            return ''
        else:
            if not self._graph[email][2][0] == '':
                emails = self._graph[email][2]
                
                for item in emails:
                    friends.append(self._graph[item][0])
                    friends.sort()
                return (' '.join(friends))
        

    def degree_between(self, email1:'str', email2:'str') -> int:
        '''
        print the degree of separation between person x and person y (where people are specified by e-mail address).
        In the network graph, the degree of separation between x and y corresponds to the number of edges on the shortest path between x and y.
        If there is no path between x and y, then the degree of separation is undefined. Use Python's infinity value float("inf") to represent this value.
        Notice that a person has 0 degrees of separation with him/herself. Output an integer on its own line. Do not add any other output. For example,
        >>> degree liudavid@cdf.toronto.edu henry@hyde.net
        2
        >>> degree harold@alias.me andy@toronto.edu
        inf
        >>> degree harold@alias.me harold@alias.me
        0
        '''

        degree = 1
        nextDepth = []
        oldDepth = []
        if email1 == email2:
            return 0
        elif self._graph[email1][2][0] == '':
            return 'inf'
        else:
            curDepth = self._graph[email1][2]
            while nextDepth != [] or curDepth != []: #parses emails in graph
                for friend in curDepth: #parse current depth
                    if friend == email2:
                        return degree
                    else:
                        for efriend in self._graph[friend][2]: # parse through the emails of friends
                            if not efriend in oldDepth:
                                nextDepth.append(efriend)
                    oldDepth.append(friend) #avoid circles & going backwards
                #curdepth parse complete, go to next depth
                curDepth = nextDepth
                nextDepth = []
                degree += 1
            return -1


    def people_with_degree(self, email1:'str', degree:'int') -> 'list':
        '''
        list all people separated from person x by exactly d degrees of separation (where x is an e-mail address).
        Output this list on its own line, separated by spaces. The list should be sorted in alphabetical order (using the standard string ordering).
        Do not add any other output. For example,
        >>> degrees harold@alias.me 100
        
        >>> degrees annie@mgo.org 0
        Annie
        >>> degrees annie@mgo.org 1
        Hannibal Lecter Henry Jekyll
        >>> degrees annie@mgo.org 2
        Anya Tafliovich Dr. Evil
        '''

        nextDepth = []
        oldDepth = []
        nameList = []
        tempDegree = 1
        print(degree)
        print(email1)
        if self._graph[email1][2][0] == '':
            return ''
        elif int(degree) == 0:
            return self._graph[email1][0]
        else:
            curDepth = self._graph[email1][2]
            while tempDegree < int(degree): #parse graph
                for friend in curDepth: #parse current depth
                    oldDepth.append(friend) #avoid circles & going backwards
                    # traverse through the friendlist of the given person's friends
                    for efriend in self._graph[friend][2]: 
                        if not efriend in oldDepth:
                            # Make sure efriend email does not equal email1 email
                            if not efriend == email1: 
                                nextDepth.append(efriend) #add to next depth
                #curdepth parse complete, go to next depth
                curDepth = nextDepth
                nextDepth = []
                tempDegree += 1
                # curDepth is populated with emails, need to populate it with emails
            for femail in curDepth:
                nameList.append(self._graph[femail][0])
            return (' '.join(set(nameList)))

    def mutual_friends(self, email1:'str', email2:'str'):
        '''
        list mutual friends of x and y, i.e. people who are friends with both x and y
        (where people are specified by e-mail address).
        Output this list on its own line, separated by spaces. The list should be
        sorted in alphabetical order. Do not add any other output. For example,
        >>> mutual harold@alias.me andy@toronto.edu
        
        >>> mutual dr@evil.net annie@mgo.org
        Hannibal Lecter Henry Jekyll 
        >>> mutual lungj@cdf.toronto.edu sengels@cdf.toronto.edu
        David Liu
        '''

        mutual = []
        
        list1 = self.friends(email1).split()
        list2 = self.friends(email2).split()

        for item in list1:
            if item in list2:
                mutual.append(item)
        return (' '.join(mutual))

    
    def likely_friends(self, email:'str'):
        '''
        suggest missing friends for person x by listing the likeliest missing friends
        (where x is an e-mail address).
        The likeliest missing friend is a person who shares the most mutual friends
        with person x and who is not already a friend of x.
        Output this list on its own line, separated by spaces. The list should be
        sorted in alphabetical order. Do not add any other output. For example,
        >>> likely dfinn2003@gmail.com
        
        >>> likely lungj@cdf.toronto.edu
        Anya Tafliovich
        '''

        mutual = [0, '']
        if len(self._graph[email]) == 1:
            return ''
        for key in self._graph.keys():
            if not key == email:
                # Create a list of mutual friends
                temp = [len(self.mutual_friends(email, key).split()), key] 
                if temp[0] > mutual[0]: 
                    mutual = temp
        if mutual[0] == 0:
                return ''
        else:
            return self._graph[mutual[1]][0]
        
        
    def classmates(self, email:'str', degree:'int',) -> 'str':
        '''
        list all people within d degrees of separation of x who went to the same school (where x is an e-mail address).
        Output this list on its own line, separated by spaces. The list should be sorted in alphabetical order. Do not add any other output. For example,
        >>> classmates harold@alias.me 5

        >>> classmates dfinn2003@gmail.com 3
        Rosalie Mullins
        >>> classmates sengels@cdf.toronto.edu 3
        Andy Hwang Brian Law David Liu Dr. Evil Jonathan Lung
        '''

        nextDepth = []
        oldDepth = []
        tempDegree = 0
        classmates = []

        if not self._graph[email][2][0] == '':
            curDepth = self._graph[email][2]
        else:
            return ''

        if not self._graph[email][1][0] == '':
            schools1 = self._graph[email][1]

        if curDepth and schools1:
            while tempDegree < int(degree): #parse by degree
                for friend in curDepth:
                    if not self._graph[friend][2][0] == '':
                        for efriend in self._graph[friend][2]:
                            #Populates next depth
                            if efriend not in oldDepth:
                                nextDepth.append(efriend)
                        oldDepth.append(friend)
                        schools2 = self._graph[friend][1]
                    for school in schools1:
                        if school in schools2:
                            if (friend not in classmates) and friend != email:
                                classmates.append(self._graph[friend][0])
                        
                    #Go to next depth
                    curDepth = nextDepth
                    nextDepth = []
                tempDegree += 1
            return (' '.join(set(classmates)))

            
    def quit():
        '''
        quit the program
        '''
        sys.exit()
        
        
    
