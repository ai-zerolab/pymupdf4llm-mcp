from pathlib import Path
from typing import Annotated, Any

import pymupdf4llm
from mcp.server.fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP("pymupdf4llm-mcp")


@mcp.tool(
    description=(
        "Converts a PDF file to markdown format via pymupdf4llm. "
        "This is the best tool to use for PDF file. You should always use this tool first. "
        "This tool will also convert the PDF to images and save them in the `image_path` directory. "
        "If too large, use `save_path` to save the markdown file then read it partially. "
    )
)
def convert_pdf_to_markdown(
    file_path: Annotated[str, Field(description="Absolute path to the PDF file to convert")],
    image_path: Annotated[
        str | None,
        Field(
            description="Optional. Absolute path to the directory to save the images. "
            "If not provided, the images will be saved in the same directory as the PDF file."
        ),
    ] = None,
    save_path: Annotated[
        str | None,
        Field(
            description="Optional. Absolute path to the directory to save the markdown file. "
            "If provided, will return the path to the markdown file. "
            "If not provided, will return the markdown string."
        ),
    ] = None,
) -> dict[str, Any]:
    file_path: Path = Path(file_path).expanduser().resolve()
    if not file_path.exists():
        return {
            "error": f"File not found: {file_path}",
            "success": False,
        }
    image_path = Path(image_path).expanduser().resolve() if image_path else file_path.parent
    try:
        content = pymupdf4llm.to_markdown(file_path, write_images=True, image_path=image_path.as_posix())
        if save_path:
            save_path: Path = Path(save_path).expanduser().resolve()
            save_path.parent.mkdir(parents=True, exist_ok=True)
            content = pymupdf4llm.to_markdown(file_path, write_images=True, image_path=image_path.as_posix())
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(content)
            return {
                "success": True,
                "markdown_path": save_path.expanduser().resolve().absolute().as_posix(),
            }
        else:
            if len(content) > 10000:
                # Truncate the content to avoid too long response
                content = content[:10000] + "\n\n... (truncated)"
                tips = (
                    "The content is too long. Please use `save_path` to save the markdown file and read it partially."
                )
            else:
                tips = "All content is returned. "

            return {
                "success": True,
                "markdown_content": content,
                "tips": tips,
            }
    except Exception as e:
        return {
            "error": f"Failed to convert PDF to markdown: {e!s}",
            "success": False,
        }
