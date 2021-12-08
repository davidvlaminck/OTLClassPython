from ModelGenerator.BaseClasses.KeuzelijstField import KeuzelijstField


class KlAIMToestand(KeuzelijstField):
    """Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen."""

    def __init__(self, optionByLabel: str = None):
        super().__init__(naam="KlAIMToestand", label="AIM toestand",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand",
                         definition="TKeuzelijst met fasen uit de levenscyclus van een object om de toestand op een "
                                    "moment mee vast te leggen.", constraints="", usagenote="", deprecated_version="", codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIMToestand")
        self.add_option("in-ontwerp", "in ontwerp", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept"
                                                        "/KlAIMToestand/in-ontwerp")
        self.add_option("gepland", "gepland", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand"
                                                  "/gepland")
        self.add_option("in-gebruik", "in gebruik", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept"
                                                        "/KlAIMToestand/in-gebruik")

        self.set_value_by_label_on_init(optionByLabel)
