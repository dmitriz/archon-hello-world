# GitHub Copilot Instructions for Archon Project

## Command Execution Preferences

**CRITICAL**: When already in the correct directory, run commands directly without prefixing with `cd`.

- ✅ **Preferred**: `python run_docker.py`
- ❌ **Avoid**: `cd c:\Users\dmitr\Projects\Archon\ && python run_docker.py`

**Reason**: Using `cd` prefix causes Windows authentication prompts which disrupts workflow.

## Package Management Preferences

**CRITICAL**: Always use `uv` instead of `pip` for Python package management. UV is confirmed working in user's environment.

- ✅ **Preferred**: `uv add package-name` or `uv pip install package-name`
- ❌ **Avoid**: `pip install package-name`

**Reason**: User prefers uv for faster and better Python package management. UV is actively used and working properly.

## Project Overview
Archon is an AI Agent Builder - Streamlit UI on port 8501, Docker setup via `run_docker.py`, MCP integration for AI IDEs.

## Key Info
- Main app: `streamlit_ui.py` (port 8501)
- Docker: `python run_docker.py` to build and run
- Core logic: `archon/` package
- UI components: `streamlit_pages/`
- Examples/tools: `agent-resources/`
