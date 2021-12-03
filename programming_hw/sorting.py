import random
import timeit

def sequential_search(sequence, item, verbose=False):
    if verbose:
        print(f'sequential_search() invoked,',
              f'item={item}, sequence={sequence}')
    for index in range(len(sequence)):
        if verbose:
            print(f'index={index}, sequence[index]={sequence[index]}')
        if sequence[index] == item:
            return index
    return None

def binary_search(sequence, item, verbose=False):
    if verbose:
        print(f'binary_search() invoked,',
              f'item={item}, sequence={sequence}')
    first = 0
    last = len(sequence) - 1  # last is INCLUSIVE

    while first <= last:
        mid = (first + last) // 2
        if verbose:
            print(f'first={first}, mid={mid}, last={last},',
                  f'sequence[mid]={sequence[mid]}')
        if sequence[mid] == item:
            return mid
        if item < sequence[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return None

def timeit_search(func, n, repetition=None):
    """Return the execution time of func() for repetition times,
       for the problem size of n
    """
    if repetition == None:
        repetition = n

    t = list(range(n))
    duration = timeit.timeit('func(t, random.randrange(n))',
                             setup='import random',
                             globals=locals(),
                             number=repetition)
    return duration

if __name__ == '__main__':
    # 1)
    n = 10
    item = 5

    t = list(range(n))
    random.shuffle(t)  # make a random list
    print(f'Searching {item} in {t}...')
    print('sequential:',  sequential_search(t, item, True))
    print('binary :',  binary_search(t, item, True))

    # 2)
    print(sequential_search([], 1))
    print(sequential_search([1], 1))
    print(sequential_search([2], 1))
    print(sequential_search([1, 2], 1))
    print(sequential_search([2, 1], 1))
    print(sequential_search([1, 2], 2))
    print(sequential_search([2, 1], 2))
    print(sequential_search([1, 2], 3))
    print(sequential_search([2, 1], 3))

    n = 100
    t = list(range(n))
    random.shuffle(t)
    print('t =', t)
    for i in range(n):
        index = sequential_search(t, i)
        if index == None:
            # since the list contains 0..(n-1), None shouldn't be returned
            print(f'There is a problem when looking for {i} in t')
        else:
            print(f'The index of the value {i}: {index}')

    # 3)
    problem_sizes = [1, 10, 20, 50, 100]
    rep = 100
    print('Sequential search...')
    for n in problem_sizes:
        print(f'{n:5d}:', timeit_search(sequential_search, n, rep))

    print('Binary search...')
    for n in problem_sizes:
        print(f'{n:5d}:', timeit_search(binary_search, n, rep))