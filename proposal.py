def levenshtein(a, b):
    i, j = len(a), len(b)

    if not min(i, j):
        return max(i, j)

    return min(
        levenshtein(a[:i - 1], b) + 1,
        levenshtein(a, b[:j - 1]) + 1,
        levenshtein(a[:i - 1], b[:j - 1]) + (1 if a[-1] != b[-1] else 0),
    )


def levenshtein_(a, b):  # according to insertion, retrieve and replacement rules (2, 2, 3)
    i, j = len(a), len(b)

    if not min(i, j):
        return max(i, j)

    return min(
        levenshtein(a[:i - 1], b) + 2,
        levenshtein(a, b[:j - 1]) + 2,
        levenshtein(a[:i - 1], b[:j - 1]) + (3 if a[-1] != b[-1] else 0),
    )


def autocompletion(word, dictionary):
    levenshtein_values = [(w, levenshtein(word, w)) for w in dictionary]

    return min(levenshtein_values, key=lambda value: value[1])


DICTIONARY = [
    "algorithme",
    "ahgorithme",
    "arbre",
    "barbe",
    "globe",
    "orbe",
    "tac",
    "bulbizarre",
    "herbizarre",
    "carapuce",
    "salameche"
]
WORDS = [
    "rythme",
    "arbore",
    # "logarithme",
    "lobe",
    "robe",
    "talc",
    # "carteapuce",
    # "salamuce",
    # "saramuce",
    # "blubizarre",
    # "herbebizarre",
    # "xxxbizarre"
]

if __name__ == '__main__':
    for item in WORDS:
        print(item, autocompletion(item, DICTIONARY))
