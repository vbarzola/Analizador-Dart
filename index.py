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

"""
Aporte valeria
"""
t_NUM_ENTERO = r'([1-9]\d+|\d)'
t_NUM_DECIMAL = r'([1-9]\d+|\d)\.\d+'
t_CADENA_CARAC = r'(\'[^\'\n]*\'|"[^"\n]*")'
t_IPAR = r'\('
t_DPAR = r'\)'
t_ICORCH = r'\['
t_DCORCH = r'\]'
t_ILLAVE = r'\{'
t_DLLAVE = r'\}'
t_ASIGNAR = r'='
t_PUNTO_COMA = r';'
t_PUNTO = r'\.'
t_COMA = r','
t_DOS_PUNTOS = r':'
t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_DIVIDIDO = r'\/'
t_DIVISION_ENTERA = r'~\/'
t_MODULO = r'%'
t_AUTOINCREMENTO = r'\+\+'
t_AUTODECREMENTO = r'\-\-'
t_MAYOR_QUE = r'>'
t_MENOR_QUE = r'<'
t_IGUAL_QUE = r'=='
t_DIFERENTE_QUE = r'!='
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='
t_NEGACION = r'!'
t_Y = r'&&'
t_O = r'\|\|'


t_ignore = " \t"