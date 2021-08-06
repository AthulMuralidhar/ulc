import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = """let a = 5

if (a > 5) {
 console.log("greater")
 } else {
 console.log("lesser")
 }
"""
# tokenized = nltk.word_tokenize(text)

# print(nltk.pos_tag(tokenized))

"""
- make a regex tagger and assign meta programatic things as tags
- the llvm spec should provide some insight here because we will want to
converge on that 
"""

patterns = [
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
    
]

regex_tagget = nltk.RegexpTagger(patterns)