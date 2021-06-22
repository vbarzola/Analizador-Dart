from ply import lex
"""
Aporte valeria
"""
reservadas = {
    'bool': 'BOOL',
    'break': 'BREAK',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'double': 'DOUBLE',
    'else': 'ELSE',
    'false': 'FALSE',
    'final': 'FINAL',
    'for': 'FOR',
    'function': 'FUNCTION',
    'if': 'IF',
    'import': 'IMPORT',
    'in': 'IN',
    'int': 'INT',
    'List': 'LIST',
    'Map': 'MAP',
    'null': 'NULL',
    'print': 'PRINT',
    'readLineSync': 'READ_LINE_SYNC',
    'return': 'RETURN',
    'Set': 'SET',
    'stdin': 'STDIN',
    'String': 'STRING',
    'true': 'TRUE',
    'var': 'VAR',
    'void': 'VOID',
    'while': 'WHILE'
}


"""
Aporte Alex
"""
tokens = ["ID", "NUM_ENTERO", "NUM_DECIMAL", "CADENA_CARAC",
          "IPAR", "DPAR", "ICORCH", "DCORCH", "ILLAVE", "DLLAVE",
          "ASIGNAR", "PUNTO_COMA", "PUNTO", "COMA", "DOS_PUNTOS",
          "MAS", "MENOS", "POR", "DIVIDIDO", "DIVISION_ENTERA", "MODULO",
          "AUTOINCREMENTO", "AUTODECREMENTO",
          "MAYOR_QUE", "MENOR_QUE", "IGUAL_QUE", "DIFERENTE_QUE", "MENOR_IGUAL", "MAYOR_IGUAL",
          "NEGACION", "Y", "O"
          ] + list(reservadas.values())
