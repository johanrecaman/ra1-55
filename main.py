import sys
from rpn_compiler.lexer import parseExpressao

def lerArquivo(file_path, lines):
    try:
        with open(file_path, 'r') as file:
            lines.extend(file.readlines())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Error: Missing input file.")
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    lines = []
    lerArquivo(file_path, lines)

    for line in lines:
        line = line.strip()
        if line:
            tokens = []
            parseExpressao(line, tokens)
            for token in tokens:
                print(token.value, end=' ')

if __name__ == "__main__":
    main()
