from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()


    if lowered == '':
        return "You're awfully quiet maGuyz!"
    elif 'niaje' in lowered:
        return 'Fiti, mambo iko poa!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice(["I don't understand...",
                       "What are you on about?",
                       "Do you mind kurudia kenye umesema?"])
    
