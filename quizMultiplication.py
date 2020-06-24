#! python3
# https://automatetheboringstuff.com/2e/chapter8/

def quizMultiplication():
    '''
    To see how much PyInputPlus is doing for you, try re-creating the
    multiplication quiz project on your own without importing it.  This program
    will prompt the user with 10 multiplication questions, ranging from 0 × 0
    to 9 × 9. You’ll need to implement the following features:

     - If the user enters the correct answer, the program displays "Correct!"
     for 1 second and moves on to the next question.
     - The user gets three tries to enter the correct answer before the program
     moves on to the next question.
     - Eight seconds after first displaying the question, the question is
     marked as incorrect - even if the user enters the correct answer after the
     8-second limit.

    Compare your code to the code using PyInputPlus in "Project: Multiplication
    Quiz" on page 196.
    '''
    import pyinputplus as pyip
    import random, time

    questionTotal = 10
    answersCorrect = 0

    for question in range(questionTotal):
        userAnswer = 0
        numberFirst = round(random.uniform(0, 9))
        numberSecond = round(random.uniform(0, 9))
        correctAnswer = numberFirst * numberSecond

        questionText = '\nQuestion ' + str(question + 1).zfill(2) + ': What is '
        questionText += str(numberFirst) + ' * ' + str(numberSecond) + '?'
        print(questionText)

        try:
            userAnswer = pyip.inputInt('Your answer: ', limit = 3, timeout = 8, blank = False)
            if userAnswer == correctAnswer:
                print(' * Correct!')
                answersCorrect += 1
                time.sleep(1)
        except pyip.RetryLimitException:
            print(' * Too many invalid responses received; moving to next question.')
        except pyip.TimeoutException:
            print(' * Answer not provided within alloted time; moving to next question.')

    print('\nYour results: ' + str(answersCorrect) + ' correct answers / ' + str(questionTotal) + ' possible')
quizMultiplication()
