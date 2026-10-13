<div align="center">

# Awesome Code World Models

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/yifliu3/awesome-code-world-models?style=social)](https://github.com/yifliu3/awesome-code-world-models/stargazers)
[![License: CC0](https://img.shields.io/badge/License-CC0%201.0-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**A curated collection of code world models: executable dynamics, programmatic simulation, and coding agents that build and reason about worlds.**

代码世界模型论文与资源精选：可执行动力学、程序化仿真，以及通过编程构建和理解世界的智能体。

</div>

**49 papers** and **2 project releases**.

**Last literature search: October 13, 2026.** This is a curated snapshot, not an exhaustive survey or an automatically maintained feed.

## Contents

- [Scope and taxonomy](#scope-and-taxonomy)
- [Start here](#start-here)
- [Project releases and rendering infrastructure](#project-releases-and-rendering-infrastructure)
- [Code-driven world evolution and physical reasoning](#code-driven-world-evolution-and-physical-reasoning)
- [Learning executable dynamics and planning](#learning-executable-dynamics-and-planning)
- [GUI world models](#gui-world-models)
- [Executable scene and 4D world construction](#executable-scene-and-4d-world-construction)
- [Related symbolic and neurosymbolic planning](#related-symbolic-and-neurosymbolic-planning)
- [Benchmarks and evaluation](#benchmarks-and-evaluation)
- [Adjacent perspectives and data engines](#adjacent-perspectives-and-data-engines)
- [Research questions](#research-questions)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Scope and taxonomy

Here, a **code world model** uses an executable program to represent environment state, transition rules, physical mechanisms, or action-conditioned observations. A coding agent can synthesize, test, and revise this program; a planner or renderer can then execute it.

This working definition organizes the list; it is not a claim that every included paper or project adopts the same terminology.

| Label | Included work | Important distinction |
| :--- | :--- | :--- |
| **Core** | Synthesized executable dynamics, code-based physical representations, and code-driven world evolution | The program itself represents the world or its evolution. |
| **GUI** | Action-conditioned prediction through renderable interface code | Rendering the next interface is not necessarily learning a complete app simulator. |
| **Construction** | Executable 3D scenes and 4D simulation programs | Scene reconstruction alone does not establish learned transition dynamics. |
| **Related** | PDDL, graph, and neurosymbolic models used for simulation or planning | Symbolic models need not be general-purpose code world models. |
| **Benchmark** | Evaluation of executable worlds, generated domains, or state-grounded planning | A benchmark may supply rather than learn a world model. |
| **Perspective** | Engine-verified data generation and browser-backed coding | Relevant infrastructure or arguments, not equivalent model architectures. |
| **Release** | Official projects and rendering infrastructure explicitly connected to code-defined worlds | A paper is optional; a renderer is not itself an executable dynamics model. |

**Not included by default:** generic coding agents, ordinary code-generation benchmarks, purely pixel/latent world models, and static graphics generation without an explicit executable-world connection. Likewise, models of *program execution* are a separate topic unless they model an external environment.

**Entry conventions**

- Paper dates are the first-submission dates reported on the arXiv abstract pages, not dates inferred from identifiers or later revisions. Paper entries are newest-first within each category.
- Summaries describe the authors' proposed method; inclusion is not an independent validation of results.
- Paper links are primary sources. Repository links are author-linked resources; their presence does **not** guarantee a complete, runnable code release.
- When no official resource was verified, only the paper is linked. Publication venues are omitted unless separately checked; do not infer peer-review status from inclusion.
- Project releases need only a verified name and official release, repository, or project URL; a paper is optional. Their verification dates are not publication dates. Announcements, placeholder repositories, and runnable code releases are distinguished, and projects are counted separately from papers.
- See [SOURCES.md](SOURCES.md) for search coverage, provenance, and limitations.

## Start here

Suggested reading paths, rather than a ranking:

1. **Origins → program synthesis:** WorldCoder → GIF-MCTS / CWMB → TheoryCoder → PoE-World; compare OPINE-World for uncertain abstractions and RoleWorld for transferable role-level rules.
2. **Coding agent → persistent visual world:** Code World Model → Programmable World Model → CoDeR → AgentGarten; compare GameDirector's predefined gameplay rules and perception-driven state updates.
3. **Physical reasoning → executable representation:** Code as Worlds → Code2Worlds; compare their reasoning and generation objectives.
4. **Online discovery → planning:** PatchWorld → Tycho → Twin → Kepler → Memento 3; compare EMPIRIC's learned residual mechanisms on top of a physics engine.
5. **Evaluation:** Text2World → WorldCoder-Bench → Video2World; compare WorldSolver for generated physical solvers, World Editing for interventions, PROWBench for program-to-render fidelity, and Ego2World for belief-state planning.

Find the papers and official resources in the categories below.

## Project releases and rendering infrastructure

Official projects connected to code-defined worlds, including projects without a verified paper. Dates below record resource checks, not necessarily first release; entries are newest-checked first. These resources are counted separately from the paper list.

| Project | Organization | Verified on | Official resources | Release status |
| :--- | :--- | :--- | :--- | :--- |
| **StreamRender-H3** | NVIDIA | 2026-10-12 | [Project](https://nvlabs.github.io/Sana/Sol-Engine/StreamRender-H3/) · [Source code](https://github.com/NVlabs/Sana/tree/sol-engine/models/streamrender_h3) | Project page and runtime source available; deployment requires external model weights and a compatible multi-GPU environment. No standalone paper destination verified. |
| **EdenLive** | VAST | 2026-10-12 | [Project](https://vast-eden.ai/?p=edenlive) · [Repository](https://github.com/VAST-AI-Research/EdenLive) | Project page and announcement repository available; code announced for release by **2026-10-18**. No paper destination verified. |

**StreamRender-H3** connects a code game engine that maintains maps, physics, rules, and player feedback to a streaming MiniMax-H3 renderer through semantic frame maps. The published demo is racing-specific; it does not establish learned executable dynamics or generalization to other games.

**EdenLive** renders proxy or reference video streams from coding agents, existing engines, or recorded footage. World state and interaction rules remain in upstream code or engines; it is included as rendering infrastructure, not as a model that synthesizes executable dynamics.

## Code-driven world evolution and physical reasoning

- **[2026-10-08] AgentGarten: Code Worlds for Evolving Agents** — `Core`  
  Couples simulation backends that maintain persistent state and program-defined interaction rules with a shared neural renderer, allowing agents to practice in code-defined worlds and refine reusable playbooks.  
  [Paper](https://arxiv.org/abs/2610.12374) · [Project](https://mirros-lab.github.io/agent-garten/) · [Repository](https://github.com/MirroS-Lab/AgentGarten)  
  *Release note: the repository currently provides the neural renderer; code worlds and the agent practice loop are listed as forthcoming.*

- **[2026-10-08] LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models** — `Core`  
  Proposes evaluable symbolic dynamics and uses deterministic identifiability diagnostics to separate inadequate search from insufficient experiments, guiding physical-mechanism discovery rather than constructing a general-purpose simulator.  
  [Paper](https://arxiv.org/abs/2610.11253) · [Repository](https://github.com/Suraskey/llm-idea)

- **[2026-09-22] Code Plans, Diffusion Renders: Open-Ended Generative World Modeling** — `Core` · **CoDeR**  
  Coordinates five roles to turn high-level concepts into executable world rules and dynamics, with video models rendering observations of persistent, autonomously evolving multi-agent worlds.  
  [Paper](https://arxiv.org/abs/2609.26458) · [Project](https://becauseimbatman0.github.io/CoDeR)

- **[2026-09-22] GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models** — `Core`  
  Maintains explicit combat state through predefined deterministic rules driven by detected gameplay events, selects NPC actions, and prompts a video renderer; it does not synthesize unknown game dynamics.  
  [Paper](https://arxiv.org/abs/2609.25652) · [Project](https://jimntu.github.io/gamedirector/)

- **[2026-09-09] Programmable World Model** — `Core`  
  Separates persistent state and executable transition rules from video rendering, using state-augmented 3D bounding boxes as the bridge; introduces CombatStateBench.  
  [Paper](https://arxiv.org/abs/2609.10540) · [Project](https://alaya-lab.github.io/pwm) · [Repository](https://github.com/AlayaLab/pwm)

- **[2026-08-27] Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning** — `Core`  
  Discovers executable physical representations through a propose–execute–render–verify loop, then uses verified worlds as supervision for quantitative physical reasoning.  
  [Paper](https://arxiv.org/abs/2608.27549) · [Project](https://mirros-lab.github.io/code-as-world/) · [Repository](https://github.com/MirroS-Lab/Code-as-World)

- **[2026-08-26] Code World Model: Coding Agent as World Brain** — `Core`  
  A coding agent maintains persistent world state and rule-based evolution; proxy videos translate executable state into conditioning for a generative video renderer.  
  [Paper](https://arxiv.org/abs/2608.25927) · [Project](https://buaacyw.github.io/cwm/) · [Repository](https://github.com/buaacyw/code-world-model)

- **[2026-07-07] World-Time Compute with Verified Code World Models** — `Core`  
  Uses verified executable worlds over symbolic states to generate exactly labeled trajectories for model training and studies the limits of cross-world transfer.  
  [Paper](https://arxiv.org/abs/2609.09163) · [Repository](https://github.com/quome-cloud/openworld)  
  *Date note: arXiv reports July 7, 2026 for v1 despite the `2609` identifier; the date above follows the submission history.*

## Learning executable dynamics and planning

- **[2026-10-08] Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks** — `Core`  
  Compiles revisable rulebooks into executable transition, observation, and goal models, refining them through prediction errors and replay before using them for planning.  
  [Paper](https://arxiv.org/abs/2610.11794)

- **[2026-09-30] Kepler: Auditable World Models for ARC-AGI-3** — `Core`  
  Builds executable game hypotheses from interaction, checks them against recorded transitions, and uses model-based search with conditional prediction checks during action execution.  
  [Paper](https://arxiv.org/abs/2610.00834) · [Project](https://kepler-harness.vercel.app/) · [Repository](https://github.com/Cveinnt/kepler)

- **[2026-09-28] EMPIRIC: Experiment-Driven Learning of Residual World Models for Robot Planning** — `Core`  
  Extends a physics engine with synthesized Python programs for missing mechanisms, using Bayesian parameter and state inference, informative experiments, and failure-driven revision for robot planning.  
  [Paper](https://arxiv.org/abs/2609.35047) · [Project](https://basisresearch.github.io/empiric) · [Repository](https://github.com/BasisResearch/empiric)

- **[2026-08-14] Twin: Playing an Unknown Game with a Test-Time Digital Twin** — `Core`  
  Constructs a game simulator at test time and repairs it using counterexamples, requiring replay consistency with observed transitions before acting.  
  [Paper](https://arxiv.org/abs/2608.14490) · [Repository](https://github.com/Alexyskoutnev/TWIN-ARC-AGI-3)

- **[2026-07-30] Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3** — `Core`  
  Builds and tests executable game hypotheses while deciding when model construction, repair, planning, or bypassing the model is worth the interaction cost.  
  [Paper](https://arxiv.org/abs/2607.28287) · [Repository](https://github.com/NIMI-research/Tycho)

- **[2026-07-01] OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration for ARC-AGI-3** — `Core`  
  Couples qualitative object hypotheses and Bayesian effect diagnostics with synthesized Python transition and reward models, using targeted exploration and replay-based repair to revise both abstractions and executable mechanics.  
  [Paper](https://arxiv.org/abs/2607.01531)

- **[2026-06-14] Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games** — `Core`  
  Synthesizes standalone pygame-style world programs from interaction traces and screenshot-derived information, evaluating their multi-step lookahead fidelity.  
  [Paper](https://arxiv.org/abs/2606.16070)

- **[2026-05-29] PatchWorld: Gradient-Free Optimization of Executable World Models for Agent Environments** — `Core`  
  Converts offline text-agent trajectories into Python belief-state programs through counterexample-guided repair and separates observation fidelity from planning utility.  
  [Paper](https://arxiv.org/abs/2605.30880) · [Repository](https://github.com/HKBU-KnowComp/PatchWorld)

- **[2026-01-31] Learning Abstractions for Hierarchical Planning in Program-Synthesis Agents** — `Core` · **TheoryCoder-2**  
  Learns reusable abstractions from experience and integrates them with hierarchical planning, reducing dependence on manually supplied abstractions.  
  [Paper](https://arxiv.org/abs/2602.00929) · [Author-linked repository](https://github.com/ZerghamAhmed/TheoryCoder)

- **[2025-10-14] One Life to Learn: Inferring Symbolic World Models for Stochastic Environments from Unguided Exploration** — `Core` · **OneLife**  
  Learns conditionally activated probabilistic program laws from limited unguided exploration and evaluates state ranking, fidelity, and planning.  
  [Paper](https://arxiv.org/abs/2510.12088) · [Project](https://onelife-worldmodel.github.io/) · [Repository](https://github.com/codezakh/onelife) · [Crafter-OO](https://github.com/codezakh/crafter_oo)

- **[2025-08-15] Finite Automata Extraction: Low-data World Model Learning as Programs from Gameplay Video** — `Core` · **FAE**  
  Extracts neuro-symbolic world models from gameplay video as programs in the Retro Coder domain-specific language.  
  [Paper](https://arxiv.org/abs/2508.11836)

- **[2025-05-16] PoE-World: Compositional World Modeling with Products of Programmatic Experts** — `Core`  
  Represents stochastic dynamics as a product of LLM-synthesized programmatic experts and uses the resulting model for planning in Atari environments.  
  [Paper](https://arxiv.org/abs/2505.10819) · [Project](https://topwasu.github.io/poe-world) · [Repository](https://github.com/topwasu/poe-world)

- **[2025-03-26] Synthesizing world models for bilevel planning** — `Core` · **TheoryCoder**  
  Grounds high-level abstractions in a Python transition model synthesized from observations, enabling bilevel planning in grid-world games.  
  [Paper](https://arxiv.org/abs/2503.20124)

- **[2024-05-24] Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search** — `Core` · **GIF-MCTS / CWMB**  
  Introduces a generate–improve–fix search procedure for Python world models and a benchmark spanning 18 reinforcement-learning environments.  
  [Paper](https://arxiv.org/abs/2405.15383)

- **[2024-02-19] WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment** — `Core`  
  Learns a Python world model from interaction, combining consistency with observed transitions and an optimistic planning constraint.  
  [Paper](https://arxiv.org/abs/2402.12275)

## GUI world models

- **[2026-08-06] AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents** — `GUI`  
  Predicts reachable next-screen code updates using transition-constrained retrieval, executable HTML, and generated visual assets.  
  [Paper](https://arxiv.org/abs/2608.05891)

- **[2026-02-10] Code2World: A GUI World Model via Renderable Code Generation** — `GUI`  
  Predicts action-conditioned interfaces as HTML, using AndroidCode data and render-aware reinforcement learning to align visual and action consistency.  
  [Paper](https://arxiv.org/abs/2602.09856) · [Project](https://amap-ml.github.io/Code2World/) · [Repository](https://github.com/AMAP-ML/Code2World)

## Executable scene and 4D world construction

These papers construct executable environments; their goals differ from identifying unknown transition dynamics through interaction.

- **[2026-10-09] VETR: Execution-Grounded Self-Improving Agent for Symbolic Graphics Reasoning** — `Construction`  
  Refines Blender scene-editing programs using captured writes, state, and resource bindings, checking realized changes and preservation of captured properties before visual verification; it does not learn physical transition dynamics.  
  [Paper](https://arxiv.org/abs/2610.13098)

- **[2026-10-08] USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation** — `Construction`  
  Writes and revises executable asset programs from partial geometric evidence, producing articulated USD assets with explicit physical properties for simulation.  
  [Paper](https://arxiv.org/abs/2610.11322) · [Project](https://xingyoujun.github.io/usdcraft/)

- **[2026-10-03] EnvDreamer: Large-Scale Multimodal-to-Environment Generation for Embodied AI** — `Construction`  
  Compiles language- and image-conditioned scene plans and task specifications into executable Unreal Engine environments, iteratively checking playability, physical consistency, and task completion.  
  [Paper](https://arxiv.org/abs/2610.04301)

- **[2026-09-29] Real2Gym: Building Gyms from Videos, Bringing Skills to Robots** — `Construction`  
  Reconstructs Blender and MuJoCo environments from human or robot demonstrations, validates interactions and scene variations through native physics, and uses the resulting gyms for feedback-driven manipulation skill development.  
  [Paper](https://arxiv.org/abs/2609.37089) · [Project](https://real2gym.github.io/) · [Real2Sim repository](https://github.com/real2gym/Real2Gym) · [Agent repository](https://github.com/real2gym/R2G_Agent)  
  *Release note: the agent repository provides continuous stage-code execution, not the paper's persistent experience library; scene assets and external perception/model services are required.*

- **[2026-09-10] Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs** — `Construction` · **RCWM**  
  Reconstructs a complex 3D scene from a reference image through recursive scene programs and nested render–compare–edit loops.  
  [Paper](https://arxiv.org/abs/2609.11499)

- **[2026-02-12] Code2Worlds: Empowering Coding LLMs for 4D World Generation** — `Construction`  
  Generates simulation code with separate object and environment construction, then refines dynamics through physics-aware visual feedback; includes Code4D evaluation.  
  [Paper](https://arxiv.org/abs/2602.11757) · [Project](https://aigeeksgroup.github.io/Code2Worlds/) · [Repository](https://github.com/AIGeeksGroup/Code2Worlds)

**Naming caution:** *Code2World* is the GUI paper; *Code2Worlds* is the 4D generation paper. *WorldCoder-Bench* below is a separate paper from the 2024 *WorldCoder* agent.

## Related symbolic and neurosymbolic planning

These works are included for their explicit transition representations and verification or planning interfaces, not because all of them synthesize general-purpose simulators.

- **[2026-10-09] RoleWorld: Knowledge Transfer in World Modeling with Functional Role Abstractions** — `Related`  
  Induces reusable role prototypes and executable DSL transition rules from source-world interactions, then adapts object-role assignments and parameters through target-world feedback while keeping the shared rules fixed.  
  [Paper](https://arxiv.org/abs/2610.13172)

- **[2026-10-02] CVE2AP: Automated Generation of PDDL-Encoded Attack Paths via Large Language Models** — `Related`  
  Generates domain-specific PDDL attack models from vulnerability descriptions, refining action preconditions and effects through planner feedback; this is symbolic cybersecurity planning rather than physical simulator learning.  
  [Paper](https://arxiv.org/abs/2610.03383) · [Repository](https://github.com/LincuiDudu/pddl-ap-generation)

- **[2026-09-30] Asking the World: Generalist Physical Reasoning through Agentic World Modeling and Probing** — `Related` · **ATW**  
  Constructs, calibrates, and probes task-relevant worlds through semantic operations on the fixed PolyWorld physics engine, using simulation and interventions for physical reasoning rather than synthesizing new engine dynamics.  
  [Paper](https://arxiv.org/abs/2609.39135)

- **[2026-09-25] Representation-Guided Generation and Integration of Executable Programs for Robot Manipulation** — `Related` · **RIVET**  
  Generates reusable perception, rendering, relation-inference, and planning programs around shared object poses and a relation graph; the planner encodes task-level action preconditions and state transitions for manipulation.  
  [Paper](https://arxiv.org/abs/2609.31337)

- **[2026-09-16] GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning** — `Related`  
  Uses a graph model of relations, action conditions/effects, and uncertain object locations to verify, repair, and reorder long-horizon plans.  
  [Paper](https://arxiv.org/abs/2609.19315)

- **[2025-04-22] WALL-E 2.0: World Alignment by NeuroSymbolic Learning improves World Model-based LLM Agents** — `Related`  
  Extracts symbolic environment knowledge from exploration and encodes it as executable rules to align an LLM world model for model-predictive control.  
  [Paper](https://arxiv.org/abs/2504.15785) · [Repository](https://github.com/elated-sawyer/WALL-E)

- **[2025-02-07] Generating Symbolic World Models via Test-time Scaling of Large Language Models** — `Related`  
  Combines candidate sampling with iterative refinement to generate PDDL domains usable by classical planners.  
  [Paper](https://arxiv.org/abs/2502.04728) · [Project](https://vmlpddl.github.io/) · [Repository](https://github.com/VMLPDDL/VML_PDDL)

## Benchmarks and evaluation

- **[2026-10-06] WorldSolver: Can LLM Agents Simulate the Physical Dynamics via Solver Generation?** — `Benchmark`  
  Evaluates generated numerical solvers on 168 tasks across seven physical domains within fixed scene scaffolds, separately checking execution, rendered behavior, and physical plausibility of state trajectories.  
  [Paper](https://arxiv.org/abs/2610.08720)

- **[2026-10-03] Video2World: Benchmarking Coding Agents for Interactive World Modeling from Embodied Videos** — `Benchmark`  
  Evaluates coding agents that reconstruct executable environments and robot behavior from embodied videos, separating geometric fidelity, dynamic fidelity, and functional correctness across 222 instances from 189 videos.  
  [Paper](https://arxiv.org/abs/2610.04432) · [Project](https://aetherlabsai.github.io/Video2World) · [Repository](https://github.com/AetherLabsAI/Video2World)

- **[2026-10-01] World Editing: Intervening on Executable Worlds at Increasing Depth** — `Benchmark` · **IGMWorld / IGMBench**  
  Evaluates coding agents that modify properties, entities, dynamics, and systems in existing executable games, checking requested behavior and preservation of unaffected properties at runtime.  
  [Paper](https://arxiv.org/abs/2610.02331) · [Project](https://vinesmsuic.github.io/IGMWorld/) · [Repository](https://github.com/vinesmsuic/IGMWorld/)  
  *Release note: the repository is currently a placeholder marked "Coming Soon".*

- **[2026-10-01] PROWBench: Do Video Models Render What the Program Specifies?** — `Benchmark`  
  Tests whether generated videos realize program-specified states and interactions, comparing rendered observations with replayable world records and timestamped events.  
  [Paper](https://arxiv.org/abs/2610.02205) · [Project](https://alaya-lab.github.io/PROWBench/) · [Repository](https://github.com/AlayaLab/PROWBench) · [Dataset](https://huggingface.co/datasets/AlayaLab/PROWBench)  
  *Release note: engine recordings, example representations, and evaluation code are available; the world-generation pipeline remains on the release roadmap. Resource availability was checked October 12, 2026; evaluations were not run.*

- **[2026-09-26] World Agent: Can Language Models Keep a World Running?** — `Benchmark`  
  Evaluates sustained maintenance of explicit world states and action-conditioned deduction through executable world interfaces, event contracts, and deterministic reference dynamics; it does not evaluate generated simulator code.  
  [Paper](https://arxiv.org/abs/2609.32692) · [Repository](https://github.com/HCPLab-SYSU/WorldAgent-Benchmark)  
  *Release note: benchmark cases and evaluation scripts are available; playback, rendering, and the playable demo remain on the release roadmap. Resource availability was checked October 12, 2026; evaluations were not run.*

- **[2026-09-14] BVB: Benchmarking Agentic Video Understanding via Programmatic Reconstruction in Blender** — `Benchmark`  
  Evaluates agents that reconstruct videos as executable animated Blender scenes, measuring retained spatiotemporal facts and perceptual similarity under a shared execution budget.  
  [Paper](https://arxiv.org/abs/2609.15478) · [Project](https://yoloytang.me/BVB/) · [Repository](https://github.com/yunlong10/BVB)

- **[2026-06-01] WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis** — `Benchmark`  
  Evaluates generated interactive 3D programs using StateProbe runtime-state and transition contracts, beyond screenshots or DOM inspection alone.  
  [Paper](https://arxiv.org/abs/2606.01869) · [Author-linked anonymous resource](https://anonymous.4open.science/r/WorldCoder-Bench/)

- **[2026-05-13] Ego2World: Compiling Egocentric Cooking Videos into Executable Worlds for Belief-State Planning** — `Benchmark`  
  Compiles video annotations into graph-transition worlds and separates hidden simulator state from the agent's partial belief state during planning.  
  [Paper](https://arxiv.org/abs/2605.13335)

- **[2025-02-18] Text2World: Benchmarking Large Language Models for Symbolic World Model Generation** — `Benchmark`  
  Evaluates text-to-PDDL world-model generation across diverse domains with multiple execution-based criteria.  
  [Paper](https://arxiv.org/abs/2502.13092) · [Project](https://text-to-world.github.io/) · [Repository](https://github.com/Aaron617/text2world)

Also see **CWMB** in the GIF-MCTS paper, **CombatStateBench** in Programmable World Model, and **Code4D** in Code2Worlds. These are not counted as additional papers.

## Adjacent perspectives and data engines

- **[2026-08-31] WebWorld: The Browser as a World Model for Self-Improving Web Code** — `Perspective`  
  Treats the browser as an existing executable simulator and admits code-improvement supervision through behavior-verifying interaction contracts. It does not learn the browser's dynamics.  
  [Paper](https://arxiv.org/abs/2608.30530)

- **[2026-08-26] Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models** — `Perspective`  
  Proposes human–engine verification as a source of grounded feedback and trajectory data for world-model training, rather than introducing another learned transition model.  
  [Paper](https://arxiv.org/abs/2608.25518)

## Research questions

Questions to keep in mind while comparing these approaches:

- **State:** Is it inferred from pixels, exposed by the environment, or manually specified? How is partial observability handled?
- **Dynamics:** Does generated code encode transitions, just render a scene, or invoke an existing simulator?
- **Verification:** Are checks limited to observed traces, or do they test counterfactual actions and long-horizon rollouts?
- **Planning:** Does higher prediction fidelity translate into better action selection?
- **Stochasticity:** Can the representation express uncertainty and probabilistic transitions?
- **Cost:** How much interaction and inference is required to synthesize, repair, and execute the model?
- **Generalization:** Does the program transfer to new goals, levels, objects, or genuinely different rules?
- **Rendering:** Is the visual observation consistent with the executable state, including off-screen entities?

## Contributing

Paper and project suggestions, corrections, and verified official resources are welcome. A paper is not required for a project release. Read [CONTRIBUTING.md](CONTRIBUTING.md), then open an issue or pull request.

Run the local structural checks before submitting:

```bash
python3 scripts/check_readme.py
```

The check validates entry structure, dates, duplicates, ordering, and local links; it does not certify scientific claims or external-link availability.

## Acknowledgements

Inspired by [Awesome-World-Models](https://github.com/knightnemo/Awesome-World-Models), with a dedicated focus on **code as the world representation**.

- [knightnemo/Awesome-World-Models](https://github.com/knightnemo/Awesome-World-Models) inspired the repository layout and supplied initial discovery leads.
- The researchers and maintainers who publish papers, code, environments, and benchmarks.

Descriptions here are newly written summaries. Papers, project pages, code, and trademarks remain the property of their respective owners.

## License

The original list, summaries, and repository tooling are dedicated to the public domain under [CC0 1.0](LICENSE). Linked resources retain their own licenses.
