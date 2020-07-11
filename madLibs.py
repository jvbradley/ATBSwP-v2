#! python3
# https://automatetheboringstuff.com/2e/chapter9/
'''
Create a Mad Libs program that reads in text files and lets the user add their
own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text
file.  For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to replace them.

Enter an adjective: silly
Enter a noun: chandelier
Enter a verb: screamed
Enter a noun: pickup truck

The following text file would then be created:
    The silly panda walked to the chandelier and then screamed. A nearby pickup
    truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.
'''
def madLibs():
    import os
    from pathlib import Path

    # Let's create a folder and store it there so I don't have to hunt and
    # peck for the files later.  We'll set that as our working directory.
    madLibsHome = Path(Path.home(), 'madLibFiles')
    if Path.exists(madLibsHome) and Path.is_dir(madLibsHome):
        os.chdir(madLibsHome) # Set the current working directory
    else:
        os.mkdir(madLibsHome) # Folder created
        os.chdir(madLibsHome) # Set the current working directory

    madLibsFiles = list(madLibsHome.glob('Mad*.txt'))
    madLibsFileName = 'madLibs-UserOutput-' + str(len(madLibsFiles) + 1) + '.txt'
    madLibsFile = open(madLibsFileName, 'w')
    # This is the text through which we'll iterate.
    madLibsText = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
    madLibsTextList = madLibsText.split(' ')

    for word in madLibsTextList:
        if word.isupper() and len(word) > 1:
            if word[-1:] == '.':
                word = word[0:-1]
            inputText = 'Enter a'

            if word == 'ADJECTIVE':
                inputText += 'n ' + word.lower() + ': '
            else:
                inputText += ' ' + word.lower() + ': '

            userInput = input(inputText)
            madLibsText = madLibsText.replace(word, userInput, 1)

    print('Your Mad Libs output:')
    print(madLibsText)
    print('\nSaved to file: ' + str(madLibsFileName))
    madLibsFile.write(madLibsText)
    madLibsFile.close()
madLibs()
