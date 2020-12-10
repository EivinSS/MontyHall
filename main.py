import random

# Liste med valg
choose = ['car', 'goat1', 'goat2']

# Liste som skal bli dørene
doors = []

# Variabler som holder kontroll på poengene
number_wins = 0
number_lose = 0

# Itererer gjennom hele greia et visst antall ganger
for x in range(1000):

    # Vi populerer listen 'doors' med verdiene, tilfeldig rekkefølge
    while len(choose) > 0:

        # Finner et tilfeldig ord av 'car', 'goat1', 'goat2'
        picked = str(choose[random.randint(0,len(choose)-1)])

        # Legger ordet til doors
        doors.append(picked)

        # Fjerner ordet som vi plukker fra listen choose
        choose.remove(picked)

    # Nå har vi en utfylt liste doors som inneholder tilfeldige verdier av 'car', 'goat1', 'goat2'

    # Første valg, tilfeldig av de 3 dørene
    first_choice = random.randint(0,2)
    print('Number of first door picked: ' + str(first_choice))

    # Finner en av geitene
    foundGoat = False
    finding_a_goat = 0
    while not foundGoat:
        finding_a_goat = random.randint(0,2)
        if finding_a_goat != first_choice and str(doors[finding_a_goat]) != 'car':
            foundGoat = True
    

    print(str(doors[finding_a_goat]) + ' behind door number ' + str(finding_a_goat))

    print('Im changing door!')

    second_choice = 0

    # Velger den siste døren
    if (first_choice == 0 or finding_a_goat == 0) and (first_choice == 1 or finding_a_goat == 1):
        second_choice = 2
    if (first_choice == 0 or finding_a_goat == 0) and (first_choice == 2 or finding_a_goat == 2):
        second_choice = 1
    if (first_choice == 1 or finding_a_goat == 1) and (first_choice == 2 or finding_a_goat == 2):
        second_choice = 0
    
    print('My second choice is door number: ' + str(second_choice) + ', and it is a ' + str(doors[second_choice]))

    # Sjekker om vi har vunnet eller tapt
    if(str(doors[second_choice]) == 'car'):
        print('I won!')
        number_wins += 1
    else:
        number_lose += 1
        print('I lost...')
    
    #Clearing for next round
    doors.clear()
    choose = ['car', 'goat1', 'goat2']
    

# Nå er vi ute av den store itereringen, og vi printer resultatet
print('Wins: ' + str(number_wins) + ', and Loss: ' + str(number_lose))
print('Winning percentage:' + str(int(number_wins) / (int(number_wins)+int(number_lose))*100))
