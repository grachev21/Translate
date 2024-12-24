import os
import time

import enchant
from googletrans import Translator
from gtts import gTTS

TRANSLATOR = Translator()


def main():
    # Creates a dictionary and stores it in a set
    def createEnDict():
        # empty set
        outList = set()
        # reads a file with a dirty word base
        with open("./words.txt", "r") as file:
            # save all text into a string
            text: str = file.read()
            # split the string into a list
            listWords = text.split(" ")
        # iterate through the list
        for lw in listWords:
            # select only letters
            if lw.isalpha():
                # add to set
                outList.add(lw.lower())
                # output to the console
                print(lw.lower())
        # display the number of words at the end
        print(len(outList))
        # return the finished set
        return outList

    def getAudio(word, lang="ru"):
        if not os.path.exists(f"./dbWords/{word}.mp3"):
            tts = gTTS(text=word, lang="en")
            tts.save(f"./dbWords/{word}.mp3")
        if not os.path.exists(f"./dbWords/{word} slow.mp3"):
            tts = gTTS(text=word, lang="en", slow=True)
            tts.save(f"./dbWords/{word} slow.mp3")

    def translateWord(word):
        # empty list
        checkList = []
        # read the file into which we will save the words
        with open("./dbWords/words.txt", "r") as file:
            # get a list of words
            textList: list = file.readlines()
            # let's go through the list
            for tl in textList:
                # split the string by spaces
                tl.split(" ")
                # add to the checklist only
                # English word
                checkList.append(tl[0])
            # check if a potential word exists in the common database
            if word not in textList:
                # if not, we translate it
                translation = TRANSLATOR.translate(word, src="en", dest="ru").text
                getAudio(word)
                # and finally add it in add mode 'a'
                with open("./dbWords/words.txt", "a") as file:
                    # add to file
                    file.write(f"{word} {translation}\n")
                    # print the entire line to the console
                    print(f"{word} {translation}\n")

    def is_word_in_dictionary(word):
        d = enchant.Dict("en_US")
        return d.check(word)

    # Launches all functions
    def run(words):
        COUNTER = 0
        for word in words:
            if is_word_in_dictionary(word):
                translateWord(word)
                print(word, COUNTER)
                COUNTER += 1
                time.sleep(2)

    listWords = createEnDict()
    run(listWords)


if __name__ == "__main__":
    main()
