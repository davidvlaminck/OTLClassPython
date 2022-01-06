import dataclasses


@dataclasses.dataclass
class OSLODatatypeUnionAttribuut:
    name: str
    label_nl: str
    definition_nl: str
    class_uri: str
    kardinaliteit_min: str
    kardinaliteit_max: str
    uri: str
    type: str
    overerving: int
    constraints: str
    readonly: int
    usagenote_nl: str
    deprecated_version: str




