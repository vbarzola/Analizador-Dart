def p_operador_mat(p):
    '''
    operador_mat : MAS
                  | MENOS
                  | POR
                  | DIVIDIDO
                  | DIVISION_ENTERA
                  | MODULO
    '''


def p_operando_mat(p):
    '''
    operando_mat : numero 
                  | ID
    '''


def p_operacion_mat_sin_par(p):
    '''
    operacion_mat_sin_par : operando_mat operador_mat operacion_mat
    '''


def p_operacion_mat_con_par(p):
    '''
    operacion_mat_con_par : IPAR operacion_mat_sin_par DPAR
    '''


def p_operacion_mat(p):
    '''
    operacion_mat : operacion_mat_con_par
                  | operacion_mat_con_par operador_mat operacion_mat
                  | operacion_mat_sin_par
                  | operando_mat
    '''


def p_operador_comp_orden(p):
    '''
    operador_comp_orden : MAYOR_QUE
                  | MENOR_QUE
                  | MENOR_IGUAL
                  | MAYOR_IGUAL
    '''


def p_operando_comp_orden(p):
    '''
    operando_comp_orden : operacion_mat_con_par
                        | numero
                        | ID
    '''


def p_operacion_comp_orden_sin_par(p):
    '''
    operacion_comp_orden_sin_par : operando_comp_orden operador_comp_orden operando_comp_orden 
    '''


def p_operacion_comp_orden_con_par(p):
    '''
    operacion_comp_orden_con_par : IPAR operacion_comp_orden_sin_par DPAR 
    '''


def p_operacion_comp_orden(p):
    '''
    operacion_comp_orden : operacion_comp_orden_sin_par
                        | operacion_comp_orden_con_par
    '''

#eq = equivalencia


def p_operando_comp_eq(p):
    '''
    operando_comp_eq : numero
                    | bool
                    | CADENA_CARAC
                    | operacion_mat_con_par
                    | operacion_comp_orden
                    | operacion_comp_con_par
                    | ID
    '''


def p_operador_comp_eq(p):
    '''
    operador_comp_eq : IGUAL_QUE
                    | DIFERENTE_QUE
    '''


def p_operacion_comp_eq(p):
    '''
    operacion_comp_eq : operando_comp_eq operador_comp_eq operando_comp_eq

    '''


def p_operacion_comp_sin_par(p):
    '''
    operacion_comp_sin_par : operacion_comp_eq
                    | operacion_comp_orden
    '''


def p_operacion_comp_con_par(p):
    '''
    operacion_comp_con_par : IPAR operacion_comp_sin_par DPAR
    '''


def p_operacion_comp(p):
    '''
    operacion_comp : operacion_comp_con_par
                    | operacion_comp_sin_par
    '''


def p_operadores_log(p):
    '''
    operadores_log : Y
                    | O
                    | O_EXCLUSIVO
    '''


def p_operandos_log(p):
    '''
    operandos_log : operacion_comp
                    | operacion_log_not
                    | ID
                    | bool
    '''


def p_operacion_log_sin_par(p):
    '''
    operacion_log_sin_par : operandos_log operadores_log operacion_log
                          | operandos_log
    '''


def p_operacion_log_con_par(p):
    '''
    operacion_log_con_par : IPAR operacion_log_sin_par DPAR 
    '''


def p_operando_log_not(p):
    '''
    operando_log_not : bool
                    | operacion_log_con_par
                    | ID
    '''


def p_operacion_log_not_sin_par(p):
    '''
    operacion_log_not_sin_par : NEGACION operando_log_not
                        |  
    '''


def p_operacion_log_not_con_par(p):
    '''
    operacion_log_not_con_par : IPAR NEGACION operando_log_not DPAR
    '''


def p_operacion_log_not(p):
    '''
    operacion_log_not : operacion_log_not_sin_par
                        | operacion_log_not_con_par
    '''


def p_operacion_log(p):
    '''
    operacion_log : operacion_log_con_par
                  | operacion_log_con_par operadores_log operacion_log
                  | operacion_log_sin_par
                  | operacion_log_not
                  | operandos_log
    '''


def p_operacion_unaria(p):
    '''
    operacion_unaria : ID AUTOINCREMENTO
                      | ID AUTODECREMENTO
                      | AUTOINCREMENTO ID
                      | AUTODECREMENTO ID
    '''


def p_operadores_autoasig(p):
    'operadores_autoasig : operador_mat ASIGNAR'


def p_operacion_autoasig(p):
    '''operacion_autoasig : ID operadores_autoasig operacion_mat'''


def p_operaciones(p):
    '''
    operaciones : operacion_mat
                | operacion_log
                | operacion_unaria
                | operacion_autoasig
    '''