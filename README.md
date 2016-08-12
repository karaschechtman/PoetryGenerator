# PoetryGenerator

By Kara Schechtman

Goals
-----
0. Create ungrammatical/basic text that matches common verse forms, as well as allowing users to invent their own verse forms
1. Create grammatically intelligible poems that match those forms
2. Given a user-provided plot or theme, and a user-selected verse form, generate metrically correct poetry that matches the plot or theme. 
3. Train on real poetry to generate poetry that matches time period, genre, etc.
4. Potential addition of other languages (could be useful for translation of poems that would have gone untranslated otherwise) 

Files
-----
- generatepoem.py - my poem generator class. Right now, upon running will generate as a demo, a line of nonsensical, nongrammatical blank verse; specific verse forms to come soon
- cmudict.rep.txt - from https://webdocs.cs.ualberta.ca/~kondrak/cmudict.html

Current abilities
-----------------
- Grab a word that matches a certain rhyme pattern as expressed in a string of 0s (no stress), 1s (stress), and 2s(secondary stress)
    - So for example, a dactyl = 100; an anapest = 001
- Get a rhyme for any given word
    - Still need to add support to double check it's not returning itself/handle no-rhyme words