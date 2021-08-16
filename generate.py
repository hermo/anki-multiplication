#!/usr/bin/env python3
import genanki

# Generate multiplication table for num num x start ... num x end
# using given model and deck
def generate(model, deck, num, start, end):
    for n in range(start, end+1):
        a = num
        b = n
        c = a*b
        card_a = genanki.Note(
            model=model,
            tags=['a', f'{a}x'],
            fields=[f'? x {b} = {c}', f'{a}'])
        card_b = genanki.Note(
            model=model,
            tags=['b', f'{a}x'],
            fields=[f'{a} x ? = {c}', f'{b}'])
        card_c = genanki.Note(
            model=model,
            tags=['c', f'{a}x'],
            fields=[f'{a} x {b} = ?', f'{c}'])

        deck.add_note(card_a)
        deck.add_note(card_b)
        deck.add_note(card_c)


def create_model(title): 
    return genanki.Model(
            56764534343,
            title,
            fields=[
                {'name': 'Kysymys'},
                {'name': 'Vastaus'},
            ],
            templates=[
                {
                    'name': 'Kortti 1',
                    'qfmt': '{{Kysymys}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{Vastaus}}',
                },
            ])

def create_deck(title):
    return genanki.Deck(
            2345454363,
            title)


title = '3 ja 4 kertotaulut'

model = create_model(title)
deck = create_deck(title)

# 3x1 ... 3x10
generate(model, deck, 3, 1, 10)
# 4x1 ... 4x10
generate(model, deck, 4, 1, 10)

filename = '3_ja_4.apkg'
genanki.Package(deck).write_to_file(filename)
