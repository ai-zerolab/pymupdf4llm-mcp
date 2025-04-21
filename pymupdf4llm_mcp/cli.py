import typer

from pymupdf4llm_mcp.app import mcp

app = typer.Typer()


@app.command()
def stdio():
    mcp.run(transport="stdio")


@app.command()
def sse(
    host: str = "localhost",
    port: int = 3000,
):
    mcp.settings.host = host
    mcp.settings.port = port
    mcp.run(transport="sse")


if __name__ == "__main__":
    app(["stdio"])
