import torch
import numpy as np
from typing import Union, Optional

from tianshou.data import Batch


def to_numpy(x: Union[
    torch.Tensor, dict, Batch, np.ndarray]) -> Union[
        dict, Batch, np.ndarray]:
    """Return an object without torch.Tensor."""
    if isinstance(x, torch.Tensor):
        x = x.detach().cpu().numpy()
    elif isinstance(x, dict):
        for k, v in x.items():
            x[k] = to_numpy(v)
    elif isinstance(x, Batch):
        x.to_numpy()
    return x


def to_torch(x: Union[torch.Tensor, dict, Batch, np.ndarray],
             dtype: Optional[torch.dtype] = None,
             device: Union[str, int] = 'cpu'
             ) -> Union[dict, Batch, torch.Tensor]:
    """Return an object without np.ndarray."""
    if isinstance(x, np.ndarray):
        x = torch.from_numpy(x).to(device)
        if dtype is not None:
            x = x.type(dtype)
    elif isinstance(x, dict):
        for k, v in x.items():
            x[k] = to_torch(v, dtype, device)
    elif isinstance(x, Batch):
        x.to_torch()
    return x
