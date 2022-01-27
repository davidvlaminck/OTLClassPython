# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Datatypes.KlLuchtkwaliteitOpstellingMerk import KlLuchtkwaliteitOpstellingMerk
from src.OTLMOW.OTLModel.Datatypes.KlLuchtkwaliteitOpstellingModelnaam import KlLuchtkwaliteitOpstellingModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Luchtkwaliteittoestel(AIMNaamObject):
    """Abstracte voor attributen van onderdelen van de luchtkwaliteitsensor installatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlLuchtkwaliteitOpstellingMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel.merk',
                                  definition='Het merk van een onderdeel uit een luchtkwaliteitsinstallatie.')

        self._modelnaam = OTLAttribuut(field=KlLuchtkwaliteitOpstellingModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel.modelnaam',
                                       definition='De modelnaam van een onderdeel uit een luchtkwaliteitsinstallatie.')

    @property
    def merk(self):
        """Het merk van een onderdeel uit een luchtkwaliteitsinstallatie."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van een onderdeel uit een luchtkwaliteitsinstallatie."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)