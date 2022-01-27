# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.VegetatieElement import VegetatieElement
from src.OTLMOW.OTLModel.Datatypes.KlVegetatieWortel import KlVegetatieWortel


# Generated with OTLClassCreator. To modify: extend, do not edit
class SolitaireHeester(VegetatieElement):
    """Afzonderlijk te onderscheiden heester. Heesters zijn houtachtige planten die in of dicht bij de grond vertakken. Anders dan een boom vormen ze in het algemeen geen duidelijke stam, maar komen de meeste soorten met een aantal takken uit de grond, die dan ook grondtakken genoemd worden. Voorwaarde is wel dat de plant in zijn eventuele stam en takken houtweefsel vormt, hoewel dat niet tot in het hart hoeft te zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SolitaireHeester'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._wortelAanplant = OTLAttribuut(field=KlVegetatieWortel,
                                            naam='wortelAanplant',
                                            label='wortel aanplant',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SolitaireHeester.wortelAanplant',
                                            definition='De manier van levering en aanplanting van het wortelgestel van de boom of plant.')

    @property
    def wortelAanplant(self):
        """De manier van levering en aanplanting van het wortelgestel van de boom of plant."""
        return self._wortelAanplant.waarde

    @wortelAanplant.setter
    def wortelAanplant(self, value):
        self._wortelAanplant.set_waarde(value, owner=self)