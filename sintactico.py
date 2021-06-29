import ply.yacc as yacc

from index import tokens, code
from sintac_operaciones import *
from sintac_estructuras import *

def p_all(p):
    '''
    all : sentencias
    '''


def p_sentencia(p):
    '''
    sentencia : declaracion_var
              | asignacion
              | operaciones PUNTO_COMA
              | print
              | estructura_control
              | estructs_metodos PUNTO_COMA
    '''


def p_sentencias(p):
    '''
    sentencias : sentencia 
                | sentencia sentencias
    '''


def p_numero(p):
    '''
    numero : NUM_ENTERO 
            | NUM_DECIMAL
    '''


def p_bool(p):
    '''
    bool : TRUE
          | FALSE 
    '''


def p_datos(p):
    '''
    datos : numero 
          | CADENA_CARAC 
          | bool
          | NULL
    '''

def p_indexacion(p):
    'indexacion : ID ICORCH valor DCORCH'


def p_tipo_dato(p):
    '''
    tipo_dato : BOOL
              | DOUBLE
              | INT
              | STRING
              | VOID
              | LIST
              | SET
              | MAP
    '''
    p[0] = p[1]

def p_declaradores(p):
    '''
    declaradores : VAR
                  | FINAL
                  | tipo_dato
    '''
    p[0] = p[1]


def p_declaracion_var(p):
    '''
    declaracion_var : declaradores ID PUNTO_COMA
    '''
    if(variables_declaradas.get(p[2]) is not None):
      print("La variable ", p[2], " ya ha sido declarada")
      raise SyntaxError
    variables_declaradas[p[2]] = p[1]

def p_declaracion_asign(p):
    '''
    declaracion_asign : declaradores ID ASIGNAR valor PUNTO_COMA
                      | CONST ID ASIGNAR valor PUNTO_COMA
    '''
    if(variables_declaradas.get(p[2]) is not None):
      print("La variable ", p[2], " ya ha sido declarada")
      raise SyntaxError
    variables_declaradas[p[2]] = p[1]

def p_asignacion(p):
    '''
    asignacion : ID ASIGNAR valor PUNTO_COMA
                | ID ICORCH valor DCORCH ASIGNAR valor PUNTO_COMA
                | operacion_autoasig PUNTO_COMA
                | declaracion_asign
    '''


def p_print(p):
    'print : PRINT IPAR valor DPAR PUNTO_COMA'


def p_cuerpo_estruct(p):
    '''
    cuerpo_estruct : ILLAVE sentencias DLLAVE
                    | sentencia
    '''


def p_error(p):
    if p is not None:
        print("Error de sintaxis en la linea %s" % (p.lineno))
    else:
        print("Final de linea inesperado")


# Build the parser
parser = yacc.yacc(start='all')

while True:
    try:
        code = input('calc> ')
    except EOFError:
        break
    if not code:
        continue
    result = parser.parse(code)
    print(result)
