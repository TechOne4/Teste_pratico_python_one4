from typing import Dict, List
import pandas as pd

from entities.repositorie import Repositories


def generate_excel_file(repositories: List[Dict[str, Repositories]]) -> None:
    df = pd.DataFrame(repositories)
    df.to_excel('repositories.xlsx', index=False)