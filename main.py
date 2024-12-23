import os

from googletrans import Translator
from gtts import gTTS

TRANSLATOR = Translator()
# Creating a transcription object for the Russian language
COUNTER = 0

def main():

    # Creates a dictionary and stores it in a set
    def createEnDict():
        # empty set
        outList = set() 
        # reads a file with a dirty word base
        with open('./words.txt', 'r') as file:  
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

    def translateWord(word):
        def get_transcription(word, lang='ru'):
            tts = gTTS(text=word, lang=lang)
            tts.save(f'./dbWords/temp.mp3')
            return tts.text
        # empty list
        checkList = [] 
        # read the file into which we will save the words
        with open('./dbWords/words.txt', 'r') as file:
            # get a list of words
            textList: list = file.readlines()

            if len(textList) == 10:
                exit()
            # let's go through the list
            for tl in textList:
                # split the string by spaces
                tl.split(' ')
                # add to the checklist only 
                # English word
                checkList.append(tl[0])
            # check if a potential word exists in the common database
            if word not in textList:
                # if not, we translate it
                translation = TRANSLATOR.translate(word, src='en', dest='ru').text
                # We receive the transcription
                transcription = get_transcription(word) 
                # and finally add it in add mode 'a'
                with open('./dbWords/words.txt', 'a') as file:
                    # add to file
                    file.write(f'{word} {transcription} {translation} \n')
                    # print the entire line to the console
                    print(f'{word} {transcription} {translation} \n')



    # def audio(word):
    #     tts = gTTS(text=word, lang='en')
    #     tts.save("temp.mp3")
    #

    def run(words):
        print('run translate...')
        for word in words:
            translateWord(word)

    # # Преобразование аудиофайла в текст (транскрипция)
    # os.system("ffmpeg -i temp.mp3 temp.wav")
    # os.system("pocketsphinx_continuous -infile temp.wav 2>&1 | grep '^[A-Z]'")
    #
    # # Удаление временных файлов
    # os.remove("temp.mp3")
    # os.remove("temp.wav")

    listWords = createEnDict()
    run(listWords)
if __name__ == "__main__":
    main()
    
