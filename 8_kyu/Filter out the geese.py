geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):

    repeat = len(geese)
    while repeat:
        repeat = repeat - 1
        if geese[repeat] in birds:
            birds.remove(geese[repeat])

    return birds
