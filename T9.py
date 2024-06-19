
class Tnine:
    '''Filter words with autocorrection using a custom dictionary.'''
    output = 'PGL Guy: No clue. Geting bot ready to learn. And you, user, get ready to teach!'
    #output = None
    def __init__(self, word:str, dictionary:dict, accuracy=0.5):

        matching =0

        #print(word)

        for key in dictionary:
            l = list(key)
            #print(len(l))

            a = list(word)
            #print(len(a))

            if len(l) >= len(a):
                for i in range(len(list(word))):
                    if l[i]==a[i]:
                       matching+=1

                       #print(matching, ' letters matched ')
                       #print()
                       if matching == len(word):                           #print(word, 'replaced',key)
                           self.output = key

                           break
