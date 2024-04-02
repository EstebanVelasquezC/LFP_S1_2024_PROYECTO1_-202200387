def generate_html(tokens):
    html_content = "<!DOCTYPE html>\n<html>\n<head>\n<meta charset='UTF-8'>\n"

    # Titulo de la página
    for token_type, token_value, _ in tokens:
        if token_type == 'TITULO_PAGINA':
            html_content += f"<title>{token_value}</title>\n"
            break
    else:
        html_content += "<title>Documento HTML generado</title>\n"

    # Estilos CSS
    html_content += "<style>\n"
    html_content += "body { font-family: Arial, sans-serif; }\n"
    html_content += "h1 { color: #FF0000; }\n"
    html_content += "p { font-size: 16px; }\n"
    html_content += ".code { font-family: 'Courier New', monospace; background-color: #f0f0f0; padding: 10px; }\n"
    html_content += "strong { font-weight: bold; }\n"
    html_content += "u { text-decoration: underline; }\n"
    html_content += "s { text-decoration: line-through; }\n"
    html_content += "em { font-style: italic; }\n"
    html_content += "table { border-collapse: collapse; width: 100%; }\n"
    html_content += "th, td { border: 1px solid #dddddd; text-align: left; padding: 8px; }\n"
    html_content += "</style>\n"

    html_content += "</head>\n<body>\n"

    in_table = False
    in_row = False
    for token_type, token_value, _ in tokens:
        if token_type == 'TABLA':
            html_content += "<table>\n"
            in_table = True
        elif token_type == 'ELEMENTOS' and in_table:
            in_row = False
        elif token_type == 'ELEMENTO' and in_table:
            if not in_row:
                html_content += "<tr>\n"
                in_row = True
            html_content += f"<td>{token_value}</td>\n"
        elif token_type == 'CIERRE_LISTA_ELEMENTOS' and in_table and in_row:
            html_content += "</tr>\n"
            in_row = False
        elif token_type == 'CIERRE' and in_table:
            html_content += "</table>\n"
            in_table = False
        elif not in_table:
            if token_type == 'ENCABEZADO':
                html_content += f"<h1>{token_value}</h1>\n"
            elif token_type == 'PARRAFO':
                html_content += f"<p>{token_value}</p>\n"
            elif token_type == 'TEXTO':
                html_content += f"<p>{token_value}</p>\n"
            elif token_type == 'CODIGO':
                html_content += f"<div class='code'>{token_value}</div>\n"
            elif token_type == 'NEGRITA':
                html_content += f"<strong>{token_value}</strong>\n"
            elif token_type == 'SUBRAYADO':
                html_content += f"<u>{token_value}</u>\n"
            elif token_type == 'TACHADO':
                html_content += f"<s>{token_value}</s>\n"
            elif token_type == 'CURSIVA':
                html_content += f"<em>{token_value}</em>\n"
            elif token_type == 'SALTO':
                html_content += "<br>\n"

    html_content += "</body>\n</html>"
    return html_content

