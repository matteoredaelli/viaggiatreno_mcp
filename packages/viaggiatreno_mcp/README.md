# viaggiatreno-mcp

Server [MCP](https://modelcontextprotocol.io) (Model Context Protocol) per
interrogare in tempo reale la rete ferroviaria italiana tramite le API di
ViaggiaTreno.

Il server è un adattatore sottile: espone come tool MCP le funzionalità della
libreria [`viaggiatreno`](https://pypi.org/project/viaggiatreno/), senza
conoscere i dettagli delle API sottostanti. Permette ad assistenti come Claude
di cercare stazioni, consultare tabelloni partenze/arrivi, monitorare ritardi e
andamento dei treni, controllare le tratte e leggere le notizie di infomobilità.

## Installazione

```bash
pip install viaggiatreno-mcp
```

## Avvio

```bash
# tramite lo script console
viaggiatreno-mcp

# oppure come modulo
python -m viaggiatreno_mcp
```

## Dipendenze

- [`viaggiatreno`](https://pypi.org/project/viaggiatreno/) — libreria client core
- [`fastmcp`](https://pypi.org/project/fastmcp/) — framework MCP

## Licenza

Vedi il file `LICENSE` nel repository.

Repository: https://github.com/matteoredaelli/pyviaggiatreno
