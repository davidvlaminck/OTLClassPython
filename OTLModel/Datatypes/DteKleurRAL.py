# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.BaseClasses.OTLField import OTLField
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteKleurRALWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._waarde = OTLAttribuut(field=StringField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL.waarde',
                                    usagenote='De waarde moet voldoen aan volgende regex: [1-9]\d{3}',
                                    definition='Beschrijft een kleur volgens het RAL classificatiesysteem.')

    @property
    def waarde(self):
        """Beschrijft een kleur volgens het RAL classificatiesysteem."""
        return self._waarde.waarde

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteKleurRAL(OTLField, AttributeInfo):
    """Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal tussen 1000 en 9999."""
    naam = 'DteKleurRAL'
    label = 'RAL-kleur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL'
    definition = 'Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal tussen 1000 en 9999.'
    waardeObject = DteKleurRALWaarden

    def __str__(self):
        return OTLField.__str__(self)

