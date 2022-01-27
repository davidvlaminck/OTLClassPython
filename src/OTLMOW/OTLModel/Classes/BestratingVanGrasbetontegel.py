# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Bestrating import Bestrating
from src.OTLMOW.OTLModel.Datatypes.KlBestratingOpvulsoort import KlBestratingOpvulsoort


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanGrasbetontegel(Bestrating):
    """Bestrating van grasbetontegels."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGrasbetontegel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._vulling = OTLAttribuut(field=KlBestratingOpvulsoort,
                                     naam='vulling',
                                     label='vulling',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGrasbetontegel.vulling',
                                     definition='Het gebruikte materiaal als toevoeging in de vrije openingen van de tegels.')

    @property
    def vulling(self):
        """Het gebruikte materiaal als toevoeging in de vrije openingen van de tegels."""
        return self._vulling.waarde

    @vulling.setter
    def vulling(self, value):
        self._vulling.set_waarde(value, owner=self)