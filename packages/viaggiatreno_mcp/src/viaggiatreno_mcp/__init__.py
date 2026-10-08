"""ViaggiaTreno MCP Server."""

from viaggiatreno import ViaggiaTrenoClient

from viaggiatreno_mcp.server import create_server, mcp

__all__ = [
    "ViaggiaTrenoClient",
    "create_server",
    "mcp",
]
