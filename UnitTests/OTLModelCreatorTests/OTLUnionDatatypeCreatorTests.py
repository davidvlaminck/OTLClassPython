import os
import unittest
from unittest import mock
from unittest.mock import patch

from Loggers.NoneLogger import NoneLogger
from ModelGenerator.FileExistChecker import FileExistChecker
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypeUnion import OSLODatatypeUnion
from ModelGenerator.OSLODatatypeUnionAttribuut import OSLODatatypeUnionAttribuut
from ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from ModelGenerator.OSLOTypeLink import OSLOTypeLink
from ModelGenerator.OTLUnionDatatypeCreator import OTLUnionDatatypeCreator
from ModelGenerator.SQLDbReader import SQLDbReader


class UnionDatatypeOSLOCollector(OSLOCollector):
    def __init__(self, reader):
        super().__init__(reader)

        self.unionDatatypes = [
            OSLODatatypeUnion('DtuLichtmastMasthoogte',
                              'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte',
                              'Union datatype om een standaard of afwijkende masthoogte te bepalen.', 'Masthoogte', '', '')
        ]
        self.unionDatatypeAttributen = [
            OSLODatatypeUnionAttribuut('afwijkendeHoogte', 'afwijkende hoogte', 'De afwijkende hoogte van de mast in meter.',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte', '0', '1',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.afwijkendeHoogte',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter', 0,
                                       '', 0, '', ''),
            OSLODatatypeUnionAttribuut('standaardHoogte', 'standaard hoogte', 'Bepaling van de standaard hoogte van een mast.',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte', '0', '1',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.standaardHoogte',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastMasthoogte', 0, '',
                                       0, '', '')
        ]

        self.typeLinks = [
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter", "OSLODatatypePrimitive", ""),
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastMasthoogte", "OSLOEnumeration", "")
        ]

        self.expectedDtu = ['# coding=utf-8',
                            'from OTLModel.Datatypes.UnionTypeField import UnionTypeField',
                            'from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField',
                            'from OTLModel.Datatypes.KlLichtmastMasthoogte import KlLichtmastMasthoogte',
                            'from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter',
                            '',
                            '',
                            '# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit',
                            'class DtuLichtmastMasthoogte(UnionTypeField):',
                            '    """Union datatype om een standaard of afwijkende masthoogte te bepalen."""',
                            '',
                            '    def __init__(self):',
                            '        super().__init__(naam="DtuLichtmastMasthoogte",',
                            '                         label="Masthoogte",',
                            '                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte",',
                            '                         definition="Union datatype om een standaard of afwijkende masthoogte te bepalen.",',
                            '                         usagenote="",',
                            '                         deprecated_version="")',
                            '',
                            '        field_afwijkendeHoogte = KwantWrdInMeter()',
                            '        """De afwijkende hoogte van de mast in meter."""',
                            '        field_afwijkendeHoogte.naam = "afwijkendeHoogte"',
                            '        field_afwijkendeHoogte.label = "afwijkende hoogte"',
                            '        field_afwijkendeHoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.afwijkendeHoogte"',
                            '        field_afwijkendeHoogte.definition = "De afwijkende hoogte van de mast in meter."',
                            '        field_afwijkendeHoogte.constraints = ""',
                            '        field_afwijkendeHoogte.usagenote = ""',
                            '        field_afwijkendeHoogte.deprecated_version = ""',
                            '',
                            '        field_standaardHoogte = KeuzelijstField(naam="standaardHoogte",',
                            '                                                label="standaard hoogte",',
                            '                                                lijst=KlLichtmastMasthoogte(),',
                            '                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.standaardHoogte",',
                            '                                                definition="Bepaling van de standaard hoogte van een mast.",',
                            '                                                constraints="",',
                            '                                                usagenote="",',
                            '                                                deprecated_version="")',
                            '        """Bepaling van de standaard hoogte van een mast."""',
                            '',
                            '        self.fieldsTuple = (field_afwijkendeHoogte, field_standaardHoogte)']


class TestOTLUnionDatatypeCreator(OTLUnionDatatypeCreator):
    def __init__(self, logger, collector):
        super().__init__(logger, collector)


class OTLUnionDatatypeCreatorTests(unittest.TestCase):
    @patch.object(NoneLogger, "log")
    def test_InitOTLModelCreator(self, mock):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        self.assertTrue(mock.called)

    def test_InvalidOSLODatatypeUnionEmptyUri(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        osloDatatypeUnion = OSLODatatypeUnion(name='name', uri='', definition_nl='', label_nl='', usagenote_nl='',
                                              deprecated_version='')

        with self.assertRaises(ValueError) as exception_empty_uri:
            creator.CreateBlockToWriteFromUnionTypes(osloDatatypeUnion)
        self.assertEqual(str(exception_empty_uri.exception), "OSLODatatypeUnion.uri is invalid. Value = ''")

    def test_InvalidOSLODatatypeUnionBadUri(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        osloDatatypeUnion = OSLODatatypeUnion(name='name', uri='Bad uri', definition_nl='', label_nl='', usagenote_nl='',
                                              deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_uri:
            creator.CreateBlockToWriteFromUnionTypes(osloDatatypeUnion)
        self.assertEqual(str(exception_bad_uri.exception), "OSLODatatypeUnion.uri is invalid. Value = 'Bad uri'")

    def test_InvalidOSLODatatypeUnionEmptyName(self):
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        osloDatatypeUnion = OSLODatatypeUnion(name='',
                                              uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',
                                              definition_nl='', label_nl='', usagenote_nl='',
                                              deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromUnionTypes(osloDatatypeUnion)
        self.assertEqual(str(exception_bad_name.exception), "OSLODatatypeUnion.name is invalid. Value = ''")

    def test_InValidType(self):
        bad_Union = True
        logger = NoneLogger()
        collector = OSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromUnionTypes(bad_Union)
        self.assertEqual(str(exception_bad_name.exception), "Input is not a OSLODatatypeUnion")

    def test_DtcIdentificatorOSLODatatypeUnion(self):
        logger = NoneLogger()
        collector = UnionDatatypeOSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(logger, collector)
        DtuLichtmastMasthoogte = collector.FindUnionDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte')
        dataToWrite = creator.CreateBlockToWriteFromUnionTypes(DtuLichtmastMasthoogte)

        self.assertEqual(collector.expectedDtu, dataToWrite)


    def test_WriteToFileDtcAdresOSLODatatypeUnion(self):
        logger = NoneLogger()

        file_location = '../../InputFiles/OTL.db'
        file_exist_checker = FileExistChecker(file_location)
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        creator = OTLUnionDatatypeCreator(logger, collector)
        dtcAdres = collector.FindUnionDatatypeByUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte')
        dataToWrite = creator.CreateBlockToWriteFromUnionTypes(dtcAdres)
        creator.writeToFile(dtcAdres, 'Datatypes', dataToWrite, '../../')

        self.assertTrue(os.path.isfile('../../OTLModel/Datatypes/DtuLichtmastMasthoogte.py'))

