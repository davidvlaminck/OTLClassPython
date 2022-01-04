from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType
from ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from ModelGenerator.OSLOClass import OSLOClass
from ModelGenerator.OSLOCollector import OSLOCollector


class OTLClassCreator(AbstractDatatypeCreator):
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
        logger.log("Created an instance of OTLClassCreator", LogType.INFO)
        self.osloCollector = osloCollector

    def CreateBlockToWriteFromClasses(self, osloClass: OSLOClass):
        if not isinstance(osloClass, OSLOClass):
            raise ValueError(f"Input is not a OSLOClass")

        if osloClass.uri == '' or not (osloClass.uri.startswith('https://wegenenverkeer.data.vlaanderen.be/ns/') or osloClass.uri.startswith('http://purl.org/dc/terms')):
            raise ValueError(f"OSLOClass.uri is invalid. Value = '{osloClass.uri}'")

        if osloClass.name == '':
            raise ValueError(f"OSLOClass.name is invalid. Value = '{osloClass.name}'")

        return self.CreateBlockToWriteFromClass(osloClass)

    def CreateBlockToWriteFromClass(self, osloClass: OSLOClass):
        attributen = self.osloCollector.FindAttributesByClass(osloClass)
        inheritances = self.osloCollector.FindInheritancesByClass(osloClass)

        datablock = []

        if osloClass.abstract == 1:
            if len(inheritances) > 0:
                datablock.append('from abc import abstractmethod')
            else:
                datablock.append('from abc import abstractmethod, ABC')

        if len(inheritances) > 0:
            for inheritance in inheritances:
                datablock.append(f'from OTLModel.Classes.{inheritance.base_name} import {inheritance.base_name}')

        if osloClass.uri == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject':
            datablock.append('from OTLModel.BaseClasses.RelatieInteractor import RelatieInteractor')
            datablock.append('from OTLModel.BaseClasses.OTLAsset import OTLAsset')

        if any(atr.kardinaliteit_max != "1" for atr in attributen):
            datablock.append('from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField')

        if any(atr.readonly == 1 for atr in attributen):
            raise NotImplementedError("readonly property is assumed to be 0 on value fields")

        listOfFields = self.getFieldsToImportFromListOfAttributes(attributen)
        for typeField in listOfFields:
            datablock.append(f'from OTLModel.Datatypes.{typeField} import {typeField}')

        datablock.append('')
        datablock.append('')
        datablock.append(f'# Generated with {self.__class__.__name__}')
        datablock.append(self.getClassLineFromClassAndInheritances(osloClass, inheritances))
        datablock.append(f'    """{osloClass.definition_nl}"""')
        datablock.append('')
        datablock.append(f'    typeURI = "{osloClass.uri}"')
        datablock.append('    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""')
        datablock.append('')
        if osloClass.abstract == 1:
            datablock.append('    @abstractmethod')
        datablock.append('    def __init__(self):')
        if len(inheritances) == 1:
            datablock.append('        super().__init__()')
        elif len(inheritances) > 1:
            for inheritance in inheritances:
                datablock.append(f'        {inheritance.base_name}.__init__(self)')

        if osloClass.uri == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject':
            datablock.append(f'        OTLAsset.__init__(self)')
            datablock.append(f'        RelatieInteractor.__init__(self)')

        self.addAttributenToDataBlock(attributen, datablock, forDatatypeUse=False)

        if datablock[-1] == '':
            datablock.pop()

        return datablock

    def getClassLineFromClassAndInheritances(self, osloClass, inheritances):
        if osloClass.abstract == 0 and len(inheritances) == 0:
            raise NotImplementedError(f"{osloClass.uri} is a base class, which is not implemented")
        if osloClass.abstract == 1 and len(inheritances) == 0:
            return f'class {osloClass.name}(ABC):'
        if len(inheritances) > 0:
            line = f'class {osloClass.name}('
            for inheritance in inheritances:
                line += inheritance.base_name + ', '
            line = line[:-2]
            line += '):'
            return line

        raise NotImplementedError(f"{osloClass.uri} class structure not implemented")