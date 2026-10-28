<div align="center">

# Awesome Code World Models

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/yifliu3/awesome-code-world-models?style=social)](https://github.com/yifliu3/awesome-code-world-models/stargazers)
[![License: CC0](https://img.shields.io/badge/License-CC0%201.0-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**A curated collection of code world models: executable dynamics, programmatic simulation, and coding agents that build and reason about worlds.**

代码世界模型论文与资源精选：可执行动力学、程序化仿真，以及通过编程构建和理解世界的智能体。

</div>

**75 papers** and **3 project releases**.

**Last literature search: October 28, 2026.** This is a curated snapshot, not an exhaustive survey or an automatically maintained feed.

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
- [Adjacent renderers, perspectives, and data engines](#adjacent-renderers-perspectives-and-data-engines)
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
| **GUI** | Renderable interface prediction and executable app/computer-environment synthesis | Next-screen rendering, app reconstruction, and environment synthesis have different modeling objectives. |
| **Construction** | Executable 3D scenes and 4D simulation programs | Scene reconstruction alone does not establish learned transition dynamics. |
| **Related** | PDDL, graph, and neurosymbolic models used for simulation or planning | Symbolic models need not be general-purpose code world models. |
| **Benchmark** | Evaluation of executable worlds, generated domains, or state-grounded planning | A benchmark may supply rather than learn a world model. |
| **Perspective** | Generative rendering, engine-verified data generation, and browser-backed coding | Relevant infrastructure or arguments, not equivalent executable-dynamics architectures. |
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
2. **Coding agent → persistent visual world:** Code World Model → Programmable World Model → CoDeR → AgentGarten → Mallea; compare Matrix-Game 4.0, State World Models, and BoxWorld for interaction-rule execution and rendering.
3. **Physical reasoning → executable representation:** Code as Worlds → Code2Worlds; compare their reasoning and generation objectives, then Code2Worlds-2 for simulator-compatible scenes and PhysEvolve for verified counterfactual training.
4. **Online discovery → planning:** PatchWorld → Tycho → Twin → Kepler → Memento 3; compare EMPIRIC's learned residual mechanisms on top of a physics engine.
5. **Evaluation:** Text2World → WorldCoder-Bench → Video2World; compare WorldSolver for generated physical solvers, World Editing for interventions, PROWBench for program-to-render fidelity, and Ego2World for belief-state planning.

Find the papers and official resources in the categories below. For app environments, compare Code2World's next-screen prediction with Trace2World's behavior reconstruction and WildAWM's cross-interface environment synthesis.

## Project releases and rendering infrastructure

Official projects connected to code-defined worlds, including projects without a verified paper. Dates below record resource checks, not necessarily first release; entries are newest-checked first. These resources are counted separately from the paper list.

| Project | Organization | Verified on | Official resources | Release status |
| :--- | :--- | :--- | :--- | :--- |
| **EdenLive** | VAST | 2026-10-28 | [Project](https://vast-eden.ai/?p=edenlive) · [Repository](https://github.com/VAST-AI-Research/EdenLive) · [Models](https://huggingface.co/VAST-AI/EdenLive) | Offline and streaming inference source, 5B/14B weights, and a prompt-to-game frontend are available. The project page and author-linked technical-report PDF returned HTTP 403 during this check; report contents were not verified. |
| **Streaming Code World Model** | Tingting Liao and Guangyi Liu | 2026-10-28 | [Repository](https://github.com/TingtingLiao/streaming-code-world-model) · [Models](https://huggingface.co/Luffuly/streaming-code-world-model) | Training/evaluation source and streaming LoRA checkpoints are available; requires the upstream CWM runtime and base weights. The documented configuration is not real time. No standalone paper verified. |
| **StreamRender-H3** | NVIDIA | 2026-10-28 | [Project](https://nvlabs.github.io/Sana/Sol-Engine/StreamRender-H3/) · [Source code](https://github.com/NVlabs/Sana/tree/sol-engine/models/streamrender_h3) | Project page and runtime source available; deployment requires external model weights and a compatible multi-GPU environment. No standalone paper destination verified. |

**StreamRender-H3** connects a code game engine that maintains maps, physics, rules, and player feedback to a streaming MiniMax-H3 renderer through semantic frame maps. The published demo is racing-specific; it does not establish learned executable dynamics or generalization to other games.

**EdenLive** renders proxy or reference video streams from coding agents, existing engines, or recorded footage. Its release also includes an EdenGolem skill and frontend for creating coarse playable games; state transitions and interaction rules execute in those upstream programs.

**Streaming Code World Model** extends CWM with causal proxy-conditioned chunk generation and few-step distillation. It is tracked as a separate author-maintained extension, not as the original CWM paper's official repository.

## Code-driven world evolution and physical reasoning

- **[2026-10-26] BoxWorld: Let World Engines Control and Video Generators Render** — `Core`  
  Uses a coding agent to implement user-defined interaction rules in a persistent world engine, exposing object boxes, attributes, and status changes to an autoregressive video renderer; introduces PairedStateBench.  
  [Paper](https://arxiv.org/abs/2610.36371) · [Project](https://boxworld-web.github.io/)

- **[2026-10-26] PhysEvolve: Verifier-grounded Self-evolution for Physical Reasoning with Executable Worlds** — `Core`  
  Proposes executable physical scenes and evidence schemas, then uses a fixed physics engine to generate verified factual and object-removal tasks that train the shared proposer–solver policy.  
  [Paper](https://arxiv.org/abs/2610.34921) · [Project](https://yelonhu.github.io/physevolve-page/) · [Repository](https://github.com/yelonhu/PhysEvolve)

- **[2026-10-20] Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds** — `Core`  
  Couples coding-agent game creation with an engine that maintains state and enforces gameplay rules, while a causal video renderer converts low-poly proxies and dynamic captions into interactive observations.  
  [Paper](https://arxiv.org/abs/2610.27999) · [Project](https://matrix-game-v4-0.github.io/page/) · [Repository](https://github.com/SkyworkAI/Matrix-Game/tree/main/Matrix-Game-4) · [Models and game assets](https://huggingface.co/Skywork/Matrix-Game-4.0)

- **[2026-10-19] State World Models: Execute the Rules, Generate the Pixels** — `Core` · **Stateful Harness**  
  Resolves user actions against explicit semantic and spatial state before rendering with a frozen video model, using editable 3D previews and generated observations across turns; introduces WorldState-Bench.  
  [Paper](https://arxiv.org/abs/2610.26811) · [Project](https://ivg-yanranzhang.github.io/StateWorldModel/) · [Repository](https://github.com/Zhangyr2022/StateWorldModel) · [Dataset](https://huggingface.co/datasets/Louis0411/StateWorldModel)

- **[2026-10-15] Mallea: Building, Steering, and Memorizing Worlds with Coding Agent** — `Core`  
  Coordinates object representations, editable behavior, and object-specific texture memory through a coding agent, with executable rules advancing persistent state and a generative renderer realizing the current world.  
  [Paper](https://arxiv.org/abs/2610.21283) · [Project](https://lxycopper.github.io/Mallea/)  
  *Release note: the author-linked repository currently contains the project website and demonstrations; a runnable modeling pipeline was not verified.*

- **[2026-10-08] AgentGarten: Code Worlds for Evolving Agents** — `Core`  
  Couples simulation backends that maintain persistent state and program-defined interaction rules with a shared neural renderer, allowing agents to practice in code-defined worlds and refine reusable playbooks.  
  [Paper](https://arxiv.org/abs/2610.12374) · [Project](https://mirros-lab.github.io/agent-garten/) · [Repository](https://github.com/MirroS-Lab/AgentGarten)  
  *Release note: neural-renderer source and checkpoints are available; the interactive frontend, code worlds, and agent practice loop remain on the roadmap. Resource status checked October 28, 2026.*

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

- **[2026-05-16] Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models** — `Core` · **Alice**  
  Learns persistent executable transition rules from interaction in a game with misleading rule labels, using failed code revisions to organize preservation counterexamples and guide further exploration.  
  [Paper](https://arxiv.org/abs/2605.16725) · [Repository](https://github.com/ssw03270/BABAinWonderland_NeurIPS-26)

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

- **[2026-10-22] Trace2World: Reconstructing App Worlds from Real Interaction Traces for Scalable GUI Agent Training** — `GUI`  
  Reconciles recorded workflows into a shared app-state model, compiles its supported behavior into a browser environment, and repairs implementation errors through independent replay while keeping unsupported transitions non-executable.  
  [Paper](https://arxiv.org/abs/2610.30792)

- **[2026-10-19] Agent World Model in the Wild: Computer-Use Agent Environment Synthesis** — `GUI` · **WildAWM**  
  Synthesizes persistent computer environments spanning GUI, MCP, and command-line interfaces, with execution-based checks for task solvability, difficulty, and verifier reliability before agent training.  
  [Paper](https://arxiv.org/abs/2610.26828) · [Project](https://msr-orchard.github.io/WildAWM/) · [Repository](https://github.com/MSR-Orchard/WildAWM)

- **[2026-08-06] AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents** — `GUI`  
  Predicts reachable next-screen code updates using transition-constrained retrieval, executable HTML, and generated visual assets.  
  [Paper](https://arxiv.org/abs/2608.05891)

- **[2026-02-10] Code2World: A GUI World Model via Renderable Code Generation** — `GUI`  
  Predicts action-conditioned interfaces as HTML, using AndroidCode data and render-aware reinforcement learning to align visual and action consistency.  
  [Paper](https://arxiv.org/abs/2602.09856) · [Project](https://amap-ml.github.io/Code2World/) · [Repository](https://github.com/AMAP-ML/Code2World)

## Executable scene and 4D world construction

These papers construct executable environments; their goals differ from identifying unknown transition dynamics through interaction.

- **[2026-10-22] WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations** — `Construction`  
  Reconstructs robot demonstrations as executable world programs, combining camera-anchored scene decomposition, specialist reconstruction tools, and verification-guided repair to support physical interaction and trajectory replay.  
  [Paper](https://arxiv.org/abs/2610.31834) · [Project](https://worldmirror-page.github.io/)

- **[2026-10-20] NeoWorld-3: From Pixels to Code-Defined Physical Worlds** — `Construction`  
  Reconstructs objects and scenes as tunable geometry programs, combining agentic code revision, differentiable parameter fitting, and articulation checks to prepare interactive digital twins.  
  [Paper](https://arxiv.org/abs/2610.27690) · [Project](https://neoworldproject.github.io/Studio/) · [Announcement repository](https://github.com/NeoWorldProject/NeoWorldStudio)  
  *Release note: the Studio repository currently contains documentation, not implementation source or an installable application.*

- **[2026-10-20] WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State** — `Construction`  
  Compiles hierarchical semantic plans into streamed terrain and entities using deterministic local code, retaining identities, edits, and boundary commitments in a persistent record for interaction and revisits.  
  [Paper](https://arxiv.org/abs/2610.28827) · [Project](https://krennic999.github.io/WorldStream/)  
  *Release note: the author-linked repository presents demonstrations and marks code as coming soon.*

- **[2026-10-13] RoboSimStudio: An Interactive Toolkit for Human and Agent Rapid Real2Sim of Robot Manipulation Tasks** — `Construction` · **RSS**  
  Provides editable solver, contact-model, and physical-parameter interfaces for humans and coding agents to iteratively reconstruct robot tasks using visual, force, and simulation feedback within existing physics engines.  
  [Paper](https://arxiv.org/abs/2610.18835) · [Project](https://robosimstudio.github.io/) · [Repository](https://github.com/robosimstudio/robosimstudio)

- **[2026-10-13] Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation** — `Construction`  
  Compiles generated scenes into MuJoCo worlds with collision geometry and physical attributes, then refines rigid and articulated behavior using simulator feedback; introduces SimCode4D state-based evaluation.  
  [Paper](https://arxiv.org/abs/2610.17651) · [Project](https://aigeeksgroup.github.io/Code2Worlds-2/) · [Repository](https://github.com/AIGeeksGroup/Code2Worlds-2) · [Dataset](https://huggingface.co/datasets/AIGeeksGroup/SimCode4D)  
  *Release note: the repository includes the DEV15 runtime packages; its 225/225 reference-package check is not a success rate for method-generated worlds.*

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

- **[2026-10-21] MemPlan: Memory-Conditioned PDDL Planning for Partially Observable Text Environments** — `Related`  
  Reconstructs PDDL problems from observations and interaction memory while keeping domain rules fixed, using positive memory to prioritize hypotheses and negative memory to exclude refuted assumptions.  
  [Paper](https://arxiv.org/abs/2610.30379) · [Repository](https://github.com/tewiSong/MemPlan)

- **[2026-10-18] LLM Agents as Suppliers of Physical System Models: Calibration and Acceptance in Modelica** — `Related`  
  Builds and calibrates executable Modelica component models from device descriptions and measurements, separating behavioral fit from structural acceptance, physical invariants, and transfer to device variants.  
  [Paper](https://arxiv.org/abs/2610.25019) · [Repository](https://github.com/jfrochte/agents-as-modelica-suppliers)

- **[2026-10-14] Neurosymbolic Learning of Interpretable World Models** — `Related` · **CGWM**  
  Learns visual concept grounding while supplied temporal-logic rules define symbolic transitions, then plans through differentiable goal satisfaction; the transition rules themselves are not learned.  
  [Paper](https://arxiv.org/abs/2610.19955)

- **[2026-10-13] From Pixels to Executable Physics: Behavior-Grounded World Models for Embodied Action Consequence Prediction** — `Related` · **DR-WM**  
  Infers terrain geometry and calibrated contact parameters for a fixed Genesis simulator, whose action rollouts condition video prediction and subsequent terrain updates; it does not synthesize new dynamics code.  
  [Paper](https://arxiv.org/abs/2610.17630)

- **[2026-10-12] D-World: An Explicit World-Language-Action Model with Recursive Self-Improvement under Dual Control** — `Related`  
  Constructs executable robot-scene twins with generated perception code, plans in simulation, and revises states and named physical parameters through measurement-grounded replay checks, rebuilding the scene when structure is inadequate.  
  [Paper](https://arxiv.org/abs/2610.17114)

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

- **[2026-10-19] From Code to Playable Systems: CEGame-Bench for Long-Horizon Game Creation Agents** — `Benchmark` · **CEGame-Bench**  
  Evaluates complete-game creation across five production engines using hidden play-based contracts for gameplay, completion, and saved-world restoration, distinguishing build success from executable game behavior.  
  [Paper](https://arxiv.org/abs/2610.26098)

- **[2026-10-15] Testing the Planning Claims of LLM-Based Agents against Formal Semantics** — `Benchmark`  
  Evaluates offline plans and online agents against hidden PDDL transition models, checking action applicability, goal achievement, sensing behavior, and recognition of unsolvable tasks.  
  [Paper](https://arxiv.org/abs/2610.22469)

- **[2026-10-12] PhysCodeGym: Benchmarking Coding Agents for Physically Verifiable 4D Reconstruction** — `Benchmark`  
  Evaluates video-to-Blender reconstruction across 156 tasks using visual rubrics, program and scene inspection, and counterfactual physical interventions to distinguish replay fidelity from robust simulation.  
  [Paper](https://arxiv.org/abs/2610.17288) · [Repository](https://github.com/ShaoShuai0605/PhysCodeGym)

- **[2026-10-11] PhySimCode: A Benchmark and Evaluation Method for Physics Video to Code Generation** — `Benchmark`  
  Evaluates reconstruction of physics videos as runnable Python simulations, separately measuring governing-law inference, numerical parameter recovery, code execution, and simulation equivalence.  
  [Paper](https://arxiv.org/abs/2610.15722) · [Project](https://sourajakundu.github.io/PhySimCode/) · [Repository](https://github.com/SourajaKundu/PhySimCode) · [Evaluation dataset](https://huggingface.co/datasets/SourajaKundu123/PhySimCode)  
  *Release note: the linked public evaluation subset contains 2,430 videos; it is not the full 160.6K-sample corpus described in the paper.*

- **[2026-10-10] ExeWorldBench: Benchmarking Code-Based Executable 3D World Modeling** — `Benchmark`  
  Tests executable realization of individual mechanisms, composed causal systems, and goal-specified 3D worlds, combining program execution with structural and behavioral evaluation.  
  [Paper](https://arxiv.org/abs/2610.15166) · [Project](https://helen1p.github.io/ExeWorldBench/) · [Dataset](https://huggingface.co/datasets/HelenPeng/ExeWorldBench)  
  *Release note: the project and dataset are available; the linked GitHub repository currently provides an overview rather than a verified evaluation-code release.*

- **[2026-10-06] WorldSolver: Can LLM Agents Simulate the Physical Dynamics via Solver Generation?** — `Benchmark`  
  Evaluates generated numerical solvers on 168 tasks across seven physical domains within fixed scene scaffolds, separately checking execution, rendered behavior, and physical plausibility of state trajectories.  
  [Paper](https://arxiv.org/abs/2610.08720) · [Repository](https://github.com/sirujiang/WorldSolver)

- **[2026-10-03] Video2World: Benchmarking Coding Agents for Interactive World Modeling from Embodied Videos** — `Benchmark`  
  Evaluates coding agents that reconstruct executable environments and robot behavior from embodied videos, separating geometric fidelity, dynamic fidelity, and functional correctness across 222 instances from 189 videos.  
  [Paper](https://arxiv.org/abs/2610.04432) · [Project](https://aetherlabsai.github.io/Video2World) · [Repository](https://github.com/AetherLabsAI/Video2World)

- **[2026-10-02] 4DCodeBench: Benchmarking Agents on Inverse Graphics of Dynamic Scenes** — `Benchmark`  
  Evaluates dynamic-scene reconstruction as executable graphics programs, checking rendered appearance, geometry, motion, and physical plausibility across real and synthetic videos; implementations can use analytic motion or simulation.  
  [Paper](https://arxiv.org/abs/2610.03715) · [Repository](https://github.com/4DCodeBench/4DCodeBench)

- **[2026-10-01] World Editing: Intervening on Executable Worlds at Increasing Depth** — `Benchmark` · **IGMWorld / IGMBench**  
  Evaluates coding agents that modify properties, entities, dynamics, and systems in existing executable games, checking requested behavior and preservation of unaffected properties at runtime.  
  [Paper](https://arxiv.org/abs/2610.02331) · [Project](https://vinesmsuic.github.io/IGMWorld/) · [Repository](https://github.com/vinesmsuic/IGMWorld/)  
  *Release note: the repository still announces a forthcoming code release as of October 28, 2026.*

- **[2026-10-01] PROWBench: Do Video Models Render What the Program Specifies?** — `Benchmark`  
  Tests whether generated videos realize program-specified states and interactions, comparing rendered observations with replayable world records and timestamped events.  
  [Paper](https://arxiv.org/abs/2610.02205) · [Project](https://alaya-lab.github.io/PROWBench/) · [Repository](https://github.com/AlayaLab/PROWBench) · [Dataset](https://huggingface.co/datasets/AlayaLab/PROWBench)  
  *Release note: engine recordings, example representations, and evaluation code are available; the world-generation pipeline remains on the release roadmap. Resource status was rechecked October 28, 2026; evaluations were not run.*

- **[2026-09-26] World Agent: Can Language Models Keep a World Running?** — `Benchmark`  
  Evaluates sustained maintenance of explicit world states and action-conditioned deduction through executable world interfaces, event contracts, and deterministic reference dynamics; it does not evaluate generated simulator code.  
  [Paper](https://arxiv.org/abs/2609.32692) · [Repository](https://github.com/HCPLab-SYSU/WorldAgent-Benchmark)  
  *Release note: benchmark cases and evaluation scripts are available; playback, rendering, and the playable demo remain on the release roadmap. Resource status was rechecked October 28, 2026; evaluations were not run.*

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

## Adjacent renderers, perspectives, and data engines

- **[2026-10-23] Tempo-Zero: Recursive Self-Play in Executable Worlds for Video Reasoning** — `Perspective`  
  Uses executable event worlds to generate videos with exact answers and evidence intervals, training a shared questioner–solver policy whose validated rule changes alter later self-play environments.  
  [Paper](https://arxiv.org/abs/2610.32433) · [Project](https://alchemist-jo.github.io/tempo-zero/)

- **[2026-10-20] SolarRenderer: Few-Step Generative Reference Rendering** — `Perspective`  
  Adapts a frozen video backbone with control and acceleration LoRAs to render structural videos from engines or agents, including a causal streaming variant; world-state evolution remains upstream.  
  [Paper](https://arxiv.org/abs/2610.28630) · [Repository](https://github.com/Enderfga/SolarRenderer) · [Models](https://huggingface.co/Enderfga/SolarRenderer)

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
