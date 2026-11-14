<div align="center">

# Awesome Code World Models

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/yifliu3/awesome-code-world-models?style=social)](https://github.com/yifliu3/awesome-code-world-models/stargazers)
[![License: CC0](https://img.shields.io/badge/License-CC0%201.0-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**A curated collection of code world models: executable dynamics, programmatic simulation, and coding agents that build and reason about worlds.**

代码世界模型论文与资源精选：可执行动力学、程序化仿真，以及通过编程构建和理解世界的智能体。

</div>

**157 papers** and **8 project releases**.

**Last literature search: November 14, 2026.** This is a curated snapshot, not an exhaustive survey or an automatically maintained feed.

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
| **CoCode-World** | IApple233 | 2026-11-14 | [Project](https://iapple233.github.io/CCW/) · [Repository](https://github.com/IApple233/CoCode-World) · [Model](https://huggingface.co/iapple1/CoCode-World-Model) · [Dataset](https://huggingface.co/datasets/iapple1/CoCode-World-Data) | Training/inference source, LoRA weights, a selected paired-video dataset, and proxy-rendering resources are available. Requires external MiniMax-H3 weights; documented generation uses eight GPUs. Recorded world state supports rerendering, not arbitrary new-action simulation; the associated paper is now listed under adjacent renderers. |
| **HolonEngine** | Jonathan Dunlap | 2026-11-12 | [Repository](https://github.com/jadbox/HolonEngine) · [Architecture](https://github.com/jadbox/HolonEngine/blob/main/docs/holon_whitepaper.md) | Experimental pre-alpha Rust compiler and 2D runtime source are available, with build instructions and video examples; requires FFmpeg. The inspected rollout uses built-in dynamics and automatic controls. Interactive control, general game-rule recovery, and the broader 3D roadmap were not verified; no standalone arXiv paper verified. |
| **H3 Streaming VAE Decoder** | SolarX-Team | 2026-11-11 | [Project](https://solarx-team.github.io/H3-Streaming-VAE-Decoder/) · [Repository](https://github.com/SolarX-Team/H3-Streaming-VAE-Decoder) | Streaming decoder source for MiniMax H3 and StreamRender-H3 is available; weights remain external, and optional fused kernels require Blackwell GPUs. Independent decoder extension, not NVIDIA's full renderer; no standalone arXiv paper verified. |
| **Code Video Model** | Microsoft Research | 2026-11-10 | [Project](https://code-video-model.github.io/) · [Repository](https://github.com/code-video-model/CodeVideoModel) · [Technical report](https://code-video-model.github.io/tech_report.pdf) · [Benchmark](https://huggingface.co/datasets/code-video-model/CodeVideoBench) | Scene-generation and rendering source, examples, and benchmark cases are available; requires external model services and MiniMax-H3 weights. No arXiv first-submission date verified; tracked as a project release. |
| **World Model Planning Reliability (WCTR)** | Zhijing Wu | 2026-11-10 | [Repository](https://github.com/ZhijingWu/world-model-planning-reliability) · [Technical note](https://raw.githubusercontent.com/ZhijingWu/world-model-planning-reliability/main/note/Zhijing_Wu_World_Model_Planning_Note_Final.pdf) | Runtime source, an illustrative example, tests, and retained study records are available. Branch isolation covers restricted Python state operations, not arbitrary side effects; no standalone arXiv paper verified. |
| **EdenLive** | VAST | 2026-10-28 | [Project](https://vast-eden.ai/?p=edenlive) · [Repository](https://github.com/VAST-AI-Research/EdenLive) · [Models](https://huggingface.co/VAST-AI/EdenLive) | Offline and streaming inference source, 5B/14B weights, and a prompt-to-game frontend are available. The project page and author-linked technical-report PDF returned HTTP 403 during this check; report contents were not verified. |
| **Streaming Code World Model** | Tingting Liao and Guangyi Liu | 2026-10-28 | [Repository](https://github.com/TingtingLiao/streaming-code-world-model) · [Models](https://huggingface.co/Luffuly/streaming-code-world-model) | Training/evaluation source and streaming LoRA checkpoints are available; requires the upstream CWM runtime and base weights. The documented configuration is not real time. No standalone paper verified. |
| **StreamRender-H3** | NVIDIA | 2026-10-28 | [Project](https://nvlabs.github.io/Sana/Sol-Engine/StreamRender-H3/) · [Source code](https://github.com/NVlabs/Sana/tree/sol-engine/models/streamrender_h3) | Project page and runtime source available; deployment requires external model weights and a compatible multi-GPU environment. No standalone paper destination verified. |

**CoCode-World** renders synchronized player views from shared geometric proxies, reference appearance, and text. Its released metadata and proxy compiler reconstruct observed game states and camera paths; generating consequences of new actions requires a separate dynamics model or compatible simulator.

**HolonEngine** extracts camera motion, world geometry, actor tracks, and motion parameters from gameplay video into a serialized world. Its supplied runtime advances explicit object and interaction state and renders rollouts; the available source does not establish unrestricted synthesis of unseen game mechanics.

**H3 Streaming VAE Decoder** emits frames as video latents arrive, with cached attention and no future-latent requirement. Its explicit StreamRender-H3 support connects it to code-defined game rendering, while state evolution and video-latent generation remain upstream.

**Code Video Model** generates executable Three.js scene and motion programs, renders proxy videos, and conditions a video model on the proxy during early sampling steps. The report and release concern controlled video generation; they do not establish interactive dynamics discovery.

**World Model Planning Reliability** supplies Witness-Compiled Transactional Rollouts (WCTR), which instruments supported state writes and isolates hypothetical branches of existing Python world models. Agreement is checked against the same program on a full copy, not against ground-truth environment dynamics.

**StreamRender-H3** connects a code game engine that maintains maps, physics, rules, and player feedback to a streaming MiniMax-H3 renderer through semantic frame maps. The published demo is racing-specific; it does not establish learned executable dynamics or generalization to other games.

**EdenLive** renders proxy or reference video streams from coding agents, existing engines, or recorded footage. Its release also includes an EdenGolem skill and frontend for creating coarse playable games; state transitions and interaction rules execute in those upstream programs.

**Streaming Code World Model** extends CWM with causal proxy-conditioned chunk generation and few-step distillation. It is tracked as a separate author-maintained extension, not as the original CWM paper's official repository.

## Code-driven world evolution and physical reasoning

- **[2026-11-06] Video-Coder: Reinforcing Agentic Coding for Video Generation** — `Core`\
  Trains an agent to write and revise executable Blender scene and motion programs, combining execution and video feedback before using rendered drafts to condition a downstream video generator.\
  [Paper](https://arxiv.org/abs/2611.09894) · [Project](https://cywang735.github.io/Video-Coder/) · [Repository](https://github.com/CYWang735/Video-Coder) · [Model](https://huggingface.co/Video-Coder/Video-Coder-9B) · [Training data](https://huggingface.co/datasets/Video-Coder/Train-Data)

- **[2026-11-02] Discovering hierarchical governing equations for community-structured complex network dynamics with LLM agents** — `Core` · **SAGE**\
  Selects and revises candidate function families, fits shared community equations and node-specific residuals, and executes the discovered vector fields for state prediction in networked dynamical systems.\
  [Paper](https://arxiv.org/abs/2611.02816) · [Implementation](https://huggingface.co/tczzx6/LLM-SAGE/tree/main) · [Data](https://huggingface.co/datasets/tczzx6/SAGEdata/tree/main)\
  *Release and scope note: The released workflow covers the synthetic multi-dynamics benchmark and defaults to deterministic agent decisions unless an LLM endpoint is enabled; its state check uses observed neighbors for one-step prediction.*

- **[2026-10-29] Fight World Model: Customizable Combat through Visual Interaction Proxies** — `Core`\
  Executes combat rules in a stateful engine and compiles attempted actions, hit reactions, and health changes into identity-aligned visual proxies, enabling rule edits while reusing the same video renderer.\
  [Paper](https://arxiv.org/abs/2610.40607) · [Project](https://fight-world-model.github.io/) · [Announcement repository](https://github.com/fight-world-model/FWM)\
  *Release note: The official repository provides an overview; inference code and pretrained weights remain on its release roadmap as of November 10, 2026.*

- **[2026-10-29] Wizard: Manipulate Any World in Real Time via Agentic Control** — `Core`\
  Combines generated scene-editing programs with a fixed combat controller that resolves hits, health, and cooldowns, rendering the resulting geometry and character-motion proxies through a video model.\
  [Paper](https://arxiv.org/abs/2610.40339)

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

- **[2026-08-05] PhysMind: From Video to Executable Worlds for Training-Free Physical Reasoning** — `Core`\
  Reconstructs a reusable world from video-derived geometry and trajectories, fits continuous-time analytic dynamics and physical parameters, and executes continuations or interventions to answer physical questions.\
  [Paper](https://arxiv.org/abs/2608.04575) · [Project](https://physmind.github.io/) · [Repository](https://github.com/ccyydd/PhysMind)

- **[2026-07-29] VideoCoCo: Code-as-CoT for Physically-Consistent Video Generation via an Agentic Dual-Engine System** — `Core`\
  Synthesizes Blender programs that specify a scene and its temporal evolution, executes them as visual drafts, and adapts a video editor to render those drafts with richer appearance.\
  [Paper](https://arxiv.org/abs/2607.27380) · [Repository](https://github.com/micky-li-hd/VideoCoCo)

- **[2026-07-07] World-Time Compute with Verified Code World Models** — `Core`  
  Uses verified executable worlds over symbolic states to generate exactly labeled trajectories for model training and studies the limits of cross-world transfer.  
  [Paper](https://arxiv.org/abs/2609.09163) · [Repository](https://github.com/quome-cloud/openworld)  
  *Date note: arXiv reports July 7, 2026 for v1 despite the `2609` identifier; the date above follows the submission history.*

- **[2026-06-23] LLM-ACES: Closed-Loop Discovery of Dynamical Systems with LLM-Guided Adaptive Search** — `Core`\
  Uses language-model operator priors to guide symbolic regression of executable ODEs, then selects new initial conditions through disagreement between candidate rollouts and queries a supplied trajectory oracle.\
  [Paper](https://arxiv.org/abs/2606.25039) · [Repository](https://github.com/scientific-discovery/LLM-ACES)

- **[2026-03-06] Symmetry-Constrained Language-Guided Program Synthesis for Discovering Governing Equations from Noisy and Partial Observations** — `Core`\
  Synthesizes symbolic dynamical laws within a grammar constrained by units and symmetries, fits their constants, and ranks alternative structures using complexity penalties and bootstrap stability under noisy or partial observations.\
  [Paper](https://arxiv.org/abs/2603.06869)

- **[2026-02-23] Pixel2Phys: Distilling Governing Laws from Visual Dynamics** — `Core`\
  Alternates visual variable extraction with symbolic equation discovery, numerically integrating candidate laws and using reconstruction, phase portraits, and extrapolation feedback to revise the representation.\
  [Paper](https://arxiv.org/abs/2602.19516)

## Learning executable dynamics and planning

- **[2026-10-29] Algebraic World Model: From Exploration to Proofs** — `Core`\
  Builds and revises executable Python game hypotheses from interaction, organizes them into typed objects and shared rules, and formalizes the resulting model in Lean to prove model-relative reachability or impossibility.\
  [Paper](https://arxiv.org/abs/2610.40503) · [Project](https://ephemeral6.github.io/awm-site/)

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

- **[2026-07-28] VisualPatchWorld: Code World Models as Latent Structured Representations for Planning** — `Core`\
  Uses active probes to choose a dynamical form from a small domain-specific family, fits its Python template to multi-step transition traces, and plans through the resulting model with optional engine verification.\
  [Paper](https://arxiv.org/abs/2607.25236) · [Repository](https://github.com/HKBU-KnowComp/VisualPatchWorld/)

- **[2026-07-20] Program Synthesis for Simulation-Based Inference: Joint Model Selection and Parameter Estimation** — `Core`\
  Proposes and mutates executable simulator programs, comparing candidate families with neural evidence estimates and inferring their parameters; uncertainty is conditional on the compared pool, and the lensing experiment configures a fixed simulator.\
  [Paper](https://arxiv.org/abs/2607.17540)

- **[2026-07-01] OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration for ARC-AGI-3** — `Core`  
  Couples qualitative object hypotheses and Bayesian effect diagnostics with synthesized Python transition and reward models, using targeted exploration and replay-based repair to revise both abstractions and executable mechanics.  
  [Paper](https://arxiv.org/abs/2607.01531)

- **[2026-06-14] Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games** — `Core`  
  Synthesizes standalone pygame-style world programs from interaction traces and screenshot-derived information, evaluating their multi-step lookahead fidelity.  
  [Paper](https://arxiv.org/abs/2606.16070)

- **[2026-05-29] PatchWorld: Gradient-Free Optimization of Executable World Models for Agent Environments** — `Core`  
  Converts offline text-agent trajectories into Python belief-state programs through counterexample-guided repair and separates observation fidelity from planning utility.  
  [Paper](https://arxiv.org/abs/2605.30880) · [Repository](https://github.com/HKBU-KnowComp/PatchWorld)

- **[2026-05-23] Distilling Game Code World Model Generation into Lightweight Large Language Models** — `Core`\
  Post-trains a small language model to implement game rules, legal actions, transitions, observations, and rewards in Python, using structural and rule-based checks as supervision and reinforcement-learning feedback.\
  [Paper](https://arxiv.org/abs/2605.24375)

- **[2026-05-16] Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models** — `Core` · **Alice**  
  Learns persistent executable transition rules from interaction in a game with misleading rule labels, using failed code revisions to organize preservation counterexamples and guide further exploration.  
  [Paper](https://arxiv.org/abs/2605.16725) · [Repository](https://github.com/ssw03270/BABAinWonderland_NeurIPS-26)

- **[2026-05-06] Executable World Models for ARC-AGI-3 in the Era of Coding Agents** — `Core`\
  Maintains a Python game model through a scripted controller, revises it against recorded observations, prompts simpler abstractions, and executes plans checked through the model.\
  [Paper](https://arxiv.org/abs/2605.05138) · [Repository](https://github.com/astroseger/arc-3-agents-baseline1)

- **[2026-01-31] Learning Abstractions for Hierarchical Planning in Program-Synthesis Agents** — `Core` · **TheoryCoder-2**  
  Learns reusable abstractions from experience and integrates them with hierarchical planning, reducing dependence on manually supplied abstractions.  
  [Paper](https://arxiv.org/abs/2602.00929) · [Author-linked repository](https://github.com/ZerghamAhmed/TheoryCoder)

- **[2026-01-30] Agentic Framework for Epidemiological Modeling** — `Core` · **EpiAgent**\
  Synthesizes compartmental flow graphs from scenario descriptions, compiles verified graphs into differentiable simulator code, and revises structure and parameters through execution checks and trajectory calibration.\
  [Paper](https://arxiv.org/abs/2602.00299)

- **[2025-12-26] Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback** — `Core`\
  Generates PDDL domains and executable simulators through specification research, model development, and adaptive execution tests, then uses the repair trajectories to train world-model generators.\
  [Paper](https://arxiv.org/abs/2512.22336) · [Project](https://agent2world.github.io/) · [Repository](https://github.com/DeepExperience/agent2world)

- **[2025-10-14] One Life to Learn: Inferring Symbolic World Models for Stochastic Environments from Unguided Exploration** — `Core` · **OneLife**  
  Learns conditionally activated probabilistic program laws from limited unguided exploration and evaluates state ranking, fidelity, and planning.  
  [Paper](https://arxiv.org/abs/2510.12088) · [Project](https://onelife-worldmodel.github.io/) · [Repository](https://github.com/codezakh/onelife) · [Crafter-OO](https://github.com/codezakh/crafter_oo)

- **[2025-10-06] Code World Models for General Game Playing** — `Core`\
  Translates game rules and trajectories into Python transition, legal-action, and termination functions, combining the resulting simulator with tree search, value heuristics, and hidden-state inference.\
  [Paper](https://arxiv.org/abs/2510.04542)

- **[2025-08-15] Finite Automata Extraction: Low-data World Model Learning as Programs from Gameplay Video** — `Core` · **FAE**  
  Extracts neuro-symbolic world models from gameplay video as programs in the Retro Coder domain-specific language.  
  [Paper](https://arxiv.org/abs/2508.11836)

- **[2025-05-20] Programmatic Video Prediction Using Large Language Models** — `Core` · **ProgGen**\
  Synthesizes programs for visual state estimation, transition dynamics, and rendering, then fits continuous parameters to predict and edit physical video trajectories in constrained environments.\
  [Paper](https://arxiv.org/abs/2505.14948) · [Repository](https://github.com/metro-smiles/ProgGen)

- **[2025-05-16] PoE-World: Compositional World Modeling with Products of Programmatic Experts** — `Core`  
  Represents stochastic dynamics as a product of LLM-synthesized programmatic experts and uses the resulting model for planning in Atari environments.  
  [Paper](https://arxiv.org/abs/2505.10819) · [Project](https://topwasu.github.io/poe-world) · [Repository](https://github.com/topwasu/poe-world)

- **[2025-05-04] LLM-Guided Probabilistic Program Induction for POMDP Model Estimation** — `Core` · **POMDP Coder**\
  Induces short probabilistic programs for initial states, transitions, observations, and rewards from experience, repairing empirical-coverage failures and planning over beliefs with a supplied state representation.\
  [Paper](https://arxiv.org/abs/2505.02216)

- **[2025-03-26] Synthesizing world models for bilevel planning** — `Core` · **TheoryCoder**  
  Grounds high-level abstractions in a Python transition model synthesized from observations, enabling bilevel planning in grid-world games.  
  [Paper](https://arxiv.org/abs/2503.20124)

- **[2024-09-26] FactorSim: Generative Simulation via Factorized Representation** — `Core`\
  Generates complete simulation code from language using a factored POMDP representation to select relevant state and functions for each construction step, then trains agents in the generated environments.\
  [Paper](https://arxiv.org/abs/2409.17652) · [Project](https://cs.stanford.edu/~sunfanyun/factorsim/) · [Repository](https://github.com/sunfanyunn/FactorSim)

- **[2024-05-24] Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search** — `Core` · **GIF-MCTS / CWMB**  
  Introduces a generate–improve–fix search procedure for Python world models and a benchmark spanning 18 reinforcement-learning environments.  
  [Paper](https://arxiv.org/abs/2405.15383)

- **[2024-02-19] WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment** — `Core`  
  Learns a Python world model from interaction, combining consistency with observed transitions and an optimistic planning constraint.  
  [Paper](https://arxiv.org/abs/2402.12275)

## GUI world models

- **[2026-11-02] WebHarbor: Docking Real Websites for Evolving GUI Agent Environments** — `GUI`\
  Reconstructs task-relevant website interfaces, databases, and persistent workflows through coding agents and human audits, producing resettable local environments for GUI-agent evaluation and training.\
  [Paper](https://arxiv.org/abs/2611.03634) · [Project](https://aiming-lab.github.io/WebHarbor/) · [Repository](https://github.com/aiming-lab/WebHarbor) · [Environments and data](https://huggingface.co/datasets/ChilleD/WebHarbor)

- **[2026-10-27] WebAnything: From the Wild Web to Scalable Agent Environments** — `GUI`\
  Reconstructs local website routes and state transitions from browser-observed evidence, using an independent verifier to guide repairs or additional capture and producing resettable environments within a declared interaction scope.\
  [Paper](https://arxiv.org/abs/2610.37786) · [Repository](https://github.com/china-qijizhifeng/Web-Anything)\
  *Release and scope note: The alpha release includes construction source, selected runnable demos, and a 244-site inventory; the full historical website trees are not bundled, and arbitrary-site automation is not established.*

- **[2026-10-22] Trace2World: Reconstructing App Worlds from Real Interaction Traces for Scalable GUI Agent Training** — `GUI`  
  Reconciles recorded workflows into a shared app-state model, compiles its supported behavior into a browser environment, and repairs implementation errors through independent replay while keeping unsupported transitions non-executable.  
  [Paper](https://arxiv.org/abs/2610.30792)

- **[2026-10-19] Agent World Model in the Wild: Computer-Use Agent Environment Synthesis** — `GUI` · **WildAWM**  
  Synthesizes persistent computer environments spanning GUI, MCP, and command-line interfaces, with execution-based checks for task solvability, difficulty, and verifier reliability before agent training.  
  [Paper](https://arxiv.org/abs/2610.26828) · [Project](https://msr-orchard.github.io/WildAWM/) · [Repository](https://github.com/MSR-Orchard/WildAWM)

- **[2026-08-21] AgentMercury: Your Agent Can Synthesize Verifiable Environments for Business Scenarios at scale** — `GUI`\
  Synthesizes persistent business environments with entities, services, tool interfaces, and cross-service invariants, then instantiates tasks and trajectories for agent training from each executable world.\
  [Paper](https://arxiv.org/abs/2608.20634) · [Project](https://minstar.github.io/AgentMercury/)

- **[2026-08-06] AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents** — `GUI`  
  Predicts reachable next-screen code updates using transition-constrained retrieval, executable HTML, and generated visual assets.  
  [Paper](https://arxiv.org/abs/2608.05891)

- **[2026-02-10] Code2World: A GUI World Model via Renderable Code Generation** — `GUI`  
  Predicts action-conditioned interfaces as HTML, using AndroidCode data and render-aware reinforcement learning to align visual and action consistency.  
  [Paper](https://arxiv.org/abs/2602.09856) · [Project](https://amap-ml.github.io/Code2World/) · [Repository](https://github.com/AMAP-ML/Code2World)

- **[2026-02-02] Generative Visual Code Mobile World Models** — `GUI` · **gWorld**\
  Predicts an action-conditioned mobile screen as renderable web code, training on screenshot-to-code targets and lookahead reasoning traces derived from offline trajectories; introduces MWMBench, while persistent app-state reconstruction remains outside the single-screen formulation.\
  [Paper](https://arxiv.org/abs/2602.01576) · [Project](https://trillionlabs-gworld.github.io/) · [Repository](https://github.com/trillion-labs/gWorld) · [8B model](https://huggingface.co/trillionlabs/gWorld-8B) · [32B model](https://huggingface.co/trillionlabs/gWorld-32B) · [Benchmark](https://huggingface.co/datasets/trillionlabs/MWMBench)

## Executable scene and 4D world construction

These papers construct executable environments; their goals differ from identifying unknown transition dynamics through interaction.

- **[2026-11-12] BWM-Forge: Agentic World Programming for Embodied Intelligence** — `Construction`\
  Builds editable Blender scene, robot-motion, and camera programs from multimodal task inputs, revising them through review and reusable experience before sending proxy videos to an appearance generator.\
  [Paper](https://arxiv.org/abs/2611.16221) · [Project](https://bwm-forge.github.io/) · [Repository](https://github.com/Lcixs/BWM-Forge)\
  *Release and scope note: Pipeline and local interface source are available; the documented Windows-oriented setup requires Blender, robot assets, and external model services. This constructs controlled robot videos rather than discovering general transition laws.*

- **[2026-11-09] HolidayFactory 1.0: Simulating, Generating, and Evaluating Industrial Robot Tasks** — `Construction`\
  Generates simulation assets, scene variants, and typed workplace process logic, then compiles human-confirmed evaluation specifications into executable checks; introduces persistent-job evaluation in 24/7-Bench.\
  [Paper](https://arxiv.org/abs/2611.11789)\
  *Scope and release note: The paper does not yet establish end-to-end generation of all seven benchmark worlds or policy comparisons over persistent runs; no official implementation destination was verified.*

- **[2026-11-07] Agentic discrete-event simulation for manufacturing system design: an open 3D simulator, a benchmark and an industrial case** — `Construction` · **SimuLean**\
  Lets agents assemble manufacturing processes through domain commands over a shared discrete-event engine, executing the resulting models in Unity or headlessly and checking their outputs against independent references; the engine supplies the simulation semantics.\
  [Paper](https://arxiv.org/abs/2611.10602) · [Repository](https://github.com/simulean/SimuLean)

- **[2026-10-29] DyCraft: An Agentic System for Long-Horizon 4D Scene Generation** — `Construction`\
  Builds editable Blender worlds through verified 3D storyboards, then authors local motions between key states using kinematics and simulation, checking physical constraints across long animations.\
  [Paper](https://arxiv.org/abs/2610.40754) · [Project](https://dy-craft.github.io/) · [Repository](https://github.com/jefftan969/dycraft) · [Films and assets](https://huggingface.co/datasets/jefftan969/dycraft-films)\
  *Release note: Source, installation documentation, and benchmark films are available as of November 11, 2026; generation requires Blender, external assets, and an authenticated coding-agent backend. The pipeline was not run during curation.*

- **[2026-10-29] RFW-A: Agentic Procedural Generation of 400K Articulated Assets over 500 Categories** — `Construction`\
  Builds reusable category-level programs from articulated assets, validates sampled configurations and motion states, and executes the generators to produce simulation-ready variants with explicit joints and physical attributes.\
  [Paper](https://arxiv.org/abs/2610.40333) · [Project](https://brain-labbb.github.io/RFW_A_web/)

- **[2026-10-28] Cinematize from Unreal: Agentic Choreography for Controllable World Simulation** — `Construction` · **CineU**\
  Writes and verifies Unreal Engine operations over persistent scene and timeline state, coordinating asset placement, entity motion, and camera choreography with localized repair of failed edits.\
  [Paper](https://arxiv.org/abs/2610.38468)

- **[2026-10-26] SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments** — `Construction`\
  Coordinates reconstruction tools and simulator inspection to turn captures or dynamic videos into interactive scenes, adding articulation, approximate physical properties, scene variants, and scripted demonstrations.\
  [Paper](https://arxiv.org/abs/2610.34745)

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

- **[2026-10-02] RoboChemGym: A Protocol-Driven Generative Simulation Framework for Long-Horizon Chemical Manipulation** — `Construction`\
  Instantiates laboratory scenes and executable manipulation sequences from protocols, refining asset placement and controller parameters through simulation feedback to generate demonstrations; physical laws and action primitives come from existing components.\
  [Paper](https://arxiv.org/abs/2610.02708)

- **[2026-09-29] Real2Gym: Building Gyms from Videos, Bringing Skills to Robots** — `Construction`  
  Reconstructs Blender and MuJoCo environments from human or robot demonstrations, validates interactions and scene variations through native physics, and uses the resulting gyms for feedback-driven manipulation skill development.  
  [Paper](https://arxiv.org/abs/2609.37089) · [Project](https://real2gym.github.io/) · [Real2Sim repository](https://github.com/real2gym/Real2Gym) · [Agent repository](https://github.com/real2gym/R2G_Agent)  
  *Release note: the agent repository provides continuous stage-code execution, not the paper's persistent experience library; scene assets and external perception/model services are required.*

- **[2026-09-29] Text2Sim: Agentic Physics-Based Simulation Generation with Distilled Expertise** — `Construction`\
  Converts text into editable Genesis simulation programs through specialized writers and a critic, using distilled simulation guidance and execution evidence to repair assets, dynamics, and controls.\
  [Paper](https://arxiv.org/abs/2609.36593)

- **[2026-09-28] VideoPhysEdit: Physical Counterfactual Video Editing via Rigid-Body Physical Scene Reconstruction** — `Construction`\
  Fits an executable PyBullet scene to observed rigid-body motion, applies object or physical-parameter interventions, and uses the simulated consequences to guide video editing; introduces PCVE-RigidBench and retains the engine's supplied dynamics.\
  [Paper](https://arxiv.org/abs/2609.35134) · [Project](https://videophysedit.github.io/) · [Announcement repository](https://github.com/Hammour-steak/VideoPhysEdit) · [Benchmark code](https://github.com/Hammour-steak/PCVE-RigidBench) · [Benchmark data](https://huggingface.co/datasets/ccmoony/PCVE-RigidBench)\
  *Release note: The method implementation remains marked coming soon as of November 12, 2026; benchmark construction/evaluation source and data are available separately.*

- **[2026-09-27] WorldAgent: Verification-Guided Agentic Physical World Construction** — `Construction`\
  Expands text into entity contracts, scene relations, and causal event requirements, then constructs and simulates the world while geometry and state checks guide specification repair and re-execution.\
  [Paper](https://arxiv.org/abs/2609.33208)

- **[2026-09-10] Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs** — `Construction` · **RCWM**  
  Reconstructs a complex 3D scene from a reference image through recursive scene programs and nested render–compare–edit loops.  
  [Paper](https://arxiv.org/abs/2609.11499)

- **[2026-08-18] aDSL: Agentic 3D Creation via Joint Agent-Program Design** — `Construction`\
  Generates Python-embedded scene and asset programs with named part hierarchies, spatial constraints, and explicit joint axes and limits, repairing them through execution and exporting articulated models to URDF.\
  [Paper](https://arxiv.org/abs/2608.17975) · [Project](https://dylanwrh.github.io/aDSL/) · [Repository](https://github.com/sig-pku/aDSL)

- **[2026-07-23] GS-Agent: Creating 4D Physical Worlds With Generative Simulation** — `Construction`\
  Coordinates specialist agents that write physics-engine code for assets, materials, placement, motion, and rendering, refining interacting rigid, deformable, and fluid worlds through multimodal feedback.\
  [Paper](https://arxiv.org/abs/2607.21522) · [Project](https://umass-embodied-agi.github.io/gs-agent/)

- **[2026-07-02] SimWorlds: A Multi-Agent System for Dynamic 3D Scene Creation** — `Construction`\
  Generates editable dynamic Blender scenes through staged planning, coding, and review, using a deterministic scene protocol and runtime inspection to detect motion and mechanism failures; introduces 4DBuildBench.\
  [Paper](https://arxiv.org/abs/2607.01766) · [Project](https://dynsimworlds.github.io/)

- **[2026-05-19] SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects** — `Construction`\
  Compiles room layouts and object requests into part-wise Blender programs, repairs them through execution, and exports articulated simulation assets linked by a persistent scene-state registry.\
  [Paper](https://arxiv.org/abs/2605.19587) · [Project](https://scene-code.github.io/) · [Repository](https://github.com/wangpuyi/SceneCode)

- **[2026-05-14] ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction** — `Construction`\
  Turns user-reviewed plans into PyChrono programs specifying bodies, constraints, controllers, and sensors, then repairs them using rendered rollouts and trajectory-based physics checks within the supplied engine.\
  [Paper](https://arxiv.org/abs/2605.14398) · [Project](https://uwsbel.github.io/chrono-agentic-website/)

- **[2026-05-10] SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning** — `Construction`\
  Uses an evolving coding agent to create and repair Unreal environments through compilation, physics, and visual feedback, exporting Gym-style tasks and adapting the generated curriculum to learner performance.\
  [Paper](https://arxiv.org/abs/2605.09423)

- **[2026-02-12] Code2Worlds: Empowering Coding LLMs for 4D World Generation** — `Construction`  
  Generates simulation code with separate object and environment construction, then refines dynamics through physics-aware visual feedback; includes Code4D evaluation.  
  [Paper](https://arxiv.org/abs/2602.11757) · [Project](https://aigeeksgroup.github.io/Code2Worlds/) · [Repository](https://github.com/AIGeeksGroup/Code2Worlds)

- **[2023-12-14] Holodeck: Language Guided Generation of 3D Embodied AI Environments** — `Construction`\
  Converts language prompts into room layouts, asset selections, and spatial constraints, then builds executable AI2-THOR environments for navigation using supplied collision and interaction semantics.\
  [Paper](https://arxiv.org/abs/2312.09067) · [Project](https://yueyang1996.github.io/holodeck/) · [Repository](https://github.com/allenai/Holodeck)

- **[2023-11-02] RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation** — `Construction`\
  Proposes robot tasks, generates simulator scene configurations with assets and articulated states, and writes training supervision for skill learning in existing physics engines; the generated environment differs from a learned transition law.\
  [Paper](https://arxiv.org/abs/2311.01455) · [Project](https://robogen-ai.github.io/) · [Repository](https://github.com/Genesis-Embodied-AI/RoboGen)\
  *Release note: The official repository documents a PyBullet implementation for rigid manipulation and locomotion; the full soft-body pipeline described in the paper is not included in that release.*

**Naming caution:** *Code2World* is the GUI paper; *Code2Worlds* is the 4D generation paper. *WorldCoder-Bench* below is a separate paper from the 2024 *WorldCoder* agent.

## Related symbolic and neurosymbolic planning

These works are included for their explicit transition representations and verification or planning interfaces, not because all of them synthesize general-purpose simulators.

- **[2026-11-11] BiPOP: Partial-Order Planning for Long-Horizon Bimanual Robotic Manipulation** — `Related`\
  Grounds instructions and scene objects in a supplied temporal PDDL model of reachability, shared workspace, and arm coordination, delegating action applicability and concurrent scheduling to a symbolic planner.\
  [Paper](https://arxiv.org/abs/2611.15317) · [Placeholder repository](https://github.com/Kchu/BiPOP)\
  *Release and scope note: The author-linked repository contains only a short README as of November 14, 2026; an implementation release was not verified. The shared action domain is supplied rather than learned.*

- **[2026-11-08] Spatial Harness: Grounding Spatial Reasoning in Executable World States with Physics Engines** — `Related`\
  Estimates a shared object-and-camera layout from images and language, instantiates proxies in MuJoCo, and answers spatial questions through executable viewpoint changes, measurements, and rendered feedback; the scene itself remains static.\
  [Paper](https://arxiv.org/abs/2611.11344) · [Placeholder repository](https://github.com/tmlr-group/Spatial-Harness)\
  *Release note: The author-linked repository contains an overview and promises a later release; implementation source was not available on November 11, 2026, despite the abstract's code-availability statement.*

- **[2026-11-02] Creating Hybrid Interactive Narrative Systems with LLM: From Formal Description to Evaluation** — `Related`\
  Runs interchangeable narrative managers over shared symbolic facts, action preconditions, effects, and goals, enforcing operation applicability and comparing the resulting state-transition traces.\
  [Paper](https://arxiv.org/abs/2611.02807)

- **[2026-10-31] WorldSketch: Sketching World Models for Zero-Shot Mobile Manipulation** — `Related`\
  Constructs task-focused kinematic models from perception queries, represents uncertain joint mechanisms as hypotheses, and updates them through execution feedback while a geometric planner computes contact and robot motion.\
  [Paper](https://arxiv.org/abs/2611.00513)

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

- **[2026-09-22] Neurosymbolic Action Model Learning under Partial Observability** — `Related` · **NeSyAM**\
  Learns visual state grounding and probabilistic action preconditions and effects from incomplete observation sequences, enforcing Boolean STRIPS semantics when computing symbolic successor states.\
  [Paper](https://arxiv.org/abs/2609.25766)

- **[2026-09-16] GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning** — `Related`  
  Uses a graph model of relations, action conditions/effects, and uncertain object locations to verify, repair, and reorder long-horizon plans.  
  [Paper](https://arxiv.org/abs/2609.19315)

- **[2026-08-31] Learning Action Models with Conditional and Quantified Effects via Uncertainty-Guided Exploration** — `Related` · **OHCAM**\
  Maintains competing symbolic action models with conditional and quantified effects, selects interactions that distinguish their predictions, and expands hypotheses when noisy execution evidence no longer supports simpler rules.\
  [Paper](https://arxiv.org/abs/2608.30955)

- **[2026-08-18] LLM-Only PDDL Domain Repair with Open-Weight Models** — `Related`\
  Evaluates LLM edits to corrupted PDDL action preconditions and effects, comparing domain-only prompts with positive and negative execution traces while measuring both structural recovery and satisfaction of behavioral constraints.\
  [Paper](https://arxiv.org/abs/2608.17341)

- **[2026-08-17] PDDL-ART: Autonomous Symbolic Abstraction From Demonstration For Long-Horizon Robotic Manipulation Using Vision-Language Models** — `Related`\
  Infers PDDL domains and problems from a demonstration, task description, and action names, then repairs them through syntax, planning, and robot-execution checks supported by visual and geometric predicate grounding.\
  [Paper](https://arxiv.org/abs/2608.17146)

- **[2026-08-17] PDDLCoder: Agentic PDDL Generation for LLM-Assisted Symbolic Planning** — `Related`\
  Generates and revises PDDL domains and problems through parser, planner, and semantic feedback, then evaluates mapped plans in held-out executable environments; introduces NL-pddlgym without claiming equivalence to the reference domains.\
  [Paper](https://arxiv.org/abs/2608.16637) · [Repository](https://github.com/vDawgg/PDDLCoder)

- **[2026-07-03] Object-Centric Environment Modeling for Agentic Tasks** — `Related` · **OCM**\
  Accumulates Python object classes encoding environment constraints and mechanisms, requires reusable procedures to execute against that model, and reveals relevant source progressively during later agent decisions.\
  [Paper](https://arxiv.org/abs/2607.02846)

- **[2026-06-14] PO-PDDL: Learning Symbolic POMDPs from Visual Demonstrations for Robot Planning Under Uncertainty** — `Related`\
  Reconstructs symbolic trajectories from robot demonstrations, learns stochastic action effects and observation rules, and compiles reusable PO-PDDL domains for online belief-space planning under execution and perception uncertainty.\
  [Paper](https://arxiv.org/abs/2606.15654) · [Project](https://roboticsjtu.github.io/PO-PDDL/) · [Repository](https://github.com/RoboticSJTU/PO_PDDL)

- **[2026-05-15] SWoMo: Neuro-Symbolic World Model for Cataract Surgery Simulation** — `Related`\
  Uses a rule-based Godot simulator to advance explicit tool and anatomical configurations, then conditions video synthesis on simulated frames and scene graphs; tissue appearance and deformation remain learned visual outputs.\
  [Paper](https://arxiv.org/abs/2605.16530) · [Project](https://ssharvienkumar.github.io/SWoMo/) · [Repository](https://github.com/MECLabTUDA/SWoMo) · [Models and processed data](https://huggingface.co/SsharvienKumar/SWoMo)\
  *Release note: Training and inference source for video synthesis are available; a complete Godot simulator release was not verified on November 13, 2026.*

- **[2025-09-30] ExoPredicator: Learning Abstract Models of Dynamic Worlds for Robot Planning** — `Related`\
  Learns Python state predicates and symbolic causal processes with stochastic delays, combining Bayesian inference and language-model proposals to plan around both robot actions and autonomous mechanisms such as heating or falling dominoes.\
  [Paper](https://arxiv.org/abs/2509.26255) · [Repository](https://github.com/BasisResearch/predicators)

- **[2025-04-22] WALL-E 2.0: World Alignment by NeuroSymbolic Learning improves World Model-based LLM Agents** — `Related`  
  Extracts symbolic environment knowledge from exploration and encodes it as executable rules to align an LLM world model for model-predictive control.  
  [Paper](https://arxiv.org/abs/2504.15785) · [Repository](https://github.com/elated-sawyer/WALL-E)

- **[2025-02-07] Generating Symbolic World Models via Test-time Scaling of Large Language Models** — `Related`  
  Combines candidate sampling with iterative refinement to generate PDDL domains usable by classical planners.  
  [Paper](https://arxiv.org/abs/2502.04728) · [Project](https://vmlpddl.github.io/) · [Repository](https://github.com/VMLPDDL/VML_PDDL)

- **[2024-10-30] VisualPredicator: Learning Abstract World Models with Neuro-Symbolic Predicates for Robot Planning** — `Related`\
  Invents Python predicates that combine visual queries with logical computation, learns action preconditions and effects from successful and failed interactions, and uses the resulting abstract transition model for robot planning with supplied motor skills.\
  [Paper](https://arxiv.org/abs/2410.23156) · [Repository](https://github.com/BasisResearch/predicators)

- **[2023-01-16] Neuro-Symbolic World Models for Adapting to Open World Novelty** — `Related` · **WorldCloner**\
  Learns condition–effect rules over observed state features, revises their applicability regions when environment mechanics change, and simulates transitions through the updated rules to adapt a neural policy with fewer real interactions.\
  [Paper](https://arxiv.org/abs/2301.06294)

- **[2019-12-30] World Programs for Model-Based Learning and Planning in Compositional State and Action Spaces** — `Related`\
  Formulates world-program induction from graph-state transitions, learning graph-rewrite actions and transition feasibility for model-based search, with chemical synthesis planning as the worked application.\
  [Paper](https://arxiv.org/abs/1912.13007)

## Benchmarks and evaluation

- **[2026-11-12] WorldDraft: If Code Builds the World, Can Video Models Just Render It?** — `Benchmark`\
  Tests generative renderers on 432 paired drafts from 48 executable 4D worlds, varying geometric detail and appearance cues while holding dynamics fixed to measure world preservation and target-appearance realization.\
  [Paper](https://arxiv.org/abs/2611.16217) · [Project](https://haroldchen19.github.io/WorldDraft-site/) · [Repository](https://github.com/KevinHuge/WorldDraft) · [Dataset](https://huggingface.co/datasets/KevinHuge/WorldDraft)\
  *Release and scope note: Evaluation source, drafts, ground truth, and optional Blender scenes are available; full evaluation requires external model weights and GPU resources. WorldDraft-Primer is a component of this paper, not a separate entry.*

- **[2026-11-11] VibePrevisBench: Evaluating Agentic Coding for 4D Scene Generation in Blender** — `Benchmark`\
  Evaluates 242 brief-to-Blender tasks by replaying delivered programs, checking exported scene states against hidden facts, and assessing whether correctly constructed events remain recognizable in rendered proxy videos.\
  [Paper](https://arxiv.org/abs/2611.15789) · [Project](https://vibeprevisbench.github.io/) · [Repository](https://github.com/vibeprevisbench/vibeprevisbench) · [Dataset](https://huggingface.co/datasets/AidanYuzhe/vibeprevisbench)\
  *Release and scope note: Evaluation source and annotations are available; third-party input media must be retrieved separately, with some requiring authorized dataset access. The release and paper protocols differ for photo tasks.*

- **[2026-11-10] Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning** — `Benchmark`\
  Evaluates generated multi-agent stochastic worlds encoded as explicit JSON transitions or executable Python, separating mechanical validity, reference-relative structure, and automated semantic diagnostics across 44 scenarios; successful execution alone does not establish fidelity to the intended situation.\
  [Paper](https://arxiv.org/abs/2611.14419) · [Repository](https://github.com/GaganaMD/world-model-suite/)

- **[2026-11-06] Frontier3DBench: Benchmarking Coding Agents for 3D Creation across Objects, Scenes, and Interactive Open Worlds** — `Benchmark`\
  Evaluates code-authored objects, scenes, and interactive worlds, with the world tasks checking traversal, local mechanisms, and persistent multi-step workflows alongside appearance and structural fidelity.\
  [Paper](https://arxiv.org/abs/2611.09017)

- **[2026-11-05] Interactive Visual Gym: Evaluating Visual Interaction Models with Simulated Users in Interactive Worlds** — `Benchmark` · **IVG-Bench**\
  Evaluates visual assistants with simulated users acting in executable cooking, household, and phone environments, deriving task progress and reference facts from scene state and recorded transitions.\
  [Paper](https://arxiv.org/abs/2611.08286) · [Project](https://interactive-visual-gym.salesforceairesearch.com/) · [Repository](https://github.com/SalesforceAIResearch/Interactive-Visual-Gym)

- **[2026-10-19] From Code to Playable Systems: CEGame-Bench for Long-Horizon Game Creation Agents** — `Benchmark` · **CEGame-Bench**  
  Evaluates complete-game creation across five production engines using hidden play-based contracts for gameplay, completion, and saved-world restoration, distinguishing build success from executable game behavior.  
  [Paper](https://arxiv.org/abs/2610.26098)

- **[2026-10-17] Beyond Next-Screen Prediction: The Decision Value of GUI World Models** — `Benchmark`\
  Tests the action-selection value of Code2World next-screen predictions by holding candidates fixed and comparing prompted lookahead with matched direct and prediction-augmented evaluators; the conclusions concern one-step GUI decisions.\
  [Paper](https://arxiv.org/abs/2610.24372)

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

- **[2026-10-02] Ego2World: Compiling Egocentric Cooking Videos into Executable Worlds for Belief-State Planning** — `Benchmark`\
  Compiles annotated cooking activities into executable symbolic worlds with separate hidden state and agent belief, tracing action validity, goal attainment, and information reuse across continuing tasks.\
  [Paper](https://arxiv.org/abs/2610.02715)\
  *Version note: this replaces the withdrawn May 13 submission under arXiv:2605.13335; October 2 is the replacement record's v1 date, not a newly counted paper.*

- **[2026-10-01] World Editing: Intervening on Executable Worlds at Increasing Depth** — `Benchmark` · **IGMWorld / IGMBench**  
  Evaluates coding agents that modify properties, entities, dynamics, and systems in existing executable games, checking requested behavior and preservation of unaffected properties at runtime.  
  [Paper](https://arxiv.org/abs/2610.02331) · [Project](https://vinesmsuic.github.io/IGMWorld/) · [Repository](https://github.com/vinesmsuic/IGMWorld/)  
  *Release note: the repository still announces a forthcoming code release as of October 28, 2026.*

- **[2026-10-01] PROWBench: Do Video Models Render What the Program Specifies?** — `Benchmark`  
  Tests whether generated videos realize program-specified states and interactions, comparing rendered observations with replayable world records and timestamped events.  
  [Paper](https://arxiv.org/abs/2610.02205) · [Project](https://alaya-lab.github.io/PROWBench/) · [Repository](https://github.com/AlayaLab/PROWBench) · [Dataset](https://huggingface.co/datasets/AlayaLab/PROWBench)  
  *Release note: engine recordings, example representations, and evaluation code are available; the world-generation pipeline remains on the release roadmap. Resource status was rechecked October 28, 2026; evaluations were not run.*

- **[2026-09-28] GPUPhysBench: Benchmarking Coding Agents for Correct and Efficient GPU Physics Simulation** — `Benchmark`\
  Tests generated CUDA implementations of physical simulation operators and complete simulators, checking numerical correctness and runtime under specified governing equations and fixed execution budgets.\
  [Paper](https://arxiv.org/abs/2609.35639)

- **[2026-09-26] World Agent: Can Language Models Keep a World Running?** — `Benchmark`  
  Evaluates sustained maintenance of explicit world states and action-conditioned deduction through executable world interfaces, event contracts, and deterministic reference dynamics; it does not evaluate generated simulator code.  
  [Paper](https://arxiv.org/abs/2609.32692) · [Repository](https://github.com/HCPLab-SYSU/WorldAgent-Benchmark)  
  *Release note: benchmark cases and evaluation scripts are available; playback, rendering, and the playable demo remain on the release roadmap. Resource status was rechecked October 28, 2026; evaluations were not run.*

- **[2026-09-14] BVB: Benchmarking Agentic Video Understanding via Programmatic Reconstruction in Blender** — `Benchmark`  
  Evaluates agents that reconstruct videos as executable animated Blender scenes, measuring retained spatiotemporal facts and perceptual similarity under a shared execution budget.  
  [Paper](https://arxiv.org/abs/2609.15478) · [Project](https://yoloytang.me/BVB/) · [Repository](https://github.com/yunlong10/BVB)

- **[2026-08-28] An Enclosed Mode Is a Gauge Choice: Topology Relative to Reach in Certified Code World Models** — `Benchmark`\
  Studies when unreachable regions make errors in synthesized dynamics untestable yet harmless, using controlled ring environments to separate sampling coverage, planner reachability, model repair, and the consequences of incorrect geometry.\
  [Paper](https://arxiv.org/abs/2608.28541) · [Repository](https://github.com/JaviMaligno/code-world-models)

- **[2026-08-18] An Omitted Mode Is a Rare Rule: The Sampling-Verification Danger Law in Continuous Code World Models** — `Benchmark`\
  Tests how sampled transition checks miss rare mode changes in continuous executable models, separating acceptance probability from planning regret and examining when additional evidence can repair missing rules.\
  [Paper](https://arxiv.org/abs/2608.17956) · [Repository](https://github.com/JaviMaligno/code-world-models)

- **[2026-08-11] ChemWorld: Programmable Chemical Worlds for Controlled and Replayable Agent Experimentation** — `Benchmark`\
  Compiles reusable chemical process and observation components into executable experimental worlds, separating public agent interfaces from private laws and supporting transactional replay and controlled rule interventions.\
  [Paper](https://arxiv.org/abs/2608.10792) · [Repository](https://github.com/sunyrain/ChemWorld-Public)

- **[2026-07-16] Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?** — `Benchmark`\
  Compares textual and executable game-model agents with separate simplification and replay-verification treatments, measuring public-game performance and resource use without claiming held-out generalization.\
  [Paper](https://arxiv.org/abs/2607.15439) · [Author-linked repository](https://github.com/astroseger/arc-3-agents-baseline1)

- **[2026-07-15] When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models** — `Benchmark`\
  Studies executable game models that pass sampled prediction checks yet mislead search, analyzing rare transition errors and hidden-state inference failures against their consequences for actual play.\
  [Paper](https://arxiv.org/abs/2607.14169) · [Repository](https://github.com/JaviMaligno/code-world-models)

- **[2026-06-30] ScratchWorld: Evaluating If World Models Compute Executable Consequences** — `Benchmark`\
  Uses replayable Scratch worlds to evaluate action-conditioned state changes, hidden state, causal traces, and counterfactuals, scoring correctly computed changes separately from unchanged-state copying.\
  [Paper](https://arxiv.org/abs/2606.31689)

- **[2026-06-12] SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model** — `Benchmark`\
  Executes household plans against curated action and object rules, tracking both immediate precondition violations and delayed, potentially irreversible failures; evaluates counterfactual state reasoning against the supplied kitchen model.\
  [Paper](https://arxiv.org/abs/2606.14574) · [Repository](https://github.com/psunlpgroup/SIMMER)

- **[2026-06-01] WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis** — `Benchmark`  
  Evaluates generated interactive 3D programs using StateProbe runtime-state and transition contracts, beyond screenshots or DOM inspection alone.  
  [Paper](https://arxiv.org/abs/2606.01869) · [Author-linked anonymous resource](https://anonymous.4open.science/r/WorldCoder-Bench/)

- **[2026-06-01] MPMWorlds: Material-Point-Method Simulations for Inferring and Extrapolating Physical Dynamics** — `Benchmark`\
  Compares executable MPM simulation synthesis with video continuation on deformable and fluid dynamics, varying available scene information to separate parameter recovery from long-horizon physical extrapolation.\
  [Paper](https://arxiv.org/abs/2606.01538) · [Project](https://zzigak.github.io/mpmworlds/)\
  *Release note: The project page marks the dataset as coming soon; a public dataset release was not verified on November 10, 2026.*

- **[2026-04-26] PhysCodeBench: Benchmarking Physics-Aware Symbolic Simulation of 3D Scenes via Self-Corrective Multi-Agent Refinement** — `Benchmark`\
  Tests text-to-simulation programs across rigid, soft-body, fluid, and mechanical scenarios, measuring execution and rendered fidelity alongside engine-state assertions and conservation diagnostics; a cross-engine subset separates physical reasoning from API familiarity.\
  [Paper](https://arxiv.org/abs/2604.23580)

- **[2026-02-09] VisPhyWorld: Probing Physical Reasoning via Code-Driven Video Reconstruction** — `Benchmark`\
  Requires models to reconstruct observed physical scenes as executable simulation programs, then evaluates rendered appearance and motion across physics and graphics backends; VisPhyBench exposes inferred mechanisms rather than relying only on verbal answers.\
  [Paper](https://arxiv.org/abs/2602.13294) · [Project](https://tiger-ai-lab.github.io/VisPhyWorld/) · [Repository](https://github.com/TIGER-AI-Lab/VisPhyWorld)

- **[2025-02-18] Text2World: Benchmarking Large Language Models for Symbolic World Model Generation** — `Benchmark`  
  Evaluates text-to-PDDL world-model generation across diverse domains with multiple execution-based criteria.  
  [Paper](https://arxiv.org/abs/2502.13092) · [Project](https://text-to-world.github.io/) · [Repository](https://github.com/Aaron617/text2world)

Also see **CWMB** in the GIF-MCTS paper, **CombatStateBench** in Programmable World Model, and **Code4D** in Code2Worlds. These are not counted as additional papers.

## Adjacent renderers, perspectives, and data engines

- **[2026-11-11] CoCode-World: Shared 3D Proxy Representation for Multi-Player World Models** — `Perspective`\
  Jointly renders two player views from a shared geometric proxy and appearance references, adapting a video model to coordinate cross-view identity while game-engine state supplies layout, motion, and occlusion.\
  [Paper](https://arxiv.org/abs/2611.15602) · [Project](https://iapple233.github.io/CCW/) · [Repository](https://github.com/IApple233/CoCode-World)\
  *Release and scope note: This is the paper associated with the separately tracked CoCode-World release above; new-action dynamics remain outside the renderer.*

- **[2026-11-09] PhysOPSD: Code as Privilege for Physically Plausible Video Generation** — `Perspective`\
  Constructs verified simulation programs and paired physical variations to supervise on-policy video-model self-distillation, transferring draft-conditioned physical guidance into a generator that runs without the simulator at inference.\
  [Paper](https://arxiv.org/abs/2611.12411) · [Project](https://haroldchen19.github.io/PhysOPSD-site/) · [Announcement repository](https://github.com/aigc3d/PhysOPSD)\
  *Release and scope note: The repository provides paper resources; training and inference code are pending approval, and pretrained weights are not included as of November 14, 2026.*

- **[2026-11-02] Isekai3D SDG: A Platform for Diverse Synthetic Gameplay Visual Data** — `Perspective`\
  Records configurable Unreal gameplay state, actions, and camera paths, then replays the same simulation under varied rendering and capture settings to produce aligned training data; coding assistants can configure and inspect generation runs.\
  [Paper](https://arxiv.org/abs/2611.03626) · [Organization page](https://research.nvidia.com/publication/2026-10_isekai3d-sdg-platform-diverse-synthetic-gameplay-visual-data)

- **[2026-10-29] Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement** — `Perspective`\
  Surveys agent runtimes around video generation, including hybrid designs where engines or written programs maintain world state, and distinguishes output revision from changes to models and improvement procedures.\
  [Paper](https://arxiv.org/abs/2610.40191) · [Project](https://agentic-videogen.github.io/)

- **[2026-10-23] Tempo-Zero: Recursive Self-Play in Executable Worlds for Video Reasoning** — `Perspective`  
  Uses executable event worlds to generate videos with exact answers and evidence intervals, training a shared questioner–solver policy whose validated rule changes alter later self-play environments.  
  [Paper](https://arxiv.org/abs/2610.32433) · [Project](https://alchemist-jo.github.io/tempo-zero/)

- **[2026-10-22] AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark** — `Perspective`\
  Adapts a video renderer to coarse recordings from agent-built games and engines, evaluating entity identity, count, position, and timing while leaving gameplay state and rules in upstream programs.\
  [Paper](https://arxiv.org/abs/2610.31466) · [Project](https://alaya-lab.github.io/AnyGameRenderer) · [Repository](https://github.com/AlayaLab/AnyGameRenderer)

- **[2026-10-20] SolarRenderer: Few-Step Generative Reference Rendering** — `Perspective`  
  Adapts a frozen video backbone with control and acceleration LoRAs to render structural videos from engines or agents, including a causal streaming variant; world-state evolution remains upstream.  
  [Paper](https://arxiv.org/abs/2610.28630) · [Repository](https://github.com/Enderfga/SolarRenderer) · [Models](https://huggingface.co/Enderfga/SolarRenderer)

- **[2026-08-31] WebWorld: The Browser as a World Model for Self-Improving Web Code** — `Perspective`  
  Treats the browser as an existing executable simulator and admits code-improvement supervision through behavior-verifying interaction contracts. It does not learn the browser's dynamics.  
  [Paper](https://arxiv.org/abs/2608.30530)

- **[2026-08-26] Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models** — `Perspective`  
  Proposes human–engine verification as a source of grounded feedback and trajectory data for world-model training, rather than introducing another learned transition model.  
  [Paper](https://arxiv.org/abs/2608.25518)

- **[2026-07-30] Video Models as Native 4D Renderers: World-Grounded Conditioning from Animated Mesh** — `Perspective` · **DAR**\
  Conditions a video renderer on persistent surface identities, world positions, normals, and camera rays from animated meshes, using programmatically assembled Blender and Unreal scenes; the upstream scene specifies motion rather than the renderer learning executable transition rules.\
  [Paper](https://arxiv.org/abs/2608.00094)

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
