from grammar_ru.common.nlp_analyzer import NlpAnalyzer
from tg.common.datasets.featurization import FeaturizationJob
from tg.common.datasets.access import DataSource, MockDfDataSource
from typing import *
import pandas as pd


class NlpAnalyzationPipeline:
    def __init__(self, analyzers: List[(str, NlpAnalyzer)]):
        self._analyzers = analyzers

    def df_to_featurization_job(self, df: pd.DataFrame, **kwargs) -> FeaturizationJob:
        return self.source_to_featurization_job(MockDfDataSource(df), **kwargs)

    def source_to_featurization_job(self, source: DataSource, **kwargs) -> FeaturizationJob:
        return FeaturizationJob(
            # name='job',
            # version='v1',
            source=source,
            featurizers=dict(self._analyzers),
            # destination=destination
            **kwargs
        )

    def analyze_dataframe(self, df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
        results = {}
        for (name, analyzer) in self._analyzers:
            results[name] = analyzer.apply(df)
        return results

    def analyze(self, source: DataSource) -> Dict[str, pd.DataFrame]:
        df = pd.DataFrame(source.get_data())
        return self.analyze_dataframe(df)
