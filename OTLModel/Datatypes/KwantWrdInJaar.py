from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.NonNegIntField import NonNegIntField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInJaar(KwantWrd):
    """Een kwantitatieve waarde die een getal in aantal jaar uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInJaar.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in jaar.",
                               constraints='"a"^^cdt:ucumunit',
                               usagenote='"a"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="a")
        """De standaard eenheid bij dit datatype is uitgedrukt in jaar."""

        waardeVeld = NonNegIntField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInJaar.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInJaar",
                         label="Kwantitatieve waarde in aantal jaar",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInJaar",
                         definition="Een kwantitatieve waarde die een getal in aantal jaar uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)