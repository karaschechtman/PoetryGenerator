# PoetryGenerator

By Kara Schechtman

Generates ungrammatical/basic text that matches common verse forms, as well as allowing users to invent their own verse forms.

Files
-----

### Current
- generatepoem.py - contains the PoemGenerator class. Right now, upon running will generate, as a demo, a line of nonsensical, nongrammatical blank verse and a bunch of rhymes for the word "PEAR," and it will fail to come up with a rhyme for "ORANGE" except the word ORANGE.
- cmudict.rep.txt - Using a syllabized version of the CMU pronouncing dictionary, from https://webdocs.cs.ualberta.ca/~kondrak/cmudict.html.
- FORMS.txt - A mini-corpus of different verse forms

Current abilities
-----------------
- Grab a word that matches a certain rhyme pattern as expressed in a string of 0s (no stress), 1s (stress), and 2s(secondary stress).
    - So for example, a dactyl = 100; an anapest = 001
- Get a rhyme for any given word
    - Still need to add support to double check it's not returning itself/handle no-rhyme words.
- Generate nonsensical, nongrammatical but formally correct poetry from a given list of verse forms. Here's an example outputted sonnet.

Example
-------

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
