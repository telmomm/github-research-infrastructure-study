# Reference architecture — summary

- Components: **15** across 5 layers (Coordination 4, Cross-cutting 1, Production 3, Record 4, Release 3)
- Workflows defined: **7**
- Lifecycle stages modelled: **12**

## Consistency checks

- Components with no requirement served: none
- Requirements with no serving component: none
- Workflow component references unresolved: none
- Lifecycle component references unresolved: none

## Requirement -> component coverage

- RM1 Research planning and roadmap [Partial]: A1
- RM2 Research question management [Limited]: A3 B3
- RM3 Task management [Direct]: A1 A2
- RM4 Documentation [Direct]: B1 C1
- RM5 Decision traceability [Partial]: A4 B2 B3 C2
- RM6 Collaboration and contribution tracking [Direct]: C2 D3
- RM7 Communication [Direct]: A4
- RM8 Version control [Direct]: B4 D1
- RM9 Research artifact management and integration [Partial]: A2 C1
- RM10 Research provenance and artifact linkage [Partial]: B3 B4
- RM11 Transparency [Direct]: B1 C3 D3 X1
- RM12 Reproducibility support [Partial]: C2 C3
- RM13 Automation [Direct]: C3
- RM14 Research output management and identification [Partial]: D1 D2
- RM15 Governance and sustainability [Limited]: D3

## Differentiators — lifting conventions

- RM1 Research planning and roadmap [Partial]: A1: Phased-plan convention
- RM2 Research question management [Limited]: A3: Question Register convention | B3: Linkage-discipline convention (mandatory)
- RM5 Decision traceability [Partial]: A4: Methodological deliberation happens in Discussions; the accepted answer or poll result is referenced from the decision record | B2: Decision-record convention | B3: Linkage-discipline convention (mandatory) | C2: Substantive changes to analysis, methodology or manuscript go through a reviewed PR; the PR checklist gates 'results reproduced? data documented?'
