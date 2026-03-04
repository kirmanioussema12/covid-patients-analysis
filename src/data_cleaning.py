import numpy as np
from typing import Tuple

def clean_regions_and_counts(
    regions: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Get unique regions + counts + inverse index"""
    unique_regions, inverse_idx, counts = np.unique(
        regions, return_inverse=True, return_counts=True
    )
    return unique_regions, counts, inverse_idx