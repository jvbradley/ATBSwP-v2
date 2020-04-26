#! python3
def aboutMe():
    '''
    Date Detection
    "Automate the Boring Stuff: Second Edition"
    Chapter 7 Project 1
    https://automatetheboringstuff.com/2e/chapter7/

    Write a regular expression that can detect dates in the DD/MM/YYYY format.
    Assume that the days range from 01 to 31, the months range from 01 to 12,
    and the years range from 1000 to 2999. Note that if the day or month is a
    single digit, it’ll have a leading zero.
    '''

def formatError(specificError):
    if specificError == 'invalidFormat':
        errorMessage = '\n * Invalid input received.  Format expected: DD/MM/YYYY'
        errorMessage += '\n * Day range: 01 to 31'
        errorMessage += '\n * Month range: 01 to 12'
        errorMessage += '\n * Year range: 1000 to 2999'
        errorMessage += '\n * For single digit months, use 0 and the corresponding month number.'
    if specificError == 'tooManyDays':
        errorMessage = '\n * Invalid date provided: day of month exceeds length of month.'

    errorMessage += '\n * Terminating program ...'
    print(errorMessage)
    exit()

def dateDetection(dateInput):
    month30 = ('04', '06', '09')
    month31 = ('01', '03', '05', '07', '08', '10', '11', '12')
    diDay = dateInput[0:2]
    diMonth = dateInput[3:5]
    diYear = dateInput[6:]
    if diMonth in month30:
        if int(diDay) > 30:
            formatError('tooManyDays')
        elif int(diDay) < 31:
            print(' * This month has 30 days.')
    elif diMonth in month31:
        print(' * This month has 31 days.')
    elif diMonth == '02':
        if diYear[-2:] == '00' and int(diYear)/400 != int(diYear)//400:
            if int(diDay) > 28:
                formatError('tooManyDays')
        elif diYear[-2:] == '00' and int(diYear)/400 == int(diYear)//400:
            print(' * This is a leap year at the turn of the century.')
    else:
        formatError('invalidFormat')

    print(' * This date is formatted as expected.')

def dateInput():
    # This function will solicit a date from the user and validate the format.
    import re
    dateRequest = input(' * Provide the date the verify: ')
    dateFormatRegex = re.compile(r'''(
        ([0-2][1-9]|[3][0-1])/ # day of month, 00 - 31
        ([0][1-9]|[1][0-2])/ # month of year, 01 - 12
        ([1000-2]{1}[000-999]{3}) # valid year, 1000 - 2999
    )''', re.VERBOSE)

    dateSearch = dateFormatRegex.search(dateRequest)
    try:
        dateSearch.group()
    except AttributeError:
        formatError('invalidFormat')

    dateDetection(dateSearch.group())

dateInput()
