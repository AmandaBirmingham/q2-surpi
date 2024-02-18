import numpy as np
import pandas
from pandas.testing import assert_frame_equal
from qiime2.plugin.testing import TestPluginBase
from q2_surpi import (
    __package_name__, SurpiCountTableFormat)
from q2_surpi._formats_and_types import (
    SPECIES_KEY, GENUS_KEY, FAMILY_KEY, TAG_KEY)


class TestSurpiCountTableFormatTransformers(TestPluginBase):
    package = f'{__package_name__}.tests'

    def test_surpicounttableformat_to_dataframe(self):
        input_fname = "surpi_output.counttable"

        expected_dict = {
            SPECIES_KEY: ["Dill cryptic virus 1", "Escherichia phage FEC14",
                          "Dickeya phage phiDP10.3", "Dickeya phage phiDP23.1",
                          "Salmonella virus SJ2", "Klebsiella phage May",
                          "Escherichia virus FI", "Escherichia virus Qbeta",
                          "Enterobacteria phage C-1 INW-2012",
                          "Enterobacteria phage Hgal1",
                          "Escherichia virus BZ13", "Escherichia virus MS2",
                          "Acinetobacter phage AP205", "Pseudomonas phage PP7",
                          "Pseudomonas phage PRR1", "*"],
            GENUS_KEY: [np.nan, "Cba120virus", "Limestonevirus",
                        "Limestonevirus", "Vi1virus", np.nan, "Allolevivirus",
                        "Allolevivirus", "Levivirus", "Levivirus", "Levivirus",
                        "Levivirus", np.nan, np.nan, np.nan, np.nan],
            FAMILY_KEY: ["Partitiviridae", "Ackermannviridae",
                         "Ackermannviridae", "Ackermannviridae",
                         "Ackermannviridae", "Ackermannviridae", "Leviviridae",
                         "Leviviridae", "Leviviridae", "Leviviridae",
                         "Leviviridae", "Leviviridae", "Leviviridae",
                         "Leviviridae", "Leviviridae", "Microviridae"],
            TAG_KEY: ["host-apicomplexans|fungi|plants;", "host-bacteria;",
                      "host-bacteria;", "host-bacteria;", "host-bacteria;",
                      "host-bacteria;", "host-bacteria;", "host-bacteria;",
                      "host-bacteria;", "host-bacteria;", "host-bacteria;",
                      "host-bacteria;", "host-bacteria;", "host-bacteria;",
                      "host-bacteria;", "host-bacteria;"],
            "AACCCGCC+GAGGATTT": [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 2, 0, 7, 0, 2, 0],
            "AATCGTCA+AGTTAAAG": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 3, 0, 0, 0],
            "ACTATGAT+TTCGATAG": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "AGTACAAG+CCCATTGC": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "AGTAGTAA+TACTGATA": [0, 0, 5, 1, 0, 0, 1, 5, 0, 1, 10, 1, 10, 4, 3, 0],
            "AGTCCCGG+GCAGAAGT": [0, 0, 0, 0, 0, 0, 0, 3, 0, 1, 6, 0, 3, 0, 0, 0],
            "AGTCTGCT+TCCAGGCT": [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "AGTGCGGA+CCGTTGTC": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "CATCTACT+TTCCGTTG": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 11, 0, 1, 0],
            "CATTCGGA+GATGGAAA": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0]
        }

        expected_df = pandas.DataFrame(expected_dict)

        _, obs_df = self.transform_format(
            SurpiCountTableFormat, pandas.DataFrame,
            filename=input_fname)

        assert_frame_equal(obs_df, expected_df)
