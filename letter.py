letters = [
['a','eɪ'], 	 	
['b','bi'], 	
['c','si'], 	
['d','di'], 	
['e','i'],  	
['f','ɛf'],  	
['g','dʒi'], 	
['h','eɪtʃ'], 	
['i','aɪ'], 		
['j','dʒeɪ'],  	
['k','keɪ'],  	
['l','ɛl'], 		
['m','ɛm'], 		
['n','ɛn'], 	 	
['o','əʊ'], 	 	
['p','pi'], 	 	
['q','kju'], 		
['r','ɑ'],  	
['s','ɛs'],  	
['t','ti'], 	 	
['u','ju'], 		
['v','vi'], 	 	
['w','dʌb(ə)l ju'],
['x','ɛks'],	 	
['y','waɪ'],	 	
['z','zi'], 	
]

def transcription(word):
    outLetter = ''
    for w in word:
        for letter in letters:
            if letter[0] == w:
                outLetter += letter[1]
    
    return outLetter
print(transcription('hello'))
