# pymupdf4llm-mcp

[![Release](https://img.shields.io/github/v/release/ai-zerolab/pymupdf4llm-mcp)](https://img.shields.io/github/v/release/ai-zerolab/pymupdf4llm-mcp)
[![Build status](https://img.shields.io/github/actions/workflow/status/ai-zerolab/pymupdf4llm-mcp/main.yml?branch=main)](https://github.com/ai-zerolab/pymupdf4llm-mcp/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/ai-zerolab/pymupdf4llm-mcp/branch/main/graph/badge.svg)](https://codecov.io/gh/ai-zerolab/pymupdf4llm-mcp)
[![Commit activity](https://img.shields.io/github/commit-activity/m/ai-zerolab/pymupdf4llm-mcp)](https://img.shields.io/github/commit-activity/m/ai-zerolab/pymupdf4llm-mcp)
[![License](https://img.shields.io/github/license/ai-zerolab/pymupdf4llm-mcp)](https://img.shields.io/github/license/ai-zerolab/pymupdf4llm-mcp)

MCP Server for pymupdf4llm, best for export PDF to markdown for LLM.

- **Github repository**: <https://github.com/ai-zerolab/pymupdf4llm-mcp/>
- **Documentation** <https://ai-zerolab.github.io/pymupdf4llm-mcp/>

## Quick Start

Run the following command to run the MCP server:

```bash
uvx pymupdf4llm-mcp@latest stdio # stdio mode
# or
uvx pymupdf4llm-mcp@latest sse # sse mode
```

Configure your cursor/windsurf/... and other MCP client to this server:

```json
{
  "mcpServers": {
    "pymupdf4llm-mcp": {
      "command": "uvx",
      "args": [
        "pymupdf4llm-mcp@latest",
        "stdio"
      ],
      "env": {}
    }
  }
}
```
