# a simple translator of the Greek alphabet into the English version


# dictionary mapping Greek letters to English
greek_letters = {
    "Α" : "A",
    "α" : "a",
    "Β" : "B",
    "β" : "b",
    "Γ" : "C",
    "γ" : "c",
    "Δ" : "D",
    "δ" : "d",
    "Ε" : "E",
    "ε" : "e",
    "Ζ" : "Z",
    "ζ" : "z",
    "Η" : "H",
    "η" : "h",
    "Θ" : "TH",
    "θ" : "th",
    "Ι" : "I",
    "ι" : "i",
    "Κ" : "K",
    "κ" : "k",
    "Λ" : "L",
    "λ" : "l",
    "Μ" : "M",
    "μ" : "m",
    "Ν" : "N",
    "ν" : "n",
    "Ξ" : "KS",
    "ξ" : "ks",
    "Ο" : "O",
    "ο" : "o",
    "Π" : "P",
    "π" : "p",
    "Ρ" : "R",
    "ρ" : "r",
    "Σ" : "S",
    "σ" : "s",
    "Τ" : "T",
    "τ" : "t",
    "Υ" : "Y",
    "υ" : "u",
    "Φ" : "F",
    "φ" : "f",
    "Χ" : "X",
    "χ" : "x",
    "Ψ" : "PS",
    "ψ" : "ps",
    "Ω" : "O",
    "ω" : "o",
    "ς" : "s"
}

# function that translates the phrase given
def translate(phrase):
    # make an empty variable to do the translation
    translation = ""
    # loop all the letters of phrase
    for letter in phrase:
        # search in the dictionary if the letter mapps
        if letter in greek_letters:
            # add to the translation variable the mapping letter of the Greek one
            translation = translation + greek_letters[letter]
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase in the greek alphabet : ")))                
