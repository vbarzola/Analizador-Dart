variables_declaradas = {}

def p_valor(p):
    '''
    valor : datos
          | operaciones
          | ID
          | estructura_dato
          | indexacion
          | estructs_metodos
    '''


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

def p_lista_join(p):
    '''
    lista_metodos : ID PUNTO JOIN IPAR CADENA_CARAC DPAR
                  | ID PUNTO JOIN IPAR DPAR
                  | ID PUNTO INDEXOF IPAR valor DPAR
                  | ID PUNTO INDEXOF IPAR valor COMA valor DPAR
                  | ID PUNTO ADD IPAR valor DPAR
    '''
    verificar_tipo(p, 'List')

def p_conjunto(p):
    '''
    conjunto : ILLAVE valores DLLAVE
              | ILLAVE DLLAVE
    '''

def p_verif_conjunto(p):
    'verif_conjunto : ID'
    p[0] = p[1]
    verificar_tipo(p, 'Set')


def p_conjunto_metodos(p):
    '''
    conjunto_metodos : ID PUNTO CONTAINS IPAR valor DPAR
                    | ID PUNTO DIFFERENCE IPAR conjunto DPAR
                    | ID PUNTO DIFFERENCE IPAR verif_conjunto DPAR
                    | ID PUNTO UNION IPAR conjunto DPAR
                    | ID PUNTO UNION IPAR verif_conjunto DPAR
    '''
    verificar_tipo(p,'Set')

def p_mapa(p):
    '''
    mapa : ILLAVE claves_valores DLLAVE
        | ILLAVE DLLAVE
    '''

def p_mapa_metodos(p):
    '''
    mapa_metodos : ID PUNTO REMOVE IPAR valor DPAR
                    | ID PUNTO CLEAR IPAR DPAR
                    | ID PUNTO CONTAINSKEY IPAR valor DPAR
    '''
    verificar_tipo(p,'Map')

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
  
def verificar_tipo(p, tipo_dato_req):
    tipo_dato = variables_declaradas.get(p[1])
    if tipo_dato is None:
      print("Esta variable no ha sido definida aun.")
      raise SyntaxError
    elif tipo_dato != tipo_dato_req:
        print("Este tipo de dato no tiene este método")
        raise SyntaxError
  