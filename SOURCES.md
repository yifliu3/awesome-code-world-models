# Sources and curation record

## Snapshot

- Search and verification date: **2026-10-13**.
- Current collection: **49 distinct papers** (27 in the initial September 18 snapshot; 2 added September 25; 1 added September 28; 14 added October 9; 5 added October 12).
- Separately tracked: **2 project releases**, added October 12. A verified paper is not required for these official resources.
- Maintainer account: **yifliu3**.
- Discovery seed: [Awesome-World-Models](https://github.com/knightnemo/Awesome-World-Models).
- Metadata source: each entry's linked arXiv abstract page.
- Official resource provenance: links on paper abstract/full-text pages, the authors' project pages, or organization-controlled release pages and repositories.

## Discovery

The initial search combined the seed list with arXiv search and the arXiv API, including these queries:

```text
"world model" code
"world models" "program synthesis"
"world models" executable
WorldCoder
Code2World
world AND symbolic
```

The broad code query and executable query were inspected newest-first, including September 2026 results. Targeted searches and the seed list supplied earlier work. Some API requests were rate-limited; successful arXiv website searches and individual paper pages were used instead.

The collection is selective. The search queries and inspected result windows do not establish exhaustive coverage, and unrelated results were excluded after examining their titles and abstracts.

## September 25, 2026 update

This incremental search focused on papers announced since the September 18 snapshot, with results available through September 24. The seed list was checked again, alongside newest-first arXiv website searches:

```text
"world model" code
"world models" executable
"code world"
"world model" programmatic
"world model" "program synthesis"
"world model" symbolic
"executable world"
"world" "code" "dynamics"
"GUI" "world model"
"world" "simulator synthesis"
```

The inspected windows covered the newest 50 results for the broad code query, 25 for the executable query, up to 20 for the targeted representation queries, and up to 15 for the dynamics, GUI, and simulator-synthesis queries. Older results supplied context; this update is not a systematic backfill of earlier literature. Search-result dates were not used in place of the abstract pages' v1 submission histories.

Two papers were added:

| Paper | Verified first submission | Scope and resource provenance |
| :--- | :--- | :--- |
| [CoDeR](https://arxiv.org/abs/2609.26458) | September 22, 2026 | The abstract describes executable world code and links the [author project page](https://becauseimbatman0.github.io/CoDeR). Its code button is marked “Coming soon”; no repository link is included. |
| [GameDirector](https://arxiv.org/abs/2609.25652) | September 22, 2026 | The abstract page links the [author project page](https://jimntu.github.io/gamedirector/). The [paper HTML](https://arxiv.org/html/2609.25652), including its rule-following implementation, confirms predefined deterministic combat rules driven by visual detections. It is included for explicit code-driven state evolution, not learned or synthesized dynamics; no official repository was verified. |

Both titles and dates were checked against the arXiv abstract pages. The two new paper links and two project links returned HTTP 200. GameDirector's reported perfect state alignment measures consistency with its own detected hit signals, not perfect recovery of hidden game states; the README therefore makes no accuracy claim.

Recent candidates outside the collection's focus were also screened. [PileBelief](https://arxiv.org/abs/2609.22858) uses learned physical belief and memory rather than executable world programs. [HappyWorld-Bench](https://arxiv.org/abs/2609.24308) was checked at abstract and selected full-text sections; its broad video, spatial, and embodied evaluation focus did not warrant a dedicated entry in this code-focused update.

## September 28, 2026 update

This incremental search checked for new work since September 25, including the September 28 arXiv announcements. The seed list and newest-first arXiv searches for code, executable, programmatic, symbolic, program-synthesis, and GUI world models were revisited. Additional searches for `"world model"`, `"world" "program"`, and `"world" "executable"` broadened discovery beyond papers using the code-world-model name. Up to 20 results per query were inspected, together with relevant titles in the September 28 cs.AI and cs.CV announcements. This remains a selective update rather than an exhaustive search or systematic backfill.

Added [RIVET: Representation-Guided Generation and Integration of Executable Programs for Robot Manipulation](https://arxiv.org/abs/2609.31337), first submitted **September 25, 2026**. The title and date were verified on the abstract page. The [paper HTML](https://arxiv.org/html/2609.31337) describes generated `perceive`, `render`, `relate`, and `plan` functions; the planning section explicitly defines action preconditions and a state-transition function over object poses and relations. This supports inclusion under **Related** for executable task-level transition modeling, without implying discovery of a general physical simulator. No official project or repository link was verified on the paper pages. Both the abstract and HTML URLs returned HTTP 200.

New adjacent work was screened but not added: [MA-WAM](https://arxiv.org/abs/2609.31281) plans with learned joint-action predictions, [AtomWorld-Mem](https://arxiv.org/abs/2609.31133) restores latent state while an existing simulator governs physical execution, and [OneWorld](https://arxiv.org/abs/2609.30946) constrains video predictions through shared latent physical mechanisms. [ExplorationBench](https://arxiv.org/abs/2609.30199), first submitted September 24, was also checked in full-text sections: its worlds are a modified programming language and deduction system, which fall under the list's exclusion of program-execution semantics without external-environment modeling. Revisions, including AD-WM's September 25 v2, were not counted as new papers.

## October 9, 2026 update

This incremental search covered work available on October 9, including October 8 submissions. It added **14 papers**: **11** first submitted after September 28, **EMPIRIC** first submitted on September 28, and **World Agent** and **BVB** as earlier September backfills. Revisions were not counted as new papers. This is a selective update, not an exhaustive survey or systematic historical backfill.

### Search coverage

The seed list was revisited. The broad arXiv query `"world model"` was inspected newest-first across five pages of 50 results, spanning October 8 to September 28 in the displayed results. Parallel targeted searches covered:

```text
world AND (code OR executable OR programmatic)
programmatic AND world
executable AND world
GUI AND code
"physical reasoning" ("code" OR "program synthesis")
"simulator synthesis"
"programmatic world" planning
("symbolic world model" OR PDDL OR "action model learning")
(simulator OR dynamics) ("program synthesis" OR "executable code")
("world model" OR "executable world") benchmark
```

An additional arXiv advanced search combining `"world model"`, `"simulator synthesis"`, and `PDDL`, with a September 29–October 9 submitted-date filter, returned 294 displayed hits across two inspected pages. Targeted September searches supplied the backfills. Search-page dates and arXiv identifiers were not treated as authoritative: every added paper's title and v1 date were checked on its abstract page, and selected HTML sections were inspected for the executable representation. General web search returned no usable content in this session; arXiv's own search pages, abstract/full-text pages, and author resources were retrieved directly instead.

### Added papers and provenance

| Paper | Verified first submission | Scope and primary-source evidence |
| :--- | :--- | :--- |
| [AgentGarten](https://arxiv.org/abs/2610.12374) | October 8, 2026 | **Core.** [Section 2](https://arxiv.org/html/2610.12374v1) describes executable simulation backends with persistent state and interaction rules coupled to a neural renderer. The paper links the [project](https://mirros-lab.github.io/agent-garten/) and [repository](https://github.com/MirroS-Lab/AgentGarten). The renderer is available; code worlds and the practice loop remain on its release roadmap. |
| [Memento 3](https://arxiv.org/abs/2610.11794) | October 8, 2026 | **Core.** [Section 2](https://arxiv.org/html/2610.11794v1) compiles reflective rulebooks into executable transition, observation, and goal models, with replay and planning. No author-linked project or repository was verified on the inspected paper pages. |
| [USDCraft](https://arxiv.org/abs/2610.11322) | October 8, 2026 | **Construction.** [Sections 3.3–3.5](https://arxiv.org/html/2610.11322v1) describe executable asset programs and iterative geometric verification. The abstract links the [project](https://xingyoujun.github.io/usdcraft/), whose code and dataset buttons are marked TODO. This constructs articulated assets, not unknown transition laws. |
| [LLM-IDEA](https://arxiv.org/abs/2610.11253) | October 8, 2026 | **Core.** [Sections 3–4 and Appendix C](https://arxiv.org/html/2610.11253v1) specify evaluable symbolic equations of motion, parameter fitting, trajectory integration, and identifiability diagnostics. Section 8 links the [repository](https://github.com/Suraskey/llm-idea). Its diagnostics and records do not constitute a complete runnable live-agent experiment: a proposer and model provider are still required. |
| [Video2World](https://arxiv.org/abs/2610.04432) | October 3, 2026 | **Benchmark.** [The paper](https://arxiv.org/html/2610.04432) evaluates executable video-to-simulation reconstruction across 222 instances from 189 videos. The abstract links the [project](https://aetherlabsai.github.io/Video2World), which links the [repository](https://github.com/AetherLabsAI/Video2World). October 7 is v2, not the first-submission date. |
| [EnvDreamer](https://arxiv.org/abs/2610.04301) | October 3, 2026 | **Construction.** [Section 3](https://arxiv.org/html/2610.04301v1) describes a plan–compile–apply–validate loop using Unreal Python and, where needed, C++. No author-linked project, repository, or dataset destination was verified on the inspected paper pages; the README does not claim that its stated dataset release was independently verified. |
| [CVE2AP](https://arxiv.org/abs/2610.03383) | October 2, 2026 | **Related.** [Sections II–III](https://arxiv.org/html/2610.03383v1) generate PDDL action preconditions and effects from vulnerability descriptions and repair them using planner feedback. Section VII links the [repository](https://github.com/LincuiDudu/pddl-ap-generation), which omits parts of the dataset, instructions, and output template. This is specialized symbolic cybersecurity modeling, not physical dynamics learning. |
| [World Editing](https://arxiv.org/abs/2610.02331) | October 1, 2026 | **Benchmark.** [The paper](https://arxiv.org/html/2610.02331v1) evaluates interventions and preservation in executable Minecraft and Terraria worlds. The abstract links the [IGMWorld project](https://vinesmsuic.github.io/IGMWorld/), which links a [placeholder repository](https://github.com/vinesmsuic/IGMWorld/) marked Coming Soon. |
| [PROWBench](https://arxiv.org/abs/2610.02205) | October 1, 2026 | **Benchmark.** [Section 3](https://arxiv.org/html/2610.02205v1) uses programmatic world records and timestamped events to evaluate rendered observations. It links the [project](https://alaya-lab.github.io/PROWBench/) and [repository](https://github.com/AlayaLab/PROWBench); data and evaluation code remain on the release roadmap. October 5 is v2. |
| [Kepler](https://arxiv.org/abs/2610.00834) | September 30, 2026 | **Core.** [Sections 2.1–2.2](https://arxiv.org/html/2610.00834v1) describe `world_model.py`, `simulate(grid, action)`, retrospective transition checks, and model-internal search. The abstract links the [project](https://kepler-harness.vercel.app/), which links the [repository](https://github.com/Cveinnt/kepler). Prediction failures or zero coverage do not block every action. September 30 is the arXiv v1 date, not necessarily the first public disclosure or a new performance result. |
| [Asking the World](https://arxiv.org/abs/2609.39135) | September 30, 2026 | **Related.** [Sections 3.1–3.3](https://arxiv.org/html/2609.39135) configure and calibrate fixed PolyWorld physics through semantic operations, then branch simulations for physical questions. It does not require the agent to synthesize new low-level engine code. No official project or repository was verified on the inspected paper pages. |
| [EMPIRIC](https://arxiv.org/abs/2609.35047) | September 28, 2026 | **Core; same-day addition relative to the prior snapshot.** [Sections 3.1–3.4](https://arxiv.org/html/2609.35047) describe Python residual mechanisms, Bayesian state/parameter inference, information-seeking experiments, and revision. The paper's original [project URL](https://yichao-liang.github.io/empiric) points to the [current project](https://basisresearch.github.io/empiric), which links the [repository](https://github.com/BasisResearch/empiric). |
| [World Agent](https://arxiv.org/abs/2609.32692) | September 26, 2026 | **Benchmark; backfill.** [Sections 3–4 and Appendix B](https://arxiv.org/html/2609.32692v1) use explicit-state executable interfaces, event contracts, and deterministic reference dynamics. The abstract links the [repository](https://github.com/HCPLab-SYSU/WorldAgent-Benchmark), currently a minimal placeholder. This tests world maintenance and deduction rather than generated simulator code. |
| [BVB](https://arxiv.org/abs/2609.15478) | September 14, 2026 | **Benchmark; backfill.** [Section 2 and Appendix A](https://arxiv.org/html/2609.15478v1) evaluate executable animated Blender reconstructions under a shared budget. The paper links the [project](https://yoloytang.me/BVB/) and [repository](https://github.com/yunlong10/BVB). September 22 and 26 revisions, and a later leaderboard update, are not new papers. |

All **32** newly added README paper, project, and repository destinations returned HTTP 200 in the final link check. The **14** new entry titles and first-submission dates were also compared against the arXiv abstract pages, and `python3 scripts/check_readme.py` passed for **44** unique papers. Author linkage and HTTP availability were checked; no research code, model weights, or experiments were run. Release-status notes describe the inspected state, not a guarantee that resources will remain unchanged.

### Screened but not added

- [WorldCast](https://arxiv.org/abs/2610.12412) estimates shared player state with a learned state model and conditions video generation; [Section 3.4](https://arxiv.org/html/2610.12412) does not establish synthesized executable world rules. [OuroWorld](https://arxiv.org/abs/2610.12461) learns periodic 4D Gaussian deformations, and [Physis-Lang](https://arxiv.org/abs/2609.40358) optimizes physical-language representations; neither supplies the programmatic world representation required here.
- [MultiWorldBench](https://arxiv.org/abs/2610.11723) offers useful shared-state and persistence diagnostics, but evaluates multiplayer video world models rather than generated executable programs or symbolic planning interfaces. It is retained as an adjacent reading lead, not a new benchmark entry in this code-focused list.
- [Kepler4D](https://arxiv.org/abs/2610.04152) is a boundary case: [Section 3.3 and Appendix A.4](https://arxiv.org/html/2610.04152v1) map structured speed/heading choices into trajectories with fixed numerical rules. It is deferred because this trajectory-control layer does not by itself establish a persistent executable rule system comparable to GameDirector; this is a curation choice, not a claim that it contains no deterministic computation.
- [Right Screen, Wrong Transition](https://arxiv.org/abs/2610.11942) verifies GUI transitions in latent space; [Proxy2World](https://arxiv.org/abs/2609.35023) learns proxy-conditioned rendering. Neither predicts interfaces or world dynamics through generated executable code.
- [Trace2Env](https://arxiv.org/abs/2610.06100) and [Long-Horizon Textual World Modeling](https://arxiv.org/abs/2610.06637) use language models to predict observations or state deltas. The latter has a deterministic state-update operator, but this is not a learned reusable transition-rule program. [E-LEDGER](https://arxiv.org/abs/2610.11552) similarly does not establish an executable learned transition simulator in the inspected sections.
- [Code to Control](https://arxiv.org/abs/2609.38733) generates controllers, not environment models. [CURIO](https://arxiv.org/abs/2610.04851), [DreamTest](https://arxiv.org/abs/2610.04494), and [Flow Policies as Actions of Skill-Level World Models](https://arxiv.org/abs/2610.04767) primarily use learned latent dynamics; the last also contains hand-written symbolic scaffolding, which was insufficient for a dedicated entry in this update.
- [OPINE-World](https://arxiv.org/abs/2607.01531) was noted as a historical backfill lead; its July 1 v1 and September revision do not make it a new paper in this search window.

## October 12, 2026 update

This search checked work publicly available on October 12, including October 9 submissions. It added **5 papers**: **RoleWorld** and **VETR** first submitted October 9, plus **WorldSolver** (October 6), **Real2Gym** (September 29), and **OPINE-World** (July 1) as backfills. These additions are not all newly submitted papers. Revisions and resource releases were not counted as additional papers.

### Search coverage

The discovery seed was revisited. The arXiv API was queried newest-first by submission date with these searches:

```text
"world model"
"world model" AND code
world AND (executable OR programmatic OR "program synthesis")
(simulator OR dynamics OR physics) AND ("program synthesis" OR "executable code")
("symbolic world model" OR PDDL OR "simulator synthesis")
(GUI AND "world model") OR "programmatic world" OR "executable world"
```

The inspected windows were 60 results for the broad world-model query, 30 for the world/executable/programmatic query, and 25 for each remaining query. The broad query's October 9 entries and relevant targeted results were screened; older targeted results supplied backfill leads. The prior OPINE-World lead was checked in selected full-text sections. General web search returned no usable results, so discovery and verification relied on direct arXiv API, abstract, HTML, and author-resource retrieval. This remains a selective search, not exhaustive coverage or a systematic historical backfill.

### Added papers and provenance

| Paper | Verified first submission | Scope and primary-source evidence |
| :--- | :--- | :--- |
| [RoleWorld](https://arxiv.org/abs/2610.13172) | October 9, 2026 | **Related.** [Sections 3.1–3.2 and Appendix A.1](https://arxiv.org/html/2610.13172v1) specify induced role prototypes and executable condition/effect rules in a predefined DSL. The interpreter and event semantics are supplied; target-world adaptation changes role assignments and parameters, not the shared rules. The paper-linked [project destination](https://future-item.github.io/RoleWorld) returned HTTP 404, with and without a trailing slash, so the README links only the paper. |
| [VETR](https://arxiv.org/abs/2610.13098) | October 9, 2026 | **Construction.** [Section 2 and Appendix R](https://arxiv.org/html/2610.13098v1) use executable Blender programs, bounded write traces, and runtime state/binding checks for scene repair. Programs execute relative to a supplied base scene, rather than necessarily constructing a standalone world. Included for execution-grounded modification of explicit scene programs, not learned physical dynamics. No official project or repository was verified on the inspected paper pages. |
| [WorldSolver](https://arxiv.org/abs/2610.08720) | October 6, 2026 | **Benchmark; backfill.** [Section 2 and Appendix A](https://arxiv.org/html/2610.08720v1) isolate generated physics solvers within fixed scene scaffolds and evaluate execution, visual fidelity, and trajectory-level physical plausibility. The paper-linked [repository destination](https://github.com/sirujiang/WorldSolver) returned HTTP 404; the README does not advertise it as available code. |
| [Real2Gym](https://arxiv.org/abs/2609.37089) | September 29, 2026 | **Construction; backfill.** [Section 3.1](https://arxiv.org/html/2609.37089v1) constructs aligned Blender/MuJoCo scenes, validates contact and task execution under native physics, and augments executable environments. This uses existing-engine dynamics rather than synthesizing new physical laws. The abstract links the [project](https://real2gym.github.io/), which links the [Real2Sim repository](https://github.com/real2gym/Real2Gym) and [agent repository](https://github.com/real2gym/R2G_Agent). The agent README explicitly limits its release to continuous stage-code execution without the persistent experience library; assets and external services are not bundled. |
| [OPINE-World](https://arxiv.org/abs/2607.01531) | July 1, 2026 | **Core; historical backfill.** [Sections 3.1–3.2 and Appendix B](https://arxiv.org/html/2607.01531v3) combine qualitative hypotheses, Bayesian effect uncertainty, and synthesized Python extraction/transition/reward components with counterexample-guided repair and replay checks. September 26 is v3, not v1. No official project or repository was verified on the inspected paper pages. |

All five titles and v1 submission dates were checked on their arXiv abstract pages. Summaries are original descriptions of the inspected representation and execution interfaces, not independent validations of results.

### Resource-status corrections

- **PROWBench:** the [official repository](https://github.com/AlayaLab/PROWBench) announces an October 11 dataset and representation-swap release, and now lists engine recordings, example representations, and evaluation code as available. Its [evaluation guide](https://github.com/AlayaLab/PROWBench/blob/main/eval/USAGE.md) was inspected, and the author-linked [Hugging Face dataset](https://huggingface.co/datasets/AlayaLab/PROWBench) was verified as public and ungated with published recording, event, scene, and preview files. The world-generation pipeline remains unchecked on the roadmap. The README's October 9 pending-release note was replaced and a dataset link added.
- **World Agent:** the [official repository](https://github.com/HCPLab-SYSU/WorldAgent-Benchmark) now provides benchmark cases and evaluation scripts. Its README and [maintenance runtime source](https://github.com/HCPLab-SYSU/WorldAgent-Benchmark/blob/main/benchmark/maintenance_track/runtime/engine.py) were inspected. Playback, rendering, and the playable demo remain pending. The old placeholder note was replaced; no precise release date is asserted.
- **AgentGarten** and **World Editing:** their official repository READMEs were rechecked. AgentGarten still lists code worlds and the agent practice loop as forthcoming; World Editing remains marked Coming Soon. Their existing caveats were retained.

The October 9 provenance record above preserves what was observed then; it is not the current release status of these repositories. No model weights, research code, robot control, or evaluations were executed during this update.

### Screened but not added

- [RSI-Anything](https://arxiv.org/abs/2610.13912) uses JEPA-based latent prediction and outcome readouts, including for code repair; [Section 2.2](https://arxiv.org/html/2610.13912v1) does not make generated executable code the environment model. [JANUS](https://arxiv.org/abs/2610.13194) scores research actions through expected-return forecasts ([Section 3.1](https://arxiv.org/html/2610.13194v1)), rather than synthesizing a reusable executable environment-transition program.
- [GLIMPSE](https://arxiv.org/abs/2610.13706), [Dream to Remember](https://arxiv.org/abs/2610.13816), and [HF-WM](https://arxiv.org/abs/2610.13522) focus on learned video/latent predictions or their use for policy learning, not executable world-rule synthesis.
- [Code4Scene](https://arxiv.org/abs/2609.36777) explicitly evaluates static engine-native construction and editing. It remains outside the default static-graphics scope in this update; VETR is included specifically for its runtime-trace-driven program repair and preservation checks. [Fly-by-Code](https://arxiv.org/abs/2610.12549) synthesizes policies and diagnostic probes in an existing simulator, rather than the simulator's world model.

### Validation

All **11** added or release-updated README destinations returned HTTP 200: five paper pages, the Real2Gym project and two repositories, the PROWBench dataset and repository, and the World Agent repository. The five added titles and first-submission dates also matched the abstract pages' citation metadata. `python3 scripts/check_readme.py` passed for **49** unique papers; the diff check passed with the README's existing two-space Markdown hard breaks allowed. These checks establish metadata consistency and link availability, not reproducibility or scientific validity.

## October 12, 2026 project-release update

This targeted follow-up checked the requested NVIDIA and VAST release leads, independently of the literature search above. Official project releases can now be listed without a paper and are not counted as additional papers.

### Added projects and provenance

| Project | Verified on | Primary-source evidence and release boundary |
| :--- | :--- | :--- |
| **[StreamRender-H3](https://nvlabs.github.io/Sana/Sol-Engine/StreamRender-H3/)** (NVIDIA) | October 12, 2026 | The user supplied the NVlabs-hosted project page, which verifies the name and links the [runtime source](https://github.com/NVlabs/Sana/tree/sol-engine/models/streamrender_h3). Its architecture sections describe a code game engine maintaining maps, physics, rules, and player feedback, with semantic frame maps conditioning a streaming MiniMax-H3 renderer. The [runtime README](https://raw.githubusercontent.com/NVlabs/Sana/sol-engine/models/streamrender_h3/README.md) documents engine, renderer, session runtime, launch scripts, and tests, with external model weights and an eight-GPU deployment profile. The project page's citation section labels this resource as a project page and separately cites the underlying Sol-Engine paper; that paper is not treated as a standalone StreamRender-H3 paper or added to the paper count. The page explicitly limits its reported results to the racing scenario. |
| **[EdenLive](https://vast-eden.ai/?p=edenlive)** (VAST) | October 12, 2026 | The organization-controlled [repository](https://github.com/VAST-AI-Research/EdenLive) and its [README](https://raw.githubusercontent.com/VAST-AI-Research/EdenLive/main/README.md) link the project page. The [project-page data](https://vast-eden.ai/data/projects.js) links the same repository and explicitly leaves state, rules, collisions, and interactions in upstream coding-agent or engine programs. The renderer consumes proxy/reference frames. Both the page and repository announce open-sourcing **by October 18, 2026**; the inspected repository is an announcement, not a runnable code release. The project's paper button points to `#`, so no paper link is included. |

The requested spelling `endlive` resolves to the official name **EdenLive**. GitHub's repository-search API returned `VAST-AI-Research/EdenLive` with a creation timestamp of `2026-10-12T01:57:33Z`; this establishes repository creation, not an independently verified first-announcement date. The README table therefore uses the verification date rather than asserting a publication date.

The NVIDIA lead initially spelled `streamh3render` was resolved to **StreamRender-H3** after the user supplied its official project page. Earlier exact-name and spelling-variant searches had not established a match; the user-supplied destination and its source-code link supplied the missing primary-source evidence. No first-publication date is inferred from the date of verification.

The StreamRender-H3 project page, runtime source directory, and raw README, together with the EdenLive project page, GitHub repository, raw README, and project-page data, were retrieved successfully. No code, weights, or experiments were executed. The existing paper structural check remains unchanged: the separate table does not require an arXiv link or affect paper counts, and project names, counts, dates, and external destinations are checked manually.

## October 13, 2026 update

This incremental search found **no newly verified, in-scope paper or project release first made public today** in the inspected sources. The collection remains **49 papers and 2 project releases**. "Today" refers to October 13 in **Asia/Shanghai (UTC+08:00)**; the search was performed through approximately 18:10 local time, not after the end of the day. This is a search outcome, not proof that no qualifying work exists.

### Search coverage

The discovery seed was revisited. The broad arXiv API query `"world model"` was inspected newest-first with a 60-result window, alongside the code, executable/programmatic, program-synthesis, symbolic/PDDL, simulator-synthesis, and GUI searches used in the October 12 update, with up to 25 results per targeted query. The broad feed's newest returned entry was still [RSI-Anything](https://arxiv.org/abs/2610.13912), first submitted October 9 and already screened in the prior update.

An additional API query returned zero indexed matches:

```text
submittedDate:[202610120000 TO 202610132359]
AND (all:world OR all:simulator OR all:PDDL)
```

This date-filter result describes the API response at check time; it does not establish that all submissions or announcements for October 13 were already indexed. General web search again returned no usable results, so verification relied on direct arXiv, GitHub, and author-resource retrieval.

GitHub repository searches for `"world model"` returned 14 repositories created on October 13 UTC, plus 6 created between October 12 16:00 and 23:59 UTC to cover the start of the Shanghai calendar day. Names and descriptions were screened, and promising or ambiguous leads were checked against repository READMEs or project pages. Additional `code-world` and `"code world"` searches covered October 12-13. Repository creation timestamps were used only for discovery, not as verified first-release dates; these searches also cannot capture every release in an older repository.

### Screened leads and release checks

- [HelixWM](https://github.com/iceezhu306-lgtm/HelixWM-for-world-model) describes a shared recurrent state-space model with latent real/imagination paths, not synthesized executable environment rules. [GUI world model](https://github.com/LamShiuChing/gui-world-model) predicts DINOv2 feature changes with a transformer rather than next-screen interface code. [What Matters for World Modeling in Vision-Language-Action Models?](https://github.com/DylanMQS/WM-in-VLAs) studies predictive visual representations and policy integration; its inspected project page did not establish executable-world synthesis.
- [World Model / Cell Demo](https://github.com/zr15504328511-debug/world-model) is an authored browser scene library; the inspected README did not establish a code-world-model research method or a renderer connected to such a method. [Varis](https://github.com/rxwxwwxw/Varis) is a Lua-derived authored narrative language and runtime with relational world state. It is not added as a code-world-model research release, and its README documents development decisions preceding today's repository creation.
- [Trajectory-lineage](https://github.com/physicalreasoning/trajectory-lineage) audits overlap in video-world-model evaluation using procedural collision trajectories. [Decision Utility Lab](https://github.com/smhajimirzaei/decision-utility-lab) audits action selection for VLA and latent world models using an existing simulator. Both are adjacent evaluation leads, not dedicated entries in this code-focused update.
- [Streaming Code World Model](https://github.com/TingtingLiao/streaming-code-world-model) was checked as a recent lead. Its Git history records an **October 12, 2026, 12:04:09 UTC** initial-release commit, which is also October 12 in Shanghai. It is therefore not counted as a release first made public today. Its proxy-conditioned streaming renderer remains a potential rendering-infrastructure backfill, not a newly verified standalone paper.
- [EdenLive's official README](https://raw.githubusercontent.com/VAST-AI-Research/EdenLive/main/README.md) still announces open-sourcing by **October 18, 2026**. The existing announcement-status caveat was retained; no new runnable release was verified.

No paper or project entries, counts, or previously recorded resource-verification dates were changed. Only the literature-search date and this curation record were updated. All 10 external destinations linked in this update returned HTTP 200. `python3 scripts/check_readme.py` passed for 49 unique papers, and `git diff --check` passed. Research code, model weights, and experiments were not executed.

## What was checked

For every paper:

- The title, first-submission date, and abstract on the arXiv abstract page.
- Whether the work fits the main topic or needs a related-work label.
- Whether the summary is supported by the source abstract.

For linked official resources:

- The destination was supplied by the paper or an author-controlled project page.
- Repository/project labels describe the resource type, not release completeness.
- No experiments, model weights, or third-party repository code were run as part of curation.
- All 51 distinct external paper, project, and repository URLs selected from the README returned HTTP 200 during the initial link check. This excludes badge-image services and this new repository's own links; a successful response does not establish scientific validity or release completeness.

Examples of the provenance chain:

| Paper/resource | Source of additional links |
| :--- | :--- |
| Code World Model | [Author project page](https://buaacyw.github.io/cwm/) links the repository. |
| Code as Worlds | [Author project page](https://mirros-lab.github.io/code-as-world/) links the repository. |
| PoE-World | [Author project page](https://topwasu.github.io/poe-world) links the repository. |
| OneLife | [Author project page](https://onelife-worldmodel.github.io/) links OneLife and Crafter-OO. |
| Text2World | [Author project page](https://text-to-world.github.io/) links the repository. |
| Symbolic world models via test-time scaling | [Author project page](https://vmlpddl.github.io/) links VML_PDDL. |
| TheoryCoder-2 | [Paper HTML](https://arxiv.org/html/2602.00929) links the TheoryCoder repository. |

## Date caveat

[World-Time Compute with Verified Code World Models](https://arxiv.org/abs/2609.09163) reports **July 7, 2026** in its v1 submission history and citation metadata even though its identifier begins with `2609`. This list preserves the reported submission date and flags the discrepancy rather than silently changing it.

Similarly, TheoryCoder-2 reports January 31, 2026 despite a `2602` identifier. Identifiers should not be used as exact publication dates.

## Limitations

This is primarily an abstract-level literature map, not a full-paper reproducibility review. Inclusion does not certify peer review, benchmark validity, code completeness, licensing suitability for downstream use, or claimed performance. Availability and source contents may change after the snapshot date.
