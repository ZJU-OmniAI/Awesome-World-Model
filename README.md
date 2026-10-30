# Awesome World Model

**English** | [简体中文](README_cn.md)

[![Awesome](https://awesome.re/badge.svg)](https://github.com/ZJU-OmniAI/Awesome-World-Model)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE.txt)
[![Papers](https://img.shields.io/badge/Papers-67-blue.svg)](docs/paper-index.md)

> **A survey of world representations, future prediction, and embodied action.**
>
> We study what world models predict, how predictions inform actions, and what evidence shows that they help an agent make better decisions.

World models connect internal representations of the environment with predictions of future states. For robotic manipulation, their value depends on how these predictions inform planning and control. Predictive interfaces and action-generation architectures define the main methodological choices; long-term state consistency, action fidelity, and action-sufficient representations remain central research challenges.

## Topics

| Order | Topic | Key question | Overview |
|---|---|---|---|
| 01 | World model primer | What is represented and predicted? | [Concepts and terminology, Chinese](docs/01-world-model-primer.md) |
| 02 | World models for action | What information reaches the policy, and how? | [Interfaces and architectures, Chinese](docs/02-world-action-models.md) |
| 03 | Research problems | Can predictions preserve state, follow actions, and support control? | [Methods, evidence, and open questions, Chinese](docs/03-problem-taxonomy.md) |

[Complete paper index](docs/paper-index.md)

## 1. World model primer

A world model represents aspects of the environment and predicts their evolution. For action-conditioned prediction, a useful conceptual decomposition is:

$$
z_t=E(o_{\le t},a_{<t}),\qquad
\hat z_{t+1}\sim p_\theta(z_{t+1}\mid z_t,a_t).
$$

The internal state may contain latent features, objects, geometry, or memory. Predictions can be decoded into observations or used directly for planning and policy learning. [World Models](https://arxiv.org/abs/1803.10122) and [Dreamer](https://arxiv.org/abs/1912.01603) provide foundational examples.

Two connected perspectives are representing the current world and predicting possible futures. Applications include interactive games, robotics, driving, and social simulation, but their state spaces and evaluation criteria differ. [GameNGen](https://arxiv.org/abs/2408.14837) and [Generative Agents](https://arxiv.org/abs/2304.03442) illustrate this breadth.

## 2. World Action Models

A policy predicts actions from observations and instructions. An action-conditioned world model predicts the consequences of a specified action. WAMs combine predictive world modeling with action generation. A language-conditioned video plan and a simulator that responds to numerical actions provide different interfaces. [WAM survey](https://arxiv.org/abs/2605.12090)

| Architecture | Approach | Representative work |
|---|---|---|
| Cascaded, explicit future | Video or visual subgoals followed by learned action extraction | [UniPi](https://arxiv.org/abs/2302.00111), [VLP](https://arxiv.org/abs/2310.10625), [MVA](https://arxiv.org/abs/2607.19343) |
| Cascaded, motion interface | Flow or geometry followed by control | [AVDC](https://arxiv.org/abs/2310.08576), [Im2Flow2Act](https://arxiv.org/abs/2407.15208), [Dream2Flow](https://arxiv.org/abs/2512.24766) |
| Cascaded, predictive features | Latent or hidden-state conditioning of an action model | [VPP](https://arxiv.org/abs/2412.14803), [RynnWorld-4D](https://arxiv.org/abs/2607.06559) |
| Joint, autoregressive backbone | Shared sequence modeling of world and action | [WorldVLA](https://arxiv.org/abs/2506.21539), [RynnVLA-002](https://arxiv.org/abs/2511.17502) |
| Joint, shared-stream diffusion | Shared world and action objectives | [UWM](https://arxiv.org/abs/2504.02792), [FLARE](https://arxiv.org/abs/2505.15659), [DreamZero](https://arxiv.org/abs/2602.15922) |
| Joint, multiple streams | Modality-specific experts and cross-stream interaction | [Motus](https://arxiv.org/abs/2512.13030), [LingBot-VA](https://arxiv.org/abs/2601.21998), [Fast-WAM](https://arxiv.org/abs/2603.16666) |

Predictive interfaces, training objectives, and inference procedures are distinct architectural dimensions. Im2Flow2Act connects a motion interface to a learned policy, while FLARE uses latent future supervision. Diffusion models can also roll out autoregressively over time, and joint training can coexist with cascaded inference.

![DreamZero: joint video-action training and closed-loop execution](assets/figures/dreamzero.png)

*Figure from [DreamZero](https://arxiv.org/abs/2602.15922): future prediction and action generation share a model, with real observations updating the execution context.*

Future information can provide training supervision, predictive features, explicit visual plans, or candidate-action evaluations. [Fast-WAM](https://arxiv.org/abs/2603.16666) removes the future branch at inference, whereas [LaWAM](https://arxiv.org/abs/2606.15768) exposes predicted latent subgoals to the action model. These choices create different trade-offs between predictive information and deployment cost.

## 3. Research problems

| Problem | Question | Representative work |
|---|---|---|
| Long-term state consistency | Does the same world persist after revisits, occlusion, or several task stages? | [Spatial Memory](https://arxiv.org/abs/2506.05284), [RELIC](https://arxiv.org/abs/2512.04040), [WorldDP](https://arxiv.org/abs/2606.08775) |
| Action and physical correctness | Do specified actions affect trajectories and interactions correctly? | [Ctrl-World](https://arxiv.org/abs/2510.10125), [PhysisForcing](https://arxiv.org/abs/2606.28128), [EVA](https://arxiv.org/abs/2603.17808), [ABot-PhysWorld](https://arxiv.org/abs/2603.23376) |
| Action-sufficient representations | Does the predictive interface retain information needed for the task? | [LaWAM](https://arxiv.org/abs/2606.15768), [AGRA](https://arxiv.org/abs/2606.12217) |

[DexWorldModel](https://arxiv.org/abs/2604.16484) spans semantic prediction, memory, and efficient inference. Object-centric planning does not by itself establish long-term memory. Likewise, visual quality, causal action response, and robot executability require different evidence.

## Evaluation and research discussion

World-model evaluation spans perceptual and manipulative quality ([WorldSimBench](https://arxiv.org/abs/2410.18072)), physical prediction ([Physics-IQ](https://arxiv.org/abs/2501.09038)), embodied video quality ([EWMBench](https://arxiv.org/abs/2505.09694)), and video understanding ([MMWorld](https://arxiv.org/abs/2406.08407)). Robot success rates additionally depend on embodiment, data, task split, and execution protocol.

[Experimental results](docs/03-problem-taxonomy.md#evidence) illustrate these different evaluation settings. Open questions include how to combine persistent object state with fast action dynamics, retrieve task-relevant memories, and choose predictive modalities under a fixed computational budget.

## Papers and resources

- [Paper index](docs/paper-index.md).
- [CVPR 2025 tutorial: From Video Generation to World Model](https://world-model-tutorial.github.io/).
- [Awesome Closed-Loop VLA](https://github.com/ZJU-OmniAI/Awesome-Closed-Loop-VLA/blob/main/README_zh.md): execution, prediction, and learning loops for robot agents.
- [Figures and references](assets/figures/README.md).
