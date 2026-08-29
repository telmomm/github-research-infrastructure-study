# Background Synthesis: Digital Infrastructure for Managing the Research Process

*Phase 2 deliverable — working synthesis, not manuscript prose. Feeds the Introduction (§8.2–8.5 of `docs/PAPER_PLAN.md`) and Results §10.1, to be redacted into `manuscript/paper.tex` in Phase 11 (earliest sensible start: end of Phase 3, once the requirements framework is locked and Track A is done). Evidence base: `literature/` (Track B, normalised from `SOTA/SOTA.md`). Citation keys resolve against `literature/references.bib`. Must be complemented with the quantitative Track A bibliometric map before submission.*

---

## 1. A field assembled from adjacent literatures

Research on digital infrastructure for the scientific research lifecycle has grown since 2008, but as several partially connected literatures rather than one field. Early work centred on **scientific workflow systems** for computational and data-intensive experiments in bioinformatics, grid, cloud and HPC settings [curcin2008; davidson2008; ludascher2009; talia2013]. Adjacent strands then matured around **research data management** [perrier2017; donner2022; ho2025], **provenance** [davidson2008; perez2018; gierend2024], **virtual research environments and science gateways** [barker2019], **open-science practice** [gilmore2017; zarghani2023; klebel2025], **preprint and repository infrastructures** [kirkham2020; bashir2021; rodrigues2022], and **research information systems** [haris2026; otroshcenko2026]. Across these strands the dominant concern shifted from *executing* computational workflows to *coordinating, documenting, preserving and evaluating* increasingly distributed research activity and its artifacts [mattoso2015; mayernik2017; donner2022].

Of the 52 review, survey and synthesis studies in our Track B evidence base, 13 sit in the scientific-workflow strand and 10 in research information systems, against only 2 explicitly on version control in research and 4 on emergent infrastructure (AI-assisted planning, digital twins, ethics platforms). The literature is strongest where research work can be formalised as data pipelines, repository transactions or institutional information flows [liu2015; rodriguez2017; perez2018], and thinner where the object of management is the evolving research process itself.

## 2. The output bias

The strongest cross-cutting finding is that most infrastructures privilege **downstream outputs and data stewardship** over active management of the research process. Data sharing, repositories, curation and dissemination are studied far more often than early-stage planning, question formulation, decision tracking and cross-stage coordination [perrier2017; donner2022; cox2018; klebel2025]. Scoping reviews of research data management repeatedly note weak attention to the early phases of projects [perrier2017], and metadata-focused open-science proposals argue explicitly for integrating documentation from the earliest stages because deferring it to dissemination leaves most projects irreproducible [holler2022].

Classifying the 52 studies by their primary lifecycle focus reproduces this bias: 22 address the execution stages (data collection, processing, analysis), 7 the output stages, and only 3 the upstream stages of idea generation, question refinement and planning. A stage-level reading of the same corpus (`literature/lifecycle_coverage.csv`) rates 7 of 15 lifecycle stages as thinly covered — idea generation, question refinement, planning, ethics review, post-publication traceability, cross-stage coordination, and governance/sustainability — against heavy coverage of data collection, processing, analysis and dissemination.

## 3. Recurring challenges and derived requirements

Six challenge–requirement pairs recur across the evidence base:

| Challenge | Management need | Derived requirement | Evidence |
|---|---|---|---|
| Fragmented tools and custom scripts | Cross-tool continuity | Integration across heterogeneous tools and artifacts | [tutko2022; crane2023; panayotova2026] |
| Scripts and workflows are poorly documented | Persistent context | Structured documentation and metadata from early stages | [fillbrunn2017; holler2022] |
| Provenance coverage is incomplete and heterogeneous | Auditable histories | Granular, scalable provenance capture and retrieval | [gierend2024; johns2023; alam2022] |
| Multisite and collaborative work is hard to align | Shared visibility | Role-aware coordination, monitoring and communication | [lu2009; zhang2026; bahor2021] |
| Systems and metadata standards are incompatible | Reusable exchange | Machine-readable standards, PIDs and interoperable metadata | [otroshcenko2026; liubchych2022; rokem2025] |
| Long-term services and financing are weakly addressed | Durable operations | Governance, funding and workforce models for maintenance | [donner2022; odero2026; poole2015] |

The requirements literature converges on integration, metadata, provenance, interoperability, training and governance, but is markedly less mature on **planning, task management and decision-history capture across the full lifecycle** [donner2022; loach2026; michalskafalkowska2026]. Provenance work in particular concentrates on data and computational workflows rather than upstream intellectual decisions [gierend2024; johns2023; jandre2020]. The full challenge-to-requirement extraction, mapped to fourteen research-management requirement domains, is in `literature/requirements_extraction.csv`; of its seventeen rows, only three are rated as well covered by existing infrastructure, while the upstream planning, question-tracking and decision-history requirements are all rated weak-gap.

## 4. Version control and GitHub in research

Git and GitHub are documented as effective for versioning and collaboration in research settings — for developing and versioning community data standards [crystalornelas2021], and, in the adjacent reproducibility literature, for laboratory and ecological research workflows. But the evidence for GitHub as an infrastructure for the *whole* research process is partial: benefits are asserted case by case, and end-to-end management evidence is sparse [tutko2022; crystalornelas2021]. Systematic study of how software repositories are mined shows the same fragmentation — heterogeneous workflows, inconsistent tooling and weak reproducibility — at the meta-level [tutko2022].

## 5. The gap this study addresses

The literature has a strong normative consensus on *what* research infrastructure should do, but limited evidence on integrated systems that actually do it across the lifecycle. Lifecycle models are common yet often oversimplify research as linear and purposive, masking iteration, tacit judgement and informal coordination [cox2018]. Many studies remain descriptive, case-based or self-reported, with little empirical evaluation of whether specific infrastructures improve traceability or coordination [perrier2017; timoteo2021; odero2026].

The gap is therefore not "GitHub in science" narrowly, but the broader absence of evidence on infrastructures that connect **coordination, documentation, decision history, versioning, provenance and artifact linkage in one traceable environment**, spanning planning through post-publication [crane2023; michalskafalkowska2026; munster2026]. This study addresses that gap by (RQ1) mapping the field bibliometrically and locating its lifecycle blind spots, (RQ2) deriving a lifecycle-structured requirements framework from this literature, (RQ3) measuring how far GitHub's native functionalities cover those requirements, and (RQ4-RQ5) consolidating the covered functionalities into a reusable architecture and template and testing it self-referentially.
