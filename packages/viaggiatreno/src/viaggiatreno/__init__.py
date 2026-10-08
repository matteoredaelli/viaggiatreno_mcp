"""ViaggiaTreno API Client - Core library.

Libreria per interrogare le API non ufficiali di ViaggiaTreno: client HTTP
asincrono, parser delle risposte e modelli dati tipizzati (pydantic).
"""

from viaggiatreno.api.client import ViaggiaTrenoClient, format_viaggiatreno_datetime
from viaggiatreno.api.parsers import (
    parse_infomobilita_rss,
    parse_infomobilita_rss_box,
    parse_infomobilita_ticker,
    parse_station_autocomplete,
    parse_station_nts_autocomplete,
    parse_train_autocomplete,
)
from viaggiatreno.models.common import (
    CLIENT_COMPANIES,
    REGIONS,
    TRAIN_STATUS_DESCRIPTIONS,
    ViaggiaTrenoBaseModel,
)
from viaggiatreno.models.route import DettaglioTratta, TrattaSegment
from viaggiatreno.models.service import (
    InfomobilitaNews,
    InfomobilitaNewsHeadline,
    StationWeather,
    Statistics,
)
from viaggiatreno.models.station import (
    StationAutocompleteItem,
    StationDetail,
    StationNTSAutocompleteItem,
    StationSearchResult,
)
from viaggiatreno.models.train import (
    Fermata,
    TrainAutocompleteItem,
    TrainBoardItem,
    TrainSearchResult,
    TrainStatus,
    TrattaCanvasItem,
)

__version__ = "0.1.0"

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
    "ViaggiaTrenoClient",
    "format_viaggiatreno_datetime",
    "parse_infomobilita_rss",
    "parse_infomobilita_rss_box",
    "parse_infomobilita_ticker",
    "parse_station_autocomplete",
    "parse_station_nts_autocomplete",
    "parse_train_autocomplete",
]
