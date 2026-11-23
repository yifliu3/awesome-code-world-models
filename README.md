<div align="center">

# Awesome Code World Models

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/yifliu3/awesome-code-world-models?style=social)](https://github.com/yifliu3/awesome-code-world-models/stargazers)
[![License: CC0](https://img.shields.io/badge/License-CC0%201.0-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**A curated collection of code world models: executable dynamics, programmatic simulation, and coding agents that build and reason about worlds.**

代码世界模型论文与资源精选：可执行动力学、程序化仿真，以及通过编程构建和理解世界的智能体。

</div>

**264 papers** and **10 project releases**.

**Last literature search: November 23, 2026.** This is a curated snapshot, not an exhaustive survey or an automatically maintained feed.

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
| **Mundo: Customized World Model** | Yihang Luo and collaborators | 2026-11-19 | [Project](https://mundo-world-model.github.io/) · [Author article](https://huggingface.co/blog/Luo-Yihang/mundo-world-model) · [Announcement repository](https://github.com/Luo-Yihang/Mundo) | Project demonstrations and method description are available; the repository contains an overview and visual assets. Code and weights are announced for the end of November but remain pending. No arXiv paper verified. |
| **Code World Model 2.0 / Invoker-Render** | Inclusion AI, Westlake University, and Zhejiang University | 2026-11-19 | [Project](https://www.inclusion-ai.org/CodeWorldModel/) · [Repository](https://github.com/inclusionAI/CodeWorldModel) · [Deployment guide](https://github.com/inclusionAI/CodeWorldModel/blob/master/docs/INFERENCE.md) · [Models](https://huggingface.co/inclusionAI/invoker-render-1.0) | Streaming inference source, session service, file/browser clients, causal model shards, and bidirectional-teacher LoRA are available. The default deployment uses eight GPUs and requires separate encoder/decoder assets; a complete deployment was not reproduced. The associated paper is now listed under adjacent renderers; training code and data remain pending. |
| **CoCode-World** | IApple233 | 2026-11-14 | [Project](https://iapple233.github.io/CCW/) · [Repository](https://github.com/IApple233/CoCode-World) · [Model](https://huggingface.co/iapple1/CoCode-World-Model) · [Dataset](https://huggingface.co/datasets/iapple1/CoCode-World-Data) | Training/inference source, LoRA weights, a selected paired-video dataset, and proxy-rendering resources are available. Requires external MiniMax-H3 weights; documented generation uses eight GPUs. Recorded world state supports rerendering, not arbitrary new-action simulation; the associated paper is now listed under adjacent renderers. |
| **HolonEngine** | Jonathan Dunlap | 2026-11-12 | [Repository](https://github.com/jadbox/HolonEngine) · [Architecture](https://github.com/jadbox/HolonEngine/blob/main/docs/holon_whitepaper.md) | Experimental pre-alpha Rust compiler and 2D runtime source are available, with build instructions and video examples; requires FFmpeg. The inspected rollout uses built-in dynamics and automatic controls. Interactive control, general game-rule recovery, and the broader 3D roadmap were not verified; no standalone arXiv paper verified. |
| **H3 Streaming VAE Decoder** | SolarX-Team | 2026-11-11 | [Project](https://solarx-team.github.io/H3-Streaming-VAE-Decoder/) · [Repository](https://github.com/SolarX-Team/H3-Streaming-VAE-Decoder) | Streaming decoder source for MiniMax H3 and StreamRender-H3 is available; weights remain external, and optional fused kernels require Blackwell GPUs. Independent decoder extension, not NVIDIA's full renderer; no standalone arXiv paper verified. |
| **Code Video Model** | Microsoft Research | 2026-11-10 | [Project](https://code-video-model.github.io/) · [Repository](https://github.com/code-video-model/CodeVideoModel) · [Technical report](https://code-video-model.github.io/tech_report.pdf) · [Benchmark](https://huggingface.co/datasets/code-video-model/CodeVideoBench) | Scene-generation and rendering source, examples, and benchmark cases are available; requires external model services and MiniMax-H3 weights. No arXiv first-submission date verified; tracked as a project release. |
| **World Model Planning Reliability (WCTR)** | Zhijing Wu | 2026-11-10 | [Repository](https://github.com/ZhijingWu/world-model-planning-reliability) · [Technical note](https://raw.githubusercontent.com/ZhijingWu/world-model-planning-reliability/main/note/Zhijing_Wu_World_Model_Planning_Note_Final.pdf) | Runtime source, an illustrative example, tests, and retained study records are available. Branch isolation covers restricted Python state operations, not arbitrary side effects; no standalone arXiv paper verified. |
| **EdenLive** | VAST | 2026-10-28 | [Project](https://vast-eden.ai/?p=edenlive) · [Repository](https://github.com/VAST-AI-Research/EdenLive) · [Models](https://huggingface.co/VAST-AI/EdenLive) | Offline and streaming inference source, 5B/14B weights, and a prompt-to-game frontend are available. The project page and author-linked technical-report PDF returned HTTP 403 during this check; report contents were not verified. |
| **Streaming Code World Model** | Tingting Liao and Guangyi Liu | 2026-10-28 | [Repository](https://github.com/TingtingLiao/streaming-code-world-model) · [Models](https://huggingface.co/Luffuly/streaming-code-world-model) | Training/evaluation source and streaming LoRA checkpoints are available; requires the upstream CWM runtime and base weights. The documented configuration is not real time. No standalone paper verified. |
| **StreamRender-H3** | NVIDIA | 2026-10-28 | [Project](https://nvlabs.github.io/Sana/Sol-Engine/StreamRender-H3/) · [Source code](https://github.com/NVlabs/Sana/tree/sol-engine/models/streamrender_h3) | Project page and runtime source available; deployment requires external model weights and a compatible multi-GPU environment. No standalone paper destination verified. |

**Mundo** reconstructs a proxy scene from context images and refines it with a vision-language agent, representing objects and physical properties in a scene program. A physics engine computes scripted interactions, and a context-conditioned video model renders the simulated trajectories; the demonstrated interface is not yet a released implementation.

**Code World Model 2.0 / Invoker-Render** converts engine-generated structural proxies, an appearance reference, and text into streaming video, supporting different proxy detail levels. The upstream engine owns world state and interaction rules; the released renderer maintains bounded visual history rather than discovering executable dynamics.

**CoCode-World** renders synchronized player views from shared geometric proxies, reference appearance, and text. Its released metadata and proxy compiler reconstruct observed game states and camera paths; generating consequences of new actions requires a separate dynamics model or compatible simulator.

**HolonEngine** extracts camera motion, world geometry, actor tracks, and motion parameters from gameplay video into a serialized world. Its supplied runtime advances explicit object and interaction state and renders rollouts; the available source does not establish unrestricted synthesis of unseen game mechanics.

**H3 Streaming VAE Decoder** emits frames as video latents arrive, with cached attention and no future-latent requirement. Its explicit StreamRender-H3 support connects it to code-defined game rendering, while state evolution and video-latent generation remain upstream.

**Code Video Model** generates executable Three.js scene and motion programs, renders proxy videos, and conditions a video model on the proxy during early sampling steps. The report and release concern controlled video generation; they do not establish interactive dynamics discovery.

**World Model Planning Reliability** supplies Witness-Compiled Transactional Rollouts (WCTR), which instruments supported state writes and isolates hypothetical branches of existing Python world models. Agreement is checked against the same program on a full copy, not against ground-truth environment dynamics.

**StreamRender-H3** connects a code game engine that maintains maps, physics, rules, and player feedback to a streaming MiniMax-H3 renderer through semantic frame maps. The published demo is racing-specific; it does not establish learned executable dynamics or generalization to other games.

**EdenLive** renders proxy or reference video streams from coding agents, existing engines, or recorded footage. Its release also includes an EdenGolem skill and frontend for creating coarse playable games; state transitions and interaction rules execute in those upstream programs.

**Streaming Code World Model** extends CWM with causal proxy-conditioned chunk generation and few-step distillation. It is tracked as a separate author-maintained extension, not as the original CWM paper's official repository.

## Code-driven world evolution and physical reasoning

- **[2026-11-18] WorldRuler: Interactive World Modeling under Configurable Rules** — `Core`\
  Executes user-defined triggers, preconditions, and object-state effects in a persistent 3D rule graph, jointly saving rules and state while binding their consequences to regions controlled by a video generator.\
  [Paper](https://arxiv.org/abs/2611.24869) · [Project](https://alaya-lab.github.io/WorldRuler/) · [Announcement repository](https://github.com/AlayaLab/WorldRuler) · [Partial dataset](https://huggingface.co/datasets/AlayaLab/RuleVerse)\
  *Release note: Inference code and weights remain pending; the model destination is a placeholder, and the RuleVerse manifest marks its upload incomplete as of November 20, 2026.*

- **[2026-11-14] GameWM: Toward Next-Generation Video Games with Interaction-Centric World Models** — `Core`\
  Keeps gameplay rules, entity state, and event outcomes in an engine while a proxy-conditioned video model generates interaction detail and appearance from reusable character and skill descriptions.\
  [Paper](https://arxiv.org/abs/2611.19247)\
  *Scope and release note: The reported evaluation uses proxies from held-out recordings, rather than establishing complete interactive-system performance. The paper-linked project and repository returned HTTP 404 on November 18, 2026.*

- **[2026-11-11] Gradient-Aware AI Agents for Autonomous Turbulence Model Discovery via Differentiable CFD** — `Core`\
  Synthesizes analytical, neural, or hybrid turbulence closures inside a supplied differentiable flow solver, using simulated statistics and parameter gradients to revise both model form and fitted parameters.\
  [Paper](https://arxiv.org/abs/2611.16082)

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

- **[2026-03-21] LLM-ODE: Data-driven Discovery of Dynamical Systems with Large Language Models** — `Core`\
  Uses language-model proposals to evolve symbolic ODE expressions, fits their constants, and combines candidate derivatives into systems ranked by complexity and numerically integrated trajectory error.\
  [Paper](https://arxiv.org/abs/2603.20910) · [Repository](https://github.com/gryaklab/llm-ode)

- **[2026-03-20] Discovering Governing Spatial Interaction Equations in Dynamic Urban Systems** — `Core` · **U-Discovery**\
  Proposes symbolic interaction equations from retrieved scientific priors, estimates their coefficients from observed urban histories, and numerically evaluates candidate dynamics to rank explanations of population changes.\
  [Paper](https://arxiv.org/abs/2603.19537) · [Repository](https://github.com/GeoDI-Lab/U-Discovery)\
  *Scope and release note: The released fitting workflow evaluates one-step predictions from observed history, with potentially time-varying coefficients. GraphRAG outputs are archived, and documented paper–artifact discrepancies limit reproduction claims; free-running forecasting is not established.*

- **[2026-03-10] Epistemic Closure: Autonomous Mechanism Completion for Physically Consistent Simulation** — `Core`\
  Assembles constitutive mechanisms from a skill library, revises their coupling using regime and boundary-condition checks, and compiles the resulting physical model into finite-element simulation code.\
  [Paper](https://arxiv.org/abs/2603.09756) · [Repository](https://github.com/shuWuYue123/Neuro-Symbolic-Auto-Coupling)\
  *Release and scope note: Coupling-agent source and illustrative simulation scripts are available; the inspected example is simplified finite-difference code, not reproduction of the paper’s full FEniCSx experiment.*

- **[2026-03-06] Symmetry-Constrained Language-Guided Program Synthesis for Discovering Governing Equations from Noisy and Partial Observations** — `Core`\
  Synthesizes symbolic dynamical laws within a grammar constrained by units and symmetries, fits their constants, and ranks alternative structures using complexity penalties and bootstrap stability under noisy or partial observations.\
  [Paper](https://arxiv.org/abs/2603.06869)

- **[2026-02-23] Pixel2Phys: Distilling Governing Laws from Visual Dynamics** — `Core`\
  Alternates visual variable extraction with symbolic equation discovery, numerically integrating candidate laws and using reconstruction, phase portraits, and extrapolation feedback to revise the representation.\
  [Paper](https://arxiv.org/abs/2602.19516)

- **[2026-02-07] In-Context System Identification for Nonlinear Dynamics Using Large Language Models** — `Core`\
  Uses language-model proposals to revise symbolic ODE structures, fits coefficients through sparse regression, and numerically integrates candidates to guide equation search with trajectory error.\
  [Paper](https://arxiv.org/abs/2602.07360)\
  *Scope and release note: Candidate selection repeatedly uses the designated test interval; it is not an untouched final generalization test. No official implementation destination was verified.*

- **[2025-05-17] MLLM-based Discovery of Intrinsic Coordinates and Governing Equations from High-Dimensional Data** — `Core` · **VER**\
  Uses a multimodal model to identify physical coordinates or latent dimension and propose symbolic function libraries, fits sparse dynamical equations, and integrates the discovered laws to extrapolate trajectories.\
  [Paper](https://arxiv.org/abs/2505.11940)

- **[2024-05-13] LLM4ED: Large Language Models for Automatic Equation Discovery** — `Core`\
  Generates symbolic ODE and PDE expressions, fits their constants against observed derivatives, and alternates local revisions with evolutionary search to recover governing laws; the evaluation emphasizes equation recovery rather than interactive planning.\
  [Paper](https://arxiv.org/abs/2405.07761) · [Repository](https://github.com/menggedu/EDL)

## Learning executable dynamics and planning

- **[2026-11-18] ABSClaw: From Invented Worlds to Reality-Grounded Social Simulation** — `Core`\
  Compiles social-simulation requests into bounded Python lifecycle programs over supplied state, relation, event, and resource operations, initializing worlds from observed data and allowing model calls for individual decisions; introduces ABSBench.\
  [Paper](https://arxiv.org/abs/2611.24517)\
  *Scope note: The operation vocabulary and runtime are supplied; generated programs compose the mechanisms, and most benchmark tasks also use live language-model decisions. No official implementation destination was verified.*

- **[2026-11-17] Think Once, Act Fast: Cost-Effective Recursive Self-Improvement for Decision Model Harness** — `Core` · **JevRSI**\
  Develops reusable Python programs that predict candidate actions' one-step effects, rewards, and termination, revising them against recorded transitions and supplying their predictions to a fast decision model.\
  [Paper](https://arxiv.org/abs/2611.22432) · [Repository](https://github.com/usail-hkust/JevRSI)\
  *Scope note: The released checker validates selected observation, inventory, reward-sign, and termination fields; this is bounded action-effect prediction rather than a complete simulator state reconstruction.*

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

- **[2026-08-10] Model Discovery Agent: LLM-assisted Bayesian experiment design for data-efficient discovery of mechanistic world models** — `Core`\
  Maintains competing executable mechanisms for reaction rates and partially observed ODE/SDE dynamics, fits their parameters and latent states, and selects experiments to distinguish hypotheses before forecasting unseen interventions.\
  [Paper](https://arxiv.org/abs/2608.09696) · [NeuronBench repository](https://github.com/murphyk/neuronbench)\
  *Release and scope note: The linked repository supplies the neuron benchmark and a reference baseline, not a verified complete MDA implementation; its bundled protocol menu differs from the paper’s main experiment.*

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

- **[2026-06-05] Learning Explicit Behavioral Models with Adaptive Questions and World-Model Probes** — `Core` · **ESBM**\
  Revises typed predicates, action rules, and executable mechanism hypotheses using adaptive questions and matched environment branches, checking predicted object, reward, and terminal-state changes alongside task performance.\
  [Paper](https://arxiv.org/abs/2606.07127)

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

- **[2024-10-01] Mechanic Maker: Accessible Game Development Via Symbolic Learning Program Synthesis** — `Core`\
  Learns executable game rules from user-edited frames and input examples, searching over conditions and state changes while exposing predicted frames and a play mode for iterative correction.\
  [Paper](https://arxiv.org/abs/2410.01096)

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

- **[2026-11-17] CrossEnv: Synthesizing Verifiable Cross-Environment Tasks for Long-Horizon Agent Training** — `GUI`\
  Synthesizes executable tools over persistent service databases, aligns shared entities across environments, and checks composed workflows through reference replay, state-based verifiers, and independent agent attempts.\
  [Paper](https://arxiv.org/abs/2611.22777)\
  *Scope note: These are tool-interface service environments, not next-screen GUI predictions; no official implementation destination was verified.*

- **[2026-11-02] WebHarbor: Docking Real Websites for Evolving GUI Agent Environments** — `GUI`\
  Reconstructs task-relevant website interfaces, databases, and persistent workflows through coding agents and human audits, producing resettable local environments for GUI-agent evaluation and training.\
  [Paper](https://arxiv.org/abs/2611.03634) · [Project](https://aiming-lab.github.io/WebHarbor/) · [Repository](https://github.com/aiming-lab/WebHarbor) · [Environments and data](https://huggingface.co/datasets/ChilleD/WebHarbor)

- **[2026-10-27] WebAnything: From the Wild Web to Scalable Agent Environments** — `GUI`\
  Reconstructs local website routes and state transitions from browser-observed evidence, using an independent verifier to guide repairs or additional capture and producing resettable environments within a declared interaction scope.\
  [Paper](https://arxiv.org/abs/2610.37786) · [Repository](https://github.com/china-qijizhifeng/Web-Anything)\
  *Release and scope note: The alpha release includes construction source, selected runnable demos, and a 244-site inventory; the full historical website trees are not bundled, and arbitrary-site automation is not established.*

- **[2026-10-27] Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis** — `GUI` · **SynthAPI**\
  Synthesizes Python app schemas and read/write APIs over persistent databases, then generates initial states, oracle programs, and executable task verifiers to study how environment diversity affects tool-agent training.\
  [Paper](https://arxiv.org/abs/2610.37648)\
  *Scope note: These are tool-interface app worlds, not rendered GUI predictions; generated tasks operate within a single app.*

- **[2026-10-22] Trace2World: Reconstructing App Worlds from Real Interaction Traces for Scalable GUI Agent Training** — `GUI`  
  Reconciles recorded workflows into a shared app-state model, compiles its supported behavior into a browser environment, and repairs implementation errors through independent replay while keeping unsupported transitions non-executable.  
  [Paper](https://arxiv.org/abs/2610.30792)

- **[2026-10-19] Agent World Model in the Wild: Computer-Use Agent Environment Synthesis** — `GUI` · **WildAWM**  
  Synthesizes persistent computer environments spanning GUI, MCP, and command-line interfaces, with execution-based checks for task solvability, difficulty, and verifier reliability before agent training.  
  [Paper](https://arxiv.org/abs/2610.26828) · [Project](https://msr-orchard.github.io/WildAWM/) · [Repository](https://github.com/MSR-Orchard/WildAWM)

- **[2026-10-12] Davinci-Tool: Scaling Agentic Tool-Use Supervision with Verifiable Executable Environments** — `GUI`\
  Synthesizes and audits stateful tool domains, composes compatible domains through shared entities and rules, and uses restored states and executable verifiers to collect demonstrations and compare alternative decisions.\
  [Paper](https://arxiv.org/abs/2610.16867) · [Repository](https://github.com/MassLab-SII/Davinci-Tool)\
  *Release note: EGTS and cross-domain composition source are available, but executable worlds and domain catalogs remain pending. The documented public trajectory subset is smaller than the paper’s training corpus; this is tool-environment synthesis, not next-screen prediction.*

- **[2026-09-04] EnvCraft: Synthesizing Executable Environments in Agentic RL for Claw-like Agent** — `GUI`\
  Synthesizes sandboxed workspaces with explicit entities, business rules, persistent state, and executable tool transitions, then builds multi-step tasks and state-based verifiers for agent training.\
  [Paper](https://arxiv.org/abs/2609.05576) · [Repository](https://github.com/zeng-yirong/EnvCraft)\
  *Release and scope note: The author-linked repository is branded ClawForge and provides environment implementations, task data, and training integration; its task snapshot is smaller than the paper’s full corpus. This models tool/CLI workspaces, not rendered next screens.*

- **[2026-08-22] Training Needs Trustworthy Worlds: Verified Synthetic Web Environments for Agent Learning** — `GUI`\
  Constructs and repairs website scaffolds linking pages, records, and task constraints, executes ordinary UI transitions deterministically, and admits LLM-proposed backend changes only through validated state-change markers.\
  [Paper](https://arxiv.org/abs/2608.21898)\
  *Release and scope note: The synthetic training environment retains generative backend writes; the claim of no LLM calls at evaluation concerns the trained policy. No official implementation destination was verified.*

- **[2026-08-21] AgentMercury: Your Agent Can Synthesize Verifiable Environments for Business Scenarios at scale** — `GUI`\
  Synthesizes persistent business environments with entities, services, tool interfaces, and cross-service invariants, then instantiates tasks and trajectories for agent training from each executable world.\
  [Paper](https://arxiv.org/abs/2608.20634) · [Project](https://minstar.github.io/AgentMercury/)

- **[2026-08-06] AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents** — `GUI`  
  Predicts reachable next-screen code updates using transition-constrained retrieval, executable HTML, and generated visual assets.  
  [Paper](https://arxiv.org/abs/2608.05891)

- **[2026-05-18] EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL** — `GUI`\
  Builds persistent database schemas and executable Python tools from source-grounded service descriptions, repairs them through generated tests, and samples tool dependencies to construct agent-training tasks.\
  [Paper](https://arxiv.org/abs/2605.18703) · [Repository](https://github.com/LARK-AI-Lab/EnvFactory)\
  *Scope and release note: Generation, validation, and trajectory source are available; these are tool-interface service environments, not rendered next-screen predictions.*

- **[2026-04-20] Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence** — `GUI`\
  Constructs executable tool environments over persistent service databases, verifies task trajectories through state changes, and uses recurring agent failures to guide further environment and task synthesis.\
  [Paper](https://arxiv.org/abs/2604.18292) · [Project](https://agent-tars-world.github.io/-/) · [Repository](https://github.com/RUC-NLPIR/Agent-World)\
  *Scope and release note: The repository provides a selected environment subset and graph-based task synthesis; complete environment-discovery and reinforcement-learning reproduction are not established. These are tool-interface worlds.*

- **[2026-02-15] AutoWebWorld: Synthesizing Infinite Verifiable Web Environments via Finite State Machines** — `GUI`\
  Synthesizes finite-state specifications with action preconditions and effects, generates corresponding web applications, and replays graph-derived GUI trajectories to filter frontend execution failures.\
  [Paper](https://arxiv.org/abs/2602.14296) · [Project](https://evanwu1125.github.io/AWW_homepage/) · [Repository](https://github.com/Evanwu1125/AutoWebWorld) · [Dataset](https://huggingface.co/datasets/Evanwu50020/travel_media_commerce_communication_productivity)\
  *Scope and release note: Generation, replay, training source, and example apps are available. The project’s Paper button points to an unrelated identifier; the paper link here is verified against arXiv metadata and the repository citation.*

- **[2026-02-15] GUI-GENESIS: Automated Synthesis of Efficient Environments with Verifiable Rewards for GUI Agent Post-Training** — `GUI`\
  Rebuilds task-relevant app behavior from interaction traces as local Flask applications, embedding rewards over backend state and repairing environments through generated browser tests.\
  [Paper](https://arxiv.org/abs/2602.14093)\
  *Scope and release note: Task-conditioned reconstruction does not establish a complete app model; generated tests and rewards are not independent proofs of fidelity. No official implementation destination was verified.*

- **[2026-02-10] Code2World: A GUI World Model via Renderable Code Generation** — `GUI`  
  Predicts action-conditioned interfaces as HTML, using AndroidCode data and render-aware reinforcement learning to align visual and action consistency.  
  [Paper](https://arxiv.org/abs/2602.09856) · [Project](https://amap-ml.github.io/Code2World/) · [Repository](https://github.com/AMAP-ML/Code2World)

- **[2026-02-06] ScaleEnv: Scaling Environment Synthesis from Scratch for Generalist Interactive Tool-Use Agent Training** — `GUI`\
  Synthesizes database-backed tool environments, repairs their code with matched state-transition tests, and expands dependency-graph paths into tasks with execution-checked reference outcomes.\
  [Paper](https://arxiv.org/abs/2602.06820)\
  *Scope and release note: These are stateful tool environments with a separate simulated user, not visual GUI predictions; generated tests do not prove unrestricted correctness. No official implementation destination was verified.*

- **[2026-02-02] Generative Visual Code Mobile World Models** — `GUI` · **gWorld**\
  Predicts an action-conditioned mobile screen as renderable web code, training on screenshot-to-code targets and lookahead reasoning traces derived from offline trajectories; introduces MWMBench, while persistent app-state reconstruction remains outside the single-screen formulation.\
  [Paper](https://arxiv.org/abs/2602.01576) · [Project](https://trillionlabs-gworld.github.io/) · [Repository](https://github.com/trillion-labs/gWorld) · [8B model](https://huggingface.co/trillionlabs/gWorld-8B) · [32B model](https://huggingface.co/trillionlabs/gWorld-32B) · [Benchmark](https://huggingface.co/datasets/trillionlabs/MWMBench)

- **[2026-01-09] EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis** — `GUI`\
  Synthesizes Python classes whose attributes hold service state and whose methods implement tool operations, checks their behavior with testing and checking agents, and generates initial states and final-state verifiers.\
  [Paper](https://arxiv.org/abs/2601.05808) · [Repository](https://github.com/RUC-NLPIR/EnvScaler)\
  *Scope and release note: Environment, scenario, interaction, and training source are available; these are executable tool-service models, not rendered GUI predictions. April 17, 2026 is a revision.*

## Executable scene and 4D world construction

These papers construct executable environments; their goals differ from identifying unknown transition dynamics through interaction.

- **[2026-11-19] PlayCraft: Designing Engaging Games from Agent Play Experience** — `Construction`\
  Revises executable game mechanics from a visual player agent’s episode reports, then tests the changed game through builds and play, using improvement across repeated attempts as a proxy for mastery.\
  [Paper](https://arxiv.org/abs/2611.26624) · [Project](https://playcraft.cheng.website) · [Repository](https://github.com/xt4d/PlayCraft)\
  *Scope and release note: The release includes construction and play-loop source; model access and Chromium are required. Agent learning curves do not establish human engagement.*

- **[2026-11-19] OceanCoder: A Verification-Guided Large Language Model for Automated Simulation Modelling in Ocean Engineering** — `Construction`\
  Trains a model to write OrcaFlex programs for offshore structures, loads, and analyses, using checks on saved models, completed solves, and physical responses to supply graded training rewards.\
  [Paper](https://arxiv.org/abs/2611.26333)\
  *Scope and release note: The engine supplies physical laws, and evaluation allows one generation attempt without simulator-feedback repair. Weights and benchmark specifications are promised upon publication; no implementation destination was verified.*

- **[2026-11-19] MorphTwin: Enriching Deformable Material Responses from Videos for Morphable and Interactive Physical Twins** — `Construction`\
  Reconstructs deformable objects as explicit spring graphs with additional internal nodes, fitting motion and calibrating separate volume and shape responses before executing material edits and new interactions.\
  [Paper](https://arxiv.org/abs/2611.25963)\
  *Scope and release note: Constructs and calibrates an executable physical representation under supplied spring laws; it does not synthesize general-purpose dynamics code. No official implementation destination was verified.*

- **[2026-11-19] PRIO: Pre-trained Representation for Interactive Objects in 4D Worlds** — `Construction`\
  Predicts an object-specific linear deformation space from static geometry, then evolves its coordinates with supplied Lagrangian mechanics and applied forces using precomputed operators instead of repeated neural prediction.\
  [Paper](https://arxiv.org/abs/2611.25500)\
  *Scope and release note: The learned representation feeds an explicit physics integrator; topology changes and untrained material behaviors remain outside its scope. No official implementation destination was verified.*

- **[2026-11-19] SceneAnything: Agentic Reconstruction of Large-Scale Mesh Scenes from a Single Video** — `Construction`\
  Coordinates agents that write parameterized Blender scene programs from video measurements, fitting object motion and retaining revisions through scene checks and independent render comparisons.\
  [Paper](https://arxiv.org/abs/2611.25340)\
  *Scope and release note: Its executable animation replays fitted motion from new cameras; it does not discover interaction laws. The harness and scene release is announced, without a verified implementation destination.*

- **[2026-11-19] Coda-DaVinci: Reimagining Video Generation with Code2Video** — `Construction`\
  Selects between direct video generation and executable Blender proxies, adapts object detail and physical simulation to the task, and preserves scene assets while visual feedback guides program and rendering revisions.\
  [Paper](https://arxiv.org/abs/2611.26595) · [Project](https://coda-davinci.github.io/) · [Announcement repository](https://github.com/FrankYang-17/Coda)\
  *Scope and release note: The shared Coda repository provides this paper’s overview and media; Coda-DaVinci implementation is marked coming soon. Its separate CodeCap-Bench directory is not the method release.*

- **[2026-11-18] VOL-Agent: Programming Your Film via Video Orchestration Language Agentic System** — `Construction`\
  Builds reusable Blender scene, motion, and camera programs within a compiled film-production workflow, renders them as video-generation conditions, and carries final proxy states into subsequent shots.\
  [Paper](https://arxiv.org/abs/2611.23950)\
  *Scope note: Inclusion concerns the evaluated Blender workflow; general shot orchestration and textual memory alone do not establish executable world dynamics. No official implementation destination was verified.*

- **[2026-11-18] GTA: Generative Tower of Agents for Scalable Holonic Scene Generation** — `Construction`\
  Recursively constructs and assembles Blender scenes through parallel agents with shared hierarchical interfaces, then integrates scene-guided animated humans, garment simulation, and contact adjustments.\
  [Paper](https://arxiv.org/abs/2611.23727) · [Project](https://zt-zeng-tao.github.io/GTA/)\
  *Scope and release note: Dynamics come from a separate motion-generation and simulation stage, not discovered transition rules. The project provides demonstrations; an implementation release was not verified.*

- **[2026-11-17] Reliability by Architecture: Agentic Workflows for Validated Multi-Physics Simulation from Natural Language** — `Construction`\
  Constructs and repairs executable GEOS simulation setups by combining language-model interpretation with deterministic mesh, material, and control configuration, checking physical consistency separately from agreement with the requested experiment.\
  [Paper](https://arxiv.org/abs/2611.23473)\
  *Scope note: GEOS supplies the governing equations; experts supply construction rules and acceptance checks for the tested configurations. No official harness implementation destination was verified.*

- **[2026-11-17] RFW-S: Everyday Deformable Objects with Independent Simulation Verification** — `Construction`\
  Builds deformable assets with structure-specific geometry and physical settings, calibrates effective solver parameters with language-model assistance, and screens frozen configurations on interactions distinct from calibration.\
  [Paper](https://arxiv.org/abs/2611.23056) · [Project](https://sjijs.github.io/RFW-S_website/)\
  *Release and scope note: Public asset and implementation links remain pending. Acceptance is configuration-specific; the deformation-derived integrity score is not a fracture simulation or a quantitative real-world transfer guarantee.*

- **[2026-11-16] EmbedGym: Letting Coding Agents Develop and Debug Embedded Firmware Without Physical Hardware** — `Construction`\
  Synthesizes and tests executable peripheral state machines from datasheets and driver examples, couples them to MCU emulators and circuit/network models, and builds timed interaction tasks for firmware agents.\
  [Paper](https://arxiv.org/abs/2611.21845) · [Project and benchmark explorer](https://embedgym.github.io/)\
  *Scope and release note: Included for generated external-device behavior beyond instruction emulation. The website exposes task data and selected browser demonstrations; a complete simulator source release was not verified.*

- **[2026-11-16] GranularGPT: Natural-Language-Driven End-to-End Discrete Element Method Simulations** — `Construction`\
  Translates granular-simulation requests into validated schemas for geometry, materials, contacts, and boundary conditions, then deterministically generates and executes LIGGGHTS cases with bounded repairs and persistent outputs.\
  [Paper](https://arxiv.org/abs/2611.20551)\
  *Scope note: The supplied solver and supported contact laws determine dynamics; the method constructs simulation cases rather than discovering new physical laws.*

- **[2026-11-13] TelePhysica: Agentic Reconstruction of Physically Interactive Scenes** — `Construction`\
  Reconstructs procedural meshes and declarative physical models from one photograph, repairs them through silhouette and gravitational-equilibrium checks, and executes force interventions in a supplied solver to condition video generation.\
  [Paper](https://arxiv.org/abs/2611.18078) · [Project](https://interactive4d.vercel.app/)\
  *Scope and release note: The project page provides demonstrations, but its linked repository returned HTTP 404 on November 17, 2026; a runnable implementation was not verified.*

- **[2026-11-12] BWM-Forge: Agentic World Programming for Embodied Intelligence** — `Construction`\
  Builds editable Blender scene, robot-motion, and camera programs from multimodal task inputs, revising them through review and reusable experience before sending proxy videos to an appearance generator.\
  [Paper](https://arxiv.org/abs/2611.16221) · [Project](https://bwm-forge.github.io/) · [Repository](https://github.com/Lcixs/BWM-Forge)\
  *Release and scope note: Pipeline and local interface source are available; the documented Windows-oriented setup requires Blender, robot assets, and external model services. This constructs controlled robot videos rather than discovering general transition laws.*

- **[2026-11-09] HolidayFactory 1.0: Simulating, Generating, and Evaluating Industrial Robot Tasks** — `Construction`\
  Generates simulation assets, scene variants, and typed workplace process logic, then compiles human-confirmed evaluation specifications into executable checks; introduces persistent-job evaluation in 24/7-Bench.\
  [Paper](https://arxiv.org/abs/2611.11789)\
  *Scope and release note: The paper does not yet establish end-to-end generation of all seven benchmark worlds or policy comparisons over persistent runs; no official implementation destination was verified.*

- **[2026-11-09] MechFoundry: An agentic loop that poses and performs engineering analyses and optimization of real-world objects** — `Construction`\
  Builds physical analysis cases from object descriptions using generated boundary-selection programs, part materials, and loads, then executes a supplied differentiable finite-element solver and uses its sensitivities for shape or topology optimization.\
  [Paper](https://arxiv.org/abs/2611.14571) · [Repository](https://github.com/LuoXueling/MechFoundry)\
  *Scope and release note: This constructs nonlinear elastostatic models, not learned temporal dynamics. Source and setup instructions are available; the workflow requires a configured GPU solver stack, external models, and model services.*

- **[2026-11-09] PneuGen: Task-Driven Agentic Co-Design of Soft Pneumatic Robots** — `Construction`\
  Generates soft-robot design programs specifying components, geometry, arrangement, and actuation, compiles them into finite-element scenes, and uses simulated diagnostics plus fitted module responses to revise the designs.\
  [Paper](https://arxiv.org/abs/2611.13344)

- **[2026-11-08] SoftPAT3D: Physics-Augmented Text-to-3D Scene Generation with Deformables** — `Construction`\
  Constructs deformable rest shapes, materials, collision supports, and initial placements from text, then uses unified contact simulation and placement or material optimization to produce editable scenes that support robot manipulation.\
  [Paper](https://arxiv.org/abs/2611.11087)

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

- **[2026-10-29] Gym-Anything for Robotics: Scaling physical simulations with digital agents** — `Construction`\
  Builds robot environments with task-specific physical mechanisms and state-based verifiers, iterating through independent audits of simulated behavior, evidence, infrastructure, and exploitable actions; introduces RoboWorld.\
  [Paper](https://arxiv.org/abs/2610.40565) · [Project](https://gym-anything.github.io/robotics) · [Repository](https://github.com/gym-anything/robotics)\
  *Scope and release note: Construction, evaluation, and environment source are available; camera rendering requires a separate Isaac Sim installation and a compatible NVIDIA GPU. No simulation was run for this check.*

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

- **[2026-10-07] LLM-Assisted Generation of Transparent, Open-Source Multiphysics Models of Electrochemical Devices** — `Construction`\
  Turns researcher-specified transport, reaction, and charge-balance equations into staged Julia solvers for an electrochemical reactor, using physical checks and reference-model comparisons to audit generated implementations.\
  [Paper](https://arxiv.org/abs/2610.10320) · [Repository](https://github.com/Sebobbit/CO2R-Bulk-Scale-Model)\
  *Scope and release note: The demonstrated model is one-dimensional, steady-state, and isothermal; it constructs coupled physical mechanisms rather than learning temporal dynamics. Some released plotting scripts require an omitted helper.*

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

- **[2026-09-19] DiagGen: Agentic Generation of Deformable Assets with Sim-based Diagnostics for Robotic Simulation** — `Construction`\
  Builds part-aware deformable assets with physical parameters, probes selected regions in a simulator, and routes observed response failures back to geometry, material, or mesh generation before exporting the revised asset.\
  [Paper](https://arxiv.org/abs/2609.23103) · [Project](https://diaggen.github.io/)\
  *Release note: The project page is available, but its linked repository returned HTTP 404 on November 16, 2026; an implementation release was not verified.*

- **[2026-09-10] Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs** — `Construction` · **RCWM**  
  Reconstructs a complex 3D scene from a reference image through recursive scene programs and nested render–compare–edit loops.  
  [Paper](https://arxiv.org/abs/2609.11499)

- **[2026-09-07] PhysMAS: Physics-Grounded Multi-Agent Synthesis of Compositional 4D Gaussians** — `Construction`\
  Grounds persistent object-part identities in a Gaussian scene, assigns material profiles and bounded actions, and compiles them into shared-domain MPM simulations screened through execution records.\
  [Paper](https://arxiv.org/abs/2609.07174)\
  *Scope and release note: Geometry, run settings, and constitutive solver families are supplied; this constructs executable physical configurations rather than discovering new laws. No official implementation destination was verified.*

- **[2026-08-25] NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation** — `Construction`\
  Translates a monocular image into object and scene programs with geometry, articulation, and physical properties, refining them through object-level and assembled-scene simulation feedback.\
  [Paper](https://arxiv.org/abs/2608.24212) · [Project](https://neoworldproject.github.io/neoworld-pro-website/) · [Repository](https://github.com/NeoWorldProject/NeoWorld-Pro)\
  *Scope and release note: Source is available with external Blender, Isaac Sim, model-service, and GPU requirements. The paper covers rigid and articulated scenes under quasi-static physics; October and November revisions are not new papers.*

- **[2026-08-18] aDSL: Agentic 3D Creation via Joint Agent-Program Design** — `Construction`\
  Generates Python-embedded scene and asset programs with named part hierarchies, spatial constraints, and explicit joint axes and limits, repairing them through execution and exporting articulated models to URDF.\
  [Paper](https://arxiv.org/abs/2608.17975) · [Project](https://dylanwrh.github.io/aDSL/) · [Repository](https://github.com/sig-pku/aDSL)

- **[2026-08-01] ParticleGen: A Multi-Agent System for Particle Effects Generation** — `Construction`\
  Synthesizes editable particle-emitter modules and parameters, compiles them into Unreal Niagara simulations, and uses rendered feedback with diagnostic rules to revise the procedural effects.\
  [Paper](https://arxiv.org/abs/2608.00629)\
  *Scope and release note: This authors dynamic visual effects in a supplied particle engine; it does not recover general physical laws. No official implementation destination was verified.*

- **[2026-07-23] GS-Agent: Creating 4D Physical Worlds With Generative Simulation** — `Construction`\
  Coordinates specialist agents that write physics-engine code for assets, materials, placement, motion, and rendering, refining interacting rigid, deformable, and fluid worlds through multimodal feedback.\
  [Paper](https://arxiv.org/abs/2607.21522) · [Project](https://umass-embodied-agi.github.io/gs-agent/)

- **[2026-07-17] PhysAgent: Reflective Agentic Physics Control for Physically Plausible Video Generation** — `Construction`\
  Reconstructs scene state and scheduled physics-control programs from images and instructions, repairs them through staged simulation checks, and renders accepted motion as a prior for video generation.\
  [Paper](https://arxiv.org/abs/2607.16355) · [Project](https://iapple233.github.io/PhysAgent) · [Repository](https://github.com/IApple233/PhysAgent)\
  *Scope and release note: Single-case agent and simulation source are available; external reconstruction models, Genesis, video weights, and model-service access are required. Distinct from the June PhysAgent paper below.*

- **[2026-07-02] SimWorlds: A Multi-Agent System for Dynamic 3D Scene Creation** — `Construction`\
  Generates editable dynamic Blender scenes through staged planning, coding, and review, using a deterministic scene protocol and runtime inspection to detect motion and mechanism failures; introduces 4DBuildBench.\
  [Paper](https://arxiv.org/abs/2607.01766) · [Project](https://dynsimworlds.github.io/)

- **[2026-06-16] MagicSim: A Unified Infrastructure for Executable Embodied Interaction** — `Construction`\
  Constructs executable worlds from declarative content, layout, behavior, and agent-interface specifications, coordinating reset/step state, robot controllers, planning, evaluation, and trajectory recording through a shared simulation runtime.\
  [Paper](https://arxiv.org/abs/2606.17511)\
  *Scope note: The proposed infrastructure supplies physics and execution semantics; it does not discover unknown transition laws. No official implementation destination was verified.*

- **[2026-06-07] PhysAgent: Automating Physics-Based 4D Synthesis via Trajectory-Grounded Multi-Agent Feedback** — `Construction`\
  Selects force-field types and parameters for supplied Gaussian objects and material estimates, executes the resulting MPM configuration, and revises it using trajectory-derived motion feedback.\
  [Paper](https://arxiv.org/abs/2606.08688)\
  *Scope and release note: The agent configures a supplied force library and physics solver; it does not synthesize new constitutive laws. No official implementation destination was verified.*

- **[2026-05-27] VFEAgent: A Multimodal Agent Framework for End-to-End Automated Finite Element Analysis** — `Construction`\
  Extracts geometry, materials, boundary conditions, and loads from diagrams into a structured model, generates Abaqus simulation scripts, and repairs execution failures using solver feedback and stored constraints.\
  [Paper](https://arxiv.org/abs/2605.28978)\
  *Scope and release note: The evaluation concerns structural finite-element analysis under supplied mechanics, not learned interaction dynamics. No official implementation destination was verified.*

- **[2026-05-19] SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects** — `Construction`\
  Compiles room layouts and object requests into part-wise Blender programs, repairs them through execution, and exports articulated simulation assets linked by a persistent scene-state registry.\
  [Paper](https://arxiv.org/abs/2605.19587) · [Project](https://scene-code.github.io/) · [Repository](https://github.com/wangpuyi/SceneCode)

- **[2026-05-14] ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction** — `Construction`\
  Turns user-reviewed plans into PyChrono programs specifying bodies, constraints, controllers, and sensors, then repairs them using rendered rollouts and trajectory-based physics checks within the supplied engine.\
  [Paper](https://arxiv.org/abs/2605.14398) · [Project](https://uwsbel.github.io/chrono-agentic-website/)

- **[2026-05-14] SR-Platform: An Agentic Pipeline for Natural Language-Driven Robot Simulation Environment Synthesis** — `Construction`\
  Combines language-guided scene planning, generated CAD assets, and layout checks with deterministic MJCF assembly and robot-model integration to produce editable MuJoCo workspaces.\
  [Paper](https://arxiv.org/abs/2605.14700)\
  *Scope and release note: The supplied engine owns dynamics; complete tasks, rewards, and demonstrations are not generated. Reported end-to-end latency is estimated from telemetry, and no official implementation destination was verified.*

- **[2026-05-10] SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning** — `Construction`\
  Uses an evolving coding agent to create and repair Unreal environments through compilation, physics, and visual feedback, exporting Gym-style tasks and adapting the generated curriculum to learner performance.\
  [Paper](https://arxiv.org/abs/2605.09423)

- **[2026-03-25] Sketch2Simulation: Automating Flowsheet Generation via Multi Agent Large Language Models** — `Construction`\
  Converts process diagrams into component-and-stream graphs, generates Python programs that instantiate and connect Aspen HYSYS models, and uses execution and structural checks to repair the flowsheets.\
  [Paper](https://arxiv.org/abs/2603.24629) · [Partial implementation](https://github.com/OptiMaL-PSE-Lab/Sketch2Simulation)\
  *Scope and release note: Agent and orchestration source are available, but required HYSYS instruction files are omitted; execution also needs a licensed HYSYS installation with COM access and external model services.*

- **[2026-02-12] Code2Worlds: Empowering Coding LLMs for 4D World Generation** — `Construction`  
  Generates simulation code with separate object and environment construction, then refines dynamics through physics-aware visual feedback; includes Code4D evaluation.  
  [Paper](https://arxiv.org/abs/2602.11757) · [Project](https://aigeeksgroup.github.io/Code2Worlds/) · [Repository](https://github.com/AIGeeksGroup/Code2Worlds)

- **[2026-01-14] World Craft: Agentic Framework to Create Visualizable Worlds via Text** — `Construction`\
  Generates structured layouts, assets, and interaction properties from narrative requests, repairs spatial constraints, and assembles navigable Godot scenes through a supplied world scaffold.\
  [Paper](https://arxiv.org/abs/2601.09150) · [Repository](https://github.com/HerzogFL/World-Craft)\
  *Scope and release note: Preliminary Python generation and Godot runtime source are available; data, model checkpoints, deployment instructions, and separately licensed visual assets are not a complete bundled release. Interaction logic remains scaffold-limited.*

- **[2024-11-12] LLMPhy: Parameter-Identifiable Physical Reasoning Combining Large Language Models and Physics Engines** — `Construction`\
  Iteratively generates Python scene programs with estimated physical parameters and object layouts, uses reconstruction errors to revise them, and executes the fitted scene in a supplied physics engine to predict outcomes.\
  [Paper](https://arxiv.org/abs/2411.08027) · [Organization project page](https://www.merl.com/research/highlights/LLMPhy) · [Repository](https://github.com/merlresearch/llmphy)\
  *Scope and release note: The described parameter-estimation experiment uses simulator-extracted trajectories. Core source and data-generation tools are available; the repository's benchmark-download link remains a TODO.*

- **[2024-10-03] Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model** — `Construction`\
  Generates compact Python programs for object-part placement and joint articulation, compiles them into URDF models, and revises the programs using rendered simulation feedback.\
  [Paper](https://arxiv.org/abs/2410.13882) · [Project](https://articulate-anything.github.io/) · [Repository](https://github.com/vlongle/articulate-anything)

- **[2024-06-12] Real2Code: Reconstruct Articulated Objects via Code Generation** — `Construction`\
  Reconstructs object-part meshes from visual observations and predicts joint structure as Python code from oriented bounding boxes, producing articulated models executable in a physics simulator.\
  [Paper](https://arxiv.org/abs/2406.08474) · [Project](https://real2code.github.io/) · [Repository](https://github.com/MandiZhao/real2code)

- **[2024-05-24] OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code** — `Construction`\
  Generates and repairs Python environments with task-specific objects, dynamic behaviors, rewards, and termination rules, using an expanding task archive and learner feedback within a supplied PyBullet simulator.\
  [Paper](https://arxiv.org/abs/2405.15568) · [Repository](https://github.com/maxencefaldor/omni-epic)

- **[2023-12-14] Holodeck: Language Guided Generation of 3D Embodied AI Environments** — `Construction`\
  Converts language prompts into room layouts, asset selections, and spatial constraints, then builds executable AI2-THOR environments for navigation using supplied collision and interaction semantics.\
  [Paper](https://arxiv.org/abs/2312.09067) · [Project](https://yueyang1996.github.io/holodeck/) · [Repository](https://github.com/allenai/Holodeck)

- **[2023-11-21] GPT4Motion: Scripting Physical Motions in Text-to-Video Generation via Blender-Oriented GPT Planning** — `Construction`\
  Turns text prompts into Blender physics scripts for rigid, cloth, and liquid motion, then uses simulated edge and depth sequences to condition video generation while the engine supplies physical dynamics.\
  [Paper](https://arxiv.org/abs/2311.12631) · [Project](https://GPT4Motion.github.io) · [Repository](https://github.com/jiaxilv/GPT4Motion)

- **[2023-11-02] RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation** — `Construction`\
  Proposes robot tasks, generates simulator scene configurations with assets and articulated states, and writes training supervision for skill learning in existing physics engines; the generated environment differs from a learned transition law.\
  [Paper](https://arxiv.org/abs/2311.01455) · [Project](https://robogen-ai.github.io/) · [Repository](https://github.com/Genesis-Embodied-AI/RoboGen)\
  *Release note: The official repository documents a PyBullet implementation for rigid manipulation and locomotion; the full soft-body pipeline described in the paper is not included in that release.*

- **[2023-10-02] GenSim: Generating Robotic Simulation Tasks via Large Language Models** — `Construction`\
  Generates robot-task programs that initialize objects, poses, and goals in a supplied manipulation simulator, checks them through execution, and reuses accepted tasks for demonstrations and policy training.\
  [Paper](https://arxiv.org/abs/2310.01361) · [Project](https://liruiw.github.io/gensim) · [Repository](https://github.com/liruiw/GenSim)\
  *Scope and release note: Generation and simulation source are available; the demonstrated task family is tabletop manipulation under existing physics, and generated tasks can require manual filtering.*

- **[2020-11-02] ProbRobScene: A Probabilistic Specification Language for 3D Robotic Manipulation Environments** — `Construction`\
  Samples robotic manipulation scenes from probabilistic programs with relational geometric constraints, instantiates them in CoppeliaSim, and executes a supplied controller to expose perception, reachability, and grasp failures.\
  [Paper](https://arxiv.org/abs/2011.01126) · [Repository](https://github.com/craigiedon/ProbRobScene)\
  *Scope note: The programs specify distributions of simulator environments; they do not learn transition dynamics. Simulation requires the external CoppeliaSim and PyRep stack.*

**Naming caution:** *Code2World* is the GUI paper; *Code2Worlds* is the 4D generation paper. *WorldCoder-Bench* below is a separate paper from the 2024 *WorldCoder* agent.

## Related symbolic and neurosymbolic planning

These works are included for their explicit transition representations and verification or planning interfaces, not because all of them synthesize general-purpose simulators.

- **[2026-11-19] DARSY: A Tool for Data-Driven Abstraction and Policy Synthesis for Stochastic Systems with Unknown Dynamics** — `Related`\
  Builds finite interval-MDP abstractions from sampled simulator transitions and Lipschitz bounds, then performs robust dynamic programming for temporal-logic objectives with statistical satisfaction bounds.\
  [Paper](https://arxiv.org/abs/2611.25654) · [Repository](https://github.com/tbadings/darsy)\
  *Scope and release note: Learns a bounded symbolic abstraction of a supplied simulator rather than synthesizing its dynamics; guarantees depend on the stated sampling and regularity assumptions.*

- **[2026-11-17] Perception into Imagination: Executable Memory for World Models** — `Related` · **EPM**\
  Propagates remembered landmark or contact relations with explicit updates alongside neural imagined dynamics, using the evolving state for reward and policy learning; a symbolic instance executes known card-game rules under partial knowledge.\
  [Paper](https://arxiv.org/abs/2611.22294)\
  *Scope note: The explicit update structure and game rules are supplied; the method does not synthesize unknown transition programs.*

- **[2026-11-12] NSDL: Neuro-Symbolic Division of Labor for Multi-Robot Task Planning** — `Related`\
  Trains a visual model to judge goals and write robot-assigned plan sketches, then expands and schedules them under a supplied STRIPS-style action model; introduces LOCUS-Bench to separate state-judgment errors from structural planning failures.\
  [Paper](https://arxiv.org/abs/2611.16671) · [Repository](https://github.com/Xincheng-Tan/NSDL)\
  *Scope note: Evaluation uses symbolic replay. Solver acceptance depends on the sketch’s asserted state and does not repair incorrect scene judgments or establish physical robot execution.*

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

- **[2026-10-22] SCOPE: Scene-graph Construction Optimized by Plan Error-correction for Robot Long-term Planning Datasets** — `Related`\
  Generates symbolic scene graphs and task instructions, compiles them into PDDL problems, and repairs missing scene attributes from planner failures to produce executable planning examples under a supplied action domain.\
  [Paper](https://arxiv.org/abs/2610.31518) · [Project](https://scope-page.github.io/)\
  *Scope and release note: Scene repair changes the generated initial state, not the domain’s transition rules; planner solvability does not establish physical fidelity. The project marks code as coming soon.*

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

- **[2026-09-10] NDT Factory: Synthesizing Verified Network Digital Twins from Semantic Models via Multi-Agent LLM** — `Related`\
  Compiles expert-authored semantic specifications into cached network-twin executables that project post-admission resource use and latency, test service constraints, and support deterministic admission decisions.\
  [Paper](https://arxiv.org/abs/2609.12170)\
  *Scope and release note: The case study implements supplied network and queueing rules, with test-based validation rather than a formal correctness proof. No official implementation destination was verified.*

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

- **[2026-07-31] Symbolic Attack Chain Generation from Atomic Red Team Techniques: An Empirical Study of Predicate Representation Granularity** — `Related`\
  Translates documented security-test behavior and execution evidence into human-checked PDDL preconditions and effects, then examines whether alternative predicate groupings preserve meaningful host-state distinctions for planning.\
  [Paper](https://arxiv.org/abs/2608.00143)\
  *Scope and release note: Plan validity and cost are identical by construction in the relabeling comparison, and one chain-ordering dependency is manually imposed. No official method implementation destination was verified.*

- **[2026-07-07] Hypothesis-driven Model Expansion under Uncertainty for Open-World Robot Planning** — `Related` · **HUME**\
  Expands a symbolic world model with hypotheses about missing objects, attributes, and action effects, plans verification alongside task actions through PDDL, and rejects or revises hypotheses using execution feedback.\
  [Paper](https://arxiv.org/abs/2607.06501) · [Project](https://open-world-planning.github.io/) · [Repository](https://github.com/threefruits/HUME)\
  *Scope and release note: The released implementation covers block processing and simulated mobile manipulation; real-robot and appliance-operation components are excluded.*

- **[2026-07-03] Object-Centric Environment Modeling for Agentic Tasks** — `Related` · **OCM**\
  Accumulates Python object classes encoding environment constraints and mechanisms, requires reusable procedures to execute against that model, and reveals relevant source progressively during later agent decisions.\
  [Paper](https://arxiv.org/abs/2607.02846)

- **[2026-06-14] PO-PDDL: Learning Symbolic POMDPs from Visual Demonstrations for Robot Planning Under Uncertainty** — `Related`\
  Reconstructs symbolic trajectories from robot demonstrations, learns stochastic action effects and observation rules, and compiles reusable PO-PDDL domains for online belief-space planning under execution and perception uncertainty.\
  [Paper](https://arxiv.org/abs/2606.15654) · [Project](https://roboticsjtu.github.io/PO-PDDL/) · [Repository](https://github.com/RoboticSJTU/PO_PDDL)

- **[2026-06-05] STRIPS-WM: Learning Grounded Propositional STRIPS-style World Models from Images** — `Related`\
  Learns binary visual predicates and grounded action preconditions and add/delete effects from image transitions, then executes the symbolic operators in graph search between start and goal images.\
  [Paper](https://arxiv.org/abs/2606.06832) · [Placeholder project](https://elpislab.org/projects/strips-wm/)\
  *Release and scope note: The author project is under construction as of November 15, 2026. Operators are deterministic and tied to supplied action labels, without lifted generalization to new object sets.*

- **[2026-06-01] From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation** — `Related`\
  Resolves references across industrial asset descriptions and compiles their types, capabilities, preconditions, effects, and instance states into PDDL models for comparing production layouts through symbolic planning.\
  [Paper](https://arxiv.org/abs/2606.02167) · [Repository](https://github.com/hsu-aut/AAS2PDDL)\
  *Scope and release note: Domain mechanics come from supplied capability models rather than learned dynamics. Transformation source and example assets are available; the pipeline was not run during curation.*

- **[2026-05-15] SWoMo: Neuro-Symbolic World Model for Cataract Surgery Simulation** — `Related`\
  Uses a rule-based Godot simulator to advance explicit tool and anatomical configurations, then conditions video synthesis on simulated frames and scene graphs; tissue appearance and deformation remain learned visual outputs.\
  [Paper](https://arxiv.org/abs/2605.16530) · [Project](https://ssharvienkumar.github.io/SWoMo/) · [Repository](https://github.com/MECLabTUDA/SWoMo) · [Models and processed data](https://huggingface.co/SsharvienKumar/SWoMo)\
  *Release note: Training and inference source for video synthesis are available; a complete Godot simulator release was not verified on November 13, 2026.*

- **[2026-05-15] Deterministic Event-Graph Substrates as World Models for Counterfactual Reasoning** — `Related`\
  Represents state as typed event logs and answers interventions through deterministic forks, replay, and causal-ancestor traversal, using domain-specific interpreters and kinematic heuristics for visual counterfactual reasoning.\
  [Paper](https://arxiv.org/abs/2605.15967)\
  *Scope note: Exactness relies on closed-event assumptions; newly created interactions require additional heuristics, and domain vocabularies are hand-authored. No official implementation destination was verified.*

- **[2026-05-13] Differentiable Learning of Lifted Action Schemas for Classical Planning** — `Related` · **DIAS**\
  Learns lifted action preconditions and add/delete effects while inferring missing action arguments from symbolic transitions, then exports PDDL schemas and evaluates their successor states on larger held-out problems.\
  [Paper](https://arxiv.org/abs/2605.13282) · [Repository](https://github.com/jonaslreiter/DIAS)\
  *Scope note: States and unary/binary predicates are supplied; the method assumes injective action bindings and excludes conditional effects and numerical fluents.*

- **[2026-05-10] NEXUS: Learning Safety Constraints and Action Models for Safe and Robust Embodied Planning** — `Related`\
  Repairs PDDL action schemas from execution failures while separately accumulating temporal-logic constraints from hazards, enforcing both during symbolic search and distinguishing model-relative infeasibility from constraint-induced refusal.\
  [Paper](https://arxiv.org/abs/2605.09387)

- **[2026-04-09] RAMP: Hybrid DRL for Online Learning of Numeric Action Models** — `Related`\
  Alternates reinforcement-learning exploration with planning over learned numeric action schemas, refitting preconditions and effects from accumulated trajectories; Numeric PDDLGym executes supplied domains through a Gym interface.\
  [Paper](https://arxiv.org/abs/2604.08685) · [Environment code](https://github.com/SPL-BGU/NumericPDDLGym)\
  *Scope and release note: The evaluated learner assumes full, noise-free symbolic states and linear numeric constraints. The linked environment is not a verified release of the complete RAMP training pipeline.*

- **[2026-01-12] Executable Ontologies in Game Development: From Algorithmic Control to Semantic World Modeling** — `Related`\
  Expresses survival-game state, action eligibility, and resource updates as declarative event-graph rules, with an interpreter propagating changes and triggering reactions when their conditions become true.\
  [Paper](https://arxiv.org/abs/2601.07964)\
  *Scope and release note: The paper demonstrates handwritten rules and small prototypes; LLM-driven model generation and production-engine integration are future directions. No official implementation destination was verified.*

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

- **[2023-06-22] From Word Models to World Models: Translating from Natural Language to the Probabilistic Language of Thought** — `Related`\
  Translates language into probabilistic programs for inference over possible worlds, including explicit physical simulation and goal-directed planning, and demonstrates extending or constructing small domain models from descriptions.\
  [Paper](https://arxiv.org/abs/2306.12672) · [Example-code repository](https://github.com/gabegrand/world-models)\
  *Release note: The repository archives manually run examples and prompts, not a complete automated world-modeling system.*

- **[2023-01-16] Neuro-Symbolic World Models for Adapting to Open World Novelty** — `Related` · **WorldCloner**\
  Learns condition–effect rules over observed state features, revises their applicability regions when environment mechanics change, and simulates transitions through the updated rules to adapt a neural policy with fewer real interactions.\
  [Paper](https://arxiv.org/abs/2301.06294)

- **[2022-08-12] RLang: A Declarative Language for Describing Partial World Knowledge to Reinforcement Learning Agents** — `Related`\
  Compiles declarative state, effect, and reward specifications into queryable partial world models, allowing reinforcement-learning agents to combine supplied transition knowledge with learned behavior.\
  [Paper](https://arxiv.org/abs/2208.06448) · [Documentation](http://rlang.ai/master/) · [Repository](https://github.com/brownirl/rlang)

- **[2019-12-30] World Programs for Model-Based Learning and Planning in Compositional State and Action Spaces** — `Related`\
  Formulates world-program induction from graph-state transitions, learning graph-rewrite actions and transition feasibility for model-based search, with chemical synthesis planning as the worked application.\
  [Paper](https://arxiv.org/abs/1912.13007)

## Benchmarks and evaluation

- **[2026-11-19] TwinLab-Bench: Evaluating AI Scientists in Agentic Twins of Real Labs** — `Benchmark`\
  Evaluates experimental design in laboratory twins whose record-derived calculators produce observations and whose runtime tracks budgets and material use, with final reports judged against hidden laboratory evidence.\
  [Paper](https://arxiv.org/abs/2611.26248)\
  *Scope and release note: Calculators extend recorded conditions locally while an LLM mediates requests and observations; this is not unrestricted mechanistic simulation. No official benchmark implementation destination was verified.*

- **[2026-11-19] Efficient Multimodal Agents for Auditing 3D Worlds** — `Benchmark`\
  Trains small agents to navigate and trigger defects in executable 3D environments using engine-verified trajectories, then combines their recorded evidence for a larger model to audit on WorldAuditBench.\
  [Paper](https://arxiv.org/abs/2611.25543) · [Placeholder repository](https://github.com/UCSB-NLP-Chang/WorldAuditor)\
  *Scope and release note: The author-linked repository is empty as of November 21, 2026. Evaluation reuses WorldAuditBench; this paper is a separate auditor method.*

- **[2026-11-19] A four-level executable validation protocol for evaluating LLM-generated topology specifications of physics-based HVAC digital twins** — `Benchmark`\
  Executes generated HVAC topology specifications through static checks, model construction, convergence, and response comparison with hidden references, distinguishing runnable models from behaviorally matching twins.\
  [Paper](https://arxiv.org/abs/2611.25471)\
  *Scope and release note: Equivalence is judged against reference simulations within calibrated tolerances, not fresh plant measurements; no official evaluation-code destination was verified.*

- **[2026-11-18] Local AI Agents in Power Electronics Simulation: Deployment, Measurements and Costs** — `Benchmark`\
  Measures correctness and inference costs for agents that construct, repair, or extend executable converter models, checking simulated behavior at withheld operating points and separately studying tasks over fixed power-system models.\
  [Paper](https://arxiv.org/abs/2611.24880)\
  *Scope note: The converter-construction and model-editing tasks establish relevance; fixed-model controller tuning alone would not. Energy measurements cover the inference device, not the simulator host.*

- **[2026-11-18] Openhagen Worlds: Calibrated Environments for Measuring and Training Scientific Discovery Agents** — `Benchmark`\
  Evaluates budgeted experiment selection in generated worlds with hidden causal or physical mechanisms, deterministic answer checks, and calibrated difficulty, including multi-stage campaigns on one persistent hidden system.\
  [Paper](https://arxiv.org/abs/2611.24711) · [Hosted evaluation](https://eval.openhagen.ai/) · [Public sample](https://eval.openhagen.ai/sample/)\
  *Scope and release note: World mechanisms are supplied rather than synthesized by evaluated agents. The public sample covers two families; hosted core-tier access requires a token, and full generators were not verified as public. Frontier difficulty was tuned using a reported model’s evaluation outcomes.*

- **[2026-11-18] Movie2Game-Bench: Holistic Evaluation of Film-to-Game Adaptation Beyond Playability** — `Benchmark`\
  Evaluates film-to-game adaptations by connecting source-specific content to observed player actions, state changes, and implementation evidence, combining game-quality judgments with GUI-agent playtesting.\
  [Paper](https://arxiv.org/abs/2611.24669)\
  *Scope note: Most scores use model judgments over recorded evidence, with limited programmatic checks; this is not comprehensive formal verification of generated gameplay. No official implementation destination was verified.*

- **[2026-11-18] 3D GameDev Arena: Benchmarking Coding Agents That Plan, Build, and Playtest extreme Long-Horizon Browser Games** — `Benchmark`\
  Evaluates complete browser-game construction with specification-derived tests of production game-state logic, recorded agent playtesting, and human preference comparisons across 108 tasks.\
  [Paper](https://arxiv.org/abs/2611.24073)\
  *Scope and resource note: Some playtesting states are reached through evaluation adapters, and unevaluated functional criteria are omitted from scores. The paper-linked arena could not be verified as an accessible application on November 20, 2026.*

- **[2026-11-18] How Complete Must an Environment Be to Train a Capable GUI Agent?** — `Benchmark` · **MobileGym-Lite**\
  Varies reward-path coverage, application records, and executable feature availability in mobile GUI environments, then tests trained policies in the full environment to isolate the effects of construction choices.\
  [Paper](https://arxiv.org/abs/2611.23946) · [Repository](https://github.com/Hydr0pon1c/Mobilegym-lite)\
  *Scope and release note: Browser-simulator and training source are available, with separate data and accelerator requirements. Reported benefits of feature pruning depend on episode weighting and do not establish that less complete environments are universally better.*

- **[2026-11-18] RoboBuilder: Agentic Robot Co-Design with Real-world Video Feedback in the Loop** — `Benchmark`\
  Evaluates robot hardware and control-program co-design through simulation and physical builds, allowing agents to fit missing simulator mechanisms from measurements and revise simulator code after filmed real-world failures.\
  [Paper](https://arxiv.org/abs/2611.23855) · [Project](https://ghadinehme.com/robobuilder.github.io/) · [Repository](https://github.com/ghadinehme/RoboBuilder) · [Dataset](https://huggingface.co/datasets/DeCoDELab/RoboBuilder)\
  *Scope and release note: Simulator and benchmark source are available. Each later simulator correction targets one failed design and is not checked against other filmed runs; it does not establish a generally improved shared model.*

- **[2026-11-18] Phantom Success, Silent Failure: Auditing the Success Checkers of Simulated Manipulation Benchmarks** — `Benchmark` · **SimAudit**\
  Generates executable probes that expose disagreements between task instructions and simulator success checkers, validates the resulting states, and evaluates repaired predicates alongside the original checker.\
  [Paper](https://arxiv.org/abs/2611.25179)\
  *Scope and release note: Probes test physically executed or settled states, and repairs undergo expert-trajectory and defect-regression checks; this audits supplied worlds rather than learning dynamics.*

- **[2026-11-16] Solver to System: LLM Reasoning Across Representations and Execution in Scientific Simulation** — `Benchmark` · **Solver2System**\
  Tests whether models reconcile PDE solver code with equations, descriptions, and trajectories, and whether executing deliberately corrupted solvers helps identify physical invalidity and its causal defects.\
  [Paper](https://arxiv.org/abs/2611.21964) · [Repository](https://github.com/RohanS14/solver2system) · [Cross-representation data](https://huggingface.co/datasets/bermaneh/pde-llm-eval-cross-representation-dataset) · [Code-validity data](https://huggingface.co/datasets/bermaneh/pde-llm-eval-code-perturbation-dataset)

- **[2026-11-15] The Flip Test: Video World Models Fail to Learn the World State** — `Benchmark`\
  Probes physical outcome boundaries with minimal image pairs, matched controls, and dense sweeps, comparing video prediction with code-based measurement and agent-built MuJoCo scene rollouts.\
  [Paper](https://arxiv.org/abs/2611.19822) · [Author project page](https://romyluo.com/blog/fliptest/)\
  *Scope note: Simulation adds little over measurement in the reported comparison; inclusion does not imply that engine execution explains the coding agent's advantage.*

- **[2026-11-13] OCTAVE: A Capability-Resolved Benchmark for End-to-End HTML5 Game Generation** — `Benchmark`\
  Evaluates complete HTML5 game generation against public mechanics and hidden system requirements across eight capability dimensions, using static source-code judgments with a limited human play-testing cross-check.\
  [Paper](https://arxiv.org/abs/2611.17681) · [Project](https://rezona-ai.github.io/benchmark-site/) · [Repository](https://github.com/rezona-ai/octave-bench) · [Dataset](https://huggingface.co/datasets/rezonalab/game-benchmark)\
  *Scope and release note: Its runnability gate and main requirement scores come from source inspection, not automated runtime verification. Tasks, evaluation source, and recorded judgments are available.*

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

- **[2026-10-14] SynthDCB: World Distillation for Scalable Device Control Benchmarking** — `Benchmark`\
  Synthesizes device properties, Python functions, and environmental effects, composes them into stateful Home, Car, and Phone worlds, and evaluates tool-driven tasks through state checks and execution traces.\
  [Paper](https://arxiv.org/abs/2611.18639) · [Project](https://x-lance.github.io/SynthDCB/) · [Announcement repository](https://github.com/X-LANCE/SynthDCB)\
  *Date and release note: The abstract page reports October 14 as v1 despite the November identifier. Code and data remain marked coming soon as of November 18, 2026.*

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

- **[2026-10-07] DrugTargetWorld: A Synthetic Biobank for Training and Benchmarking AI Scientists** — `Benchmark`\
  Generates synthetic biobanks from hidden structural causal programs, executes budgeted experimental interventions, and scores agents’ causal conclusions against the same world’s concealed ground truth.\
  [Paper](https://arxiv.org/abs/2610.09558) · [Project](https://DrugTargetWorld.vercel.app/) · [Documentation repository](https://github.com/sammargolis/DrugTargetWorld/)\
  *Scope and release note: The repository contains documentation and reserved training/testing folders; generator, oracle, scorer, and harness source remain pending. A prebuilt benchmark route is documented but was not run; the causal mechanisms are designed, not recovered biological laws.*

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

- **[2026-09-30] WorldAuditBench: Interactive 3D World Auditing with Multimodal Agents** — `Benchmark`\
  Tests whether agents can expose and document injected collision, temporal, spatial, and semantic defects by navigating and interacting with executable Unreal Engine and Three.js worlds.\
  [Paper](https://arxiv.org/abs/2609.40325) · [Project](https://ucsb-nlp-chang.github.io/WorldAuditBench/) · [Repository](https://github.com/UCSB-NLP-Chang/WorldAuditBench)\
  *Scope and release note: Auditing and evaluation source is available, with environment downloads and external model clients required. Most tasks contain one hinted anomaly, and reports are graded by a model.*

- **[2026-09-28] GPUPhysBench: Benchmarking Coding Agents for Correct and Efficient GPU Physics Simulation** — `Benchmark`\
  Tests generated CUDA implementations of physical simulation operators and complete simulators, checking numerical correctness and runtime under specified governing equations and fixed execution budgets.\
  [Paper](https://arxiv.org/abs/2609.35639)

- **[2026-09-27] ArticulateArena: A Metric for Articulated Kinematics** — `Benchmark`\
  Evaluates articulated simulator assets by comparing the motions encoded by joints and kinematic trees, accounting for equivalent parameterizations; introduces ArticulateArena-20K and reassesses reconstruction methods.\
  [Paper](https://arxiv.org/abs/2609.33931) · [Project](https://heyumeng.com/ArticulateArena-web/) · [Repository](https://github.com/YumengHe/ArticulateArena)\
  *Release note: Metric implementation, examples, and rendering utilities are available; the complete 19,977-object dataset release was not verified.*

- **[2026-09-26] The GUI Is Not the State: Diagnosing State Aliasing in GUI World Models** — `Benchmark` · **StateAliasBench**\
  Pairs identical GUI observations and actions with different hidden states to test next-screen models, including Code2World and gWorld; a history-based estimator supplies state to a fixed interface that resolves action consequences before rendering.\
  [Paper](https://arxiv.org/abs/2609.32679)\
  *Scope and release note: The state interface includes family-specific transition logic and rendering constraints; gains do not isolate hidden-state estimation alone. No official implementation destination was verified.*

- **[2026-09-26] World Agent: Can Language Models Keep a World Running?** — `Benchmark`  
  Evaluates sustained maintenance of explicit world states and action-conditioned deduction through executable world interfaces, event contracts, and deterministic reference dynamics; it does not evaluate generated simulator code.  
  [Paper](https://arxiv.org/abs/2609.32692) · [Repository](https://github.com/HCPLab-SYSU/WorldAgent-Benchmark)  
  *Release note: benchmark cases and evaluation scripts are available; playback, rendering, and the playable demo remain on the release roadmap. Resource status was rechecked October 28, 2026; evaluations were not run.*

- **[2026-09-14] BVB: Benchmarking Agentic Video Understanding via Programmatic Reconstruction in Blender** — `Benchmark`  
  Evaluates agents that reconstruct videos as executable animated Blender scenes, measuring retained spatiotemporal facts and perceptual similarity under a shared execution budget.  
  [Paper](https://arxiv.org/abs/2609.15478) · [Project](https://yoloytang.me/BVB/) · [Repository](https://github.com/yunlong10/BVB)

- **[2026-08-30] GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments** — `Benchmark`\
  Tests whether GUI world models, including HTML-generating Code2World and gWorld, preserve context and action effects when their predictions are reused across reference-action and agent-driven rollouts.\
  [Paper](https://arxiv.org/abs/2609.00048) · [Repository](https://github.com/Fu-Fu-Fu-Fu/GUI-CC) · [Dataset](https://huggingface.co/datasets/minuzero/GUI-CC)

- **[2026-08-28] An Enclosed Mode Is a Gauge Choice: Topology Relative to Reach in Certified Code World Models** — `Benchmark`\
  Studies when unreachable regions make errors in synthesized dynamics untestable yet harmless, using controlled ring environments to separate sampling coverage, planner reachability, model repair, and the consequences of incorrect geometry.\
  [Paper](https://arxiv.org/abs/2608.28541) · [Repository](https://github.com/JaviMaligno/code-world-models)

- **[2026-08-18] An Omitted Mode Is a Rare Rule: The Sampling-Verification Danger Law in Continuous Code World Models** — `Benchmark`\
  Tests how sampled transition checks miss rare mode changes in continuous executable models, separating acceptance probability from planning regret and examining when additional evidence can repair missing rules.\
  [Paper](https://arxiv.org/abs/2608.17956) · [Repository](https://github.com/JaviMaligno/code-world-models)

- **[2026-08-11] ChemWorld: Programmable Chemical Worlds for Controlled and Replayable Agent Experimentation** — `Benchmark`\
  Compiles reusable chemical process and observation components into executable experimental worlds, separating public agent interfaces from private laws and supporting transactional replay and controlled rule interventions.\
  [Paper](https://arxiv.org/abs/2608.10792) · [Repository](https://github.com/sunyrain/ChemWorld-Public)

- **[2026-07-31] Simulation Code Generation for Fluid Systems using Large Language Models: Benchmarking Models and Prompting Strategies** — `Benchmark`\
  Evaluates generated translators from component graphs to WNTR and Modelica fluid-system programs, comparing code structure, parameter agreement, and simulated behavior against reference models.\
  [Paper](https://arxiv.org/abs/2607.29389)\
  *Scope and release note: Physical equations come from supplied simulator libraries; the benchmark tests executable model construction rather than dynamics discovery. No official implementation destination was verified.*

- **[2026-07-16] Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?** — `Benchmark`\
  Compares textual and executable game-model agents with separate simplification and replay-verification treatments, measuring public-game performance and resource use without claiming held-out generalization.\
  [Paper](https://arxiv.org/abs/2607.15439) · [Author-linked repository](https://github.com/astroseger/arc-3-agents-baseline1)

- **[2026-07-15] When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models** — `Benchmark`\
  Studies executable game models that pass sampled prediction checks yet mislead search, analyzing rare transition errors and hidden-state inference failures against their consequences for actual play.\
  [Paper](https://arxiv.org/abs/2607.14169) · [Repository](https://github.com/JaviMaligno/code-world-models)

- **[2026-06-30] ScratchWorld: Evaluating If World Models Compute Executable Consequences** — `Benchmark`\
  Uses replayable Scratch worlds to evaluate action-conditioned state changes, hidden state, causal traces, and counterfactuals, scoring correctly computed changes separately from unchanged-state copying.\
  [Paper](https://arxiv.org/abs/2606.31689)

- **[2026-06-29] Toward Secure and Reliable PDDL Formalization of Large Language Models with Planner-in-the-Loop Feedback** — `Benchmark`\
  Evaluates language-to-PDDL problem construction under fixed action domains, using planner diagnostics for localized repair and measuring solvability and agreement with reference plans across object-count difficulty levels.\
  [Paper](https://arxiv.org/abs/2606.29700) · [Repository](https://github.com/ibasicplan/NL-PDDL-Bench)\
  *Scope and release note: Evaluation and repair source plus a 1,000-instance test archive are available; the full dataset, fine-tuned weights, and complete training configurations remain pending. The task generates problem states and goals, not domain dynamics.*

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

- **[2026-05-08] EnvSimBench: A Benchmark for Evaluating and Improving LLM-Based Environment Simulation** — `Benchmark`\
  Tests predicted tool feedback and state edits against executor-produced service-environment transitions, supplying each sample with its true starting state and implementation context to isolate one-step simulation fidelity.\
  [Paper](https://arxiv.org/abs/2605.07247) · [Repository](https://github.com/cookieApril/EnvSimBench)\
  *Scope and release note: Benchmark data and evaluation source are available, but the README launcher path differs from the checked tree. Samples reset to recorded states, so the protocol does not measure compounding rollout error.*

- **[2026-04-26] PhysCodeBench: Benchmarking Physics-Aware Symbolic Simulation of 3D Scenes via Self-Corrective Multi-Agent Refinement** — `Benchmark`\
  Tests text-to-simulation programs across rigid, soft-body, fluid, and mechanical scenarios, measuring execution and rendered fidelity alongside engine-state assertions and conservation diagnostics; a cross-engine subset separates physical reasoning from API familiarity.\
  [Paper](https://arxiv.org/abs/2604.23580)

- **[2026-02-09] VisPhyWorld: Probing Physical Reasoning via Code-Driven Video Reconstruction** — `Benchmark`\
  Requires models to reconstruct observed physical scenes as executable simulation programs, then evaluates rendered appearance and motion across physics and graphics backends; VisPhyBench exposes inferred mechanisms rather than relying only on verbal answers.\
  [Paper](https://arxiv.org/abs/2602.13294) · [Project](https://tiger-ai-lab.github.io/VisPhyWorld/) · [Repository](https://github.com/TIGER-AI-Lab/VisPhyWorld)

- **[2025-02-18] Text2World: Benchmarking Large Language Models for Symbolic World Model Generation** — `Benchmark`  
  Evaluates text-to-PDDL world-model generation across diverse domains with multiple execution-based criteria.  
  [Paper](https://arxiv.org/abs/2502.13092) · [Project](https://text-to-world.github.io/) · [Repository](https://github.com/Aaron617/text2world)

- **[2023-05-24] ByteSized32: A Corpus and Challenge Task for Generating Task-Specific World Models Expressed as Text Games** — `Benchmark`\
  Provides 32 Python text-game worlds and evaluates generated task simulations for executable validity, requested objects and actions, physical constraints, and winnability, including interpreter-guided repair.\
  [Paper](https://arxiv.org/abs/2305.14879) · [Repository](https://github.com/cognitiveailab/BYTESIZED32)

Also see **CWMB** in the GIF-MCTS paper, **CombatStateBench** in Programmable World Model, and **Code4D** in Code2Worlds. These are not counted as additional papers.

## Adjacent renderers, perspectives, and data engines

- **[2026-11-19] ContextRenderer: Dynamic-Context Video Generation for Interactive Game Worlds** — `Perspective`\
  Renders engine-provided proxies with chunk-wise prompt and subject-reference updates, compressed visual history, and alignment across proxy formats; WorldPrism supplies paired observations from several world sources.\
  [Paper](https://arxiv.org/abs/2611.25838) · [Project](https://rainzor.github.io/contextrenderer/)\
  *Scope and release note: World state and interaction rules remain upstream. The project provides demonstrations; implementation, weights, and dataset-release destinations were not verified.*

- **[2026-11-18] Game2Player: Scaling Gameplay Experience for Visual Agents through Environment-Player Co-Development** — `Perspective`\
  Adapts existing web games into state-observable task environments, uses player feedback to repair their implementations and verifiers, and collects progress-labeled trajectories for visual-policy training; introduces PlayerBench.\
  [Paper](https://arxiv.org/abs/2611.24154) · [Project](https://game2player.github.io/) · [Repository](https://github.com/game2player/Game2Player)\
  *Release and scope note: Environment-building, rollout, and training source are available; third-party game builds and assets are excluded and must be reconstructed from their sources. This is an executable-environment data engine, not a learned dynamics model.*

- **[2026-11-17] Code World Model 2.0: Towards Infinite Controllable Video Generation** — `Perspective` · **Invoker-Render**\
  Renders engine-defined proxy streams at varying geometric detail through bidirectional and causal video models, progressively training few-step generation on increasingly self-generated histories while world rules remain upstream.\
  [Paper](https://arxiv.org/abs/2611.22925) · [Project](https://www.inclusion-ai.org/CodeWorldModel/) · [Repository](https://github.com/inclusionAI/CodeWorldModel) · [Models](https://huggingface.co/inclusionAI/invoker-render-1.0)

- **[2026-11-17] When the World Is the Test Suite: Agentic Intelligence for the Physical World** — `Perspective`\
  Surveys how agents construct and verify physical programs, including generated training worlds, distinguishing execution, task feasibility, and intended physical behavior while examining how accepted programs become reusable experience.\
  [Paper](https://arxiv.org/abs/2611.22291) · [Project](https://physicalworldagent.github.io/) · [Companion reading list](https://github.com/PhysicalWorldAgent/Awesome-PhysicalWorldAgent)

- **[2026-11-11] CoCode-World: Shared 3D Proxy Representation for Multi-Player World Models** — `Perspective`\
  Jointly renders two player views from a shared geometric proxy and appearance references, adapting a video model to coordinate cross-view identity while game-engine state supplies layout, motion, and occlusion.\
  [Paper](https://arxiv.org/abs/2611.15602) · [Project](https://iapple233.github.io/CCW/) · [Repository](https://github.com/IApple233/CoCode-World)\
  *Release and scope note: This is the paper associated with the separately tracked CoCode-World release above; new-action dynamics remain outside the renderer.*

- **[2026-11-09] PhysOPSD: Code as Privilege for Physically Plausible Video Generation** — `Perspective`\
  Constructs verified simulation programs and paired physical variations to supervise on-policy video-model self-distillation, transferring draft-conditioned physical guidance into a generator that runs without the simulator at inference.\
  [Paper](https://arxiv.org/abs/2611.12411) · [Project](https://haroldchen19.github.io/PhysOPSD-site/) · [Announcement repository](https://github.com/aigc3d/PhysOPSD)\
  *Release and scope note: The repository provides paper resources; training and inference code are pending approval, and pretrained weights are not included as of November 14, 2026.*

- **[2026-11-08] From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models** — `Perspective` · **Script2Play**\
  Uses coding agents to build skill-conditioned games, scene generators, rule mirrors, and state-based verifiers, then records successful programmatic teachers to train a visual game policy by behavior cloning.\
  [Paper](https://arxiv.org/abs/2611.11136)

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

- **[2026-08-27] Magpie: Real-Time World Renderer for Interactive Games** — `Perspective`\
  Keeps authored gameplay rules and persistent state in a game engine, streams its white-box observations to a video renderer, and retrieves viewpoint-relevant visual history while the engine resolves player actions.\
  [Paper](https://arxiv.org/abs/2608.27168)\
  *Scope note: Reported rendering throughput excludes chunk collection and transfer; the paper estimates approximately 1.55 seconds of action-to-observation latency. No official implementation destination was verified.*

- **[2026-08-26] Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models** — `Perspective`  
  Proposes human–engine verification as a source of grounded feedback and trajectory data for world-model training, rather than introducing another learned transition model.  
  [Paper](https://arxiv.org/abs/2608.25518)

- **[2026-07-30] Video Models as Native 4D Renderers: World-Grounded Conditioning from Animated Mesh** — `Perspective` · **DAR**\
  Conditions a video renderer on persistent surface identities, world positions, normals, and camera rays from animated meshes, using programmatically assembled Blender and Unreal scenes; the upstream scene specifies motion rather than the renderer learning executable transition rules.\
  [Paper](https://arxiv.org/abs/2608.00094)

- **[2026-07-23] Closing the Loop: Training-Free Revisit Consistency for Autoregressive Generative Rendering** — `Perspective`\
  Retrieves earlier video latents by camera pose and uses depth reprojection to guide attention when revisiting engine-defined scenes, improving rendering consistency while leaving world geometry and dynamics upstream.\
  [Paper](https://arxiv.org/abs/2607.21848) · [Project](https://wenchao-m.github.io/ClosetheLoop.github.io/)\
  *Release note: The project provides demonstrations, but its Code button has no implementation destination as of November 16, 2026.*

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
