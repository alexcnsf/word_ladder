#!/bin/python3
from collections import deque
from copy import copy

def word_ladder(start_word, end_word, dictionary_file='words5.dict'): 
    if start_word == end_word:
        return [start_word]   
    if len(start_word) != len(end_word):
        return None
    stack = [start_word]
    queue = deque([])
    queue.append(stack)
    with open('words5.dict') as x:
        dictionary = [y.strip() for y in x.readlines()]  
    dictionary.remove(start_word)
    while queue:
            current_stack = queue.popleft()
            current_word = current_stack[-1]
            if current_word == end_word:
                return current_stack
            current_dict = copy(dictionary)
            for next_word in current_dict:
                if _adjacent(current_word, next_word):
                    if next_word in dictionary:
                        new_stack = current_stack.copy()
                        new_stack.append(next_word)
                        queue.append(new_stack)
                        dictionary.remove(next_word)
    return None 
    
 

    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)
    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''


def verify_word_ladder(ladder):
    if ladder:
        count = 0
        for i in range(len(ladder)-1):
            if _adjacent(ladder[i], ladder[i+1]):
                count += 0
            else:
                count += 1
        return (count == 0)
    else:
        return False


    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''


def _adjacent(word1, word2):
    count = 0
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                count += 0
            else:
                count += 1
    else:
        return False
    return count == 1

    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

