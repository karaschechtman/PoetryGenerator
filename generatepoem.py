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

        self.meter = Dictlist()

        for word in self.syllables:
            marked = self.syllables[word]
            self.meter[self._getpattern_(marked)] = word

        self.rhymes = Dictlist()
        for word in self.syllables:
            marked = self.syllables[word]
            self.rhymes[self._getrhymepattern_(marked)] = word

    @staticmethod
    def _getstress_(syllablelist):
        stressprocessed = []
        for item in syllablelist:
            number = [char for char in item if char.isdigit()] # stress type
            string = ''.join([char for char in item if char.isalpha()]) # string of digit

            phonemes = item.split(' ')

            phonemestress = ''
            for phoneme in phonemes:
                isdig = False
                for char in phoneme:
                    if char.isdigit() == True:
                        phonemestress = phoneme
                        break

            if (len(number) > 0):
                stressprocessed.append([string,phonemestress,number[0]])
            else:
                stressprocessed.append([string,phonemestress,-1])

        return stressprocessed

    @staticmethod
    def _getpattern_(markedsyllables):
        total = ''
        for syllable in markedsyllables:
            num = syllable[-1]
            total += str(num)
        return total

    @staticmethod
    def _getrhymepattern_(markedsyllables):
        start = 0
        rhymestart = ''
        for i in range (len(markedsyllables)):
            num = markedsyllables[i][-1]
            if str(num) != '0':
                start = i
                rhymestart = ''.join([char for char in markedsyllables[i][1] if char.isalpha()])
                break

        rhymepattern = ''

        for j in range (start,len(markedsyllables)):
            rhymepattern += markedsyllables[j][0]

        mystart = rhymepattern.index(rhymestart)
        return rhymepattern[mystart:]

    def match_pattern(self,pattern):
        return random.choice(self.meter[pattern])

    def rhymefinder(self, word):
        rhymepattern = self._getrhymepattern_(self.syllables[word])
        return random.choice(self.rhymes[rhymepattern])



class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)


def main():
    generator = PoetryGenerator('cmudict.rep.txt')

    print 'generating a line of blank verse: '
    print generator.match_pattern('01'), generator.match_pattern('01'), generator.match_pattern('01'), generator.match_pattern('01'), generator.match_pattern('01')

    print 'finding rhyme for word PEAR:'
    print generator.rhymefinder('PEAR')


    print 'finding rhyme for word ORANGE: (will return itself)'
    print generator.rhymefinder('ORANGE')


main()