#!/usr/local/bin/python3.7

def tag_block(texto,classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == "__main__":
    print(tag_block('bloco'))
    print(tag_block("Texto qualquer",inline=True))