from django import template

register = template.Library()

BAD_WORDS = ['нежелательное_слово1', 'нежелательное_слово2', 'нежелательное_слово3']

@register.filter(name='censor')
def censor(value):
    words = value.split()
    censored_words = []
    for word in words:
        if word.lower() in BAD_WORDS:
            censored_words.append('*' * len(word))
        else:
            censored_words.append(word)
    return ' '.join(censored_words)
