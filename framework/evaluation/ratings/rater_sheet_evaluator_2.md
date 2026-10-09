# Platform rating sheet

**Escala aplicada:** 3 = nativo; 2 = posible por convención; 1 = marginal; 0 = ausente.  
**Criterio:** planes gratuitos, proyectos públicos y hasta cinco personas. He tratado como “nativo” únicamente lo que la plataforma ofrece como función estructurada; README, etiquetas, nombres de ramas o convenciones documentales se han puntuado como 2 o menos. GitHub Free ofrece funciones completas en repositorios públicos y 2.000 minutos mensuales de Actions; GitLab Free integra issues, milestones, tableros, CI/CD y releases; Bitbucket Free limita Pipelines a 50 minutos mensuales y Git LFS a 1 GB. [docs.github](https://docs.github.com/en/get-started/learning-about-github/githubs-plans)

## Hoja de puntuación

| Test | A | B | C | D | Notes |
|---|---:|---:|---:|---:|---|
| **RM1.1** | 2 | 3 | 1 | 3 | GitHub Projects/issues y Bitbucket/Jira pueden representar fases, fechas y trabajo, pero GitHub/Bitbucket solo requieren configuración por convención. GitLab milestones son nativos; Jira ofrece versiones/epics y fechas. |
| **RM1.2** | 2 | 2 | 1 | 3 | GitHub y GitLab permiten objetivos mediante issues, milestones o campos; no ofrecen un sistema completo de objetivos en este contexto. Jira permite objetivos y seguimiento mediante sus objetos de planificación. |
| **RM1.3** | 1 | 2 | 0 | 3 | GitLab puede representar una hoja de ruta con milestones, aunque la vista de roadmap depende de la configuración disponible. Jira ofrece roadmap básico en Free; los Advanced Roadmaps son de pago.  [docs.gitlab](https://docs.gitlab.com/user/project/issue_board/) |
| **RM1.4** | 3 | 3 | 3 | 3 | Git guarda historial de archivos y commits; Jira/Confluence añaden historial de cambios en la configuración D. |
| **RM2.1** | 2 | 2 | 1 | 3 | GitHub/GitLab pueden usar issues; GitLab los trata como objetos de planificación. En C sería principalmente un issue o documento genérico. Jira permite un tipo de work item identificable.  [docs.gitlab](https://docs.gitlab.com/user/project/issues/) |
| **RM2.2** | 3 | 3 | 3 | 3 | El historial de commits, ediciones de issues y páginas permite recuperar formulaciones anteriores. |
| **RM2.3** | 2 | 2 | 1 | 3 | GitHub/GitLab permiten referencias y enlaces cruzados, pero la relación pregunta–evidencia no es un tipo nativo específico. Jira permite enlazar work items; Confluence añade enlaces bidireccionales razonables. |
| **RM3.1** | 3 | 3 | 2 | 3 | Issues nativos en GitHub/GitLab; Bitbucket dispone de objetos de colaboración más limitados; Jira ofrece tareas. |
| **RM3.2** | 3 | 3 | 2 | 3 | GitHub Projects y GitLab issue boards permiten estados; Bitbucket puede aproximarlo con estados o integración, mientras Jira lo modela nativamente. |
| **RM3.3** | 3 | 3 | 3 | 3 | Los cuatro permiten asignar elementos a personas. |
| **RM3.4** | 3 | 3 | 2 | 3 | GitHub/GitLab tienen prioridad mediante campos, etiquetas o peso; GitLab ofrece metadatos más ricos. Bitbucket requiere convención. Jira tiene prioridad estructurada y ordenación. |
| **RM3.5** | 2 | 2 | 1 | 3 | GitHub y GitLab permiten dependencias mediante enlaces o relaciones, pero la cobertura exacta en Free es limitada. Bitbucket no ofrece una dependencia de tareas equivalente. Jira proporciona enlaces de dependencia. |
| **RM3.6** | 3 | 3 | 1 | 3 | GitHub Projects y GitLab issue boards ofrecen tableros; Bitbucket por sí solo no ofrece un tablero de tareas comparable. Jira ofrece tableros Kanban/Scrum.  [docs.gitlab](https://docs.gitlab.com/user/project/issue_board/) |
| **RM4.1** | 3 | 3 | 2 | 3 | Markdown renderizado en repositorios y wikis; Bitbucket renderiza Markdown, pero la experiencia documental es menos completa. Confluence ofrece documentos enriquecidos. |
| **RM4.2** | 2 | 2 | 1 | 3 | GitHub/GitLab permiten plantillas de issues, pull/merge requests y documentos mediante archivos. Bitbucket tiene plantillas más limitadas. Confluence ofrece plantillas de páginas. |
| **RM4.3** | 3 | 3 | 3 | 3 | Los archivos versionados por Git y las páginas de Confluence mantienen historial y autoría. |
| **RM4.4** | 3 | 3 | 2 | 3 | GitHub/GitLab pueden almacenar YAML, JSON, CSV, CITATION.cff y otros metadatos desde el inicio. En Bitbucket es posible, pero sin tanta funcionalidad documental integrada. |
| **RM5.1** | 2 | 2 | 1 | 3 | GitHub/GitLab pueden usar issues o documentos como decisiones; no existe necesariamente un tipo “decisión” dedicado. Jira permite tipos de work item configurables dentro de sus límites. |
| **RM5.2** | 2 | 2 | 1 | 3 | Se pueden crear plantillas con campos de rationale y alternativas, pero GitHub/GitLab no los imponen estructuralmente. Confluence/Jira permiten plantillas y campos más claros. |
| **RM5.3** | 2 | 2 | 1 | 3 | La fecha puede registrarse mediante fechas de issue, commit o plantilla. Jira proporciona campos de fecha más explícitos. |
| **RM5.4** | 2 | 2 | 1 | 3 | Participantes identificables por autores, comentaristas o etiquetas; no es un registro estructurado de asistentes salvo mediante convención. |
| **RM5.5** | 2 | 2 | 1 | 3 | Enlaces y referencias son posibles, pero GitHub/GitLab requieren mantener la relación manualmente. Jira/Confluence ofrecen enlaces entre artefactos. |
| **RM6.1** | 3 | 3 | 3 | 3 | Pull requests/merge requests permiten revisión y reglas de protección; GitHub Free en repositorios públicos permite reglas de rama y revisiones requeridas.  [docs.github](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) |
| **RM6.2** | 3 | 3 | 3 | 3 | Los tres servicios de control de código permiten comentarios por línea y propuestas de cambio en revisiones. |
| **RM6.3** | 3 | 3 | 3 | 3 | Historial de commits, autores, pull/merge requests y actividad permiten recuperar contribuciones. |
| **RM6.4** | 3 | 3 | 3 | 3 | Git, ramas y merge/pull requests lo soportan nativamente. |
| **RM7.1** | 3 | 3 | 1 | 3 | GitHub Discussions, GitLab issue discussions y Confluence/Jira ofrecen conversación fuera de una revisión de código. Bitbucket aislado depende sobre todo de issues o pull requests. |
| **RM7.2** | 3 | 3 | 2 | 3 | Conversaciones pueden asociarse a issues, commits, pull requests o páginas. En C la relación es menos amplia y depende de enlaces. |
| **RM7.3** | 3 | 3 | 1 | 3 | GitHub/GitLab ofrecen búsqueda de issues y discusiones; Bitbucket tiene búsqueda menos orientada a conversaciones. Confluence/Jira permiten buscar contenido y work items. |
| **RM8.1** | 3 | 3 | 3 | 3 | Git proporciona historial completo por archivo, con commits y autores. |
| **RM8.2** | 3 | 3 | 3 | 3 | Comparación de commits, ramas y versiones disponible en los tres servicios. |
| **RM8.3** | 3 | 3 | 3 | 3 | Es posible revertir commits o recuperar estados anteriores mediante Git. |
| **RM8.4** | 3 | 3 | 3 | 3 | Tags, releases y ramas permiten nombrar y recuperar estados. |
| **RM8.5** | 2 | 2 | 2 | 2 | Git LFS permite versionar archivos grandes, pero no equivale a almacenamiento ilimitado. GitHub/GitLab/Bitbucket tienen límites o cuotas gratuitas; Bitbucket Free incluye 1 GB de LFS.  [support.atlassian](https://support.atlassian.com/bitbucket-cloud/docs/manage-your-plan-and-billing/) |
| **RM9.1** | 2 | 2 | 2 | 3 | La estructura de carpetas y plantillas puede reutilizarse por convención. Jira/Confluence permiten una organización más explícita con proyectos, espacios, páginas y tipos de trabajo. |
| **RM9.2** | 2 | 2 | 1 | 3 | Etiquetas, extensiones y carpetas permiten clasificación convencional; Jira ofrece tipos, campos y filtros estructurados. |
| **RM9.3** | 3 | 3 | 2 | 3 | Enlaces, referencias y URLs pueden registrar artefactos externos; en A/B son fáciles de mantener mediante issues y documentos. |
| **RM9.4** | 2 | 2 | 1 | 3 | GitHub/GitLab pueden funcionar como punto central mediante README, issues y enlaces. Bitbucket aislado ofrece menos componentes. Jira/Confluence integran planificación, documentación y código. |
| **RM10.1** | 3 | 3 | 3 | 3 | Referencias entre commits, issues y pull/merge requests permiten vincular trabajo con cambios. Jira añade integración explícita con Bitbucket. |
| **RM10.2** | 2 | 2 | 1 | 3 | El encadenamiento completo de salida–proceso–origen puede construirse mediante referencias, pero no existe como consulta de provenance científica nativa. Jira/Confluence permiten una consulta más sistemática, aunque siguen requiriendo modelado. |
| **RM10.3** | 2 | 2 | 1 | 3 | Se pueden enlazar objetos de distintas etapas, pero en A/B/C la relación suele depender de URLs, IDs y convenciones. |
| **RM10.4** | 3 | 3 | 3 | 3 | Git blame y el historial de commits atribuyen cambios por línea. |
| **RM11.1** | 3 | 3 | 3 | 2 | Los repositorios/proyectos públicos muestran código, issues y actividad sin cuenta. En D, Jira/Confluence pueden tener restricciones de acceso o configuración separada; el repositorio Bitbucket sí es público. |
| **RM11.2** | 3 | 3 | 3 | 3 | Historial de commits, pull/merge requests y cambios son visibles en proyectos públicos, según la configuración concreta. |
| **RM11.3** | 3 | 3 | 3 | 2 | README, wikis y archivos son legibles en repositorios públicos. Confluence Free puede requerir permisos o una configuración explícita de acceso anónimo. |
| **RM11.4** | 3 | 3 | 2 | 3 | GitHub/GitLab ofrecen feeds y actividad del proyecto; Bitbucket muestra actividad, pero con menor riqueza. Jira registra actividad e historial. |
| **RM12.1** | 2 | 2 | 2 | 2 | El entorno puede describirse en archivos de configuración, contenedores o documentación, pero no queda registrado automáticamente como entorno reproducible completo. |
| **RM12.2** | 3 | 3 | 3 | 3 | Git commits/tags fijan versiones exactas de código y, si se incluyen o referencian, de datos. |
| **RM12.3** | 2 | 3 | 2 | 3 | GitHub Actions, GitLab CI/CD y Bitbucket Pipelines pueden ejecutar pasos reproducibles; GitLab/D y sus pipelines ofrecen una integración especialmente directa. Los límites gratuitos siguen siendo relevantes.  [docs.github](https://docs.github.com/en/get-started/learning-about-github/githubs-plans) |
| **RM12.4** | 3 | 3 | 3 | 3 | Actions, GitLab CI/CD y Pipelines pueden ejecutar comprobaciones y bloquear integración mediante reglas de rama o merge checks. |
| **RM13.1** | 3 | 3 | 3 | 3 | Los tres servicios ofrecen automatización disparada por eventos del repositorio. |
| **RM13.2** | 3 | 3 | 3 | 3 | Se pueden ejecutar validaciones en cada push o pull/merge request. |
| **RM13.3** | 3 | 3 | 3 | 3 | GitHub Actions, GitLab CI/CD y Bitbucket Pipelines admiten ejecuciones programadas, con límites de uso en Free. |
| **RM13.4** | 3 | 3 | 3 | 3 | Los tres pueden construir y publicar releases o artefactos automáticamente, aunque el almacenamiento y los minutos gratuitos son limitados. |
| **RM14.1** | 3 | 3 | 3 | 3 | GitHub Releases, GitLab Releases y Bitbucket downloads/tags permiten versiones nombradas con notas y archivos. GitLab releases combinan código, binarios, documentación y notas.  [docs.gitlab](https://docs.gitlab.com/user/project/releases/) |
| **RM14.2** | 2 | 2 | 2 | 2 | La capacidad depende de depositar en un archivo externo, como Zenodo. La plataforma puede automatizar o documentar el depósito, pero el identificador persistente lo asigna el archivo externo, no el proveedor. |
| **RM14.3** | 3 | 2 | 2 | 2 | GitHub reconoce `CITATION.cff` y muestra “Cite this repository”; GitLab/Bitbucket pueden almacenar metadatos citables, pero no los usan con el mismo grado de integración.  [docs.github](https://docs.github.com/en/enterprise-server@3.18/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files) |
| **RM14.4** | 3 | 3 | 3 | 3 | Tags/releases pueden enlazarse con commits, ramas, pull/merge requests y pipelines que los produjeron. |
| **RM15.1** | 2 | 2 | 2 | 1 | GitHub/GitLab/Bitbucket ofrecen permisos generales y roles, aunque con granularidad limitada en Free. En D, Jira Free tiene limitaciones explícitas en permisos, roles y seguridad a nivel de trabajo.  [support.atlassian](https://support.atlassian.com/jira-cloud-administration/docs/explore-jira-cloud-plans/) |
| **RM15.2** | 3 | 3 | 3 | 3 | Se puede transferir la propiedad del repositorio/proyecto dentro de las reglas de cada servicio; Confluence/Jira también permiten cambios de administración, sujetos a permisos. |
| **RM15.3** | 3 | 3 | 3 | 3 | CONTRIBUTING, plantillas, reglas de revisión y archivos de gobernanza permiten mostrar reglas a colaboradores. |
| **RM15.4** | 2 | 2 | 2 | 2 | Se puede congelar mediante tags, permisos de solo lectura y exportación/clonado, pero no hay un procedimiento científico de cierre y preservación plenamente nativo. |

## Comentarios generales

- La distinción más importante es entre **gestión de código** y **gestión integral de un proyecto de investigación**. GitHub, GitLab y Bitbucket son muy sólidos en control de versiones, revisión, trazabilidad de cambios y automatización, pero no modelan de forma nativa conceptos como preguntas de investigación, decisiones, provenance científica o metadatos de artefactos.
- GitLab resulta especialmente fuerte como plataforma única porque combina issues, milestones, tableros, wiki, merge requests, CI/CD y releases. Sus issues admiten asignados, etiquetas, fechas, peso, discusiones y referencias cruzadas. [docs.gitlab](https://docs.gitlab.com/user/project/issues/)
- La configuración D es la más completa para planificación, documentación y dependencias porque Jira aporta objetos de trabajo, prioridades, relaciones, tableros, automatización y roadmap básico, mientras Confluence aporta documentación versionada y plantillas. Sin embargo, la integración de tres productos no elimina la necesidad de diseñar convenciones de identificadores y enlaces.
- GitHub obtiene una ventaja específica en identificación y citación mediante `CITATION.cff`, que es legible por máquinas y añade un enlace de citación en la página del repositorio. [docs.github](https://docs.github.com/en/enterprise-server@3.18/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)
- Bitbucket por sí solo es fuerte en Git, pull requests y Pipelines, pero es claramente más débil como plataforma de gestión de investigación cuando no se acompaña de Jira y Confluence.
- RM14.2 es deliberadamente conservador: Zenodo u otro repositorio externo puede asignar DOI, pero la plataforma evaluada no debe recibir el crédito completo por una función que pertenece al archivo externo.
- La capacidad RM12.1 debería distinguir entre “el entorno se puede documentar” y “la plataforma captura y ejecuta un entorno reproducible”. En su formulación actual, parece medir ambas cosas a la vez.
- RM15.4 combina dos capacidades diferentes: congelar un proyecto y exportarlo/preservarlo. Sería más claro separarlo en “estado final inmutable” y “exportación completa con metadatos”.

## About you

- **Name:** Evaluador independiente.
- **Date of rating:** 2026-10-09.
- **Role and field:** Evaluador independiente; gestión de proyectos de investigación, software colaborativo y ciencia reproducible.
- **Platforms you use regularly (and on which plan):** No procede; no se estableció uso personal de plataformas ni cuentas comerciales.
- **Platforms you scored mainly from documentation:** GitHub Free, GitLab.com Free, Bitbucket Cloud Free, Jira Free y Confluence Free.
- **Approximate time spent:** Aproximadamente 2–4 horas equivalentes de revisión y síntesis documental.

## Consentimiento para los agradecimientos

No puedo consentir que se me nombre como persona en los agradecimientos ni proporcionar un nombre personal.