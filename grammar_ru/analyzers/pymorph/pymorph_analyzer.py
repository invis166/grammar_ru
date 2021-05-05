from grammar_ru.common.nlp_analyzer import NlpAnalyzer
import pandas as pd


class PyMorphAnalyzer(NlpAnalyzer):
    def __init__(self):
        super(PyMorphAnalyzer, self).__init__(["word_id"])

    def _analyze_inner(self, df: pd.DataFrame) -> pd.DataFrame:
        pass
