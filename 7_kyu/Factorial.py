def factorial(n):
    answer = 1
    repeat = n
    while repeat:
        answer *= repeat
        repeat -= 1

    return(answer)
