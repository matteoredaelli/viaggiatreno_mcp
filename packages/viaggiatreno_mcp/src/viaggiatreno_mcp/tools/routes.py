"""Tool MCP per le tratte ferroviarie e il monitoraggio della rete."""

from fastmcp import FastMCP
from viaggiatreno import DettaglioTratta, TrattaSegment, ViaggiaTrenoClient


def register_route_tools(mcp: FastMCP, client: ViaggiaTrenoClient) -> None:
    """Registra i tool relativi a tratte e rete ferroviaria sul server FastMCP."""

    @mcp.tool(
        name="elenco_tratte_ferroviarie",
        description=(
            "Restituisce i segmenti della rete ferroviaria nazionale (coppie di nodi ferroviari con coordinate geografiche) "
            "e l'indicazione se ciascun segmento è attualmente occupato da almeno un treno in viaggio. "
            "Le categorie filtrabili (separate da virgola) includono: 'ES*,IC,EXP,EC,EN,REG'."
        ),
    )
    async def elenco_tratte_ferroviarie(
        categorie: str = "ES*,IC,EXP,EC,EN,REG",
    ) -> list[TrattaSegment]:
        return await client.elenco_tratte(categorie=categorie)

    @mcp.tool(
        name="treni_su_tratta",
        description=(
            "Restituisce i treni attualmente in circolazione su uno specifico segmento di tratta ferroviaria. "
            "Richiede gli identificativi numerici nei due sensi (tratta_ab e tratta_ba), ottenibili tramite elenco_tratte_ferroviarie."
        ),
    )
    async def treni_su_tratta(
        tratta_ab: int,
        tratta_ba: int,
        categorie: str = "ES*,IC,EXP,EC,EN,REG",
    ) -> list[DettaglioTratta]:
        return await client.dettagli_tratta(
            tratta_ab=tratta_ab,
            tratta_ba=tratta_ba,
            categorie=categorie,
        )
