import re

token_specs = [
    ('NUMBER',   r'\d+(\.\d*)?'),   # Números inteiros ou decimais
    ('ID',       r'[A-Za-z_]\w*'),  # Identificadores (variáveis)
    ('ASSIGN',   r'='),             # Operador de atribuição
    ('PLUS',     r'\+'),            # Operador de adição
    ('MINUS',    r'-'),             # Operador de subtração
    ('TIMES',    r'\*'),            # Operador de multiplicação
    ('DIVIDE',   r'/'),             # Operador de divisão
    ('LPAREN',   r'\('),            # Parêntese esquerdo
    ('RPAREN',   r'\)'),            # Parêntese direito
    ('SKIP',     r'[ \t]+'),        # Espaços em branco
    ('NEWLINE',  r'\n'),            # Nova linha
    ('MISMATCH', r'.'),             # Qualquer outro caractere
]

token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_specs)

def tokenize(code):
    line_num = 1
    line_start = 0
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group(kind)
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID':
            pass  
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} inesperado na linha {line_num}')
        yield kind, value, line_num, column

def main():
    print("Digite o código a ser analisado (ou pressione Enter para finalizar):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    code = "\n".join(lines) 
    print("\nTokens encontrados:")
    for token in tokenize(code):
        print(token)

if __name__ == '__main__':
    main()
