import datetime, random

def getBirthdays(numberOfBirthdays):
    birthdays = []  
    for i in range(numberOfBirthdays):
        # Year is unimportant for the simulation as long as all occur in same year
        startOfYear = datetime.date(2001, 1, 1) # Sets year to be used

        # Below will pull out a random day in the year
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays # Setting a random birthday
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)): 
        return None # All birthdays are the same so return None
    
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            return birthdayA
        
print("""The Birthday Paradox shows us that in a group of N people, the odds that two of them will have the same birthday is 
    surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated random simulations)
    to explore this concept.

(This isn't really a paradox, just a surprising result).""")

MONTHS = ('January', 'Febuary', 'March', 'April', 'May', 'June',
           'July', 'August', 'September', 'October', 'November', 'December') # Tuple of month names in order

while True: # Will keep asking user for amount between 1 and 100
    print("How many birthdays shall we generate (Max 100)")
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100): # Checks all numbers are 0-9 and between 0 and 100
        numBDays = int(response)
        break # Valid amount inputted
print()


print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday
        print(', ', end='')
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')
print()
print()

# Check if two birthdays are the same
match = getMatch(birthdays)

print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a brithday on', dateText)
else:
    print('There are no matching birthdays.')
print()

# Running 100,000 simulations

print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to Begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0 # How many simulations had matching birthdays in them
for i in range(100_000):
    if i % 1000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

# Display simulation results
probability = round(simMatch / 100_000 * 100 , 2) # Rounds this to two decimal places
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of ')
print('having the same birthday in their group')
print('That\'s probably more than you would think!')