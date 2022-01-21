# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.BaseClasses.OTLField import OTLField
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInVierkanteMeterWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVierkanteMeter.standaardEenheid',
                                              usagenote='"m2"^^cdt:ucumunit',
                                              constraints='"m2"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in vierkante meter.')

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVierkanteMeter.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.')

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt in vierkante meter."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self):
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.waarde

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInVierkanteMeter(OTLField, AttributeInfo):
    """Een kwantitatieve waarde die een getal in vierkante meter uitdrukt."""
    naam = 'KwantWrdInVierkanteMeter'
    label = 'Kwantitatieve waarde in vierkante meter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVierkanteMeter'
    definition = 'Een kwantitatieve waarde die een getal in vierkante meter uitdrukt.'
    waardeObject = KwantWrdInVierkanteMeterWaarden

    def __str__(self):
        return OTLField.__str__(self)

