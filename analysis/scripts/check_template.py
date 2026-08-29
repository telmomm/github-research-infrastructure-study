#!/usr/bin/env python3
"""Consistency checks for the reusable template (Phase 7).

- every path in template/template_manifest.csv exists
- every architecture component (framework/architecture/architecture_components.csv)
  is covered by >= 1 template file, OR is an explicit configuration-only component
- every requirement RM1-RM15 is touched by >= 1 template file

Outputs results/framework/template_coverage.csv + template_summary.md
Standard library only.
"""

import csv
import os
import re
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TPL = os.path.join(ROOT, "template")
ARCH = os.path.join(ROOT, "framework", "architecture", "architecture_components.csv")
OUT = os.path.join(ROOT, "results", "framework")

# components realised as GitHub configuration, not files
CONFIG_ONLY = {"A1", "A2", "D2", "X1"}  # Project fields/board, Zenodo webhook, public visibility


def read(p):
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def toks(s):
    return [t.strip() for t in re.split(r"[;|]", s or "") if t.strip()]


def main():
    manifest = read(os.path.join(TPL, "template_manifest.csv"))
    comps = read(ARCH)
    comp_ids = [c["comp_id"] for c in comps]

    missing = [m["path"] for m in manifest
               if not os.path.exists(os.path.join(TPL, "github-research-project-template", m["path"]))]

    comp_files = defaultdict(list)
    rm_files = defaultdict(list)
    for m in manifest:
        for c in toks(m["arch_component"]):
            comp_files[c].append(m["path"])
        for rm in toks(m["requirements"]):
            rm_files[rm].append(m["path"])

    comp_gap = [c for c in comp_ids if not comp_files.get(c) and c not in CONFIG_ONLY]
    rm_ids = [f"RM{i}" for i in range(1, 16)]
    rm_gap = [rm for rm in rm_ids if not rm_files.get(rm)]

    # also: files on disk not in the manifest (excluding .gitkeep)
    on_disk = []
    base = os.path.join(TPL, "github-research-project-template")
    for dp, _, fns in os.walk(base):
        for fn in fns:
            if fn == ".gitkeep":
                continue
            rel = os.path.relpath(os.path.join(dp, fn), base)
            on_disk.append(rel)
    manifest_paths = {m["path"] for m in manifest}
    unlisted = sorted(set(on_disk) - manifest_paths)

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "template_coverage.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["comp_id", "name", "config_only", "n_template_files", "files"])
        for c in comps:
            cid = c["comp_id"]
            w.writerow([cid, c["name"], "yes" if cid in CONFIG_ONLY else "",
                        len(comp_files.get(cid, [])), " ".join(comp_files.get(cid, []))])

    lines = ["# Template coverage — summary\n",
             f"- Template files in manifest: **{len(manifest)}**",
             f"- Files on disk not in manifest: {unlisted or 'none'}",
             f"- Manifest paths missing on disk: {missing or 'none'}",
             f"- Architecture components with no template file (excl. config-only "
             f"{sorted(CONFIG_ONLY)}): {comp_gap or 'none'}",
             f"- Requirements RM1-RM15 not touched by any template file: {rm_gap or 'none'}\n",
             "## Files per architecture component\n"]
    for c in comps:
        cid = c["comp_id"]
        tag = " (config-only)" if cid in CONFIG_ONLY else ""
        lines.append(f"- {cid} {c['name']}{tag}: {len(comp_files.get(cid, []))}")
    lines.append("")
    with open(os.path.join(OUT, "template_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("\n".join(lines))

    if missing or comp_gap or rm_gap or unlisted:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
