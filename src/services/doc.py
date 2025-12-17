import numpy as np
import pandas as pd


class DocService:

    def read_doc(self, file_path: str):
        df = pd.read_excel(file_path, engine="openpyxl", sheet_name="Лист1")
        df = df.replace({np.nan: None})
        data = df.to_dict(orient="records")
        return data


def get_doc_service() -> DocService:
    result = DocService()
    return result
