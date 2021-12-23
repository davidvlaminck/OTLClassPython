from OTLModel.Classes.Buitenkast import Buitenkast
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator
class Montagekast(Buitenkast):
    """Een kleine kast voor binnen of buiten die net omwille van zijn beperkte omvang doorgaans aan een paal, muur of andere objecten bevestigd wordt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.eplanMechanischPlan = DtcDocument()
        """Elektrisch aansluitschema van de kast en mechanisch plan van de volledige installatie in de kast."""
        self.eplanMechanischPlan.naam = "eplanMechanischPlan"
        self.eplanMechanischPlan.label = "e-plan en m-plan"
        self.eplanMechanischPlan.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast.eplanMechanischPlan"
        self.eplanMechanischPlan.definition = "Elektrisch aansluitschema van de kast en mechanisch plan van de volledige installatie in de kast."
        self.eplanMechanischPlan.constraints = ""
        self.eplanMechanischPlan.usagenote = "Bestanden van het type dwg."
        self.eplanMechanischPlan.deprecated_version = ""
