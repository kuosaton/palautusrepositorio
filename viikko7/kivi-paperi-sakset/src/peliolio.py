from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class Kaksinpeli:
    def __init__(self):
        self._peli = KPSPelaajaVsPelaaja()

    def pelaa(self):
        self._peli.pelaa()


class Yksinpeli:
    def __init__(self):
        self._peli = KPSTekoaly()

    def pelaa(self):
        self._peli.pelaa()


class HaastavaYksinpeli:
    def __init__(self):
        self._peli = KPSParempiTekoaly()

    def pelaa(self):
        self._peli.pelaa()
