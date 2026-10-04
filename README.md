# ViaggiaTreno MCP Server

Server MCP (Model Context Protocol) sviluppato con **FastMCP**, **Pydantic** e **uv** per interrogare in tempo reale le API della rete ferroviaria italiana attraverso il portale **ViaggiaTreno**.

## Caratteristiche

- **Separazione architetturale pulita**:
  - `viaggiatreno_mcp/api/`: client HTTP asincrono (`ViaggiaTrenoClient`) e parser dedicati per testi e frammenti HTML.
  - `viaggiatreno_mcp/models/`: modelli Pydantic v2 strutturati con validazione permissiva (`extra="ignore"`) per gestire le particolarità e i formati eterogenei delle API non ufficiali.
  - `viaggiatreno_mcp/tools/`: registrazione modulare dei tool MCP suddivisi per area logica (stazioni, tabelloni partenze/arrivi, treni, tratte/rete e servizi).
  - `viaggiatreno_mcp/server.py`: istanza del server FastMCP e punto di ingresso.
- **Risoluzione intelligente**: il tool `stato_treno` accetta solo il numero di treno (es. `9611`) e ricava automaticamente stazione di origine e data di partenza senza richiedere passaggi intermedi.
- **Gestione robusta degli endpoint ViaggiaTreno**: supporto corretto per `204 No Content`, risposte `text/plain`, date in formato JavaScript e frammenti HTML di infomobilità.

## Struttura del Progetto

```
viaggiatreno_mcp/
├── pyproject.toml
├── README.md
├── VIAGGIATRENO.md            # Riferimento completo endpoint API
├── src/
│   └── viaggiatreno_mcp/
│       ├── __init__.py
│       ├── __main__.py
│       ├── server.py          # FastMCP server e CLI
│       ├── api/               # Chiamate di rete e parser
│       │   ├── __init__.py
│       │   ├── client.py      # ViaggiaTrenoClient (async)
│       │   └── parsers.py     # Parser autocompletamento e RSS HTML
│       ├── models/            # Modelli Pydantic
│       │   ├── __init__.py
│       │   ├── common.py      # Costanti (regioni, codici cliente, stati)
│       │   ├── station.py     # Stazioni e dettagli geografici
│       │   ├── train.py       # Treni, fermate, tabelloni e canvas
│       │   ├── route.py       # Tratte e segmenti ferroviari
│       │   └── service.py     # Statistiche, infomobilità e meteo
│       └── tools/             # Tool MCP registrati con FastMCP
│           ├── __init__.py
│           ├── stations.py
│           ├── departures_arrivals.py
│           ├── trains.py
│           ├── routes.py
│           └── service.py
├── samples/                   # Risposte campione reali per test offline
└── tests/                     # Suite di test pytest completa
    ├── conftest.py
    ├── test_client.py
    ├── test_models.py
    ├── test_parsers.py
    └── test_tools.py
```

## Tool MCP Disponibili

### 1. Stazioni (`tools/stations.py`)
- `autocompleta_stazione(prefisso: str)`: suggerimenti veloci per prefisso (restituisce nome e codice stazione `S...`).
- `cerca_stazione(prefisso: str)`: ricerca stazioni con anagrafica strutturata (id, nome breve, nome lungo, comune).
- `dettaglio_stazione(codice_stazione: str, codice_regione: int | None = None)`: coordinate GPS (lat/lon), comune e dettagli della stazione. Se `codice_regione` è omesso, viene risolto automaticamente.
- `elenco_stazioni_regione(codice_regione: int)`: elenco completo stazioni di una regione (1=Lombardia, 3=Piemonte, 5=Lazio, 8=Emilia Romagna, 13=Toscana, 0=Principali italiane).
- `codice_regione_stazione(codice_stazione: str)`: restituisce il codice regione per una stazione.
- `autocompleta_stazione_nts(prefisso: str)`: ricerca nodi tecnici ferroviari con codici RICS NTS (83...).

### 2. Partenze e Arrivi (`tools/departures_arrivals.py`)
- `tabellone_partenze(codice_stazione: str, data_ora: str | None = None)`: partenze in tempo reale, orario programmato, ritardo, binario programmato ed effettivo, stato.
- `tabellone_arrivi(codice_stazione: str, data_ora: str | None = None)`: arrivi in tempo reale con stazione di provenienza, orario, ritardo e binario.

### 3. Treni (`tools/trains.py`)
- `cerca_numero_treno(numero_treno: int)`: trova le corse attive per il numero indicato, con stazione di partenza e data.
- `stato_treno(numero_treno: int, codice_stazione_origine: str | None = None, data_partenza: int | None = None)`: andamento in tempo reale, ritardo, ultimo rilevamento, stato e dettaglio di tutte le fermate commerciali con orari e binari.
- `itinerario_treno_canvas(codice_stazione_origine: str, numero_treno: int, data_partenza: int)`: rappresentazione ad albero delle fermate con flag di attraversamento e treno in stazione.

### 4. Tratte e Rete (`tools/routes.py`)
- `elenco_tratte_ferroviarie(categorie: str = "ES*,IC,EXP,EC,EN,REG")`: segmenti della rete nazionale con nodi estremi e flag di occupazione da treni.
- `treni_su_tratta(tratta_ab: int, tratta_ba: int, categorie: str = "ES*,IC,EXP,EC,EN,REG")`: treni attualmente in circolazione sul segmento specificato.

### 5. Servizi e Infomobilità (`tools/service.py`)
- `statistiche_servizio()`: totale treni previsti oggi e treni attualmente in circolazione.
- `notizie_infomobilita(solo_lavori: bool = False)`: notizie complete su circolazione, scioperi, guasti o lavori programmati.
- `titoli_infomobilita(solo_lavori: bool = False)`: titoli sintetici degli avvisi attivi.
- `ticker_infomobilita()`: messaggi brevi della striscia informativa.
- `meteo_stazioni(codice_regione: int)`: previsioni meteo per le stazioni della regione.
- `dizionario_lingua(id_lingua: str = "it")`: dizionario traduzioni interfaccia ViaggiaTreno.

## Installazione e Avvio

Con `uv`:

```bash
# Installa le dipendenze
uv sync

# Esegui il server MCP (protocollo stdio per client MCP)
uv run viaggiatreno-mcp
```

Oppure direttamente con `python`:

```bash
uv run python -m viaggiatreno_mcp
```

## Configurazione nei Client MCP

### Claude Desktop (`claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "viaggiatreno": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/percorso/a/viaggiatreno_mcp",
        "viaggiatreno-mcp"
      ]
    }
  }
}
```

### Cursor / VS Code / Altri Client

Configura un server MCP di tipo `command`:
- **Command**: `uv`
- **Args**: `["run", "--directory", "/percorso/a/viaggiatreno_mcp", "viaggiatreno-mcp"]`

## Esecuzione dei Test

Tutti i test usano risposte reali salvate nella directory `samples/` e vengono eseguiti offline senza dipendere dalla rete esterna:

```bash
uv run pytest
```
