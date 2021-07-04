import ply.yacc as yacc

from index import construir_lexer, tokens, code, find_column
from estado import manejar_estado
from sintac_operaciones import *
from sintac_estructuras import *


def p_all(p):
    '''
    all : simbolos_globales
    '''


def p_simbolo_global(p):
    '''
    simbolo_global : declaracion_asign
                    | funcion
                    | import
    '''


def p_simbolos_globales(p):
    '''
    simbolos_globales : simbolo_global
                      | simbolo_global simbolos_globales
                      | empty
    '''


def p_empty(p):
    '''
    empty :
    '''


def p_sentencia(p):
    '''
    sentencia : declaracion_var
              | asignacion
              | declaracion_asign
              | operaciones PUNTO_COMA
              | print
              | estructura_control
              | estructs_metodos PUNTO_COMA
              | return
              | continue
              | break
    '''


def p_sentencias(p):
    '''
    sentencias : sentencia
                | sentencia sentencias
                | empty
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


def p_valor(p):
    '''
    valor : datos
          | operaciones
          | ID
          | estructura_dato
          | indexacion
          | estructs_metodos
          | read
          | ejecutar_funcion
          | negativo
          | casting
    '''


def p_negativo(p):
    '''
    negativo : MENOS numero
              | MENOS ID
              | MENOS indexacion
              | MENOS ejecutar_funcion

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
    declaradores : tipo_dato
                  | FINAL
                  | VAR
    '''
    p[0] = p[1]


def p_declaracion_var(p):
    '''
    declaracion_var : declaradores ID PUNTO_COMA
    '''


def p_declaracion_asign(p):
    '''
    declaracion_asign : tipo_dato ID ASIGNAR valor PUNTO_COMA
                      | FINAL ID ASIGNAR valor PUNTO_COMA
                      | VAR ID ASIGNAR valor PUNTO_COMA
                      | CONST ID ASIGNAR valor PUNTO_COMA
    '''


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


def p_for(p):
    '''
    for : FOR IPAR asignacion operacion_log PUNTO_COMA operaciones DPAR cuerpo_estruct
        | FOR IPAR ID IN ID DPAR cuerpo_estruct
        | FOR IPAR tipo_dato ID IN ID DPAR cuerpo_estruct
        | FOR IPAR VAR ID IN ID DPAR cuerpo_estruct
    '''


def p_if(p):
    '''
    if : IF IPAR operacion_log DPAR cuerpo_estruct
    '''


def p_if_else(p):
    '''
    if_else : IF IPAR operacion_log DPAR cuerpo_estruct ELSE cuerpo_estruct
    '''


def p_while(p):
    '''
    while : WHILE IPAR operacion_log DPAR cuerpo_estruct
    '''


def p_estructura_control(p):
    '''
    estructura_control : if
                        | if_else
                        | while
                        | for
    '''


def p_break(p):
    'break : BREAK PUNTO_COMA'


def p_continue(p):
    'continue : CONTINUE PUNTO_COMA'


def p_read(p):
    '''
    read : STDIN PUNTO READ_LINE_SYNC IPAR DPAR
    '''


def p_import(P):
    'import : IMPORT CADENA_CARAC PUNTO_COMA'


def p_return(p):
    '''
    return : RETURN valor PUNTO_COMA
            | RETURN PUNTO_COMA
    '''


def p_arg_funcion(p):
    '''
    arg_funcion : ID
                | VAR ID
                | tipo_dato ID
    '''


def p_args_funcion(p):
    '''
    args_funcion : arg_funcion COMA args_funcion
                  | arg_funcion
                  | empty
    '''


def p_declarar_funcion(p):
    '''
    funcion : tipo_dato ID IPAR args_funcion DPAR ILLAVE sentencias DLLAVE
    '''


def p_ejecutar_funcion(p):
    '''
    ejecutar_funcion : ID IPAR valores DPAR
                      | ID IPAR DPAR
    '''


def p_casting(p):
    'casting : IPAR valor AS tipo_dato DPAR'
    p[0] = p[4]


def p_error(p):
    manejar_estado.err_sintacticos += 1
    print(code)
    if p is not None:
        col = find_column(manejar_estado.codigo, p)
        print(
            f"Error de sintaxis antes de definir '{p.value}' en la linea {p.lineno}, en la columna {col}")
        manejar_estado.descr_err_sintacticos += f"Error de sintaxis antes de definir '{p.value}' en la linea {p.lineno}, en la columna {col}.\n\n"
    else:
        print("Final de linea inesperado")
        manejar_estado.descr_err_sintacticos = "Final de linea inesperado\n"


# Build the parser
code = ''


def prueba():
    parser = yacc.yacc(start='operaciones', debug=True)
    while True:
        code = input('comp> ')
        result = parser.parse(code)
        print(result)

# parser = yacc.yacc(start='all')
# with open('prueba.txt') as f:
#     code = ''.join(f.readlines())
#     result = parser.parse(code)
# print(result)


def analizar_sintac(codigo):
    manejar_estado()
    manejar_estado.codigo = codigo
    construir_lexer()
    code = codigo
    parser = yacc.yacc(start='all')
    parser.parse(code)
    return manejar_estado
