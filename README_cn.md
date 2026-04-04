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
  - [模型和系统类论文](#models-systems)
- [仓库资源](#resources)
  - [测试基准](#benchmarks)
  - [开源系统](#open-source-systems)
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
      <td rowspan="2" style="width: 15%;">2026-03-05</td>
      <td style="width: 55%;"><strong>Beyond the Context Window: A Cost-Performance Analysis of Fact-Based Memory vs. Long-Context LLMs for Persistent Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Long%20Context-blue" alt="Long Context">
        <img src="https://img.shields.io/badge/Cost%20Analysis-brightgreen" alt="Cost Analysis">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2603.04814">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 解决业界关于长上下文模型与外部记忆系统在构建持久化代理时的效能与成本优劣之争。<br>
        • 在三大主流记忆基准上，从准确率与累计 API 推理成本双重维度，系统交叉评测长上下文与事实型外部记忆方案。<br>
        • 长上下文在事实召回上具有优势，但成本随轮次递增；在 100k 上下文长度下，记忆系统在约 10 轮交互后即可实现成本反超，为实际工程选型提供了量化依据。
      </td>
    </tr>
  </table>
</details>

<br>

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
      <td style="width: 55%;"><strong>Governing Evolving Memory in LLM Agents: Risks, Mechanisms, and the Stability and Safety Governed Memory (SSGM) Framework</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Safety-red" alt="Safety">
        <img src="https://img.shields.io/badge/Evolution-brightgreen" alt="Evolution">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2603.11768v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 大模型智能体的记忆系统正从静态检索转向动态自主更新，这虽然提升了智能体的适应性，但也引发了严峻的稳定与安全问题。其中包括语义漂移、固化错误工作流的程序漂移、外部恶意注入的记忆投毒。<br>
        • 提出稳定与安全治理记忆（SSGM）框架。该框架的核心设计理念是将智能体的“生成式认知策略”与“底层记忆存储介质”彻底解耦。它在两者之间引入了一个主动拦截的治理中间件，使记忆的更新不再是盲目的直接写入，而是必须经过多重网关的审查。<br>
        • 合并前验证：在写入前进行逻辑一致性检查，拒绝与核心事实相矛盾的更新，防止幻觉被固化。时间与权限过滤：在读取时结合衰减函数过滤过期失效数据，并基于访问控制防止跨用户隐私泄露。可逆的定期对齐：采用“可变活动图 + 不可变情景日志”的双轨存储结构，系统会定期将当前记忆与不可变日志进行对齐与错误回滚，从而在数学上为长期的“语义漂移”设定了严格的误差上限。
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
      <td rowspan="1" style="width: 15%;">2026-03-04</td>
      <td style="width: 55%;"><strong>Towards Realistic Personalization: Evaluating Long-Horizon Preference Following in Personalized User-LLM Interactions</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Personalized-yellow" alt="Personalized">
        <img src="https://img.shields.io/badge/Interaction-blue" alt="Interaction">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2603.04191">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
  </table>
</details>

<br>

<a id="models-systems"></a>
<details>
  <summary><strong>模型和系统类论文</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>时间</strong></td>
      <td><strong>论文与摘要</strong></td>
      <td><strong>标签</strong></td>
      <td><strong>链接</strong></td>
    </tr>
    <tr>
      <td rowspan="1" style="width: 15%;">2026-03-15</td>
      <td style="width: 55%;"><strong>SuperLocalMemory V3: Information-Geometric Foundations for Zero-LLM Enterprise Agent Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Information%20Geometry-red" alt="Information Geometry">
        <img src="https://img.shields.io/badge/Agent%20Memory-teal" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Data%20Sovereignty-blue" alt="Data Sovereignty">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2603.14588">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
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
| **个性化任务评估** | [IMPLEXCONV](https://aclanthology.org/2025.emnlp-main.580.pdf), [PERSONAMEM](https://arxiv.org/pdf/2504.14225), [PERSONAMEM-v2](https://www.arxiv.org/pdf/2512.06688), [PersonaBench](https://aclanthology.org/2025.findings-acl.49.pdf), [PersonaFeedback](https://arxiv.org/pdf/2506.12915), [LaMP](https://aclanthology.org/2024.acl-long.399.pdf), [MemDaily](https://arxiv.org/pdf/2409.20163), [MPR](https://arxiv.org/pdf/2508.13250), [KnowMe-Bench](https://arxiv.org/abs/2601.04745) |

<a id="open-source-systems"></a>
### 💻 开源系统
下面系统按照时间顺序排列：

| 系统 | 时间 | 关注数 | 开源网址和官方网站 |
| --- | --- | --- | --- |
| Zep | 2023-05-19 | ![GitHub Repo stars](https://img.shields.io/github/stars/getzep/zep?style=social) | [GitHub](https://github.com/getzep/zep)<br>[Official Website](https://www.getzep.com/) |

<a id="multimedia"></a>
### 🎥 多媒体资源

<table>
  <thead>
    <tr>
      <th>类型</th>
      <th>网址链接</th>
      <th>视频内容简介</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>记忆基本理论</strong></td>
      <td><a href="https://www.youtube.com/watch?v=k3FUWWEwgfc">https://www.youtube.com/watch?v=k3FUWWEwgfc</a></td>
      <td>基于 LangGraph 的短期记忆</td>
    </tr>
    <tr>
      <td><strong>记忆相关工具</strong></td>
      <td><a href="https://www.bilibili.com/video/BV1hom8YAEhX">https://www.bilibili.com/video/BV1hom8YAEhX</a></td>
      <td>记忆 Agent</td>
    </tr>
    <tr>
      <td><strong>记忆相关论文</strong></td>
      <td><a href="https://www.bilibili.com/video/BV1XT8ez6E46">https://www.bilibili.com/video/BV1XT8ez6E46</a></td>
      <td>AI Agent 记忆综述</td>
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
