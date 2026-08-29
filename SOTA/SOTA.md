# Research Process Management Infrastructure

## 1. Introduction

Research on digital infrastructure for managing the scientific research lifecycle has expanded markedly since 2008, but it has grown as several partially connected literatures rather than as one coherent field. Early work centered on scientific workflow systems for computational and data-intensive experiments, especially in bioinformatics, grid, cloud, and HPC settings  (Davidson & Freire, 2008; Curcin & Ghanem, 2008; Ludäscher et al., 2009; Talia, 2013). Over time, adjacent strands matured around research data management, provenance, virtual research environments, open-science platforms, preprint and repository infrastructures, and research information systems  (Perrier et al., 2017; Donner, 2022; Pérez et al., 2018; Barker et al., 2019; Haris et al., 2026). Across these strands, the dominant concern shifted from executing computational workflows to coordinating, documenting, preserving, and evaluating increasingly distributed research activity and its artifacts  (Mattoso et al., 2015; Donner, 2022; Mayernik et al., 2017).

The strongest cross-cutting finding is that most infrastructures still privilege downstream outputs and data stewardship over active management of the research process itself. Research data sharing, repositories, curation, and dissemination are studied far more often than early-stage planning, question formulation, decision tracking, and cross-stage coordination  (Perrier et al., 2017; Donner, 2022; Cox & Tam, 2018). At the same time, reproducibility pressures, larger collaborations, heterogeneous data, and policy mandates have made integrated documentation, provenance, interoperability, and workflow support increasingly central  (Gierend et al., 2024; Klebel et al., 2025; Gilmore et al., 2017; Zhang et al., 2026).


**Figure 1:** Consensus on output-focused research infrastructure literature

The meter indicates a clear yes: the corpus emphasizes output, data, and workflow execution more than integrated lifecycle management. Evidence for end-to-end coordination exists, but it is thinner, newer, and less standardized than the literatures on repositories, RDM, and computational workflows.

## 2. Methods

This review synthesizes a Deep Search over more than 220 million research papers indexed in Consensus from Semantic Scholar, PubMed, and other sources. The search strategy combined six groups of concepts: foundational workflow and infrastructure models; terminology variants for lifecycle, coordination, provenance, and platforms; lifecycle-stage-specific searches; challenges and requirements; Git/version-control terms; and adjacent literatures such as open science, digital humanities, and data curation.

A total of 1,290,829 records were initially identified in the broad seed search, with additional targeted searches returning large overlapping sets and citation crawling identifying 3,231 related papers. Machine-learned relevance filtering screened 230 papers, 155 passed the relevance threshold after deduplication, and the top 100 most relevant review, survey, and synthesis papers were included for qualitative analysis. The review prioritized 2008–2025, while allowing earlier conceptual anchors when needed for field formation.


**Figure 2:** Deep search screening and inclusion flow

The strategy combined broad lifecycle terms with targeted searches on workflows, RDM, provenance, repositories, open science, and version control.

## 3. Results

### 3.1 Key Papers

The field is anchored by a small set of influential reviews that define the main conceptual scaffolding: scientific workflows as a response to data-intensive science, provenance as a reproducibility mechanism, and research data management as an institutional service and infrastructure problem  (Davidson & Freire, 2008; Liew et al., 2016; Perrier et al., 2017; Pérez et al., 2018). These papers matter because later domain-specific reviews repeatedly inherit their assumptions about lifecycle structure, workflow formalization, and the centrality of data and metadata stewardship  (Cox & Tam, 2018; Ho et al., 2025; Gierend et al., 2024).

| Paper | Summary |
|---|---|
|  (Davidson & Freire, 2008)| Provenance as **reproducibility infrastructure**  (Davidson & Freire, 2008)|
|  (Perrier et al., 2017)| RDM literature skews to **data sharing**  (Perrier et al., 2017)|
|  (Liew et al., 2016)| Workflows organize **complex data-intensive experiments**  (Liew et al., 2016)|

**Figure 3:** Foundational papers anchoring the review corpus

### 3.2 Field Development

Publication growth is strongest after 2010 across workflow management, RDM, provenance, and open science, with several reviews explicitly marking 2008–2010 as a turning point linked to cloud infrastructures, big data, and policy attention to research data stewardship  (Ahmad et al., 2021; Perrier et al., 2017; Pérez et al., 2018). The field remains multidisciplinary but unevenly distributed, with computer science and life sciences dominating workflow and provenance research, while library and information science leads much of the RDM, repository, and institutional support literature  (Vivas et al., 2024; Curcin & Ghanem, 2008; Perrier et al., 2017; Bóte-Vericad & Healy, 2022).

A second development is thematic diversification. Scientific workflow research branched into scheduling, resource management, dynamic steering, and user evaluation  (Vivas et al., 2024; Gonzalez et al., 2017; Mattoso et al., 2015; Loach et al., 2026). In parallel, institutional and open-science infrastructures expanded around CRIS/RIS, repositories, preprint servers, and library-led RDM services  (Otroshcenko et al., 2026; Kirkham et al., 2020; Bashir et al., 2021; Ho et al., 2025). More recent work adds AI-assisted planning, digital twins, and domain-spanning collaborative platforms, but these remain conceptually emergent relative to older workflow and RDM traditions  (Devkota et al., 2026; Yang et al., 2026; Bischl et al., 2025).

### 3.3 Challenges and Requirements

| Dimension | Challenge | Management Need | Derived Requirement | Citations |
|---|---|---|---|---|
| Tool ecosystem | Fragmented tools and custom scripts | Cross-tool continuity | **Integration across heterogeneous tools and artifacts** |  (Tutko et al., 2022; Crane et al., 2023; Panayotova, 2026)|
| Documentation | Scripts and workflows are poorly documented | Persistent context | **Structured documentation and metadata from early stages** |  (Fillbrunn et al., 2017; Holler & Kedron, 2022)|
| Provenance | Coverage is incomplete and heterogeneous | Auditable histories | **Granular, scalable provenance capture and retrieval** |  (Gierend et al., 2024; Johns et al., 2023; Alam & Roy, 2022)|
| Coordination | Multisite and collaborative work is hard to align | Shared visibility | **Role-aware coordination, monitoring, and communication** |  (Lu & Zhang, 2009; Zhang et al., 2026; Bahor et al., 2021)|
| Interoperability | Systems and metadata standards are incompatible | Reusable exchange | **Machine-readable standards, PIDs, and interoperable metadata** |  (Otroshcenko et al., 2026; Liubchych & Mamaiev, 2022; Rokem et al., 2025)|
| Sustainability | Long-term services and financing are weakly addressed | Durable operations | **Governance, funding, and workforce models for maintenance** |  (Donner, 2022; Odero & Groenewald, 2026; Poole, 2015)|

**Figure 4:** Recurring challenges and derived infrastructure requirements

The requirements literature converges on integration, metadata, provenance, interoperability, training, and governance, but it is less mature on planning, task management, and decision-history capture across the full lifecycle  (Donner, 2022; Loach et al., 2026; Michalska-Falkowska & Sargsyan, 2026).

### 3.4 Lifecycle Coverage

Lifecycle coverage is highly uneven. Data collection, processing, analysis, sharing, archiving, and publication outputs are heavily studied through SWfMSs, repositories, RDM services, preprints, and CRIS/RIS platforms  (Liu et al., 2015; Gonzalez et al., 2017; Rodrigues & Lopes, 2022; Kirkham et al., 2020; Haris et al., 2026). Provenance work also concentrates on data and computational workflows rather than upstream intellectual decisions  (Gierend et al., 2024; Oliveira et al., 2018; Jandre et al., 2020).

By contrast, idea generation, research question refinement, planning, ethics review, and decision rationale are under-represented. Reviews of RDM repeatedly note weak attention to early project phases  (Perrier et al., 2017). Metadata-rich open-science proposals explicitly recommend integrating documentation from the earliest phases because waiting until dissemination leaves most projects irreproducible  (Holler & Kedron, 2022). Emerging literatures on AI-supported planning and digital ethics platforms indicate growing interest in upstream stages, but they remain comparatively thin and conceptually unsettled  (Devkota et al., 2026; Odero & Groenewald, 2026).

### Results Timeline

- **2008**
  - 2 papers:  (Davidson & Freire, 2008; Curcin & Ghanem, 2008)- **2009**
  - 1 paper:  (Ludäscher et al., 2009)- **2013**
  - 1 paper:  (Talia, 2013)- **2015**
  - 1 paper:  (Mattoso et al., 2015)- **2016**
  - 1 paper:  (Liew et al., 2016)- **2017**
  - 3 papers:  (Perrier et al., 2017; Mayernik et al., 2017; Gilmore et al., 2017)- **2018**
  - 2 papers:  (Pérez et al., 2018; Cox & Tam, 2018)- **2019**
  - 1 paper:  (Barker et al., 2019)- **2021**
  - 1 paper:  (Ahmad et al., 2021)- **2022**
  - 1 paper:  (Donner, 2022)- **2024**
  - 2 papers:  (Gierend et al., 2024; Vivas et al., 2024)- **2025**
  - 2 papers:  (Klebel et al., 2025; Ho et al., 2025)- **2026**
  - 2 papers:  (Haris et al., 2026; Zhang et al., 2026)**Figure 5:** Research arc with larger markers indicating more citations

### Top Contributors

| Type | Name | Papers |
|------|------|--------|
| Author | Marta Mattoso | [5ae6dfa49257551a9348c6d348c1b1fb][67f838bcc37958ce9b65576b4ba5db10] |
| Author | Daniel de Oliveira | [67f838bcc37958ce9b65576b4ba5db10][29e0e9548cb95bc689f028c62388c9f1] |
| Author | Vanessa Braganholo | [29e0e9548cb95bc689f028c62388c9f1][719a5ff9367d53da9bf758a40a8fa8d7] |
| Journal | *Journal of the Association for Information Science and Technology* | [6954c5a5a257512e924a7bf4254a822b][c5339046246a5628887884fb9d9a92bc][290714c9dbab5eac902c3c72ad75d0d6] |
| Journal | *Future Gener. Comput. Syst.* | [c648dc6d75e2557c9766e52aaaa2a846][67f838bcc37958ce9b65576b4ba5db10] |
| Journal | *Journal of Medical Internet Research* | [950a80bd536a5b238895f618affd21b2][94d5e1ce9f795eaba07e802693113590] |

**Figure 6:** Authors and journals appearing most in corpus

## 4. Discussion

The literature is strongest where research work can be formalized as data pipelines, repository transactions, or institutional information flows. Workflow systems, cloud scheduling, and provenance in computational science have mature taxonomies and repeated review activity  (Liu et al., 2015; Rodriguez & Buyya, 2017; Pérez et al., 2018). RDM and library-service literatures also provide broad coverage of institutional implementation factors, stakeholders, and policy drivers  (Donner, 2022; Ho et al., 2025; Bóte-Vericad & Healy, 2022).

The literature is weaker when the object of management is not data or execution but the evolving research process itself. Lifecycle models are common, but they often oversimplify research as linear and purposive, masking iteration, tacit judgment, and informal coordination  (Cox & Tam, 2018). Many studies remain descriptive, case-based, or self-reported, with relatively little empirical evaluation of whether specific infrastructures improve research quality, traceability, or coordination outcomes  (Perrier et al., 2017; Timóteo et al., 2021; Odero & Groenewald, 2026).

A consistent validity problem is that interoperability, FAIRness, and reproducibility are often treated as design ideals rather than demonstrated end-to-end achievements. Provenance coverage is incomplete, standards uptake is uneven, metadata maintenance is burdensome, and methodological reporting often remains insufficient for replication  (Johns et al., 2023; Gierend et al., 2024; Holler & Kedron, 2022; Tutko et al., 2022). This means the field has strong normative consensus on what infrastructures should do, but more limited evidence on integrated systems that actually do it across the whole lifecycle.

| Claim | Evidence Strength | Reasoning | Papers |
|---|---|---|---|
| The field emphasizes **data, outputs, and dissemination** over full process management | Evidence strength: Strong (9/10) | Repeated across RDM, repository, and OS reviews |  (Perrier et al., 2017; Klebel et al., 2025; Donner, 2022)|
| **Workflow systems** are the most mature infrastructure tradition | Evidence strength: Strong (8/10) | Multiple surveys and taxonomies since 2008 |  (Curcin & Ghanem, 2008; Liew et al., 2016; Vivas et al., 2024)|
| **Provenance and metadata** are essential but incompletely implemented | Evidence strength: Strong (8/10) | Strong agreement on importance and coverage gaps |  (Gierend et al., 2024; Johns et al., 2023)|
| Git/GitHub support **versioning and collaboration**, but evidence is partial | Evidence strength: Moderate (5/10) | Benefits are documented, end-to-end management evidence is sparse |  (Zarghani et al., 2023; Holler & Kedron, 2022; Crystal‐Ornelas et al., 2021)|
| Early-stage planning and decision-traceability remain **understudied** | Evidence strength: Weak (3/10) | Often identified as gaps rather than evaluated interventions |  (Perrier et al., 2017; Odero & Groenewald, 2026; Devkota et al., 2026)|

**Figure 7:** Key claims and supporting evidence strength

## 5. Conclusion

Across 2008–2025, research on digital infrastructure for managing scientific work evolved from computational workflow execution toward broader concerns with data stewardship, open science, institutional information systems, and collaborative platforms. The field now has substantial evidence on workflow orchestration, repositories, RDM, and provenance, but much less on integrated management of the research process from idea formation through planning, execution, publication, and post-publication traceability.

The main implication for your study is that the literature gap is not simply “GitHub in science,” but the broader absence of evidence on infrastructures that connect coordination, documentation, decision history, versioning, provenance, and artifact linkage across the whole research lifecycle. That positioning is supported by recurring findings that current systems are fragmented, output-focused, and weak on upstream and cross-stage integration  (Crane et al., 2023; Michalska-Falkowska & Sargsyan, 2026; Münster & Apollonio, 2026).

### Research Gaps

The clearest gap is the lack of integrated lifecycle infrastructures that connect planning, execution, documentation, outputs, and provenance in one traceable environment. Existing literatures remain siloed between workflow execution, data stewardship, institutional reporting, and open dissemination.

| | Planning | Coordination | Metadata | Governance | Outputs |
|---|---|---|---|---|---|
| Workflow Systems | GAP | GAP | GAP | GAP | GAP |
| RDM Services | GAP | GAP | GAP | GAP | GAP |
| Provenance | GAP | GAP | GAP | GAP | GAP |
| Research Platforms | GAP | GAP | GAP | GAP | GAP |
| Version Control | GAP | GAP | GAP | GAP | GAP |

### Open Research Questions

Future work should move from feature descriptions to comparative, empirical studies of how infrastructures shape actual research practice. The most important unanswered questions concern integration, traceability, and institutional adoption.

| Question | Why |
|---|---|
| **How can digital infrastructures link planning decisions, workflow execution, and downstream outputs in a single traceable research record?** | Current literatures treat these functions separately, leaving decision history and cross-stage provenance weakly supported. |
| **Which combinations of version control, metadata, and repository practices measurably improve coordination and reproducibility in real research teams?** | Benefits are widely asserted, but comparative evidence on integrated practices remains limited and fragmented across domains. |
| **What organizational and governance conditions determine whether lifecycle-wide research infrastructures are adopted and sustained?** | Financing, legal alignment, workforce skills, and institutional readiness are repeatedly named barriers, but rarely evaluated systematically. |

For a *Scientometrics* study on GitHub as research infrastructure, the literature supports positioning the work in the gap between artifact hosting and genuine end-to-end research process management.
 
_These search results were found and analyzed using Consensus, an AI-powered search engine for research. Try it at https://consensus.app. © 2026 Consensus NLP, Inc. Personal, non-commercial use only; redistribution requires copyright holders’ consent._
 
## References
 
Ahmad, Z., Jehangiri, A. I., Ala'anzy, M. A., Othman, M., Latip, R., Zaman, S. K. U., & Umar, A. I. (2021). Scientific Workflows Management and Scheduling in Cloud Computing: Taxonomy, Prospects, and Challenges. *IEEE Access, 9*, 53491-53508. https://doi.org/10.1109/access.2021.3070785
 
Alam, K., & Roy, B. (2022). Challenges of Provenance in Scientific Workflow Management Systems. *2022 IEEE/ACM Workshop on Workflows in Support of Large-Scale Science (WORKS)*, 10-18. https://doi.org/10.1109/works56498.2022.00007
 
Bahor, Z., Liao, J., Currie, G. L., Ayder, C., Macleod, M., McCann, S., Bannach‐Brown, A., Wever, K., Soliman, N., Wang, Q., Doran-Constant, L., Young, L., Sena, E., & Sena, C. (2021). Development and uptake of an online systematic review platform: the early years of the CAMARADES Systematic Review Facility (SyRF). *BMJ Open Science, 5*. https://doi.org/10.1136/bmjos-2020-100103
 
Barker, M., Olabarriaga, S. D., Wilkins-Diehr, N., Gesing, S., Katz, D. S., Shahand, S., Henwood, S., Glatard, T., Jeffery, K. G., Corrie, B. D., Treloar, A. E., Glaves, H., Wyborn, L., Hong, N. C. P., & Costa, A. (2019). The global impact of science gateways, virtual research environments and virtual laboratories. *Future Gener. Comput. Syst., 95*, 240-248. https://doi.org/10.1016/j.future.2018.12.026
 
Bashir, S., Gul, S., Bashir, S., Nisa, N. T., & Ganaie, S. A. (2021). Evolution of institutional repositories: Managing institutional research output to remove the gap of academic elitism. *Journal of Librarianship and Information Science, 54*, 518 - 531. https://doi.org/10.1177/09610006211009592
 
Bischl, B., Casalicchio, G., Das, T., Feurer, M., Fischer, S., Gijsbers, P., Mukherjee, S., Müller, A., Németh, L., Oala, L., Purucker, L., Ravi, S., Van Rijn, J. N., Singh, P., Vanschoren, J., Van Der Velde, J., & Wever, M. (2025). OpenML: Insights from 10 years and more than a thousand papers. *Patterns, 6*. https://doi.org/10.1016/j.patter.2025.101317
 
Bóte-Vericad, J.-J., & Healy, S. (2022). Academic libraries and research data management. *Vjesnik bibliotekara Hrvatske*. https://doi.org/10.30754/vbh.65.3.1016
 
Cox, A., & Tam, W. (2018). A critical analysis of lifecycle models of the research process and research data management. *Aslib J. Inf. Manag., 70*, 142-157. https://doi.org/10.1108/ajim-11-2017-0251
 
Crane, K., Blatch-Jones, A., & Fackrell, K. (2023). The post-award effort of managing and reporting on funded research: a scoping review. *F1000Research, 12*. https://doi.org/10.12688/f1000research.133263.2
 
Crystal‐Ornelas, R., Varadharajan, C., Bond‐Lamberty, B., Boye, K., Burrus, M., Cholia, S., Crow, M., Damerow, J., Devarakonda, R., Ely, K., Goldman, A., Heinz, S., Hendrix, V., Kakalia, Z., Pennington, S., Robles, E., Rogers, A., Simmonds, M., Velliquette, T., . . . Agarwal, D. (2021). A Guide to Using GitHub for Developing and Versioning Data Standards and Reporting Formats. *Earth and Space Science, 8*. https://doi.org/10.1029/2021ea001797
 
Curcin, V., & Ghanem, M. (2008). Scientific workflow systems - can one size fit all?. *2008 Cairo International Biomedical Engineering Conference*, 1-9. https://doi.org/10.1109/cibec.2008.4786077
 
Davidson, S., & Freire, J. (2008). Provenance and scientific workflows: challenges and opportunities. 1345-1350. https://doi.org/10.1145/1376616.1376772
 
Devkota, N., Siddique, M., Karki, D., & Thapa, D. (2026). Research in the Age of AI – How to Plan? A Bibliometric Exploration of the Research Lifecycle. *International Research Journal of MMC*. https://doi.org/10.3126/irjmmc.v7i3.97169
 
Donner, E. K. (2022). Research data management systems and the organization of universities and research institutes: A systematic literature review. *Journal of Librarianship and Information Science, 55*, 261 - 281. https://doi.org/10.1177/09610006211070282
 
Fillbrunn, A., Dietz, C., Pfeuffer, J., Rahn, R., Landrum, G., & Berthold, M. (2017). KNIME for reproducible cross-domain analysis of life science data.. *Journal of biotechnology, 261*, 149-156. https://doi.org/10.1016/j.jbiotec.2017.07.028
 
Gierend, K., Krüger, F., Genehr, S., Hartmann, F., Siegel, F., Waltemath, D., Ganslandt, T., & Zeleke, A. (2024). Provenance Information for Biomedical Data and Workflows: Scoping Review. *Journal of Medical Internet Research, 26*. https://doi.org/10.2196/51297
 
Gilmore, R., Diaz, M. T., Wyble, B., & Yarkoni, T. (2017). Progress Toward Openness, Transparency, and Reproducibility in Cognitive Neuroscience. *Annals of the New York Academy of Sciences, 1396*, 5 - 18. https://doi.org/10.1111/nyas.13325
 
Gonzalez, N., Carvalho, T., & Miers, C. (2017). Cloud resource management: towards efficient execution of large-scale scientific applications and workflows on complex infrastructures. *Journal of Cloud Computing, 6*. https://doi.org/10.1186/s13677-017-0081-4
 
Haris, M., Auer, S., & Stocker, M. (2026). Research information systems and knowledge graphs: a review. *Frontiers in Research Metrics and Analytics, 11*. https://doi.org/10.3389/frma.2026.1786866
 
Ho, R. C. Y., Wong, S. N., Chia, P., Tang, C., & Ng, M. (2025). Research data management services in academic libraries to support the research data life cycle: A systematic review. An Annual Review of Information Science and Technology (ARIST) paper. *Journal of the Association for Information Science and Technology, 77*, 272 - 300. https://doi.org/10.1002/asi.70008
 
Holler, J., & Kedron, P. (2022). MAINSTREAMING METADATA INTO RESEARCH WORKFLOWS TO ADVANCE REPRODUCIBILITY AND OPEN GEOGRAPHIC INFORMATION SCIENCE. *The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences*. https://doi.org/10.5194/isprs-archives-xlviii-4-w1-2022-201-2022
 
Jandre, E., Diirr, B., & Braganholo, V. (2020). Provenance in Collaborative in Silico Scientific Research. *ACM SIGMOD Record, 49*, 36 - 51. https://doi.org/10.1145/3442322.3442329
 
Johns, M., Meurers, T., Wirth, F., Haber, A., Müller, A., Halilovic, M., Balzer, F., & Prasser, F. (2023). Data Provenance in Biomedical Research: Scoping Review. *Journal of Medical Internet Research, 25*. https://doi.org/10.2196/42289
 
Kirkham, J., Penfold, N. C., Murphy, F., Boutron, I., Ioannidis, J., Polka, J. K., & Moher, D. (2020). Systematic examination of preprint platforms for use in the medical and biomedical sciences setting. *BMJ Open, 10*. https://doi.org/10.1136/bmjopen-2020-041849
 
Klebel, T., Traag, V., Grypari, I., Stoy, L., & Ross-Hellauer, T. (2025). The academic impact of Open Science: a scoping review. *Royal Society Open Science, 12*. https://doi.org/10.1098/rsos.241248
 
Liew, C., Atkinson, M., Galea, M., Ang, T. F., Martin, P., & Van Hemert, J. (2016). Scientific Workflows. *ACM Computing Surveys (CSUR), 49*, 1 - 39. https://doi.org/10.1145/3012429
 
Liu, J., Pacitti, E., Valduriez, P., & Mattoso, M. (2015). A Survey of Data-Intensive Scientific Workflow Management. *Journal of Grid Computing, 13*, 457 - 493. https://doi.org/10.1007/s10723-015-9329-8
 
Liubchych, A., & Mamaiev, I. (2022). Topical issues of information support of research infrastructures. *Law and innovations*. https://doi.org/10.37772/2518-1718-2022-2(38)-4
 
Loach, M., Smith, K., & Bacon, W. (2026). A scoping review of approaches to evaluating workflow management systems for bioinformatics users. *Briefings in Bioinformatics, 27*. https://doi.org/10.1093/bib/bbag396
 
Lu, S., & Zhang, J. (2009). Collaborative Scientific Workflows. *2009 IEEE International Conference on Web Services*, 527-534. https://doi.org/10.1109/icws.2009.150
 
Ludäscher, B., Weske, M., McPhillips, T., & Bowers, S. (2009). Scientific Workflows: Business as Usual?. 31-47. https://doi.org/10.1007/978-3-642-03848-8_4
 
Mattoso, M., Dias, J., Ocaña, K. A. C. S., Ogasawara, E., Costa, F., Horta, F., Sousa, V., & De Oliveira, D. (2015). Dynamic steering of HPC scientific workflows: A survey. *Future Gener. Comput. Syst., 46*, 100-113. https://doi.org/10.1016/j.future.2014.11.017
 
Mayernik, M., Hart, D. L., Maull, K., & Weber, N. M. (2017). Assessing and tracing the outcomes and impact of research infrastructures. *Journal of the Association for Information Science and Technology, 68*. https://doi.org/10.1002/asi.23721
 
Michalska-Falkowska, A., & Sargsyan, K. (2026). Connecting biospecimens and data: a scoping review-informed conceptual framework for digital infrastructure in biobanking and genomic research in low- and middle-income countries. *Frontiers in Public Health, 14*. https://doi.org/10.3389/fpubh.2026.1835421
 
Münster, S., & Apollonio, F. (2026). Digital Visualization Infrastructures of 3D Models in a Scientific Contest. *Heritage*. https://doi.org/10.3390/heritage9020059
 
Odero, B., & Groenewald, C. (2026). Digital platforms for ethics review: a mini review. *Frontiers in Digital Health, 8*. https://doi.org/10.3389/fdgth.2026.1854560
 
Oliveira, W., De Oliveira, D., & Braganholo, V. (2018). Provenance Analytics for Workflow-Based Computational Experiments. *ACM Computing Surveys (CSUR), 51*, 1 - 25. https://doi.org/10.1145/3184900
 
Otroshcenko, M., Kramarenko, O., Hudkov, S., Maletova, O., & Utkina, M. (2026). Digital transformation in academic libraries: implementing integrated research information systems for enhanced scholarly communication and institutional knowledge management. *Digital Library Perspectives*. https://doi.org/10.1108/dlp-08-2025-0122
 
Panayotova, G. (2026). Software Applications in Biomedicine: A Narrative Review of Translational Pathways from Data to Decision. *BioMedInformatics*. https://doi.org/10.3390/biomedinformatics6010009
 
Pérez, B., Rubio, J., & Sáenz-Adán, C. (2018). A systematic review of provenance systems. *Knowledge and Information Systems, 57*, 495 - 543. https://doi.org/10.1007/s10115-018-1164-3
 
Perrier, L., Blondal, E., Ayala, A. P., Dearborn, D., Kenny, T., Lightfoot, D., Reka, R., Thuna, M., Trimble, L., & MacDonald, H. (2017). Research data management in academic institutions: A scoping review. *PLoS ONE, 12*. https://doi.org/10.1371/journal.pone.0178261
 
Poole, A. H. (2015). How has your science data grown? Digital curation and the human factor: a critical literature review. *Archival Science, 15*, 101-139. https://doi.org/10.1007/s10502-014-9236-y
 
Rodrigues, J., & Lopes, C. (2022). Solutions for Data Sharing and Storage: A Comparative Analysis of Data Repositories. 512-517. https://doi.org/10.1007/978-3-031-16802-4_55
 
Rodriguez, M. A., & Buyya, R. (2017). A taxonomy and survey on scheduling algorithms for scientific workflows in IaaS cloud computing environments. *Concurrency and Computation: Practice and Experience, 29*. https://doi.org/10.1002/cpe.4041
 
Rokem, A., Mandava, V., Cristea, N., Tambay, A., Bouchard, K. E., Berys-Gonzalez, C., & Connolly, A. J. (2025). Open-source models for development of data and metadata standards. *Patterns, 6*. https://doi.org/10.1016/j.patter.2025.101316
 
Talia, D. (2013). Workflow Systems for Science: Concepts and Tools. *International Scholarly Research Notices, 2013*, 1-15. https://doi.org/10.1155/2013/404525
 
Timóteo, M., Lourenço, E., Brochado, A. C., Domenico, L., Da Silva, J., Oliveira, B., Barbosa, R., Montemezzi, P., Mourão, C., Olej, B., & Alves, G. (2021). Digital Management Systems in Academic Health Sciences Laboratories: A Scoping Review. *Healthcare, 9*. https://doi.org/10.3390/healthcare9060739
 
Tutko, A., Henley, A. Z., & Mockus, A. (2022). How are Software Repositories Mined? A Systematic Literature Review of Workflows, Methodologies, Reproducibility, and Tools. *ArXiv, abs/2204.08108*. https://doi.org/10.48550/arxiv.2204.08108
 
Vivas, A., Tchernykh, A., & Castro, H. (2024). Trends, Approaches, and Gaps in Scientific Workflow Scheduling: A Systematic Review. *IEEE Access, 12*, 182203-182231. https://doi.org/10.1109/access.2024.3509218
 
Yang, C., Malarvizhi, A. S., Masri, Y., Smith, J., Li, Z., Huang, Q., Liu, L., & Kim, J. (2026). Digital twins as decision infrastructure: evolution, architecture, and research roadmap. *Big Earth Data*. https://doi.org/10.1080/20964471.2026.2678046
 
Zarghani, M., Nemati-Anaraki, L., Sedghi, S., Chakoli, A. N., & Rowhani-Farid, A. (2023). The Application of Open Science Potentials in Research Processes: A Comprehensive Literature Review. *Libri, 73*, 167 - 186. https://doi.org/10.1515/libri-2022-0007
 
Zhang, Y., Lal, L. S., Kim, S., Swint, J., Mauger, D. T., Merchlinski, A., Valencia, P. A., Holmes, B., Phillips, B., Baab, K. T., & Chinchilli, V. M. (2026). Evolving roles of Data Coordinating Centers in multisite research: Challenges and adaptations from a rapid scoping review. *Journal of Clinical and Translational Science, 10*. https://doi.org/10.1017/cts.2026.10755
 
