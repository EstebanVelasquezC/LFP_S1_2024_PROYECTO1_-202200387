import re

# Aquí va el resto del código...

def translate(tokens):
    html_code = "<!DOCTYPE html>\n<html>\n<head>\n"

    for token_type, token_value, _ in tokens:
        if token_type == "ENCABEZADO":
            # Traducir el título de la página
            title = get_title(token_value)
            html_code += f"<title>{title}</title>\n"
        # Agregar aquí lógica para otros tipos de tokens
        
    html_code += "</head>\n<body>\n</body>\n</html>"
    
    return html_code

def get_title(token_value):
    match = re.search(r'"(.*?)"', token_value)
    if match:
        return match.group(1)
    return ""
