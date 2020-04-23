Enkapsulacja - to ukrywanie metod, zmiennych i atrybutów dla klas zewnętrznych.
Dostęp do nich jest możliwy tylko z wewnątrz klasy do której należą lub klas zaprzyjaźnionych
ukryte metody widać poprzez umieszczenie "podłogi" przed nazwą metody


class enkapsulacja:
    _protected_class_attribute = "ProtClassAttr"

        def _protected_method(self):
        print("wywolales metode chroniona")