#!/usr/local/bin/python3.7

def gen_tag(conteudo,classe='success',tag=True,*args):
    tag = 'div' if tag else 'span'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'

def gen_li(*itens):
    lis = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lis}</ul>'

if __name__ == "__main__":
    print(gen_tag("Nova Tag"))
    print(gen_li('Carol','Leal'))
    print(gen_tag(gen_li,'Sabado','Domingo',classe='Info',tag=False))