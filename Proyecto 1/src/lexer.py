import re

tokens = [
    ('INICIO', r'^\s*Inicio\s*:\s*{'),
    ('ENCABEZADO', r'^\s*Encabezado\s*:\s*{'),
    ('TITULO_PAGINA', r'^\s*TituloPagina\s*:\s*"(.*?)"'),
    ('PARRAFO', r'^\s*Parrafo\s*:\s*{'),
    ('TEXTO', r'^\s*Texto\s*:\s*{'),
    ('FUENTE', r'^\s*fuente\s*=\s*"(.*?)"'),
    ('COLOR', r'^\s*color\s*=\s*"(.*?)"'),
    ('TAMANO', r'^\s*tamaño\s*=\s*"(.*?)"'),
    ('CODIGO', r'^\s*Codigo\s*:\s*{'),
    ('NEGRITA', r'^\s*Negrita\s*:\s*{'),
    ('SUBRAYADO', r'^\s*Subrayado\s*:\s*{'),
    ('TACHADO', r'^\s*Tachado\s*:\s*{'),
    ('CURSIVA', r'^\s*Cursiva\s*:\s*{'),
    ('SALTO', r'^\s*Salto\s*:\s*{'),
    ('TABLA', r'^\s*Tabla\s*:\s*{'),
    ('ELEMENTOS', r'^\s*elementos\s*:\s*\['),
    ('ELEMENTO', r'^\s*elemento\s*:\s*{'),
    ('FILA', r'^\s*"fila"\s*:\s*"\d+"'),
    ('COLUMNA', r'^\s*"columna"\s*:\s*"\d+"'),
    ('TEXTO_CELDA', r'^\s*"texto"\s*:\s*"(.*?)"'),
    ('CIERRE', r'^\s*},?'),  
    ('CIERRE_LISTA_ELEMENTOS', r'^\s*]'),
    ('COMENTARIO', r'^\s*#.*'),
    ('ERROR', r'^.*')  
]

def lex(file_content):
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens)
    line_number = 0

    for line in file_content.split('\n'):
        line_number += 1
        for match in re.finditer(token_regex, line, re.IGNORECASE):
            token_type = match.lastgroup
            token_value = match.group(token_type)
            if token_type != 'COMENTARIO' and token_type != 'ERROR':
                yield token_type, token_value.strip(), line_number
            elif token_type == 'ERROR' and token_value.strip():  
                yield 'ERROR', token_value.strip(), line_number
            elif token_type == 'COMENTARIO':
                break