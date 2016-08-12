import os
import random

class PoetryGenerator:
    def __init__(self,dictionary):
        dictionaryfile = open(dictionary,'r')
        lines = [line for line in dictionaryfile.readlines() if line[0].isalpha()]

        self.syllables = {}

        for line in lines:
            word = ''.join([char for char in line.split('  ')[0] if char.isalpha()])
            notword = line[len(word):].strip()
            syllablelist = notword.split(' - ')
            markedsyllables = self._getstress_(syllablelist)
            self.syllables[word] = markedsyllables

        self.characterizations = Dictlist()

        for word in self.syllables:
            marked = self.syllables[word]
            self.characterizations[self._getpattern_(marked)] = word


    @staticmethod
    def _getstress_(syllablelist):
        stressprocessed = []
        for item in syllablelist:
            number = [char for char in item if char.isdigit()]
            string = ''.join([char for char in item if char.isalpha()])

            if (len(number) > 0):
                stressprocessed.append([string,number[0]])
            else:
                stressprocessed.append([string,-1])

        return stressprocessed

    @staticmethod
    def _getpattern_(markedsyllables):
        total = ''
        for syllable in markedsyllables:
            num = syllable[-1]
            total += str(num)
        return total

    def match_pattern(self,pattern):
        return random.choice(self.characterizations[pattern])

class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)

generator = PoetryGenerator('cmudict.rep.txt')

print 'generating a line of blank verse: '
print generator.match_pattern('01'), generator.match_pattern('01'), generator.match_pattern('01'), generator.match_pattern('01'), generator.match_pattern('01')
