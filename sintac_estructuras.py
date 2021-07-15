from estado import manejar_estado


def p_valores(p):
    '''
    valores : valor
            | valor COMA valores
    '''


def p_clave_valor(p):
    '''
      clave_valor : valor DOS_PUNTOS valor
    '''


def p_claves_valores(p):
    '''
    claves_valores : clave_valor
                    | clave_valor COMA claves_valores
    '''


def p_lista(p):
    '''
    lista : ICORCH valores DCORCH
          | ICORCH DCORCH
    '''


def p_lista_metodos_var(p):
    '''
    lista_metodos_var : ID PUNTO JOIN IPAR CADENA_CARAC DPAR
                  | ID PUNTO JOIN IPAR DPAR
                  | ID PUNTO INDEXOF IPAR valor DPAR
                  | ID PUNTO INDEXOF IPAR valor COMA valor DPAR
                  | ID PUNTO ADD IPAR valor DPAR
                  | ID PUNTO LENGTH
    '''

#Regla semántica
def p_lista_metodos_estruct(p):
    '''
    lista_metodos_estruct : lista PUNTO JOIN IPAR CADENA_CARAC DPAR
                  | lista PUNTO JOIN IPAR DPAR
                  | lista PUNTO INDEXOF IPAR valor DPAR
                  | lista PUNTO INDEXOF IPAR valor COMA valor DPAR
                  | lista PUNTO ADD IPAR valor DPAR
                  | lista PUNTO LENGTH
    '''


def p_lista_metodos(p):
    '''
    lista_metodos : lista_metodos_var
                  | lista_metodos_estruct 
    '''


def p_conjunto(p):
    '''
    conjunto : ILLAVE valores DLLAVE
              | ILLAVE DLLAVE
    '''


def p_conjunto_metodos_var(p):
    '''
    conjunto_metodos_var : ID PUNTO CONTAINS IPAR valor DPAR
                    | ID PUNTO DIFFERENCE IPAR conjunto DPAR
                    | ID PUNTO DIFFERENCE IPAR ID DPAR
                    | ID PUNTO UNION IPAR conjunto DPAR
                    | ID PUNTO UNION IPAR ID DPAR
    '''


#Regla semántica
def p_conjunto_metodos_struct(p):
    '''
    conjunto_metodos_struct : conjunto PUNTO CONTAINS IPAR valor DPAR
                            | conjunto PUNTO DIFFERENCE IPAR conjunto DPAR
                            | conjunto PUNTO DIFFERENCE IPAR ID DPAR
                            | conjunto PUNTO UNION IPAR conjunto DPAR
                            | conjunto PUNTO UNION IPAR ID DPAR
    '''


def p_conjunto_metodos(p):
    '''
    conjunto_metodos : conjunto_metodos_var
                     | conjunto_metodos_struct
    '''


def p_mapa(p):
    '''
    mapa : ILLAVE claves_valores DLLAVE
        | ILLAVE DLLAVE
    '''


def p_mapa_metodos_var(p):
    '''
    mapa_metodos_var : ID PUNTO REMOVE IPAR valor DPAR
                    | ID PUNTO CLEAR IPAR DPAR
                    | ID PUNTO CONTAINSKEY IPAR valor DPAR
    '''


#Regla semántica
def p_mapa_metodos_struct(p):
    '''
    mapa_metodos_struct : mapa PUNTO REMOVE IPAR valor DPAR
                        | mapa PUNTO CLEAR IPAR DPAR
                        | mapa PUNTO CONTAINSKEY IPAR valor DPAR
    '''


def p_mapa_metodos(p):
    '''
    mapa_metodos : mapa_metodos_var
                 | mapa_metodos_struct
    '''


def p_estructura_dato(p):
    '''
    estructura_dato : lista
                    | conjunto
                    | mapa
    '''


def p_estructs_metodos(p):
    '''
    estructs_metodos : lista_metodos
                      | conjunto_metodos
                      | mapa_metodos
    '''
