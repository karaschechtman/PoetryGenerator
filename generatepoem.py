import random

class PoetryGenerator:
    def __init__(self,dictionary):
        self.forms = {}
        self.syllables = {}
        self.meter = Dictlist()
        self.rhymes = Dictlist()


        # save all the forms
        formlist = open('FORMS.txt', 'r')
        formlines = [line for line in formlist.readlines()]
        for form in formlines:
            tokens = form.split("|")
            poem = []
            key = tokens[0].strip()
            for token in tokens[1:]:
                lines = token.split("/")
                stanza = []
                for line in lines:
                    line = line.strip()
                    stanza.append([line.split(" ")[0],line.split(" ")[1]])

                poem.append(stanza)
            self.forms[key] = poem

        # generate the syllable list
        dictionaryfile = open(dictionary,'r')
        lines = [line for line in dictionaryfile.readlines() if line[0].isalpha()]

        for line in lines:
            word = ''.join([char for char in line.split('  ')[0] if char.isalpha()])
            notword = line[len(word):].strip()
            syllablelist = notword.split(' - ')
            markedsyllables = self._getstress_(syllablelist)
            self.syllables[word] = markedsyllables

        # generate the meters Dictlist
        for word in self.syllables:
            marked = self.syllables[word]
            self.meter[self._getpattern_(marked)] = word

        # generate the rhymes Dictlist
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
        return self.meter[pattern]

    def rhymefinder(self, word):
        rhymepattern = self._getrhymepattern_(self.syllables[word])
        return self.rhymes[rhymepattern]

    def generate_line(self,linescheme,mapping):
        meter = linescheme[0]
        rhyme = linescheme[1]
        self.metertokenize()

    @staticmethod
    def totokens(metertoken):
        i = 0
        tokens = []
        syllable = PoetryGenerator.generatesyllable()
        while i + syllable < (len(metertoken)):
            word = metertoken[i:i+syllable]
            tokens.append(word)
            i+=syllable
            syllable = PoetryGenerator.generatesyllable()

        if i < len(metertoken):
            word = metertoken[i:]
            tokens.append(word)
        return tokens

    @staticmethod
    def generatesyllable():
        number = random.choice(range(100))
        syllable = 0
        if number < 50:
            syllable = 1
        else:
            syllable = 2
        return syllable

    def generate_poem(self,poemtype):
        scheme = self.forms[poemtype]
        rhymemapping = Dictlist()

        print '\nA ' + poemtype
        print '-------------------------------------- \n'
        for stanza in scheme:
            for line in stanza:
                wordmeter = PoetryGenerator.totokens(line[0])
                textline = ''
                rhymekey = line[1]

                for i, word in enumerate(wordmeter):
                    if i == len(wordmeter)-1:
                        meterset = set(self.match_pattern(word))
                        if (rhymekey in rhymemapping):
                            rhymeset = set(self.rhymefinder(random.choice(rhymemapping[rhymekey])))
                        else:
                            matchfound = False
                            while (matchfound != True):
                                newrhyme = random.choice(list(meterset))
                                rhymeset = set(self.rhymefinder(newrhyme))
                                overlaps = rhymeset.intersection(meterset)
                                if (len(overlaps) > 0):
                                    matchfound = True

                        finalword = random.choice(list(rhymeset.intersection(meterset)))
                        rhymemapping[rhymekey] = finalword
                        textline += finalword
                    else:
                        textline += random.choice(self.match_pattern(word)) + ' '
                print textline

            print ''
class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)


def main():
    generator = PoetryGenerator('cmudict.rep.txt')

    print 'Generating a line of blank verse: '
    print random.choice(generator.match_pattern('01')), random.choice(generator.match_pattern('01')), random.choice(generator.match_pattern('01')), random.choice(generator.match_pattern('01')), random.choice(generator.match_pattern('01'))

    generator.generate_poem('ELIZABETHAN-SONNET')


main()