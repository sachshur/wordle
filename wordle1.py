# Wordle
import requests
from colorama import init, Fore


def valid_guess():
    guess = input("What is your five-letter guess?: ").upper()
    dictionary_url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + guess
    response = requests.get(dictionary_url)
    while len(guess) != 5 or response.status_code != 200:
        guess = input("Guesses can only be five letter words. Try again: ").upper()
        dictionary_url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + guess
        response = requests.get(dictionary_url)
    return guess


def green_check(wordle, guess, results):
    for i in range(len(wordle)):
        if guess[i] == wordle[i]:
            results[i] = "G"
    return


def yellow_check(wordle, guess, results):
    for i in range(0, len(wordle)):
        for j in range(0, len(guess)):
            if results[j] == "G":
                continue
            elif wordle[i] == guess[j] and i != j:
                results[j] = "Y"
    return


def main():
    init(autoreset=True)
    wordle_url = "https://wordle-answers-solutions.p.rapidapi.com/today"
    headers = {
        "X-RapidAPI-Key": "9468e2e5f4msh5fae85f7ad7a9cbp1d86d7jsnc461ad7e8d75",
        "X-RapidAPI-Host": "wordle-answers-solutions.p.rapidapi.com"
    }
    word = requests.get(wordle_url, headers=headers)
    wordle = word.json().get('today')

    guesses = 0

    while guesses < 6:
        guess = valid_guess()
        guesses += 1
        results = ['B', 'B', 'B', 'B', 'B']
        green_check(wordle, guess, results)
        yellow_check(wordle, guess, results)
        output = ''

        for i in range(len(results)):
            if results[i] == "G":
                output += Fore.GREEN + guess[i]
            elif results[i] == "Y":
                output += Fore.YELLOW + guess[i]
            else:
                output += Fore.LIGHTBLACK_EX + guess[i]

        print(output)

        if results[0] == "G" and results[1] == "G" and results[2] == "G" and results[3] == "G" and results[4] == "G":
            print("You solved the Wordle in " + str(guesses) + " tries!")
            return

    print("You failed to solve the Wordle. The word is " + wordle + ".")
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
