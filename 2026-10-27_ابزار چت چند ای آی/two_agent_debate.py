#!/usr/bin/env python3
"""
Two-agent debate prototype using OpenRouter's OpenAI-compatible API.
- Round 1: independent analyses (agents do not see each other's answers)
- Round 2: each critiques the other's analysis
- Round 3: each responds to the critique and states remaining disagreement

Only uses Python's standard library. No API key is stored in this file.
"""

import getpass
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime

API_URL = "https://openrouter.ai/api/v1/chat/completions"

# These are examples, not guarantees of current availability.
DEFAULT_A = "google/gemma-4-31b-it:free"
DEFAULT_B = "nvidia/nemotron-3-ultra-550b-a55b:free"

def call_model(api_key, model, system_prompt, user_prompt, max_tokens=1200):
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.7,
        "max_tokens": max_tokens,
    }
    request = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "Two-Agent Debate Prototype",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc
    except Exception as exc:
        raise RuntimeError(f"Request failed: {exc}") from exc

    try:
        return data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError):
        raise RuntimeError("Unexpected API response:\n" + json.dumps(data, ensure_ascii=False, indent=2))

def save_transcript(topic, model_a, model_b, sections):
    folder = "debate_results"
    os.makedirs(folder, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(folder, f"debate_{stamp}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Two-Agent Debate\n\n")
        f.write(f"**Date:** {datetime.now().isoformat(timespec='seconds')}\n\n")
        f.write(f"**Agent A:** `{model_a}`  \n**Agent B:** `{model_b}`\n\n")
        f.write("> Keep private or confidential information out of prompts. Provider logging and retention policies may apply.\n\n")
        f.write("## Topic\n\n" + topic + "\n\n")
        for heading, body in sections:
            f.write(f"## {heading}\n\n{body}\n\n")
    return path

def main():
    print("=" * 66)
    print(" TWO-AGENT DEBATE — prototype")
    print("=" * 66)
    print("Uses OpenRouter API. Free endpoints can be rate-limited or unavailable.")
    print("Do not enter confidential or personal information in the topic.")
    print()

    api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not api_key:
        api_key = getpass.getpass("OpenRouter API key (input hidden): ").strip()
    if not api_key:
        print("No API key supplied. Exiting.")
        sys.exit(1)

    model_a = input(f"Model A [{DEFAULT_A}]: ").strip() or DEFAULT_A
    model_b = input(f"Model B [{DEFAULT_B}]: ").strip() or DEFAULT_B
    if model_a == model_b:
        print("Note: both agents use the same model ID; this weakens the test of viewpoint diversity.")

    print("\nEnter the discussion topic/prompt. Finish with a line containing only END.")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "END":
            break
        lines.append(line)
    topic = "\n".join(lines).strip()
    if not topic:
        print("Empty topic. Exiting.")
        sys.exit(1)

    role_a = (
        "You are Agent A in a multi-perspective debate. Think independently. "
        "State your assumptions, recommendation or position, strongest reasons, "
        "uncertainties, and the strongest objection to your own position. "
        "Do not try to agree with an unseen agent. Be specific and concise."
    )
    role_b = (
        "You are Agent B in a multi-perspective debate. Think independently and do not imitate "
        "a presumed consensus. State assumptions, position, strongest reasons, uncertainties, "
        "and the strongest objection to your own position. Look for alternative framings."
    )

    sections = []
    print("\n[1/3] Getting independent answers. Each agent sees only the original topic...")
    try:
        a1 = call_model(api_key, model_a, role_a, topic)
        print("\n--- Agent A: initial position ---\n")
        print(a1)
        b1 = call_model(api_key, model_b, role_b, topic)
        print("\n--- Agent B: initial position ---\n")
        print(b1)
        sections.append(("Round 1 — independent positions", f"### Agent A\n\n{a1}\n\n### Agent B\n\n{b1}"))

        print("\n[2/3] Each agent now sees the other's answer and critiques it...")
        a2_prompt = (
            f"Original topic:\n{topic}\n\nYour initial answer:\n{a1}\n\n"
            f"Agent B's answer:\n{b1}\n\n"
            "Critique Agent B's reasoning fairly and specifically. Identify its strongest point, "
            "weakest assumption or inference, missing evidence, and what (if anything) changes your view. "
            "Do not manufacture disagreement; if you agree on a point, say why."
        )
        b2_prompt = (
            f"Original topic:\n{topic}\n\nYour initial answer:\n{b1}\n\n"
            f"Agent A's answer:\n{a1}\n\n"
            "Critique Agent A's reasoning fairly and specifically. Identify its strongest point, "
            "weakest assumption or inference, missing evidence, and what (if anything) changes your view. "
            "Do not manufacture disagreement; if you agree on a point, say why."
        )
        a2 = call_model(api_key, model_a, role_a, a2_prompt)
        print("\n--- Agent A: critique of B ---\n")
        print(a2)
        b2 = call_model(api_key, model_b, role_b, b2_prompt)
        print("\n--- Agent B: critique of A ---\n")
        print(b2)
        sections.append(("Round 2 — mutual critique", f"### Agent A critiques B\n\n{a2}\n\n### Agent B critiques A\n\n{b2}"))

        print("\n[3/3] Each agent responds to the critique and records unresolved differences...")
        a3_prompt = (
            f"Original topic:\n{topic}\n\nYour initial answer:\n{a1}\n\n"
            f"Agent B's initial answer:\n{b1}\n\nYour critique of B:\n{a2}\n\n"
            f"B's critique of you:\n{b2}\n\n"
            "Respond to the strongest criticism of your position. State what you revise, what you still defend, "
            "what evidence would change your mind, and any disagreement that remains unresolved. "
            "Do not claim consensus unless the reasoning supports it."
        )
        b3_prompt = (
            f"Original topic:\n{topic}\n\nYour initial answer:\n{b1}\n\n"
            f"Agent A's initial answer:\n{a1}\n\nYour critique of A:\n{b2}\n\n"
            f"A's critique of you:\n{a2}\n\n"
            "Respond to the strongest criticism of your position. State what you revise, what you still defend, "
            "what evidence would change your mind, and any disagreement that remains unresolved. "
            "Do not claim consensus unless the reasoning supports it."
        )
        a3 = call_model(api_key, model_a, role_a, a3_prompt)
        print("\n--- Agent A: final position ---\n")
        print(a3)
        b3 = call_model(api_key, model_b, role_b, b3_prompt)
        print("\n--- Agent B: final position ---\n")
        print(b3)
        sections.append(("Round 3 — response and unresolved disagreement", f"### Agent A\n\n{a3}\n\n### Agent B\n\n{b3}"))

        path = save_transcript(topic, model_a, model_b, sections)
        print(f"\nSaved transcript: {os.path.abspath(path)}")
        print("Note: this is a prototype. It does not guarantee genuinely independent reasoning or equal model quality.")

    except RuntimeError as exc:
        print("\nERROR:", exc)
        print("\nIf the error mentions rate limits, try again later or choose another currently free model ID.")
        print("If it mentions an unavailable model, check OpenRouter's current free-model list.")
        print("No paid fallback is configured in this script.")

if __name__ == "__main__":
    main()
