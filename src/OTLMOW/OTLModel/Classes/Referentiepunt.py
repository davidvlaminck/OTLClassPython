# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from src.OTLMOW.OTLModel.Classes.Signalisatie import Signalisatie
from src.OTLMOW.OTLModel.Classes.BevestigingGC import BevestigingGC
from src.OTLMOW.OTLModel.Datatypes.DteTekstblok import DteTekstblok
from src.OTLMOW.OTLModel.Datatypes.KlSignalisatieReferentiepuntType import KlSignalisatieReferentiepuntType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Referentiepunt(AIMObject, Signalisatie, BevestigingGC):
    """Een kilometer- of hectometerpaal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Referentiepunt'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        BevestigingGC.__init__(self)
        Signalisatie.__init__(self)

        self._opschrift = OTLAttribuut(field=DteTekstblok,
                                       naam='opschrift',
                                       label='opschrift',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Referentiepunt.opschrift',
                                       definition='De notatie van het referentiepunt.')

        self._type = OTLAttribuut(field=KlSignalisatieReferentiepuntType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Referentiepunt.type',
                                  definition='Het type van referentiepunt.')

    @property
    def opschrift(self):
        """De notatie van het referentiepunt."""
        return self._opschrift.waarde

    @opschrift.setter
    def opschrift(self, value):
        self._opschrift.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van referentiepunt."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)