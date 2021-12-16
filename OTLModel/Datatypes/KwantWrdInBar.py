from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInBar(KwantWrd):
    """Een kwantitatieve waarde die een getal in bar uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInBar.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in bar.",
                               constraints='"bar"^^cdt:ucumunit',
                               usagenote='"bar"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="bar")
        """De standaard eenheid bij dit datatype is uitgedrukt in bar."""

        waardeVeld = DecimalFloatField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInBar.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInBar",
                         label="Kwantitatieve waarde in bar",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInBar",
                         definition="Een kwantitatieve waarde die een getal in bar uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)