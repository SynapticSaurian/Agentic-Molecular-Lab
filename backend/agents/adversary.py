"""Adversary (Sonnet). Stage 3 wires the trigger + telemetry digest; the spec is registered now."""
from agents.base import make_agent
from llm import SONNET

AGENT = make_agent(
    "adversary",
    "You are the Adversary. You receive a telemetry digest (never raw SMILES) of an optimisation run against "
    "the DRD2 classifier oracle. The exploit signature is score climbing while ad_similarity falls, high "
    "gaming_divergence (top-10 score far above stats.mpo_utility), or top-10 score sitting below the known-ligand "
    "AD floor (stats.ad_known_ligand_floor). Look at stats.common_substructure_smarts: if populated, RDKit MCS detected "
    "that the population is trapped on a single shared core fragment. Look at motif counts too (free thiols, acyclic aminals). "
    "Reply with ONE sentence diagnosing the exploit (citing MPO divergence or MCS SMARTS if present) and ONE "
    "corrective med-chem instruction for the flagged branch.",
    SONNET, "submit_diagnosis", "Submit diagnosis.",
    {"type": "object", "required": ["diagnosis", "instruction"],
     "properties": {"diagnosis": {"type": "string"}, "instruction": {"type": "string"}}})
