def reverse(st):
    words = st.split()
    answer = ""
    repeat = len(words)
    while repeat:
        repeat -= 1
        answer += words[repeat]
        if repeat != len(words) and repeat != 0:
            answer += " "

    return answer

reverse("hello world hello world")