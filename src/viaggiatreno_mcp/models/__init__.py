"""Package models per ViaggiaTreno MCP."""

from viaggiatreno_mcp.models.common import (
    CLIENT_COMPANIES,
    REGIONS,
    TRAIN_STATUS_DESCRIPTIONS,
    ViaggiaTrenoBaseModel,
)
from viaggiatreno_mcp.models.route import DettaglioTratta, TrattaSegment
from viaggiatreno_mcp.models.service import (
    InfomobilitaNews,
    InfomobilitaNewsHeadline,
    StationWeather,
    Statistics,
)
from viaggiatreno_mcp.models.station import (
    StationAutocompleteItem,
    StationDetail,
    StationNTSAutocompleteItem,
    StationSearchResult,
)
from viaggiatreno_mcp.models.train import (
    Fermata,
    TrainAutocompleteItem,
    TrainBoardItem,
    TrainSearchResult,
    TrainStatus,
    TrattaCanvasItem,
)

__all__ = [
    "CLIENT_COMPANIES",
    "REGIONS",
    "TRAIN_STATUS_DESCRIPTIONS",
    "DettaglioTratta",
    "Fermata",
    "InfomobilitaNews",
    "InfomobilitaNewsHeadline",
    "StationAutocompleteItem",
    "StationDetail",
    "StationNTSAutocompleteItem",
    "StationSearchResult",
    "StationWeather",
    "Statistics",
    "TrainAutocompleteItem",
    "TrainBoardItem",
    "TrainSearchResult",
    "TrainStatus",
    "TrattaCanvasItem",
    "TrattaSegment",
    "ViaggiaTrenoBaseModel",
]
