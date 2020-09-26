#!/usr/local/bin/python3.7

#def tag_bloco(texto,classe='success'):
#    return f'<div class="{classe}">{texto}</div>'

def tag_bloco(texto,classe='success',inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == "__main__":
    #assert tag_bloco('Incluido com sucesso!') == \
        #'<div class="success">Incluido com sucesso!</div>'
    print(tag_bloco('Incluido com sucesso!',inline=True, classe='info'))