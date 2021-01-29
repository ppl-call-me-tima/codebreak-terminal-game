print('CODEBREAK\nA 4-digit code has been generated, your aim is to crack it using the hints given.\nYou will be prompted whether your guessed code has digits in the correct place or wrong place if they are in the code.')
# CODE GENERATION
import random
numbers = [0,1,2,3,4,5,6,7,8,9]
code = ''
for x in range(0,4):
    n = random.choice(numbers)
    code += str(n)
    numbers.remove(n)

# VARIABLES
guess_status=False
place_true=0
place_false=0
n_guesses=0
max_guess=int(input('\nHow many guesses do you want: '))
guesses=[]

print('\nYour Guesses:\n')

# LOOP
while not guess_status:
    if max_guess-n_guesses==0:
        print(f'\nYou lost. The code was {code}.')
        break
    guess=input()
    if len(guess)!=4:
        print('Please enter a 4-digit number only.\n')
        continue
    if guess in guesses:
        print('You have already tried this combination!')
        for i in range(4):
            if guess[i]==code[i]:
                place_true+=1
            else:
                if guess[i] in code:
                    place_false+=1
    guesses.append(guess)
    if guess==code:
        print('SUCCESS')
        guess_status=True
        break            #beacuse printing of place_true/false is inside loop
    else:
        n_guesses+=1
        place_true=0     #variable reset for loop run
        place_false=0    #variable reset for loop run
        for i in range(len(guess)):            
            if guess[i]==code[i]:
                place_true+=1           
            else:
               if guess[i] in code:
                   place_false+=1
    if max_guess-n_guesses==0:
        continue           
    print(f'{place_true} are at correct place\n{place_false} are at wrong place\n')

esc=input('Finished')