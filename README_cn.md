# Awesome-World-Model

<p align="center">
  中文 | <a href="README_EN.md">English</a>
</p>

<div align="center">
  <img src="assets/Gemini_Generated_Image_awesome_world_model.png" alt="Survey Framework" width="82%">
</div>

[![Awesome](https://awesome.re/badge.svg)](https://github.com/pm1255/Awesome-World-Model)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-red)

<a id="intro"></a>
## 👋 简介
当前的人工智能，特别是在强化学习（RL）和自主智能体（Autonomous Agents）领域，在复杂、动态且不可预测的真实世界中进行规划与决策时，仍面临巨大挑战。传统的“无模型”（Model-Free）方法往往依赖大量的试错（Trial-and-Error），数据效率极低，且难以推广到未曾见过的场景。即便是在其他领域表现优异的大语言模型（LLM），也常常因为缺乏对物理世界运作规律的深刻理解（缺乏“常识”），而表现出推理能力不稳、规划脱离实际等问题。

为解决这些瓶颈，世界模型（World Model）逐渐成为 AI 迈向更高阶智能的关键研究方向。世界模型旨在为 AI 系统构建一个关于外部世界的“内部心智模型”：它能够理解物理定律、因果关系以及环境的动态变化。通过这一模型，智能体可以在其“头脑”中进行内部模拟（Simulate）——不仅能准确感知当前状态，还能利用想象力（Imagination）预测未来、评估不同行动的后果，从而实现高效的规划、反思与推理，而无需在真实环境中承担试错的代价。

Awesome-World-Model 是一个专门围绕 AI 世界模型（World Models）及其在强化学习、具身智能、自动驾驶及多模态感知等领域应用构建的资源汇编仓库。它系统性地收集相关的研究论文、开源框架、基准测试（Benchmarks）以及前沿实践。该仓库致力于梳理世界模型这一跨学科领域的快速发展脉络，连接深度学习、生成式模型（尤其是视频生成）、控制理论、计算机视觉与认知科学等多个研究方向。

---

<a id="goals"></a>
## 🎯 仓库目标
我们致力于建立一个中心化、持续演进的知识库，为研究人员和从业者提供关于 AI 世界模型（World Models）的高价值参考资料。我们的最终目标是加速具身智能（Embodied AI）、自主智能体（Autonomous Agents）以及基础多模态模型的发展，使其能够深刻理解物理世界的运作规律，具备强大的想象力、长期规划能力以及高效的数据利用率，从而在复杂、未知的真实环境中实现可靠决策。

---

<a id="scope"></a>
## 📏 项目范围
本仓库核心关注使 AI 系统能够构建外部世界（包括物理、因果和社会规律）内部心智模型（Mental Models）的机制、架构与应用，而非单纯关注通用的生成式模型（除非涉及将视频/图像生成作为世界模拟器）。内容涵盖从基础理论研究（如表征学习）到具体的工程实践（如模拟器和部署）。

### 🌀 包含内容（In Scope）
- 世界模型架构设计：专门用于学习环境动态（Environment Dynamics）的潜在空间模型（Latent Space Models）、预测性编码（Predictive Coding）架构、递归神经网络（RNNs/Transformers）作为转换器的模型。
- 面向世界模型的表征学习：学习具有因果关系（Causality）、物理意义或对象中心（Object-Centric）的表征，以及自监督学习（Self-Supervised Learning）在构建世界模型中的应用。
- 模拟与想象机制：使用生成式视频/图像模型（如扩散模型、GANs）作为可交互的世界模拟器（World Simulators），以及智能体在内部模型中的“梦境”（Dreaming）或模拟（Simulation-in-the-head）。
- 基于模型的规划与控制（MPC）：将世界模型与轨迹规划、树搜索（MCTS）或梯度优化（Gradient Descent）相结合的决策方法。
- 基于世界模型的强化学习（MBRL）：使用学习到的世界模型来加速策略优化（Policy Optimization），通过“想象”进行离线或在线 RL。
- 特定领域的应用：用于自动驾驶、具身机器人操作、导航以及科学模拟的世界模型。
- 认知科学与生物学灵感：关于海马体（Hippocampus）或大脑皮层（Neocortex）如何构建环境图谱的神经科学模型，及其对 AI 世界模型的启示。
- 评估与基准测试：用于衡量世界模型的预测精度、规划效率、数据效率和概括（Generalization）能力的 Benchmarks 和 Datasets。
- 开源框架与工具：专门用于构建和测试世界模型的代码库和模拟环境。

### 🌀 不包含内容（Out of Scope）
- 通用的视频或图像生成研究：如果其目的并非作为世界模型来支持智能体的规划或理解（例如：一般的艺术生成、无条件的视频插帧）。
- 通用的无模型（Model-Free）强化学习：除非其展示了与世界模型的结合（例如作为 Actor-Critic 中的基线，但重点不在世界模型本身）。
- 单纯的大语言模型（LLM）推理：除非其研究集中于 LLM 如何作为世界的逻辑或常识模型，并应用于物理实体。
- 传统的确定性物理模拟器：除非其专注于从数据中学习（Learn from Data）物理规律，或作为构建数据驱动世界模型的工具。
- 通用的机器学习或计算机视觉方法：缺乏直接的世界模型应用场景。

---

<a id="news"></a>
## 🔔 近期热点研究与新闻
- 2026-04-04 – 🎉 仓库初始化

---

<a id="toc"></a>
## 🗺️ 目录表
- [简介](#intro)
- [仓库目标](#goals)
- [项目范围](#scope)
- [近期热点研究与新闻](#news)
- [核心概念](#core-concepts)
- [论文列表](#papers)
  - [综述](#surveys)
  - [方法类与框架类论文](#methods-frameworks)
  - [数据集和评估基准类论文](#datasets-benchmarks)
- [仓库资源](#resources)
  - [测试基准](#benchmarks)
  - [多媒体资源](#multimedia)
- [如何贡献](#contributing)
- [社区和支持](#community-support)

---

<a id="core-concepts"></a>
## 🧠 核心概念

- **世界模型（World Model）**：一个人工智能系统的内部心智模型，旨在理解物理世界的运作规律、因果关系以及环境的动态变化。它赋予智能体“想象力”，使其能够在内部模拟未来状态、评估行动后果，从而实现高效的规划与决策，而无需在真实环境中进行昂贵的试错。
- **状态表征学习（State Representation Learning）**：将高维、冗余的原始观测数据（如图像、视频）转化为低维、紧凑且包含关键语义信息的潜在向量（Latent Vectors）的过程。优秀的表征应具备马尔可夫性质，并能够解耦出环境中的不同实体及其属性。
- **转换模型 / 动态模型（Transition Model / Dynamics Model）**：世界模型的核心组件，负责预测在当前状态下执行特定行动后，环境将如何演化到下一个状态（$S_t, A_t \rightarrow S_{t+1}$）。它捕捉了环境的物理规律和因果逻辑。
- **潜在空间模拟（Latent Space Simulation）**：在低维潜在空间中进行未来的预测和推演，而非在原始像素空间。这极大地提高了计算效率，并允许模型关注高层语义变化而忽略无关细节。
- **基于模型的规划（Model-Based Planning）**：智能体利用世界模型在前瞻（Lookahead）或“梦境”（Dreaming）中搜索最优行动序列的过程。常用算法包括模型预测控制（MPC）、蒙特卡洛树搜索（MCTS）等。
- **基于模型的强化学习（Model-Based Reinforcement Learning, MBRL）**：一种强化学习范式，智能体首先学习一个世界模型，然后利用该模型生成模拟经验来训练策略（Policy）或价值函数（Value Function），从而显著提高数据效率。
- **可微物理引擎（Differentiable Physics Engine）**：一种能够计算输出对输入梯度的物理模拟器。当集成到世界模型中时，它允许通过梯度下降直接优化控制策略，实现极具效率的学习。
- **对象中心表征（Object-Centric Representation）**：将环境视为一组离散对象及其相互作用的表征方式。这种方式符合人类认知，有助于提高模型对未见过场景的泛化能力和因果推理能力。
- **多模态世界模型（Multimodal World Model）**：能够处理和整合多种感知模态（如视觉、语言、触觉、动作）的世界模型。它利用不同模态的互补信息来构建更全面、更鲁棒的环境理解。
- **因果发现与推理（Causal Discovery & Reasoning）**：在世界模型中区分相关性（Correlation）与因果性（Causation）的能力。这使智能体能够理解“如果我这样做，会发生什么”（Intervention），并进行反事实推理（Counterfactual Reasoning）。
- **认知地图（Cognitive Map）**：世界模型的一种特定形式，侧重于对环境空间结构、拓扑关系以及关键地标的内部表征，常用于导航和长期规划任务。
- **广义世界模型 / 基础世界模型（General / Foundation World Model）**：在海量、多样化数据（如互联网规模的视频）上预训练的具有强大泛化能力的世界模型。它可以作为下游具身智能任务（如机器人操控、自动驾驶）的通用物理常识库。

---

<a id="papers"></a>
## 📚 论文列表
以下论文按发表日期排列：

<a id="surveys"></a>
<details>
  <summary><strong>综述</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>时间</strong></td>
      <td><strong>论文与摘要</strong></td>
      <td><strong>标签</strong></td>
      <td><strong>链接</strong></td>
    </tr>
     <tr>
      <td><strong>Date</strong></td>
      <td><strong>Paper & Summary</strong></td>
      <td><strong>Tags</strong></td>
      <td><strong>Links</strong></td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-03-05</td>
      <td style="width: 55%;"><strong>Learning to Model the World: A Survey of World Models in Artificial Intelligence</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Long%20Context-blue" alt="Long Context">
      </td>
      <td style="width: 15%;"><a href="https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.177274570.09578608/v1">
      <img src="https://img.shields.io/badge/TechRxiv-Paper-orange" alt="TechRxiv Badge">
    </a></td>
    </tr>
    <tr>
      <td colspan="3">
            • 系统梳理了人工智能中 world model 的研究脉络，指出该方向正在从经典的状态预测与潜变量建模，逐步扩展到由大规模生成模型和多模态基础模型驱动的更通用建模范式。<br>
            • 将现有方法归纳为多类代表性路线，包括观测层生成式 world model、潜空间 world model、基于强化学习的 world model，以及面向复杂场景建模的对象中心方法。<br>
            • 进一步总结了 world model 在机器人、自主驾驶、科学发现、游戏仿真、GUI 智能体等领域的应用，并系统讨论了评测基准、评价指标、仿真平台以及长时程一致性、泛化能力与可信性等关键开放问题，为后续研究提供了较完整的参考框架。
        </td>
    </tr>
  </table>
</details>

<a id="methods-frameworks"></a>
<details>
  <summary><strong>方法类与框架类论文</strong></summary>


  <table style="width: 100%;">
    <tr>
      <td><strong>时间</strong></td>
      <td><strong>论文与摘要</strong></td>
      <td><strong>标签</strong></td>
      <td><strong>链接</strong></td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-03-11</td>
      <td style="width: 55%;"><strong>EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/RL Training-red" alt="safety">
        <img src="https://img.shields.io/badge/Physical Consistency-yellow" alt="Evolution">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2406.08407">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
      <tr>
      <td colspan="3">
            • 该工作关注机器人视频 world model 中的一个核心问题：生成的视频轨迹可能在视觉上看似合理，但并不一定对应物理可执行、运动学一致的真实机器人动作，这种偏差被作者称为 executability gap。<br>
            • 为解决这一问题，论文提出 EVA，一种基于强化学习的后训练对齐框架：先利用真实机器人轨迹训练逆动力学模型，再将其作为奖励模型，根据生成视频所诱导出的动作序列来评估视频质量。<br>
            • EVA 通过鼓励更平滑的速度、加速度和 jerk 变化，并惩罚超出 embodiment 约束或不稳定的动作，减少了生成轨迹中的机器人伪影，最终提升了 RoboTwin 基准和真实双臂机器人上的下游执行成功率。
        </td>
    </tr>
  </table>
</details>

<br>


<a id="datasets-benchmarks"></a>
<details>
  <summary><strong>数据集和评估基准类论文</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>时间</strong></td>
      <td><strong>论文与摘要</strong></td>
      <td><strong>标签</strong></td>
      <td><strong>链接</strong></td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-03-04</td>
      <td style="width: 55%;"><strong>MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Physics Consistency-yellow" alt="Personalized">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2406.08407">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
      <tr>
      <td colspan="3">
            • MMWorld 提出了一个面向视频的 world-model 能力评测基准，重点考察多模态模型对真实世界动态过程、因果关系以及复杂时序信息的理解与推理能力。<br>
            • 它的两个核心特点是：一方面具有跨学科属性，覆盖 7 个大类和 69 个子学科；另一方面具有多维推理属性，涉及解释、反事实推理、未来预测等多种世界理解能力。<br>
            • 整个 benchmark 包含 1,910 个视频、6,627 组问答及相关字幕。实验结果表明，即使是较强的闭源和开源多模态模型，在该基准上仍然表现有限，说明视频场景下的 world-model 评测仍有很大提升空间。
        </td>
    </tr>
  </table>
</details>

---

<a id="resources"></a>
## 🧰 仓库资源

<a id="benchmarks"></a>
### 📊 测试基准

| 任务类型 | 数据集和评估基准 |
| --- | --- |
| **物理一致性** | [MMWorld](https://arxiv.org/abs/2406.08407) |

<a id="multimedia"></a>
### 🎥 多媒体资源

<table>
  <thead>
    <tr>
      <th>类型</th>
      <th>网址链接</th>
      <th>内容简介</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="1"><strong>Tutorial</strong></td>
      <td>https://world-model-tutorial.github.io/</td>
      <td>CVPR 2025 Tutorial: From Video Generation to World Model</td>
    </tr>
  </tbody>
</table>

---

<a id="contributing"></a>
## 🤝 如何贡献
提交样式：

```text
Title: [paper's title]
Head: [head name1] (, [head name2] ...)
Published: [arXiv / ACL / ICLR / NeurIPS / ...]
Summary:
  - Innovation:
  - Tasks:
  - Significant Result:
```

---

<a id="community-support"></a>
## 💬 社区和支持

加入我们的社区，提出问题，分享您的项目，并与其他开发人员联系。

- **GitHub Issues**：在我们的 [GitHub Issues](https://github.com/pm1255/Awesome-World-Model/issues) 中报告问题或提出功能需求。
- **GitHub Pull Requests**：通过 [Pull Requests](https://github.com/pm1255/Awesome-World-Model/pulls) 提交代码改进。
- **小红书**：扫描下方二维码加入我们的讨论组，获取最新的 World Model 相关研究信息，或推广您的相关研究成果。

<div align="center">
  <img src="assets/rednote-qr-code.jpg" alt="QR Code" width="255">
</div>
