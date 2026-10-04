"""Modelli Pydantic per tratte ferroviarie e segmenti di rete."""

from pydantic import Field

from viaggiatreno_mcp.models.common import ViaggiaTrenoBaseModel
from viaggiatreno_mcp.models.train import TrainBoardItem


class TrattaSegment(ViaggiaTrenoBaseModel):
    """Segmento della rete ferroviaria tra due nodi (elencoTratte)."""

    nodoA: str = Field(..., description="Codice nodo o stazione estremo A")
    nodoB: str = Field(..., description="Codice nodo o stazione estremo B")
    trattaAB: int = Field(
        ..., description="Identificativo numerico del segmento in direzione A -> B"
    )
    trattaBA: int = Field(
        ..., description="Identificativo numerico del segmento in direzione B -> A"
    )
    parentAB: int | None = Field(None, description="ID del segmento padre A -> B")
    parentBA: int | None = Field(None, description="ID del segmento padre B -> A")
    latitudineA: float | None = Field(None, description="Latitudine dell'estremo A")
    longitudineA: float | None = Field(None, description="Longitudine dell'estremo A")
    latitudineB: float | None = Field(None, description="Latitudine dell'estremo B")
    longitudineB: float | None = Field(None, description="Longitudine dell'estremo B")
    occupata: bool = Field(
        ..., description="True se almeno un treno è presente su questo segmento"
    )


class DettaglioTratta(ViaggiaTrenoBaseModel):
    """Gruppo di treni presenti su un senso di marcia di una tratta (dettagliTratta)."""

    tratta: int | None = Field(None, description="ID della tratta o segmento")
    treni: list[TrainBoardItem] = Field(
        default_factory=list, description="Lista dei treni attualmente sul segmento"
    )
