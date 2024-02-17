import pandas
from q2_types.feature_table import FeatureTable, Frequency
from q2_types.feature_data import FeatureData, Taxonomy
from qiime2.plugin import (Plugin, Citations)
import q2_surpi
from q2_surpi._formats_and_types import (
    SurpiCountTable, SurpiCountTableFormat,
    SurpiSampleSheet, SurpiSampleSheetFormat, FEATURE_ID_KEY)


plugin = Plugin(
    name=q2_surpi.__plugin_name__,
    version=q2_surpi.__version__,
    website=q2_surpi.__url__,
    package=q2_surpi.__package_name__,
    citations=Citations.load(
        q2_surpi.__citations_fname__, package=q2_surpi.__package_name__),
    description=q2_surpi.__long_description__,
    short_description=q2_surpi.__description__,
)

plugin.register_formats(SurpiCountTableFormat)
plugin.register_semantic_types(SurpiCountTable)
plugin.register_semantic_type_to_format(
    SurpiCountTable, SurpiCountTableFormat)
plugin.register_formats(SurpiSampleSheet)
plugin.register_semantic_types(SurpiSampleSheetFormat)
plugin.register_semantic_type_to_format(
    SurpiSampleSheet, SurpiSampleSheetFormat)


@plugin.register_transformer
# load a SurpiCountTableFormat into a dataframe
def _1(ff: SurpiCountTableFormat) -> pandas.DataFrame:
    result = pandas.read_csv(str(ff), sep='\t', header=0, index_col=0)
    result.index.name = FEATURE_ID_KEY
    result.reset_index(inplace=True)
    return result


@plugin.register_transformer
# load a SurpiSampleSheetFormat into a dataframe
def _1(ff: SurpiSampleSheetFormat) -> pandas.DataFrame:
    result = pandas.read_csv(str(ff), sep='\t', header=0)
    return result


plugin.methods.register_function(
    function=q2_surpi.extract_surpi_data,
    name='Extract SURPI data for use in QIIME.',
    description=(
        'Extract SURPI data into a feature table and a feature taxonomy.'),
    inputs={'surpi_counts': SurpiCountTable,
            'surpi_sample_info': SurpiSampleSheet},
    input_descriptions={
        'surpi_counts': "SURPI counts per species per barcode.",
        'surpi_sample_info': 'Info linking sample ids to barcodes.'},
    outputs=[('table', FeatureTable[Frequency]),
             ('taxonomy', FeatureData[Taxonomy])],
    output_descriptions={
        'table': 'Output feature table.',
        'taxonomy': 'Output feature metadata.'},
)
