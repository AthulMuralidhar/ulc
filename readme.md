# overview
- the aim is to cerate a wrapper arpund the LLVM intermediate representation to allow for code compilation from any language to any other language
- the strucute must support a newral net to build an abstract syntax tree that is close to the user of the computer

# language overview

## 1st iteration
- make a create, read, update and delete route for the core abstract syntax tree
- use code to convert the ast to llvm intermediate representation
- expose the crud routs to a simple natural language processing end point
- expose the front end of the nlp to the user

### the current goal
- identify conditional logic from a series of texts and construct an abstract syntax tree out of it
- compile the ast to llvm ir

# references
- **llvm**: https://llvm.org/docs/tutorial/
- **chatbot**: https://www.digitalocean.com/community/tutorials/how-to-create-an-intelligent-chatbot-in-python-using-the-spacy-nlp-library