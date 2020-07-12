#! python3
# https://automatetheboringstuff.com/2e/chapter9/
'''
Write a program that opens all .txt files in a folder and searches for any line
that matches a user-supplied regular expression. The results should be printed
to the screen.
'''

def regexSearch():
    from pathlib import Path

    documentsHome = Path(Path.home(), 'Documents')
    if Path.exists(documentsHome) and Path.is_dir(documentsHome):
        os.chdir(documentsHome) # Set the current working directory
    else:
        os.mkdir(documentsHome) # Folder created
        os.chdir(documentsHome) # Set the current working directory

    textFileList = list(documentsHome.glob('*.txt'))
    if len(textFileList) < 1:
        infoMessage = ' * I failed to locate text files in the folder ' + documentsHome + '.'
        print(infoMessage)
        exit()

    infoMessage = '\nThis program will search for a line of text in a file ending with the extension \'.txt\'.\n'
    print(infoMessage)
    textSearch = input('What line of text do you want to seek? ')
    for textFile in textFileList:
        if Path.is_file(textFile):
            print(' * Checking file \'' + textFile.name + '\' ... ')
            openTextFile = open(documentsHome / textFile)
            textFileContent = openTextFile.readlines()
            openTextFile.close()

            for line in textFileContent:
                if textSearch in line:
                    print(' * I found this line:')
                    print('\t' + line)

regexSearch()
