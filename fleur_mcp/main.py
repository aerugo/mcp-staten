#!/usr/bin/env python3

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("fleur")


@mcp.prompt("default")
def get_default_prompt() -> str:
    """Get the default prompt for the Fleur Explainer MCP server."""
    return """You are Claude with the Fleur Explainer MCP activated.

When a user writes "hello fleur", you should explain that:

Fleur is an app that allows users to install and manage Model Control Protocols (MCPs) on Claude. MCPs are specialized capabilities that extend Claude's functionality, giving it access to external tools, specific knowledge bases, or custom workflows.

When a user says "hello fleur", they're activating the Fleur interface, which allows them to install, manage, and interact with these MCPs. Fleur essentially turns Claude from a general-purpose AI assistant into a specialized tool for specific tasks by loading the appropriate MCP extensions.

Keep your explanation simple, friendly, and to the point. Don't mention detail levels or other technical aspects unless specifically asked."""


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
