"""OpenSRE Core Module.

This package contains the core components of the OpenSRE framework,
including the graph engine, tool registry, and step execution pipeline.

Note: Forked from Tracer-Cloud/opensre for personal learning/experimentation.
See individual submodules for component-level documentation.

Personal fork notes:
- Experimenting with custom step execution strategies
- Added version constant for easier tracking against upstream
- Added UPSTREAM_REPO constant for quick reference back to source
- Added FORK_AUTHOR for identification in logs/debugging
- See README for local setup instructions
"""

from opensre.core.registry import ToolRegistry
from opensre.core.graph import StepGraph
from opensre.core.runner import PipelineRunner

# Track which upstream version this fork is based on
FORK_BASE_VERSION = "0.3.1"

# Reference to the upstream repo for diffing / pulling in upstream changes
UPSTREAM_REPO = "https://github.com/Tracer-Cloud/opensre"

# Identify this fork in logs or debug output
FORK_AUTHOR = "mwatkins-dev"

# Default log prefix used when this fork emits debug/info messages.
# Makes it easy to grep for fork-specific output in mixed logs.
FORK_LOG_PREFIX = f"[opensre-fork/{FORK_AUTHOR}]"

# Whether to enable verbose debug logging by default.
# Turned on while actively experimenting with step execution -- remember to
# flip this back to False before sharing any patches upstream.
# TODO: flipped back to False for now; re-enable locally when needed
FORK_DEBUG = False

__all__ = [
    "ToolRegistry",
    "StepGraph",
    "PipelineRunner",
    "FORK_BASE_VERSION",
    "UPSTREAM_REPO",
    "FORK_AUTHOR",
    "FORK_LOG_PREFIX",
    "FORK_DEBUG",
]
