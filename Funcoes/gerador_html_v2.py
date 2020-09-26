#!/usr/local/bin/python3.7

def tag_block(conteudo, *args,classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'

def tag_listas(*itens):
    lista = ''.join(f'<li>{i}</li>' for i in itens)
    return f'<ul>{lista}</ul>'

if __name__ == "__main__":
    print(tag_block('bloco'))
    print(tag_block("Texto qualquer",inline=True))
    lis_nomes = ('Ana','Bia','Carla')
    print(tag_listas(*lis_nomes))

    print(tag_block(tag_listas(*lis_nomes),inline=True))

    print(tag_block('Inline e classe', classe='info',inline=False))

    print(tag_block(tag_listas,'Sabado','Domingo',classe='info', inline=False))