import sys
import unittest

##text = open('input.txt')
##>>> text_r = text.read()

class SocialNetwork(object):

    def __init__(self):
        self._graph = {}

    def load_from_file(self, f) -> None:
        '''
        Reads a file and populates self._graph with contents
        '''
        with open(f, 'r') as infp:
            for line in infp:
        
##        with open(f) as infp:
##            data = infp.read()
##            print(isinstance(data, str))
##            print(data)
##            len(data)
##            for line in data:
                other_list = []
                school_list = []
                e_mail_list = []
                other = ''
    #             initalizing the lists
                lineLen = len(line)
                print(line)
                # print(lineLen)
                index_1 = line.find('<') + 1
                index_2 = line.find('>')
    #             looking for the specific characters to an index
                e_mail = line[index_1:index_2 - 1]
                # print(e_mail)
                name = line[0:index_1 - 1]
                # print(e_mail)
                other = name + line[index_2 + 1:]
    #             take all of the characters between the 2 index's and
    #             add them to the dictionary list
                index_1 = line.find('(') + 1
                index_2 = line.find(')')
                other_list.append(name)
                e_mail_list.append(line[index_2 + 3:-2])
                # print(e_mail_list)
                other_list.append(line[index_1:index_2].split(','))
                other_list.append(e_mail_list[0].split(','))
                self._graph[e_mail] = other_list
                print(self._graph[e_mail])
 #>>> a = SocialNetwork()
#>>> a.load_from_file('input.txt')               

    #         Makes friendship mutual
            for person in self._graph:
                pFriends = self._graph[person][2]
                print(pFriends)
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
            
            print(other_list) 
            print(school_list)
            print(e_mail_list)
        
    def friends(self, email: 'str') -> str:
        '''
        List all friends of person x (where x is an e-mail address).
        Output this list on its own line, separated by spaces.
        The list should be sorted in alphabetical order.
        Do not add any other output. For example,
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
#                check to see if the people have friends
                for item in emails:
                    friends.append(self._graph[item][0])
                    friends.sort()
                return (' '.join(friends))
#                 adds people to the friends list and returns the output

    def degree_between(self, email1: 'str', email2: 'str') -> int:
        '''
        print the degree of separation between person x and person y
        (where people are specified by e-mail address).
        In the network graph, the degree of separation between x
        and y corresponds to the number of edges on
        the shortest path between x and y. If there is no path between x and y,
        then the degree of separation is undefined. Use Python's infinity
        value float("inf") to represent this value.
        Notice that a person has 0 degrees of separation with him/herself.
        Output an integer on its own line. Do not add any other output.
        For example,
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
#           parses emails in graph
            while nextDepth != [] or curDepth != []:
                #   parse current depth
                for friend in curDepth:
                    if friend == email2:
                        return degree
                    else:
                        for efriend in self._graph[friend][2]:
                            #   parse through the emails of friends
                            if efriend not in oldDepth:
                                nextDepth.append(efriend)
                    oldDepth.append(friend)
#                    avoid circles & going backwards
#                    curdepth parse complete, go to next depth
                curDepth = nextDepth
                nextDepth = []
                degree += 1
            return -1

    def people_with_degree(self, email1: 'str', degree: 'int') -> 'list':
        '''
        list all people separated from person x
        by exactly d degrees of separation (where x is an e-mail address).
        Output this list on its own line, separated by spaces. The list
        should be sorted in alphabetical order (using the standard
        string ordering).Do not add any other output.
        For example,
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
            while tempDegree < int(degree):
                #   parse graph
                for friend in curDepth:
                    #   parse current depth
                    oldDepth.append(friend)
                    #   avoid circles & going backwards
                    #   goes through the friendlist of the person's friends
                    for efriend in self._graph[friend][2]:
                        if efriend not in oldDepth:
                            #   Make sure efriend email does not equal email
                            if not efriend == email1:
                                nextDepth.append(efriend)
                    #   curdepth parse complete, go to next depth
                curDepth = nextDepth
                nextDepth = []
                tempDegree += 1
#                curDepth is populated with emails
            for femail in curDepth:
                nameList.append(self._graph[femail][0])
            return (' '.join(set(nameList)))

    def mutual_friends(self, email1: 'str', email2: 'str'):
        '''
        list mutual friends of x and y, i.e.
        people who are friends with both x and y (where
        people are specified by e-mail address).Output this
        list on its own line, separated by spaces. The list should be
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
#         uses 2 lists to compare the people in both to find the mutual friends
        for item in list1:
            if item in list2:
                mutual.append(item)
        return (' '.join(mutual))

    def likely_friends(self, email: 'str'):
        '''
        suggest missing friends for person x by listing the likeliest
        missing friends (where x is an e-mail address).
        The likeliest missing friend is a person who shares the most mutual
        friends with person x and who is not already a friend of x.
        Output this list on its own line, separated by spaces. The list should
        be sorted in alphabetical order. Do not add any other output.
        For example,
        >>> likely dfinn2003@gmail.com

        >>> likely lungj@cdf.toronto.edu
        Anya Tafliovich
        '''

        mutual = [0, '']
        if len(self._graph[email]) == 1:
            return ''
        for key in self._graph.keys():
            if not key == email:
                #   Create a list of mutual friends
                temp = [len(self.mutual_friends(email, key).split()), key]
                if temp[0] > mutual[0]:
                    mutual = temp
        if mutual[0] == 0:
                return ''
                #   case if there is no mutual friends
        else:
            return self._graph[mutual[1]][0]

    def classmates(self, email: 'str', degree: 'int',) -> 'str':
        '''
        list all people within d degrees of separation of x
        who went to the same school (where x is an e-mail address).
        Output this list on its own line, separated by spaces.
        The list should be sorted in alphabetical order.
        Do not add any other output. For example,
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
#       initalize all of the required lists
        if not self._graph[email][2][0] == '':
            curDepth = self._graph[email][2]
        else:
            return ''

        if not self._graph[email][1][0] == '':
            schools1 = self._graph[email][1]

        if curDepth and schools1:
            while tempDegree < int(degree):
                #   parse by degree
                for friend in curDepth:
                    if not self._graph[friend][2][0] == '':
                        for efriend in self._graph[friend][2]:
                            #   Populates next depth
                            if efriend not in oldDepth:
                                nextDepth.append(efriend)
                        oldDepth.append(friend)
                        schools2 = self._graph[friend][1]
                    for school in schools1:
                        if school in schools2:
                            if (friend not in classmates) and friend != email:
                                classmates.append(self._graph[friend][0])
#                    Go to next depth
                    curDepth = nextDepth
                    nextDepth = []
                tempDegree += 1
            return (' '.join(set(classmates)))

    def quit():
        '''
        quit the program
        '''
        sys.exit()


    def initialize_graph(filename) -> 'SocialNetwork':

        '''Return a SocialNetwork that is loaded from a file. The name of the file
        to be loaded is provided at the command line or defaults to 'example.timf'
        '''
    #     slightly modified version of the initialize_graph used for the testcases
    #     Choose a file name
        graph_filename = (sys.argv[1:] + [filename])[0]
    #     Build and return a graph
        graph = SocialNetwork()
        graph.load_from_file(open(graph_filename))
        return graph


class SocialnetworkTests(unittest.TestCase):

    #    test case 1
##    f = open('degree_test_file', 'w')
##    f.write('Anya Tafliovich<anya@cdf.toronto.edu>(University of Toronto):sengels@cdf.toronto.edu,liudavid@cdf.toronto.edu,henry@hyde.\n' + 'Steve Engels<sengels@cdf.toronto.edu>(Urban Technical School,University of Waterloo):liudavid@cdf.toronto.edu \n' + 'Jonathan Lung<lungj@cdf.toronto.edu>(Urban Technical School,University of Toronto):sengels@cdf.toronto.edu,liudavid@cdf.toronto.edu,blaw@cdf.toronto.edu \n' + 'Harold Finch<harold@alias.me>(): \n' + 'Brian Law<blaw@cdf.toronto.edu>(Urban Technical School,University of Waterloo,University of Toronto):andy@toronto.edu,lungj@cdf.toronto.edu,liudavid@cdf.toronto.edu,dr@evil.net \n' + 'Dr. Evil<dr@evil.net>(Queens University,University of Waterloo,Evil Medical School):henry@hyde.net,hl@imaeatchu.com \n' + 'Annie<annie@mgo.org>(School of Hard Knocks): \n' + 'Henry Jekyll<henry@hyde.net>(Evil Medical School):annie@mgo.org,dr@evil.net \n' + 'Hannibal Lecter<hl@imaeatchu.com>(Evil Medical School,School of Hard Knocks):annie@mgo.org,dr@evil.net \n' + 'Andy Hwang<andy@toronto.edu>(University of Toronto,University of Waterloo):blaw@cdf.toronto.edu \n' + 'Dewey Finn<dfinn2003@gmail.com>(School of Rock):principal@gppr.edu \n' + 'Rosalie Mullins<principal@gppr.edu>(School of Rock):dfinn2003@gmail.com')
##    f.close()
    g = open('degree_test_file', 'r')
    g.read("Anya Tafliovich<anya@cdf.toronto.edu>(University of Toronto):sengels@cdf.toronto.edu,liudavid@cdf.toronto.edu,henry@hyde.\n' + 'Steve Engels<sengels@cdf.toronto.edu>(Urban Technical School,University of Waterloo):liudavid@cdf.toronto.edu \n' + 'Jonathan Lung<lungj@cdf.toronto.edu>(Urban Technical School,University of Toronto):sengels@cdf.toronto.edu,liudavid@cdf.toronto.edu,blaw@cdf.toronto.edu \n' + 'Harold Finch<harold@alias.me>(): \n' + 'Brian Law<blaw@cdf.toronto.edu>(Urban Technical School,University of Waterloo,University of Toronto):andy@toronto.edu,lungj@cdf.toronto.edu,liudavid@cdf.toronto.edu,dr@evil.net \n' + 'Dr. Evil<dr@evil.net>(Queen's University,University of Waterloo,Evil Medical School):henry@hyde.net,hl@imaeatchu.com \n' + 'Annie<annie@mgo.org>(School of Hard Knocks): \n' + 'Henry Jekyll<henry@hyde.net>(Evil Medical School):annie@mgo.org,dr@evil.net \n' + 'Hannibal Lecter<hl@imaeatchu.com>(Evil Medical School,School of Hard Knocks):annie@mgo.org,dr@evil.net \n' + 'Andy Hwang<andy@toronto.edu>(University of Toronto,University of Waterloo):blaw@cdf.toronto.edu \n' + 'Dewey Finn<dfinn2003@gmail.com>(School of Rock):principal@gppr.edu \n' + 'Rosalie Mullins<principal@gppr.edu>(School of Rock):dfinn2003@gmail.com")
##    g.read()
    g.close()
    
    graph1 = SocialNetwork.initialize_graph('degree_test_file')
##    graph1 = SocialNetwork.initialize_graph(g)

    def test_no_connection_between_2_profiles(self):
        ''' 2 profiles have no connection with one another and are isolated '''
        input_val = graph1.degree_between("liudavid@cdf.toronto.edu", "harold@alias.me")
        expected_output = ''
        assertEqual(input_val == expected_output)

    def Test_seperate_webs(self):
        ''' test for searching between 2 seperate webs that are
        connected and filled with profiles'''
        input_val = graph1.degree_between("liudavid@cdf.toronto.edu", "harold@alias.me")
        expected_output = 'inf'
        assertEqual(input_val == expected_output)

    def Test_for_yourself(self):
        ''' test for when degree is 0 '''
        input_val = graph1.degree_between("harold@alias.me", "harold@alias.me")
        expected_output = int(0)
        assertEqual(input_val == expected_output)

    def Test_1_degree(self):
        ''' test for when degree is 1 '''
        input_val = graph1.degree_between("anya@cdf.toronto.edu", "liudavid@cdf.toronto.edu")
        expected_output = int(1)
        assertEqual(input_val == expected_output)

    def test_shortest_path(self):
        ''' test for shortest path between 2 linked people '''
        input_val = graph1.degree_between("anya@cdf.toronto.edu", "annie@mgo.org")
        expected_output = int(2)
        assertEqual(input_val == expected_output)

    def shortest_path_1_degree(self):
        ''' finds the shortes path for 1 degree in a connected web'''
        input_val = graph1.degree_between("blaw@cdf.toronto.edu", "lungj@cdf.toronto.edu")
        expected_output = int(1)
        assertEqual(input_val == expected_output)

    def test_for_4_degrees(self):
        ''' tests to see 4 degrees of seperation '''
        x = graph1.degree_between("lungj@cdf.toronto.edu", "annie@mgo.org")
        expected_output = int(4)
        assertEqual(x == expected_output)

    def test_for_5_degrees(self):
        ''' tests for 5 degrees of seperation '''
        input_val = graph1.degree_between("andy@toronto.edu", "annie@mgo.org")
        expected_output = int(4)
        assertEqual(input_val == expected_output)

    def test_isolation(self):
        ''' test for a single isolated network '''
        input_val = graph1.degree_between("harold@alias.me", "annie@mgo.org")
        expected_output = 'inf'
        assertEqual(input_val == expected_output)

    def test_edges(self):
        ''' test for shortest path in a square network'''
        input_val = graph1.degree_between("dr@evil.net", "annie@mgo.org")
        expected_output = int(2)
        assertEqual(input_val == expected_output)

    def test_Shortest_path_pentagon(self):

        ''' test for when network resembles a pentagon'''
        x = graph1.degree_between("blaw@cdf.toronto.edu", "anya@cdf.toronto.edu")
        expected_output = (2)
        assertEqual(x == expected_output)
        
if __name__ == '__main__':
   unittest.main()
