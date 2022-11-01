import random 

attempts = []
maxAttempts = 3

number = int(random.randint(1, 50) * random.randint(1, 50) / random.randint(1, 50))

money = 0

def checkNumber(num):
    global number
    global attempts
    global guess
    global money

    if (num == number):
        print(f'You guessed the correct number! {num}')
        print('The game restarting.')

        number = random.randint(0, 50) * random.randint(0, 50) / random.randint(0, 50)
        attempts.clear()

        money+=100
        print(f'Your cash: {money}')

        startGuessing()

        return
    elif (num in attempts):
        print('You already tried this number, try a new one!')

        startGuessing()

        return
    elif (abs(num - number) <= 100):
        print("You didn't hit it, but close brotha. Have another attempt")

    attempts.append(num)

    print(f'Remaining attempts: {3 - len(attempts)}')

    if (3 - len(attempts) <= 0):
        attemptsString = ' '.join(str(i) for i in attempts)
        print('Your final 3 guesses: ' + attemptsString)
        print(f'The number you tried to guess: {number}')
        print("Sorry you couldn't guess the correct number. The game restarts!")
        number = random.randint(0, 50) * random.randint(0, 50) / random.randint(0, 50)
        attempts.clear()

        startGuessing()

    startGuessing()

def startGuessing():
    global guess

    guess = input('Please type a number! ')

    print(f'Your guess is: {guess}')
    checkNumber(int(guess))
startGuessing()