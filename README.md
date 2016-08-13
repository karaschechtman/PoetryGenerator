# PoetryGenerator

By Kara Schechtman

Goals
-----
0. Generate ungrammatical/basic text that matches common verse forms, as well as allowing users to invent their own verse forms (in progress).
1. Create grammatically intelligible poems that match those forms.
2. Given a user-provided plot or theme, and a user-selected verse form, generate metrically correct poetry that matches the plot or theme.
3. Intelligent form violation - Using meanings of words in a poem, create subtle violations of the poem's form that enhance that meaning. So for example, if a line of blank verse is talking about say, reversion, then the computer would recognize that and flip some of the iambs to trochees.
4. Train on real poetry to generate poetry that matches time period, genre, etc..
5. Analysis - perform scansion on poems and recognize their forms forms, identify ambiguities, etc.. Could even try to "understand" or explain poems.
6. Potential addition of support for other languages (could be useful for translation of poems that would go untranslated otherwise; would be able to take into account at least some of the factors of poetic integrity that a human translator could).

Files
-----

###Current
- generatepoem.py - contains the PoemGenerator class. Right now, upon running will generate, as a demo, a line of nonsensical, nongrammatical blank verse and a bunch of rhymes for the word "PEAR," and it will fail to come up with a rhyme for "ORANGE" except the word ORANGE.
- cmudict.rep.txt - Using a syllabized version of the CMU pronouncing dictionary, from https://webdocs.cs.ualberta.ca/~kondrak/cmudict.html.
- FORMS.txt - A mini-corpus of different verse forms

###Soon to be added
- corpusgenerator.py - Will generate the corpus and save to files for faster performance by PoemGenerator class

Current abilities
-----------------
- Grab a word that matches a certain rhyme pattern as expressed in a string of 0s (no stress), 1s (stress), and 2s(secondary stress).
    - So for example, a dactyl = 100; an anapest = 001
- Get a rhyme for any given word
    - Still need to add support to double check it's not returning itself/handle no-rhyme words.
- Generate nonsensical, nongrammatical but formally correct poetry from a given list of verse forms. Here's an example outputted sonnet.

```

A ELIZABETHAN-SONNET
--------------------------------------

EXPECT CHICKED LOWLY KNUT WHOVE STRINGED HYE YOKED
MAZOR DEVOLVE LABREE CHICKED LEAVE CHICKED VAN
CORRECTS WHOVE LOOP BROUSSARD LE KOPPES INVOKED
DEPASS DEMAND CHICKED SPROULS WHOVE PEELING GNANN

IMPAIRS MCQUINN INSURE LE SPEAS IMPLIES
MISTAKE HYE HICKCOX LIMES LE REILLEY KNORR
ER TAMBO WAGLER DARES SUBVERT CHICKED DYES
OBTUSE DEBUNK CHICKED BAILLIE WIEGAND DOERR

HYE ZINC WHOVE HILLOCK BOORDA TOKENS CAY
ER RAYSOR BAY LE BOORDAS WARDA MATCH
ER POLDER FEE APPRISE GIRAUD GERAIS
CHICKED SCHMUHL INCANT MARCOU OBSESSED LE KACH

ATTRIDGE ENDORSED HYE CHUG OBEYS DILATE
ER STEMMING NOUN CHICKED BRUNKOW SHAMAS CATE
```