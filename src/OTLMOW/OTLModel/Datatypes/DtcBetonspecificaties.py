# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from src.OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from src.OTLMOW.OTLModel.Datatypes.KlBetonmilieuklasse import KlBetonmilieuklasse
from src.OTLMOW.OTLModel.Datatypes.KlBetonomgevingsklasse import KlBetonomgevingsklasse
from src.OTLMOW.OTLModel.Datatypes.KlBetonsterkteklasse import KlBetonsterkteklasse
from src.OTLMOW.OTLModel.Datatypes.KlGebruiksdomein import KlGebruiksdomein
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBetonspecificatiesWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._betondekking = OTLAttribuut(field=KwantWrdInMillimeter,
                                          naam='betondekking',
                                          label='betondekking',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betondekking',
                                          definition='De afstand in millimeter tussen de buitenkant van het beton (het oppervlak van het beton) tot het dichtstbijzijnde wapeningsstaal.')

        self._betonmilieuklassen = OTLAttribuut(field=KlBetonmilieuklasse,
                                                naam='betonmilieuklassen',
                                                label='betonmilieuklassen',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betonmilieuklassen',
                                                kardinaliteit_max='*',
                                                definition='Milieuklassen (X-klassen) leggen rechtstreeks de link met bepaalde aantastingsmechanismen, waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere milieuklassen van toepassing zijn.')

        self._betonomgevingsklassen = OTLAttribuut(field=KlBetonomgevingsklasse,
                                                   naam='betonomgevingsklassen',
                                                   label='betonomgevingsklassen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betonomgevingsklassen',
                                                   kardinaliteit_max='*',
                                                   definition='De omgeving waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere omgevingsklassen van toepassing zijn.')

        self._betonsterkteklasse = OTLAttribuut(field=KlBetonsterkteklasse,
                                                naam='betonsterkteklasse',
                                                label='betonsterkteklasse',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betonsterkteklasse',
                                                definition='De sterkteklasse is een maat voor de druksterkte van beton.')

        self._gebruiksdomein = OTLAttribuut(field=KlGebruiksdomein,
                                            naam='gebruiksdomein',
                                            label='gebruiksdomein',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.gebruiksdomein',
                                            definition='De gebruiksomstandigheden van het beton. Dit bepaalt tevens het maximum chloridegehalte.')

        self._grootsteKorrelafmetingDmax = OTLAttribuut(field=KwantWrdInMillimeter,
                                                        naam='grootsteKorrelafmetingDmax',
                                                        label='grootste korrelafmeting (Dmax)',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.grootsteKorrelafmetingDmax',
                                                        definition='De nominale grootste korrelafmeting (Dmax).')

        self._isCementMetBeperktAlkaligehalte = OTLAttribuut(field=BooleanField,
                                                             naam='isCementMetBeperktAlkaligehalte',
                                                             label='is cement met beperkt alkaligehalte',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetBeperktAlkaligehalte',
                                                             definition='Aanduiding of het cement een beperkt alkaligehalte heeft (LA).')

        self._isCementMetHogeAanvangssterkte = OTLAttribuut(field=BooleanField,
                                                            naam='isCementMetHogeAanvangssterkte',
                                                            label='is cement met hoge aanvangssterkte',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetHogeAanvangssterkte',
                                                            definition='Geeft aan of het cement gebruikt wordt voor een snelle binding (bijvoorbeeld in de winter) (HES).')

        self._isCementMetHogeBestandheidTegenSulfaten = OTLAttribuut(field=BooleanField,
                                                                     naam='isCementMetHogeBestandheidTegenSulfaten',
                                                                     label='is cement met hoge bestandheid tegen sulfaten',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetHogeBestandheidTegenSulfaten',
                                                                     definition='Geeft aan of het cement een hoge bestandheid heeft tegen sulfaten (SR).')

        self._isCementMetLageHydratatiewarmte = OTLAttribuut(field=BooleanField,
                                                             naam='isCementMetLageHydratatiewarmte',
                                                             label='is cement met lage hydratatiewarmte',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetLageHydratatiewarmte',
                                                             definition='Geeft aan of het cement gebruikt wordt voor een tragere sterkteontwikkeling (LH).')

        self._isColloidaalbeton = OTLAttribuut(field=BooleanField,
                                               naam='isColloidaalbeton',
                                               label='is colloïdaalbeton',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isColloidaalbeton',
                                               definition='Geeft aan of het beton zich niet ontmengt onder of in water.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.technischeFiche',
                                             definition='De technische fiche van het beton. Deze moet volgende eigenschappen bevatten: de norm waaraan het beton voldoet, de sterkteklasse, de duurzaamheid (bestaande uit het gebruiksdomein en de omgevingsklasse(n)), de consistentieklasse, de nominale grootste korrelafmeting,...')

    @property
    def betondekking(self):
        """De afstand in millimeter tussen de buitenkant van het beton (het oppervlak van het beton) tot het dichtstbijzijnde wapeningsstaal."""
        return self._betondekking.waarde

    @betondekking.setter
    def betondekking(self, value):
        self._betondekking.set_waarde(value, owner=self._parent)

    @property
    def betonmilieuklassen(self):
        """Milieuklassen (X-klassen) leggen rechtstreeks de link met bepaalde aantastingsmechanismen, waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere milieuklassen van toepassing zijn."""
        return self._betonmilieuklassen.waarde

    @betonmilieuklassen.setter
    def betonmilieuklassen(self, value):
        self._betonmilieuklassen.set_waarde(value, owner=self._parent)

    @property
    def betonomgevingsklassen(self):
        """De omgeving waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere omgevingsklassen van toepassing zijn."""
        return self._betonomgevingsklassen.waarde

    @betonomgevingsklassen.setter
    def betonomgevingsklassen(self, value):
        self._betonomgevingsklassen.set_waarde(value, owner=self._parent)

    @property
    def betonsterkteklasse(self):
        """De sterkteklasse is een maat voor de druksterkte van beton."""
        return self._betonsterkteklasse.waarde

    @betonsterkteklasse.setter
    def betonsterkteklasse(self, value):
        self._betonsterkteklasse.set_waarde(value, owner=self._parent)

    @property
    def gebruiksdomein(self):
        """De gebruiksomstandigheden van het beton. Dit bepaalt tevens het maximum chloridegehalte."""
        return self._gebruiksdomein.waarde

    @gebruiksdomein.setter
    def gebruiksdomein(self, value):
        self._gebruiksdomein.set_waarde(value, owner=self._parent)

    @property
    def grootsteKorrelafmetingDmax(self):
        """De nominale grootste korrelafmeting (Dmax)."""
        return self._grootsteKorrelafmetingDmax.waarde

    @grootsteKorrelafmetingDmax.setter
    def grootsteKorrelafmetingDmax(self, value):
        self._grootsteKorrelafmetingDmax.set_waarde(value, owner=self._parent)

    @property
    def isCementMetBeperktAlkaligehalte(self):
        """Aanduiding of het cement een beperkt alkaligehalte heeft (LA)."""
        return self._isCementMetBeperktAlkaligehalte.waarde

    @isCementMetBeperktAlkaligehalte.setter
    def isCementMetBeperktAlkaligehalte(self, value):
        self._isCementMetBeperktAlkaligehalte.set_waarde(value, owner=self._parent)

    @property
    def isCementMetHogeAanvangssterkte(self):
        """Geeft aan of het cement gebruikt wordt voor een snelle binding (bijvoorbeeld in de winter) (HES)."""
        return self._isCementMetHogeAanvangssterkte.waarde

    @isCementMetHogeAanvangssterkte.setter
    def isCementMetHogeAanvangssterkte(self, value):
        self._isCementMetHogeAanvangssterkte.set_waarde(value, owner=self._parent)

    @property
    def isCementMetHogeBestandheidTegenSulfaten(self):
        """Geeft aan of het cement een hoge bestandheid heeft tegen sulfaten (SR)."""
        return self._isCementMetHogeBestandheidTegenSulfaten.waarde

    @isCementMetHogeBestandheidTegenSulfaten.setter
    def isCementMetHogeBestandheidTegenSulfaten(self, value):
        self._isCementMetHogeBestandheidTegenSulfaten.set_waarde(value, owner=self._parent)

    @property
    def isCementMetLageHydratatiewarmte(self):
        """Geeft aan of het cement gebruikt wordt voor een tragere sterkteontwikkeling (LH)."""
        return self._isCementMetLageHydratatiewarmte.waarde

    @isCementMetLageHydratatiewarmte.setter
    def isCementMetLageHydratatiewarmte(self, value):
        self._isCementMetLageHydratatiewarmte.set_waarde(value, owner=self._parent)

    @property
    def isColloidaalbeton(self):
        """Geeft aan of het beton zich niet ontmengt onder of in water."""
        return self._isColloidaalbeton.waarde

    @isColloidaalbeton.setter
    def isColloidaalbeton(self, value):
        self._isColloidaalbeton.set_waarde(value, owner=self._parent)

    @property
    def technischeFiche(self):
        """De technische fiche van het beton. Deze moet volgende eigenschappen bevatten: de norm waaraan het beton voldoet, de sterkteklasse, de duurzaamheid (bestaande uit het gebruiksdomein en de omgevingsklasse(n)), de consistentieklasse, de nominale grootste korrelafmeting,..."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBetonspecificaties(ComplexField, AttributeInfo):
    """Complex datatype om de eigenschappen van beton te bundelen."""
    naam = 'DtcBetonspecificaties'
    label = 'Betonspecificaties'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties'
    definition = 'Complex datatype om de eigenschappen van beton te bundelen.'
    waardeObject = DtcBetonspecificatiesWaarden

    def __str__(self):
        return ComplexField.__str__(self)
