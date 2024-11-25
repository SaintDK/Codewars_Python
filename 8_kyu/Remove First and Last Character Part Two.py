answer = ""
def array(string):
    if len(string) < 4:
        return None
    else:
        answer = string[2:-2]
        return answer.replace(","," ")