class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if kapasiteetti != 5:
            if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
                raise Exception("Virheellinen kapasiteetti")
        self.kapasiteetti = kapasiteetti

        if kasvatuskoko != 5:
            if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
                raise Exception("Virheellinen kasvatuskoko")
        self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def mahtavuus(self):
        return self.alkioiden_lkm

    def kuuluu(self, n):
        return n in self.ljono

    def lista_taynna(self):
        return self.alkioiden_lkm == len(self.ljono)

    def _laajenna_listaa(self):
        for _ in range(self.kasvatuskoko):
            self.ljono.append(0)

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.alkioiden_lkm += 1
            return True

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.lista_taynna():
                self._laajenna_listaa()

            return True

        return False

    def poista(self, n):
        if self.kuuluu(n):
            self.ljono.remove(n)
            self.ljono.append(0)
            self.alkioiden_lkm -= 1
            return True

        return False

    def kopioi_lista(self, alkuperainen, kopio):
        for i in range(0, len(alkuperainen)):
            kopio[i] = alkuperainen[i]

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)
        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdistejoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdistejoukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdistejoukko.lisaa(b_taulu[i])

        return yhdistejoukko

    @staticmethod
    def leikkaus(a, b):
        leikkausjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkausjoukko.lisaa(b_taulu[j])

        return leikkausjoukko

    @staticmethod
    def erotus(a, b):
        erotusjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            erotusjoukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotusjoukko.poista(b_taulu[i])

        return erotusjoukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos += str(self.ljono[i])
                tuotos += ", "
            tuotos += str(self.ljono[self.alkioiden_lkm - 1])
            tuotos += "}"
            return tuotos
