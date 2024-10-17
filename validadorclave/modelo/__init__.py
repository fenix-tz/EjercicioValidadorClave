# validador.py
from errores import ReglaValidacionGanimedesError, ReglaValidacionCalistoError

class ReglaValidacion:
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        if len(clave) <= self._longitud_esperada:
            raise self.error_class(f"La clave debe tener una longitud de más de {self._longitud_esperada} caracteres")

    def _contiene_mayuscula(self, clave):
        if not any(c.isupper() for c in clave):
            raise self.error_class("La clave debe contener al menos una letra mayúscula")

    def _contiene_minuscula(self, clave):
        if not any(c.islower() for c in clave):
            raise self.error_class("La clave debe contener al menos una letra minúscula")

    def _contiene_numero(self, clave):
        if not any(c.isdigit() for c in clave):
            raise self.error_class("La clave debe contener al menos un número")

    def es_valida(self, clave):
        raise NotImplementedError("Este método debe ser implementado por subclases")


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)
        self.error_class = ReglaValidacionGanimedesError

    def contiene_caracter_especial(self, clave):
        if not any(c in '@_#$%' for c in clave):
            raise self.error_class("La clave debe contener al menos un caracter especial (@, _, #, $, %)")

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_caracter_especial(clave)
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)
        self.error_class = ReglaValidacionCalistoError

    def contiene_calisto(self, clave):
        count = sum(1 for c in clave if c in 'CALISTO')
        if count < 2 or count == len('CALISTO'):
            raise self.error_class("La palabra calisto debe estar escrita con al menos dos letras en mayúscula")

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_numero(clave)
        self.contiene_calisto(clave)
        return True


class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        return self.regla.es_valida(clave)