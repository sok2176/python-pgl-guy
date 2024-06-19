import random
from T9 import Tnine
import json

memo0 = None
bad_symb = ['!','@','#','$',';','%','^',':','&','?','*','(',')',' ','.', "'"]
signals = ['Respond','Learn']
cs = 1
directory='d:/VS Code/PGLGuy/memory.json'

print("PGL Guy: Hello! Let's begin talking! ")


class Chat:
    # FUCK
    '''rewriteMemory(self, input:str, data:str): Updates the memory with new input and data by filtering, converting, and updating the memory file.
__init__(self, prompt='loks24975dfk4sd234fnmcdji343'): Initializes the Chat instance, loads memory from a file, processes user input, and generates a response based on the input using a matching algorithm.'''
    reply = 'No response'
    sigl=signals[0]
     # no one will pick that pass!
    enter = None
    memory = {'zgl': 'Oops'}
    def rewriteMemory(self, input:str, data:str):
        with open(directory, "r") as fp3:
            loaded = json.load(fp3)
            print(loaded)

            fp3.close()
        with open(directory, 'w') as fp2:

            filter2= ' '.join(i for i in input if not i in bad_symb) # 3 этапа фильтрации ввода
            filter3 = filter2.replace(' ','')
            convert = str.lower(filter3)

            loaded.update({convert: list(data)})
            print(loaded)
            json.dump(loaded, fp2)


            fp2.close()

    def __init__(self, prompt='loks24975dfk4sd234fnmcdji343'):
        userInput = prompt # Ввод
        separ = userInput.split(' ')
        global cs
        if len(separ) == 1:
            with open(directory, "r") as fp:
            # Unpickling

                memory = json.load(fp)
                print(memory)
                memo0 = memory
                fp.close()

            filter2= ' '.join(i for i in userInput if not i in bad_symb) # 3 этапа фильтрации ввода
            filter3 = filter2.replace(' ','')
            convert = str.lower(filter3)
            memo = memo0

            print("Uhh, I'm uhh... ") # Система дает знак, что думает

            for key in memory:
                global cs

                user = convert # Из туториала по оптимизации из Youtube Shorts
                memoTupled = tuple(memory) # Туплит память memory.txt


                tn = Tnine(user, memory,0.65)

                if tn.output == str.lower(key):
                    self.sigl='Respond'
                    cs = 1

                    print("Success!\n") #TODO: send message insted of it
                    print(f"PGL Guy: {random.choice(memory.get(tn.output))}\n") # ответ TODO: send message insted of it
                    self.reply = random.choice(memory.get(tn.output))

                    break # остановить поиск, если найден ответ

                elif str.lower(key) != str.lower(user) and cs >= len(memoTupled):
                    cs = 1
                    self.reply = 'ERROR_CODE_NOT_FOUND_REPLY_28439sxdffd83ФЫВФЫВASD8КВЕНТИНТАРАНТИНО762asd902ggg###&*&^@(*763723&&*@#@)4734328#CNfrdsyvne8^%^ED'
                    self.sigl = 'Learn'
                    self.enter = str.lower(user)
                    print(self.enter, 'line 75 GUy')
                    #print(self.sigl,' IM DUMBBB LOOK AT ME ',self.reply)


                    print("PGL Guy has no idea! Can you explain him your prompt? y = yes; n = no\n") # ЮЗЕР волонтер #TODO: send message insted of it


                elif str.lower(key) != str.lower(user) and cs <= len(memoTupled):

                    cs +=1

        elif len(separ) >1:
            print('\nOh crap. Gotta think more. Please, wait...')
            # CODE
            with open(directory, "r") as fp:
            # Unpickling

                memory = json.load(fp)
                print(memory)
                memo0 = memory
                fp.close()

            filter2= ' '.join(i for i in userInput if not i in bad_symb) # 3 этапа фильтрации ввода
            filter3 = filter2.replace(' ','')
            convert = str.lower(filter3)
            memo = memo0

            print("Uhh, I'm uhh... ") # Система дает знак, что думает

            for key in memory:
               
                
                user = convert # Из туториала по оптимизации из Youtube Shorts
                memoTupled = tuple(memory) # Туплит память memory.txt


                tn = Tnine(user, memory,0.65)

                if tn.output == str.lower(key):
                    self.sigl='Respond'
                    cs = 1

                    print("Success!\n") #TODO: send message insted of it
                    print(f"PGL Guy: {random.choice(memory.get(tn.output))}\n") # ответ TODO: send message insted of it
                    self.reply = random.choice(memory.get(tn.output))

                    break # остановить поиск, если найден ответ


                elif str.lower(key) != str.lower(user):

                    for id in range(len(separ)):
                        self.__init__(separ[id])
                        if self.reply ==key:
                            cs = 1
                            print('DAMMIT ', self.reply)
                            
                            break
                        else:
                            cs += 1


            
ch = Chat('ты любишь чай')
# initializing dictionary

