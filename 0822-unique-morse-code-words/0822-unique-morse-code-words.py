class Solution:

    def __init__(self):
        self.morseArr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    def getMorseValue(self, char: str) -> str:
        index: int = ord(char) - 97
        return self.morseArr[index]

    def getMorseCode(self, word: str) -> str:
        res = ""
        for letter in word:
            res += self.getMorseValue(letter)
        return res


    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        morseSet = set()

        for word in words:
            morseSet.add(self.getMorseCode(word))

        return len(morseSet)


        