# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Buis import Buis
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.KlRioleringsbuisFunctie import KlRioleringsbuisFunctie
from OTLMOW.OTLModel.Datatypes.KlRioleringsbuisMateriaal import KlRioleringsbuisMateriaal
from OTLMOW.OTLModel.Datatypes.KlSterktereeks import KlSterktereeks


# Generated with OTLClassCreator. To modify: extend, do not edit
class Rioleringsbuis(Buis):
    """Ondergronds kanaal of pijp voor gravitaire afvoer van water."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecokoker')

        self._aantalAfgedichteAansluitingen = OTLAttribuut(field=IntegerField,
                                                           naam='aantalAfgedichteAansluitingen',
                                                           label='Aantal afgedichte aansluitingen',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.aantalAfgedichteAansluitingen',
                                                           definition='De afgedichte verlaten aansluitingsopeningen van straatkolken en/of huisaansluitingen in de rioleringsbuis.',
                                                           owner=self)

        self._functie = OTLAttribuut(field=KlRioleringsbuisFunctie,
                                     naam='functie',
                                     label='functie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.functie',
                                     definition='Bepaalt de functie van de rioleringsbuis.',
                                     owner=self)

        self._materiaal = OTLAttribuut(field=KlRioleringsbuisMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.materiaal',
                                       definition='Bepaalt het materiaal van de rioleringsbuis.',
                                       owner=self)

        self._sterktereeks = OTLAttribuut(field=KlSterktereeks,
                                          naam='sterktereeks',
                                          label='sterktereeks',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.sterktereeks',
                                          definition='De stabiliteitsklasse van de buis.',
                                          owner=self)

    @property
    def aantalAfgedichteAansluitingen(self):
        """De afgedichte verlaten aansluitingsopeningen van straatkolken en/of huisaansluitingen in de rioleringsbuis."""
        return self._aantalAfgedichteAansluitingen.get_waarde()

    @aantalAfgedichteAansluitingen.setter
    def aantalAfgedichteAansluitingen(self, value):
        self._aantalAfgedichteAansluitingen.set_waarde(value, owner=self)

    @property
    def functie(self):
        """Bepaalt de functie van de rioleringsbuis."""
        return self._functie.get_waarde()

    @functie.setter
    def functie(self, value):
        self._functie.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Bepaalt het materiaal van de rioleringsbuis."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def sterktereeks(self):
        """De stabiliteitsklasse van de buis."""
        return self._sterktereeks.get_waarde()

    @sterktereeks.setter
    def sterktereeks(self, value):
        self._sterktereeks.set_waarde(value, owner=self)
