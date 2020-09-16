#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    isEven = (len(string)%2) == 0
    return isEven


def remove_third_char(string: str) -> str:
    string = string[0:2]+string[3:]
    return string


def replace_char(string: str, old_char: str, new_char: str) -> str:
    string = string.replace(old_char, new_char)
    return string


def get_nb_char(string: str, char: str) -> int:
    cnt = 0
    for letters in string:
        if letters == char:
            cnt +=1
    return cnt


def get_nb_words(sentence: str) -> int:
    space = " "
    cnt = 1
    for letters in sentence:
        if letters == space:
            cnt+=1
    return cnt


def main() -> None:
    string = "Bonjour!"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")

    string = "hello"
    print(f"Le nombre d'occurrence de l dans hello est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
