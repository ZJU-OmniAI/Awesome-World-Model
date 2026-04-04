# Awesome-World-Model

<p align="center">
    【中文 | <a href="README.md">English</a>】
</p>

<div align="center">
    <img src="assets/Gemini_Generated_Image_awesome_world_model.png" alt="Survey Framework" width="82%">
</div>

[![Awesome](https://awesome.re/badge.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![](https://img.shields.io/badge/PRs-Welcome-red)


## 👋 简介
当前的人工智能，特别是在强化学习（RL）和自主智能体（Autonomous Agents）领域，在复杂、动态且不可预测的真实世界中进行规划与决策时，仍面临巨大挑战。传统的“无模型”（Model-Free）方法往往依赖大量的试错（Trial-and-Error），数据效率极低，且难以推广到未曾见过的场景。即便是在其他领域表现优异的大语言模型（LLM），也常常因为缺乏对物理世界运作规律的深刻理解（缺乏“常识”），而表现出推理能力不稳、规划脱离实际等问题。

为解决这些瓶颈，世界模型（World Model） 逐渐成为 AI 迈向更高阶智能的关键研究方向。世界模型旨在为 AI 系统构建一个关于外部世界的“内部心智模型”：它能够理解物理定律、因果关系以及环境的动态变化。通过这一模型，智能体可以在其“头脑”中进行内部模拟（Simulate）——不仅能准确感知当前状态，还能利用想象力（Imagination）预测未来、评估不同行动的后果，从而实现高效的规划、反思与推理，而无需在真实环境中承担试错的代价。

Awesome-World-Model 是一个专门围绕 AI 世界模型（World Models） 及其在强化学习、具身智能、自动驾驶及多模态感知等领域应用构建的资源汇编仓库。它系统性地收集相关的研究论文、开源框架、基准测试（Benchmarks）以及前沿实践。该仓库致力于梳理世界模型这一跨学科领域的快速发展脉络，连接深度学习、生成式模型（尤其是视频生成）、控制理论、计算机视觉与认知科学等多个研究方向。

---

## 🎯 仓库目标
我们致力于建立一个中心化、持续演进的知识库，为研究人员和从业者提供关于 AI 世界模型（World Models）的高价值参考资料。我们的最终目标是加速具身智能（Embodied AI）、自主智能体（Autonomous Agents）以及基础多模态模型的发展，使其能够深刻理解物理世界的运作规律，具备强大的想象力、长期规划能力以及高效的数据利用率，从而在复杂、未知的真实环境中实现可靠决策。

---

## 📏 项目范围
本仓库核心关注使 AI 系统能够构建外部世界（包括物理、因果和社会规律）内部心智模型（Mental Models）的机制、架构与应用，而非单纯关注通用的生成式模型（除非涉及将视频/图像生成作为世界模拟器）。内容涵盖从基础理论研究（如表征学习）到具体的工程实践（如模拟器和部署）。

🌀 包含内容（In Scope）
- 世界模型架构设计： 专门用于学习环境动态（Environment Dynamics）的潜在空间模型（Latent Space Models）、预测性编码（Predictive Coding）架构、递归神经网络（RNNs/Transformers）作为转换器的模型。

- 面向世界模型的表征学习： 学习具有因果关系（Causality）、物理意义或对象中心（Object-Centric）的表征，以及自监督学习（Self-Supervised Learning）在构建世界模型中的应用。

- 模拟与想象机制： 使用生成式视频/图像模型（如扩散模型、GANs）作为可交互的世界模拟器（World Simulators），以及智能体在内部模型中的“梦境”（Dreaming）或模拟（Simulation-in-the-head）。

- 基于模型的规划与控制（MPC）： 将世界模型与轨迹规划、树搜索（MCTS）或梯度优化（Gradient Descent）相结合的决策方法。

- 基于世界模型的强化学习（MBRL）： 使用学习到的世界模型来加速策略优化（Policy Optimization），通过“想象”进行离线或在线 RL。

- 特定领域的应用： 用于自动驾驶、具身机器人操作、导航以及科学模拟的世界模型。

- 认知科学与生物学灵感： 关于海马体（Hippocampus）或大脑皮层（Neocortex）如何构建环境图谱的神经科学模型，及其对 AI 世界模型的启示。

- 评估与基准测试： 用于衡量世界模型的预测精度、规划效率、数据效率和概括（Generalization）能力的 Benchmarks 和 Datasets。

- 开源框架与工具： 专门用于构建和测试世界模型的代码库和模拟环境。

🌀 不包含内容（Out of Scope）
- 通用的视频或图像生成研究： 如果其目的并非作为世界模型来支持智能体的规划或理解（例如：一般的艺术生成、无条件的视频插帧）。

- 通用的无模型（Model-Free）强化学习： 除非其展示了与世界模型的结合（例如作为 Actor-Critic 中的基线，但重点不在世界模型本身）。

- 单纯的大语言模型（LLM）推理： 除非其研究集中于 LLM 如何作为世界的逻辑或常识模型，并应用于物理实体。

- 传统的确定性物理模拟器： 除非其专注于从数据中学习（Learn from Data）物理规律，或作为构建数据驱动世界模型的工具。

- 通用的机器学习或计算机视觉方法： 缺乏直接的世界模型应用场景。

---

<!-- ## 🗂️ AI-Memory Taxonomy

To systematically organize the diverse research and practical resources in the field of AI large model memory, this repository categorizes memory systems across multiple orthogonal dimensions, reflecting variations in storage methods, temporal scales, content forms, operational processes, and system architectures.
1. Memory by Storage Location
- Parametric Memory
  - Knowledge implicitly encoded within model weights
  - Static and not directly editable during inference
- External / Explicit Memory
  - Memory stored outside model parameters
  - Readable, writable, and dynamically updatable
2. Memory by Temporal Scope
- Short-Term Memory
  - Entirely dependent on context window
  - Session-level, temporary information
- Long-Term Memory
  - Persistent memory across sessions and time scales
  - Supports long-term consistency and personalization
3. Memory by Content Type
- Episodic Memory
  - Event-based historical interaction memory
  - Preserves temporal sequence and contextual relationships
- Semantic Memory
  - Facts, rules, and preferences abstracted from multiple experiences
  - Typically derived from compression or induction of episodic memory
- Procedural Memory
  - Memory related to action patterns, skills, and task execution strategies
4. Memory Operations
- Writing: Determining which information should be stored
- Retrieval: Selecting relevant memories for current tasks
- Updating: Correcting or merging existing memories
- Forgetting: Removing or weakening low-value information
- Compression: Summarizing historical information to fit context windows
5. Memory Mechanisms & Architectures
- Retrieval-Augmented Generation (RAG)
- Summary-based memory mechanisms
- Vectorized semantic retrieval
- Symbolic-neural hybrid memory systems
- Event-driven and trigger-based memory mechanisms
- Reinforcement learning-based memory strategy optimization
6. Memory in Agent Systems
- Single-agent memory
- Multi-agent shared memory
- Tool-augmented memory
- Planning-aware memory
- Personality and emotion-related memory
7. Evaluation & Benchmarks
- Long-term consistency evaluation
- Continuous interaction and long-term task benchmarks
- Memory recall and utilization efficiency metrics
- Personalization and user preference retention evaluation

--- -->

## 🔔 近期热点研究与新闻
+ 2026-4-4 – 🎉 仓库初始化

---

🗺️ 目录表
- [简介](#-简介)
- [仓库目标](#-仓库目标)
- [项目范围](#-项目范围)
- [近期热点研究与新闻](#-近期热点研究与新闻)
- [核心概念](#-核心概念)
- [论文列表](#-论文列表)
  - [综述](#综述)
  - [方法类与框架类论文](#方法类与框架类论文)
  - [数据集和评估基准类论文](#数据集与评估基准类论文)
  - [模型和系统类论文](#模型和系统类论文)
- [仓库资源](#-仓库资源)
  - [测试基准](#测试基准)
  - [开源系统](#开源系统)
  - [多媒体资源](#多媒体资源)
- [如何贡献](#-如何贡献)
- [仓库关注量](#-仓库关注量)

---

## 🧠 核心概念

- **世界模型 (World Model)**：一个人工智能系统的内部心智模型，旨在理解物理世界的运作规律、因果关系以及环境的动态变化。它赋予智能体“想象力”，使其能够在内部模拟未来状态、评估行动后果，从而实现高效的规划与决策，而无需在真实环境中进行昂贵的试错。

- **状态表征学习 (State Representation Learning)**：将高维、冗余的原始观测数据（如图像、视频）转化为低维、紧凑且包含关键语义信息的潜在向量（Latent Vectors）的过程。优秀的表征应具备马尔可夫性质，并能够解耦出环境中的不同实体及其属性。

- **转换模型 / 动态模型 (Transition Model / Dynamics Model)**：世界模型的核心组件，负责预测在当前状态下执行特定行动后，环境将如何演化到下一个状态（$S_t, A_t \rightarrow S_{t+1}$）。它捕捉了环境的物理规律和因果逻辑。

- **潜在空间模拟 (Latent Space Simulation)**：在低维潜在空间中进行未来的预测和推演，而非在原始像素空间。这极大地提高了计算效率，并允许模型关注高层语义变化而忽略无关细节。

- **基于模型的规划 (Model-Based Planning)**：智能体利用世界模型在前瞻（Lookahead）或“梦境”（Dreaming）中搜索最优行动序列的过程。常用算法包括模型预测控制 (MPC)、蒙特卡洛树搜索 (MCTS) 等。

- **基于模型的强化学习 (Model-Based Reinforcement Learning, MBRL)**：一种强化学习范式，智能体首先学习一个世界模型，然后利用该模型生成模拟经验来训练策略（Policy）或价值函数（Value Function），从而显著提高数据效率。

- **可微物理引擎 (Differentiable Physics Engine)**：一种能够计算输出对输入梯度的物理模拟器。当集成到世界模型中时，它允许通过梯度下降直接优化控制策略，实现极具效率的学习。

- **对象中心表征 (Object-Centric Representation)**：将环境视为一组离散对象及其相互作用的表征方式。这种方式符合人类认知，有助于提高模型对未见过场景的泛化能力和因果推理能力。

- **多模态世界模型 (Multimodal World Model)**：能够处理和整合多种感知模态（如视觉、语言、触觉、动作）的世界模型。它利用不同模态的互补信息来构建更全面、更鲁棒的环境理解。

- **因果发现与推理 (Causal Discovery & Reasoning)**：在世界模型中区分相关性（Correlation）与因果性（Causation）的能力。这使智能体能够理解“如果我这样做，会发生什么”（Intervention），并进行反事实推理（Counterfactual Reasoning）。

- **认知地图 (Cognitive Map)**：世界模型的一种特定形式，侧重于对环境空间结构、拓扑关系以及关键地标的内部表征，常用于导航和长期规划任务。

- **广义世界模型 / 基础世界模型 (General / Foundation World Model)**：在海量、多样化数据（如互联网规模的视频）上预训练的具有强大泛化能力的世界模型。它可以作为下游具身智能任务（如机器人操控、自动驾驶）的通用物理常识库。

---

## 📚 论文列表
以下论文按发表日期排列：

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
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.04814">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
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
          <img src="https://img.shields.io/badge/safety-red" alt="safety">
          <img src="https://img.shields.io/badge/Evolution-brightgreen" alt="Evolution">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.11768v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
          <td colspan="3">
              • 大模型智能体的记忆系统正从静态检索转向动态自主更新，这虽然提升了智能体的适应性，但也引发了严峻的稳定与安全问题。其中包括语义漂移、固化错误工作流的程序漂移、外部恶意注入的记忆投毒。<br>
              • 提出稳定与安全治理记忆（SSGM）框架。该框架的核心设计理念是将智能体的“生成式认知策略”与“底层记忆存储介质”彻底解耦。它在两者之间引入了一个主动拦截的治理中间件，使记忆的更新不再是盲目的直接写入，而是必须经过多重网关的审查。<br>
              • 合并前验证，在写入前进行逻辑一致性检查，拒绝与核心事实相矛盾的更新，防止幻觉被固化
              。时间与权限过滤，在读取时结合衰减函数过滤过期失效数据，并基于访问控制防止跨用户隐私泄露。可逆的定期对齐，采用“可变活动图+ 不可变情景日志”的双轨存储结构，系统会定期将当前记忆与不可变日志进行对齐与错误回滚，从而在数学上为长期的“语义漂移”设定了严格的误差上限。
          </td>
      </tr>
  </table>
</details>




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
        <td style="width: 55%;"><strong>Towards Realistic Personalization: Evaluating Long-Horizon Preference Following in Personalized User-LLM Interactions</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Personalized-yellow" alt="Personalized">
            <img src="https://img.shields.io/badge/Interaction-blue" alt="Interaction">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.04191">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 评估大型语言模型在真实且极度长程的交互场景下，持续遵循用户多样化偏好的能力盲区。<br>
            • 构建覆盖 100 个用户画像及海量交互数据的 RealPref 基准，专门考察从显式到隐式偏好表达的泛化理解。<br>
            • 明确量化了“偏好表达隐式化”与“上下文过度拉长”会导致 LLM 遵循性能出现断崖式下跌，界定了个人感知助手的发展瓶颈。
        </td>
    </tr>  
     <tr>
        <td rowspan="2" style="width: 15%;">2026-03-04</td>
        <td style="width: 55%;"><strong>LifeBench: A Benchmark for Long-Horizon Multi-Source Memory</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Multi-Source-yellow" alt="Multi-Source">
            <img src="https://img.shields.io/badge/Real%20World-blue" alt="Real World">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.03781">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 长期个人助手的演进要求模型具备基于非声明性记忆（如通过数字痕迹推断习惯）的复杂推理能力，而现有基准对此完全空白。<br>
            • 推出 LifeBench 基准，利用真实世界先验与认知科学层级结构，模拟跨时间大跨度的多源密集事件以考察智能体整合能力。<br>
            • 当前顶尖记忆系统在该基准下准确率仅勉强过半（55.2%），凸显了从零散数字痕迹中进行长程推理的极高难度。
        </td>
    </tr>   
     <tr>
        <td rowspan="2" style="width: 15%;">2026-03-02</td>
        <td style="width: 55%;"><strong>AMemGym: Interactive Memory Benchmarking for Assistants in Long-Horizon Conversations</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Interactive-yellow" alt="Interactive">
            <img src="https://img.shields.io/badge/Long-Horizon-blue" alt="Long-Horizon">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.01966">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 静态离线评估数据难以真实反映智能体在动态长周期交互中记忆管理策略的可扩展性与可靠性。<br>
            • 构建支持在线策略评估的交互式环境 AMemGym，利用结构化采样低成本生成高保真用户画像与状态演化轨迹。<br>
            • 动态环境客观暴露了 RAG 等现有系统的长程性能衰减，并验证了该框架在驱动策略自我进化方面的有效性。
        </td>
    </tr>   
     <tr>
        <td rowspan="2" style="width: 15%;">2026-03-02</td>
        <td style="width: 55%;"><strong>According to Me: Long-Term Personalized Referential Memory QA</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Multi-Modal-yellow" alt="Multi-Modal">
            <img src="https://img.shields.io/badge/Privacy%20Data-blue" alt="Privacy Data">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.01990">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 传统基准多基于单文本对话历史，无法有效评估智能体在真实生活、多模态及长周期下的个性化指代推理能力。<br>
            • 构建包含四年隐私数据的多模态多源基准 ATM-Bench，并提出模式引导记忆用于异构数据的结构化表示。<br>
            • 揭露现有系统在复杂真实经验集上的性能缺陷，并证明结构化的 SGM 在多源场景中优于传统描述性方法。
        </td>
    </tr>   
     <tr>
        <td rowspan="2" style="width: 15%;">2026-02-27</td>
        <td style="width: 55%;"><strong>MemEmo: Evaluating Emotion in Memory Systems of Agents</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Emotion-yellow" alt="Emotion">
            <img src="https://img.shields.io/badge/Benchmark-blue" alt="Benchmark">
            <img src="https://img.shields.io/badge/Multi--Session-orange" alt="Multi-Session">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.23944">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 现有记忆系统评测多侧重于事实召回，缺乏对长程交互中情感信息处理效能的衡量。<br>
            • 推出首个情感增强型评估基准及 HLME 数据集，涵盖情感信息提取、情感记忆更新与情感问答三大维度。<br>
            • 实验暴露出当前最先进的记忆系统在情感处理任务上均存在显著的不稳定性，为后续情感连贯性优化指明了方向。
        </td>
    </tr>    
     <tr>
        <td rowspan="2" style="width: 15%;">2026-02-18</td>
        <td style="width: 55%;"><strong>MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Benchmark-yellow" alt="Benchmark">
            <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
            <img src="https://img.shields.io/badge/Multi--Session-orange" alt="Multi-Session">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.16313.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 介绍了 MemoryArena，这是一个用于基准测试多会话任务中代理记忆的统一评估平台。<br>
            • 该基准涵盖网络导航、规划、信息搜索和推理等任务，要求代理在执行过程中持续学习并利用记忆。<br>
            • 研究揭示了现有长上下文记忆基准在评估真实交互场景时的不足，强调了记忆与行动协同评估的必要性。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-18</td>
        <td style="width: 55%;"><strong>AgentLAB: Benchmarking LLM Agents against Long-Horizon Attacks</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Benchmark-yellow" alt="Benchmark">
            <img src="https://img.shields.io/badge/Memory%20Poisoning-lightgrey" alt="Memory Poisoning">
            <img src="https://img.shields.io/badge/Long--Horizon-blueviolet" alt="Long-Horizon">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.16901.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出了首个专门评估 LLM 代理对适应性长时间攻击（Long-Horizon Attacks）脆弱性的基准 AgentLAB。<br>
            • 支持包括记忆投毒在内的五种新型攻击类型，涵盖 28 个现实代理环境和 644 个安全测试案例。<br>
            • 实验发现 LLM 代理在长时攻击下极度脆弱，现有的单次交互防御措施无法有效应对此类复杂的安全威胁。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-11</td>
      <td style="width: 55%;"><strong>Locomo-Plus: Beyond-Factual Cognitive Memory Evaluation Framework for LLM Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-red" alt="Benchmark">
        <img src="https://img.shields.io/badge/Long--Context-gold" alt="Long-Context">
        <img src="https://img.shields.io/badge/Environment%20Sim-darkgreen" alt="Environment Simulation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.10715">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 LoCoMo-Plus 基准测试，该测试旨在评估 LLM 智能体在长对话中保留和应用隐含约束（如用户目标、状态和价值观）的“认知记忆”能力，而非传统的表面事实召回。<br>
        • 该基准构造了复杂的对话实例，要求模型在后续查询与原始记忆线索缺乏表面语义相似度的情况下，仍能准确应用潜在的上下文约束。<br>
        • 论文提出了一种统一的评估框架，通过实验揭示了现有 LLM 和记忆系统在处理此类非事实性、认知驱动的记忆任务时面临的严峻挑战。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-29</td>
      <td style="width: 55%;"><strong>AgentLongBench: A Controllable Long Benchmark For Long-Contexts Agents via Environment Rollouts</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Benchmark-red" alt="Benchmark">
      <img src="https://img.shields.io/badge/Long--Context-gold" alt="Long-Context">
      <img src="https://img.shields.io/badge/Environment%20Sim-darkgreen" alt="Environment Simulation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.20730">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
      • 提出了 AgentLongBench，一个通过模拟环境推演（Environment Rollouts）来评估长上下文智能体的基准测试，包含 32K 到 4M 的上下文长度。<br>
      • 基于横向思维谜题（Lateral Thinking Puzzles）构建动态交互轨迹，包含知识密集型和无知识型两种设定，以区分推理能力与参数化知识。<br>
      • 揭示了现有模型在处理海量工具响应中的高信息密度时，比处理长对话中的记忆碎片化面临更大的挑战，提出了“最小 Token 需求”作为关键因素。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-24</td>
      <td style="width: 55%;"><strong>MemoryRewardBench: Benchmarking Reward Models for Long-Term Memory Management in Large Language Models</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-red" alt="Benchmark">
        <img src="https://img.shields.io/badge/Reward%20Model-purple" alt="Reward Model">
        <img src="https://img.shields.io/badge/Memory%20Evaluation-blue" alt="Memory Evaluation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.11969">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 MemoryRewardBench，这是第一个系统评估奖励模型（RM）对 LLM 长期记忆管理过程评价能力的基准测试。<br>
        • 涵盖长上下文推理、多轮对话和长文本生成三大类任务，包含 10 种不同的记忆管理设置，上下文长度从 8K 到 128K。<br>
        • 设计了基于结果（Outcome-based）和基于过程（Process-based）的评估标准，发现新一代模型在评估记忆管理方面表现出代际优势。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-23</td>
      <td style="width: 55%;"><strong>How Does Personalized Memory Shape LLM Behavior? Benchmarking Rational Preference Utilization in Personalized Assistants</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-red" alt="Benchmark">
        <img src="https://img.shields.io/badge/Personalization-indigo" alt="Personalization">
        <img src="https://img.shields.io/badge/Rationality-lightgrey" alt="Rationality">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.16621">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 LLM 理性个性化（Rational Personalization）的问题，并发布了 RPEval 基准测试，用于评估个性化助手在不同场景下对用户偏好的利用是否合理。<br>
        • 包含个性化意图推理数据集和多粒度评估协议，揭示了现有 LLM 中广泛存在的“非理性个性化”（如 Filter Bubble）现象。<br>
        • 提出了 RP-Reasoner，一种基于语用学推理的机制，通过推断用户潜在意图来选择性地整合个性化信息，显著减少了非理性个性化错误。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-13</td>
      <td style="width: 55%;"><strong>Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-red" alt="Benchmark">
        <img src="https://img.shields.io/badge/Tool%20Use-orange" alt="Tool Use">
        <img src="https://img.shields.io/badge/Active%20Memory-green" alt="Active Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.19935">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 Mem2ActBench，用于评估智能体主动利用长期记忆执行基于工具的任务的能力，而非简单的被动事实检索。<br>
        • 通过自动化流程构建了包含 2029 个会话的数据集，并采用逆向生成方法创建了 400 个必须依赖记忆才能完成的工具调用任务。<br>
        • 实验表明，现有系统在“参数接地”（Parameter Grounding）方面表现不佳，即难以从记忆中提取正确参数来执行工具调用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-11</td>
      <td style="width: 55%;"><strong>CloneMem: Benchmarking Long-Term Memory for AI Clones</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
      <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.07023">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 CLONEMEM，一个旨在评估 AI 克隆体长期记忆的基准测试，利用非对话式数字痕迹（如日记、社交媒体、邮件）跨越 1-3 年，而非传统的对话历史。<br>
        • 提出了一个层级数据构建框架，生成连贯的纵向生活轨迹，捕捉个体经历、情感和观点随时间的演变。<br>
        • 实验结果表明，现有记忆系统（如 A-Mem 和 Mem0）在该设置下表现不佳，往往不如扁平检索，且由于有损压缩和对叙事模板的依赖而无法准确追踪内部状态变化。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-11</td>
      <td style="width: 55%;"><strong>RealMem: Benchmarking LLMs in Real-World Memory-Driven Interaction</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
        <img src="https://img.shields.io/badge/Long--Term%20Memory%20Evaluation-darkslateblue" alt="Long-Term Memory Evaluation">
        <img src="https://img.shields.io/badge/Long--Context%20Understanding-cornflowerblue" alt="Long-Context Understanding">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.06966">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • RealMem 是一个旨在评估 LLM 在"长期项目导向"交互中表现的基准测试，与休闲或任务导向对话基准不同，它专注于不断演变的目标和动态状态。<br>
          • 该框架采用三阶段合成管道（项目基础、多智能体生成、记忆管理），在 11 个现实场景中创建超过 2000 个跨会话对话。<br>
          • 评估表明，当前 SOTA 记忆系统在管理长期项目状态、时间推理和主动对齐方面存在困难，揭示了自主智能体能力的关键差距。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-08</td>
      <td style="width: 55%;"><strong>KnowMe-Bench: Benchmarking Person Understanding for Lifelong Digital Companions</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
        <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
        <img src="https://img.shields.io/badge/Long--Context%20Understanding-cornflowerblue" alt="Long-Context Understanding">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.04745">
      <img src="https://img.shields.io/badge/arXiv-Paper-B31B1B" alt="arXiv Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • <strong>简介：</strong> 提出了 KnowMe-Bench，这是一个基于长篇自传叙事（470万 token）构建的基准测试，旨在超越简单的事实检索，评估终身数字伴侣对用户动机、原则等深层“人”的理解能力。<br>
          • <strong>方法：</strong> 采用了“认知流重构”管道，将非线性叙事转化为具备倒叙感知和时间锚定的流式数据，包含内心独白和感官细节，并实施了从事实提取到精神分析深度的三层分级评估体系。<br>
          • <strong>发现：</strong> 对不同记忆架构（RAG, Mem0, MemOS）的实验表明，虽然检索增强系统在事实准确性上表现良好，但在处理时间逻辑和深度推理（如“更新悖论”）时存在显著缺陷，揭示了当前模型在模拟人类复杂非线性记忆方面的差距。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-07</td>
      <td style="width: 55%;"><strong>Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Multimodal-darkorchid" alt="Multimodal">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.03515">
      <img src="https://img.shields.io/badge/arXiv-Paper-B31B1B" alt="arXiv Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • <strong>简介：</strong> 提出了 <strong>Mem-Gallery</strong>，这是一个用于评估多模态大语言模型（MLLM）智能体在长期对话中多模态记忆能力的基准测试，旨在解决现有基准在多模态与长期记忆评估上的错位问题。<br>
          • <strong>方法：</strong> 构建了一个基于视觉和文本信息的高质量多会话对话数据集，并提出了一个包含三个功能维度的评估框架：记忆提取与适应、记忆推理以及记忆知识管理（包括冲突检测和知识更新）。<br>
          • <strong>发现：</strong> 对13个记忆系统的基准测试表明，显式的多模态信息保留是有效的，但现有模型在涉及复杂推理和动态知识管理的场景中仍存在局限，且面临存储和检索的效率瓶颈。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-07</td>
      <td style="width: 55%;"><strong>EvolMem: A Cognitive-Driven Benchmark for Multi-Session Dialogue Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
        <img src="https://img.shields.io/badge/Multi--Turn%20Dialogue-rosybrown" alt="Multi-Turn Dialogue">
        <img src="https://img.shields.io/badge/Agentic%20Memory-darkturquoise" alt="Agentic Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.03543">
      <img src="https://img.shields.io/badge/arXiv-Paper-B31B1B" alt="arXiv Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • <strong>简介：</strong> 提出了 EvolMem，这是一个基于认知心理学的基准测试，旨在评估大语言模型（LLMs）和智能体系统在多会话场景下的记忆能力，填补了对非陈述性记忆和长期一致性评估的空白。<br>
          • <strong>方法：</strong> 该基准将记忆划分为陈述性（如检索、推理）和非陈述性（如习惯化）两类。它采用混合数据合成框架——结合话题驱动生成和叙事启发转换——构建了多样化且可控的多会话对话数据。<br>
          • <strong>发现：</strong> 评估显示，没有任何模型能在所有记忆维度上持续领先，且在非陈述性任务上表现普遍较弱。此外，现有的智能体记忆机制在性能上往往无法超越强大的基础模型，并面临严重的延迟问题。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-07</td>
      <td style="width: 55%;"><strong>PersonaMem-v2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
        <img src="https://img.shields.io/badge/Agentic%20Memory-darkturquoise" alt="Agentic Memory">
        <img src="https://img.shields.io/badge/Reinforcement Learning-orange" alt="Reinforcement Learning">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2512.06688">
      <img src="https://img.shields.io/badge/arXiv-Paper-B31B1B" alt="arXiv Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 简介：推出了 PersonaMem-v2，这是一个用于 LLM 个性化的 SOTA 数据集，包含 1,000 个真实用户画像、300 多个场景以及嵌入在长达 128k token 上下文中的 20,000 多个隐式用户偏好。<br>
          • 发现与差距：评测显示，包括 GPT-5 在内的前沿 LLM 在隐式个性化方面表现挣扎，准确率仅为 37-48%。研究发现，强化微调（RFT）能显著提升模型在用户理解方面的长上下文推理能力。<br>
          • 方法创新：提出了一种“代理记忆（Agentic Memory）”框架，该框架维护一个持续演进的、人类可读的单一记忆体。该方法以 16 倍的效率优势（仅使用 2k 记忆 token 对比 32k 历史记录）超越了 GPT-5，达到了 55% 的准确率。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-11-04</td>
      <td style="width: 55%;"><strong>Toward Multi-Session Personalized Conversation: A Large-Scale Dataset and Hierarchical Tree Framework for Implicit Reasoning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2025.emnlp-main.580.pdf">
      <img src="https://img.shields.io/badge/EMNLP-Paper-black?labelColor=green" alt="EMNLP Paper">
      </a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 介绍了 IMPLEXCONV 数据集以及 TACITREE 框架，用于研究个性化对话中的隐式推理能力。<br>
          • IMPLEXCONV 包含 2500 个以隐式推理场景为核心的示例，能够捕捉对话中细微的句法与语义关系。<br>
          • TACITREE 通过对对话历史进行分层式组织，增强了大型语言模型（LLMs）在长对话中进行隐式上下文推理的能力。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-27</td>
      <td style="width: 55%;"><strong>Know Me, Respond to Me, benchmarking LLMs for Dynamic User profiling and personalized response at scale</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2504.14225">
      <img src="https://img.shields.io/badge/COLM-Paper-black?labelColor=gold" alt="COLM Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 介绍了 PERSONAMEM 基准测试，该基准旨在评估大型语言模型（LLMs）在动态用户画像建模与个性化回复生成方面的表现。<br>
        • 尽管现有模型在回忆用户偏好方面取得了一定成效，但在应对全新场景时仍然存在显著的性能差距。<br>
        • 论文详细阐述了该基准的结构、用户对话的生成流程、模型性能的评估方法以及相关研究，强调了个性化对话生成在提升用户体验中的重要性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-10</td>
      <td style="width: 55%;"><strong>Human-inspired Episodic Memory for Infinite Context LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Long--Context%20Understanding-cornflowerblue" alt="Long-Context Understanding">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2407.09450">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • EM-LLM（事件记忆大语言模型）是一种新型大语言模型，旨在解决现有模型在长文本处理中的局限性。<br>
        • EM-LLM 无需微调即可实现近乎无限的上下文处理能力，在多个基准测试中显著优于现有模型。<br>
        • 该模型整合了基于突发性事件分割、图论边界优化和两阶段记忆检索机制，显著提升信息检索与问答任务的性能。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2023-09-26</td>
      <td style="width: 55%;"><strong>Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2507.05257">
      <img src="https://img.shields.io/badge/ICML-Paper-black?labelColor=brightgreen" alt="ICML Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemoryAgentBench 是一个用于评估具备记忆机制的语言模型（记忆智能体，Memory Agents）四项核心能力的基准测试，包括精准检索、测试时学习、长程理解以及冲突消解。<br>
        • 通过整合现有数据集与新构建的数据，MemoryAgentBench 实现了对上述能力的系统性评估。<br>
        • 该基准揭示了当前方法在记忆更新与长时跨度对话处理方面的局限性，凸显了未来研究亟需解决的关键挑战。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-07-27</td>
      <td style="width: 55%;"><strong>Unveiling Privacy Risks in LLM Agent Memory</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
      <img src="https://img.shields.io/badge/Memory%20Modules-orange" alt="Memory Modules">
      <img src="https://img.shields.io/badge/LLM%20Evaluation-dodgerblue" alt="LLM Evaluation">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2025.acl-long.1227.pdf">
      <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper"></a></td>
    </tr>
    <tr>
        <td colspan="3">
          • 研究大语言模型代理记忆中的隐私漏洞，特别关注从长期记忆中提取敏感用户-代理交互信息的风险。<br>
          • 提出记忆提取攻击（MEXTRA），该黑盒攻击通过创新的提示设计（定位器+对齐器）和自动化提示生成技术，实现敏感用户查询的提取。<br>
          • 在代表性代理系统（EHRAgent和RAP）上的实验表明存在显著漏洞，通过分析相似性评分函数、内存配置等影响泄露的关键因素，揭示了记忆系统安全性的薄弱环节。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-07-27</td>
      <td style="width: 55%;"><strong>MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Long--Text%20Understanding-darkseagreen" alt="Long-Text Understanding">
      <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2025.acl-long.560.pdf">
      <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">        
        • MiniLongBench是一个低成本的长文本理解基准，旨在提升大语言模型（LLMs）在长上下文理解（LCU）任务中的评估效率与经济可行性。<br>
        • 通过应用数据压缩技术，MiniLongBench在保持评估结果一致性的前提下显著减少评估样本数量，并显示出与原始LongBench基准高度相关的结果。<br>
        • 多任务类别的评估验证了MiniLongBench的有效性，尽管在总结生成和信息综合类任务上仍需进一步优化。
      </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-07-27</td>
        <td style="width: 55%;"><strong>PersonaBench: Evaluating AI Models on Understanding Personal Information through Accessing (Synthetic) Private User Data</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Personalized%20Evaluation-tealgreen" alt="Personalized Evaluation">
        </td>
        <td style="width: 15%;"><a href="https://aclanthology.org/2025.findings-acl.49.pdf">
        <img src="https://img.shields.io/badge/ACL%20Findings-Paper-black?labelColor=pink" alt="ACL Findings Paper">
        </td>
    </tr>
    <tr>
      <td colspan="3">
        • PersonaBench 是一个用于评估 AI 模型理解个人信息能力的基准测试。<br>
        • 论文强调了个性化在 AI 助手中的重要性，并指出由于缺乏可公开获取的数据集，用于评估此类能力面临着显著挑战。<br>
        • 评测主要聚焦于检索增强生成（RAG）模型，结果表明当前模型在有效处理个人化查询方面仍然存在困难。
      </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-07-27</td>
        <td style="width: 55%;"><strong>MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        </td>
        <td style="width: 15%;"><a href="https://aclanthology.org/2025.findings-acl.989.pdf">
        <img src="https://img.shields.io/badge/ACL%20Findings-Paper-black?labelColor=pink" alt="ACL Findings Paper">
        </td>
    </tr>
    <tr>
      <td colspan="3">
        • MemBench 旨在对基于 LLM 的智能体记忆能力进行全面评估。<br>
        • 通过构建同时涵盖事实记忆与反思记忆的数据集，该研究弥补了现有评测方法的局限性。<br>
        • 论文详细介绍了记忆机制的构建方式——包括用户关系图与多层级记忆设计——并强调了准确率、效率与容量等评估指标的重要性。
      </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-07-27</td>
        <td style="width: 55%;"><strong>Evaluating the Long-term memory of large language models</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
        <img src="https://img.shields.io/badge/Long--Term%20Memory%20Evaluation-darkslateblue" alt="Long-Term Memory Evaluation">
        </td>
        <td style="width: 15%;"><a href="https://aclanthology.org/2025.findings-acl.1014.pdf">
        <img src="https://img.shields.io/badge/ACL%20Findings-Paper-black?labelColor=pink" alt="ACL Findings Paper">
        </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文探究了大型语言模型（LLMs）在长期任务中的记忆能力，重点聚焦于对话系统。<br>
        • 通过构建 Long-Order Chronological Conversation（LOCCO）数据集，研究对 LLM 的长期记忆性能进行了定量评估。<br>
        • 实验结果表明，尽管 LLM 在一定程度上能够保留历史对话信息，但其记忆能力会随着时间推移而逐步衰退。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-07-27</td>
      <td style="width: 55%;"><strong>Know You First and Be You Better: Modeling Human-Like User Simulators via Implicit Profiles</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Dialogue%20Augmentation-olive" alt="Dialogue Augmentation">
      <img src="https://img.shields.io/badge/Human--AI%20Interaction-firebrick" alt="Human-AI Interaction">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2025.acl-long.1025.pdf">
      <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 介绍了一种用户模拟框架——隐式用户画像用户模拟器（Implicit User Profile User Simulator，USP），该框架通过推断用户的隐式属性来增强对话系统与人类用户之间的交互效果。<br>
        • USP 从用户对话中提取隐式特征，并将条件监督微调与循环一致性约束下的强化学习相结合，从而提升生成对话的真实感与连贯性。<br>
        • 实验结果表明，USP 在多项评估指标上展现出显著优势，尤其是在与 GPT-4o、PlatoLM 等其他对话生成模型对比时表现更为突出。
      </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-06-15</td>
        <td style="width: 55%;"><strong>PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Personalized%20Evaluation-tealgreen" alt="Personalized Evaluation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2506.12915">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 PersonaFeedback 基准测试，用于评估大型语言模型（LLMs）在个性化回复生成方面的能力。<br>
        • 研究表明，尽管 LLM 在生成个性化内容方面已有一定进展，但在复杂场景下仍然存在明显局限。<br>
        • 研究者通过引入动态用户属性推断、个性化画像以及奖励模型，旨在提升个性化问答的整体效果。
      </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2025-06-09</td>
        <td style="width: 55%;"><strong>Minerva: A Programmable memory test benchmark for language models</strong></td>
        <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2502.03358">
        <img src="https://img.shields.io/badge/ICML-Paper-black?labelColor=brightgreen" alt="ICML Paper">
        </td>
    </tr>
    <tr>
      <td colspan="3">
        • Minerva 是一个可编程的记忆测试基准，用于在多样化的记忆任务上评估大型语言模型（LLMs）的表现。<br>
        • 该基准对模型使用记忆的能力进行了定量评估，重点关注信息检索、推理以及状态跟踪等任务。<br>
        • 实验结果表明，尽管部分模型在简单任务上表现良好，但在更复杂的任务中仍然存在显著差距。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-28</td>
      <td style="width: 55%;"><strong>Self-Taught Agentic Long-Context Understanding</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        <img src="https://img.shields.io/badge/Long--Text%20Understanding-darkseagreen" alt="Long-Text Understanding">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2502.15920">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • AgenticLU框架（智能代理长上下文理解框架）旨在增强大语言模型（LLMs）在长文本理解与推理任务中的表现。<br>
        • 该框架提出澄清链机制（Chain-of-Clarifications, CoC），通过优化模型自我澄清过程并采用树状搜索路径生成澄清性问题，从而显著提升多步骤推理的准确率与有效性。<br>
        • 验证结果表明，该框架在长上下文问答任务中优于现有提示技术，同时将计算开销控制在合理范围内。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-22</td>
      <td style="width: 55%;"><strong>EMBODIED AGENTS MEET PERSONALIZATION: INVESTIGATING CHALLENGES AND SOLUTIONS THROUGH THE LENS OF MEMORY UTILIZATION</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
        <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
        <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
        <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2505.16348">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 本文研究了大语言模型驱动的具身智能体在个性化辅助任务中面临的挑战，特别聚焦于物体语义记忆与用户行为模式的记忆利用问题。<br>
        • 研究提出MEMENTO（记忆评估框架），通过两阶段评估揭示当前智能体在处理连续用户行为模式及多记忆协同时存在困难，其根本原因在于信息过载问题。<br>
        • 该工作设计了基于分层知识图谱的用户画像记忆模块，通过分离个性化知识与情景记忆历史，在单一记忆任务和联合记忆任务中均取得显著性能提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-03-11</td>
      <td style="width: 55%;"><strong>SCBench: A Benchmark for Long Context Methods Based on KV-Cache</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Long--Context%20Evaluation-darkslategray" alt="Long-Context Evaluation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2412.10319">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • SCBENCH（共享上下文基准）是一个专为评估长上下文大语言模型（LLMs）设计的基准测试框架。<br>
        • 该基准聚焦于键值缓存（KV缓存）的生命周期管理，涵盖生成、压缩、检索与加载等核心环节，旨在填补现有基准在多轮交互场景下KV缓存评估方面的空白。<br>
        • 实验结果表明，不同方法在任务中展现出显著性能差异，其中动态稀疏注意力机制与缓存优化策略在复杂场景中表现出更优性能。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2022-03-04</td>
      <td style="width: 55%;"><strong>LongMemEval: Benchmarking chat assistants on long-term interactive memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      <img src="https://img.shields.io/badge/Long--Term%20Memory%20Evaluation-darkslateblue" alt="Long-Term Memory Evaluation">
      <img src="https://img.shields.io/badge/Evaluation%20Framework-darkgoldenrod" alt="Evaluation Framework">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2410.10813">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 论文提出了 LONGMEMEVAL，这是一个用于评估聊天助手长期记忆能力的综合性基准测试。<br>
        • 该基准评估了五项核心记忆能力，覆盖了现有系统面临的关键挑战。<br>
        • LONGMEMEVAL 采用统一的三阶段框架——索引、检索与阅读，并提出了多项设计优化，以提升记忆召回效果与问答准确率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-02-25</td>
      <td style="width: 55%;"><strong>Towards Effective Evaluations and Comparisons for LLM Unlearning Methods</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
      <img src="https://img.shields.io/badge/Memory%20Erasure-darkcyan" alt="Memory Erasure">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2406.09179">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 探讨了大型语言模型（LLMs）中的机器遗忘问题及其评估的重要性，重点关注消除不必要的数据记忆。<br>
        • 研究针对两个关键挑战展开：评估指标的稳健性，以及在移除目标知识与保留其他知识之间的权衡。<br>
        • 研究建议将 提取强度（Extraction Strength，ES）作为主要评估指标，以确保遗忘评估的准确性与可靠性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2022-02-13</td>
      <td style="width: 55%;"><strong>DO LLMS RECOGNIZE YOUR PREFERENCES? EVAL-UATING PERSONALIZED PREFERENCE FOLLOWING IN LLMS</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Long--Dialogue%20Reasoning-teal" alt="Long-Dialogue Reasoning">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2502.09597">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • PREFEVAL 是一个用于评估大型语言模型（LLMs）在长对话中推断、记忆并遵循用户偏好能力的基准测试。<br>
        • 该基准包含 3000 组用户偏好—查询对，涵盖 20 个主题，揭示了当前 LLM 在遵循用户偏好方面面临的显著挑战。<br>
        • 研究表明，相较于隐式偏好，模型更容易推断显式偏好，同时任务类型与偏好表达方式都会对模型性能产生显著影响。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2015-01-25</td>
      <td style="width: 55%;"><strong>Episodic Memory Benchmark: Episodic Memories Generation and Evaluation Benchmark for Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2501.13121">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 探讨情景记忆在大语言模型（LLMs）中的重要性，并提出构建新型基准测试框架以评估模型推理能力。<br>
        • 研究人员开发了包含全新设计任务与评估协议的综合性框架，强调需要创新训练策略以有效融合情景记忆机制。<br>
        • 该框架为评估大语言模型中的情景记忆提供了一种可行的技术路径。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-01-23</td>
      <td style="width: 55%;"><strong>LongGenBench: Benchmarking long-form generation in long context LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Complex%20Instruction%20Following-darkolivegreen" alt="Complex Instruction Following">
      <img src="https://img.shields.io/badge/Long--Text%20Generation-slategray" alt="Long-Text Generation">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2409.02076">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • LongGenBench 是一个用于评估大型语言模型（LLMs）生成高质量长文本能力的基准测试，重点强调对复杂指令的遵循能力。<br>
        • 不同于现有基准，LongGenBench 专门聚焦于长文本生成场景，涵盖日记写作、菜单设计等任务。<br>
        • 尽管在其他评测中表现强劲，LLM 在 LongGenBench 基准上仍面临显著挑战。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2015-01-03</td>
      <td style="width: 55%;"><strong>LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Long--Context%20Understanding-cornflowerblue" alt="Long-Context Understanding">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2412.15204">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • LongBench v2（长文本理解与推理基准测试）是一个用于评估大语言模型在长上下文任务中表现的多任务基准测试框架。<br>
        • 该框架包含503道涵盖多种任务类型的多项选择题，重点评估模型对长文本的理解与回答能力。<br>
        • 研究发现表现最佳的模型在长上下文任务中已超越人类专家，凸显了增强推理能力与提升推理时计算资源的重要性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-11-12</td>
      <td style="width: 55%;"><strong>MT-Eval: A Multi-Turn Capabilities Evaluation Benchmark for  Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Multi--Turn%20Dialogue-rosybrown" alt="Multi-Turn Dialogue">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2024.emnlp-main.1124.pdf">
      <img src="https://img.shields.io/badge/EMNLP-Paper-black?labelColor=green" alt="EMNLP Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MT-Eval 是一个用于评估大型语言模型（LLMs）在多轮对话中表现的基准测试。<br>
        • 现有评测多聚焦于单轮对话，MT-Eval 通过构建 1170 条多轮查询弥补了这一空白。<br>
        • 该基准将交互模式划分为回忆、扩展、细化与跟进四类，结果显示大多数模型在多轮场景下的表现明显弱于单轮对话。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-11-12</td>
      <td style="width: 55%;"><strong>LONGGENBENCH: Long-context Generation Benchmark</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Long--Text%20Generation-slategray" alt="Long-Text Generation">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2024.findings-emnlp.48.pdf">
      <img src="https://img.shields.io/badge/EMNLP-Paper-black?labelColor=green" alt="EMNLP Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • LongGenBench 是新近提出的一项长上下文生成基准，用于评估大型语言模型（LLMs）在长文本生成任务中的表现。<br>
        • 该基准补充了主要侧重检索能力的现有评测体系，转而强调在多个子问题之间保持连贯性与逻辑一致性。<br>
        • 研究表明，不同模型在长文本生成方面存在显著的性能差异。
      </td>
    </tr>
     <tr>
      <td rowspan="2" style="width: 15%;">2024-10-23</td>
      <td style="width: 55%;"><strong>MADial-Bench Towards real-world evaluation of memory-augmented diglogue generation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Memory%20Evaluation-indigo" alt="Memory Evaluation">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/abs/2409.15240">
        <img src="https://img.shields.io/badge/NAACL-Paper-black?labelColor=cyan" alt="NAACL Paper">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • MADial-Bench（记忆增强型对话生成基准测试）旨在评估对话系统在长期记忆能力上的局限性。<br>
        • 该基准测试融合认知科学理论，通过记忆检索与识别能力评估框架，并引入多维度评估指标。<br>
        • 研究表明，尽管大语言模型在情感支持任务中表现优异，但其记忆识别与注入能力仍需提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-10-04</td>
      <td style="width: 55%;"><strong>L-CiteEval: A Long-Context Citation Evaluation Benchmark</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
        <img src="https://img.shields.io/badge/Long--Context%20Evaluation-darkslategray" alt="Long-Context Evaluation">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2410.02115">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • L-CiteEval（长上下文模型理解与引用评估基准）是一个面向长上下文模型的多任务评估基准测试，旨在评估其在理解和引用方面的能力。<br>
        • 该基准测试涵盖11项任务，支持从8K至48K的上下文长度，并提供了综合性评估框架。<br>
        • 研究表明，闭源模型在引用质量和生成准确性上优于开源模型，而检索增强生成（RAG）技术能显著提升引用质量。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-08-16</td>
      <td style="width: 55%;"><strong>A personal long-term memory dataset for memory classification,Retrieval, and Synthesis in question Answering</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      <img src="https://img.shields.io/badge/Memory%20Taxonomy-lightgrey" alt="Memory Taxonomy">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Mid--Term%20Memory-saddlebrown" alt="Mid-Term Memory">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2024.sighan-1.18.pdf">
      <img src="https://img.shields.io/badge/ACL%20Workshop-Paper-black?labelColor=purple" alt="ACL Workshop Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • PerLTQA 是一个问答数据集，旨在增强对话系统中的长期记忆整合能力。<br>
        • PerLTQA 融合了语义记忆与情景记忆，涵盖 30 个角色下的 8593 个问题，目标在于提升记忆分类、检索与综合能力。<br>
        • 实验结果表明，在记忆分类任务中，基于 BERT 的模型优于其他大型语言模型。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-08-11</td>
      <td style="width: 55%;"><strong>CAN LONG-CONTEXT LANGUAGE MODELS UNDER-STAND LONG CONTEXTS</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Long--Text%20Understanding-darkseagreen" alt="Long-Text Understanding">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2024.acl-long.859/">
      <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 探讨大语言模型在长文本处理中的能力与局限性，并提出GLE（长文本理解评估）基准测试以评估其在长上下文理解中的表现。<br>
        • 论文阐述了长依赖问答任务的构建过程与评估标准，并对比了不同模型的性能。<br>
        • 实验结果表明，GLE基准测试能够有效评估大语言模型对长文本的处理能力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-08-11</td>
      <td style="width: 55%;"><strong>Evaluating Very Long-Term Conversational Memory of LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      <img src="https://img.shields.io/badge/Long--Term%20Memory%20Evaluation-darkslateblue" alt="Long-Term Memory Evaluation">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2024.acl-long.747.pdf">
      <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评估了大型语言模型（LLMs）在长时对话中的记忆能力，尤其聚焦于多模态对话场景。<br>
        • 研究者通过构建 LOCOMO 数据集，建立了一个覆盖问答、事件总结以及多模态对话生成等任务的综合评测基准。<br>
        • 实验结果表明，尽管部分 LLM 表现出较强能力，但在记忆与推理方面仍显著落后于人类，同时论文还提出了相应的评测框架与未来改进方向。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-08-11</td>
      <td style="width: 55%;"><strong>Lamp: When large language models meet personalization</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Personalized%20Tasks-darkkhaki" alt="Personalized Tasks">
      <img src="https://img.shields.io/badge/Retrieval%20Augmentation-mediumvioletred" alt="Retrieval Augmentation">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2024.acl-long.399.pdf">
      <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 探讨了大型语言模型（LLMs）在个性化回复生成中的重要性，并提出了 LaMP，这是一个专门用于训练与评估个性化文本生成和分类任务的新基准。<br>
        • LaMP 包含七项个性化子任务，突出了利用用户特定输入（如历史数据）以及检索增强策略来提升语言模型性能的有效性。<br>
        • 实验结果表明，个性化方法能够显著提升模型表现，其中通过微调并结合合适的检索策略可取得最佳效果。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-06-19</td>
      <td style="width: 55%;"><strong>LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      <img src="https://img.shields.io/badge/Bilingual%20Evaluation-darkorchid" alt="Bilingual Evaluation">
      <img src="https://img.shields.io/badge/Long--Text%20Understanding-darkseagreen" alt="Long-Text Understanding">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2308.14508">
      <img src="https://img.shields.io/badge/ACL-Paper-black?labelColor=deepskyblue" alt="ACL Paper"></a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • LongBench（长文本理解基准测试）是一个面向大语言模型的双语多任务基准测试框架，旨在评估其长上下文理解能力。<br>
        • 该基准测试包含21个涵盖六类任务的数据集：单文档问答、多文档问答、摘要生成、少样本学习、合成任务和代码补全，平均文本长度达6,711单词（13,386字符）。<br>
        • 实验结果表明，商业模型（如GPT-3.5-Turbo-16k）在长上下文任务中普遍优于开源模型。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-04-16</td>
      <td style="width: 55%;"><strong>HIERARCHICAL CONTEXT MERGING: BETTER LONG CONTEXT UNDERSTANDING FOR PRE-TRAINED LLMS</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Long--Text%20Understanding-darkseagreen" alt="Long-Text Understanding">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2404.10308">
      <img src="https://img.shields.io/badge/ICLR-Paper-black?labelColor=lightgrey" alt="ICLR Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • HOMER（分层上下文合并算法）是一种旨在解决大语言模型在长上下文处理中局限性的算法。<br>
        • 该算法通过将长输入分割为较小的块并进行分层合并，在处理长文本时显著提升内存效率与推理能力。<br>
        • 实验结果表明，HOMER在32K和64K上下文输入中表现出色，保持低困惑度与较低内存消耗。
      </td>
    </tr>
  </table>

</details>


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
        <td rowspan="2" style="width: 15%;">2026-03-15</td>
        <td style="width: 55%;"><strong>SuperLocalMemory V3: Information-Geometric Foundations for Zero-LLM Enterprise Agent Memory</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Information%20Geometry-red" alt="Information Geometry">
            <img src="https://img.shields.io/badge/Agent%20Memory-teal" alt="Agent Memory">
            <img src="https://img.shields.io/badge/Data%20Sovereignty-blue" alt="Data Sovereignty">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.14588">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 面向企业级代理持久记忆，提出检索、生命周期与一致性验证三位一体的数学化方案，突破传统记忆系统高度依赖工程启发式的问题。 <br>
            • 在 LoCoMo 基准上，相比工程基线平均提升 12.7%，最难样本提升 19.9%，验证了信息几何方法在复杂记忆检索中的有效性。<br>
            • 该工作将代理记忆从工程组件堆叠推进到可证明、可治理、可合规的系统设计范式，对高隐私、高主权场景具有代表意义。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-03-05</td>
        <td style="width: 55%;"><strong>Memory as Ontology: A Constitutional Memory Architecture for Persistent Digital Citizens</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Ontology-red" alt="Ontology">
            <img src="https://img.shields.io/badge/Digital%20Citizens-teal" alt="Digital Citizens">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.04740v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出记忆即本体的新范式，面向持续性数字主体，解决 AI 模型跨代演进中的身份连续性问题。<br>
            • 建立宪法式记忆架构，通过四层治理层级、多层语义存储与完整生命周期设计，支撑数字公民的长期存在与演化。<br>
            • 将底层计算模型降级为可替换载体，优先保障数字实体的身份与治理持久性，而非仅优化短期记忆调用与检索效率。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-03-04</td>
        <td style="width: 55%;"><strong>Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/RL-red" alt="RL">
            <img src="https://img.shields.io/badge/Experience%20Memory-teal" alt="Experience Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.04257v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 现有通过截断或摘要处理长上下文窗口限制的方法，容易导致关键交互证据丢失。<br>
            • 提出索引经验记忆机制 Memex 实现无损压缩，并引入强化学习框架 MemexRL 优化智能体的读写归档策略。<br>
            • 该系统使得智能体能够自主决策归档与检索时机，在显著压缩工作上下文的同时大幅提升了长程任务成功率。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-25</td>
        <td style="width: 55%;"><strong>MemoPhishAgent: Memory-Augmented Multi-Modal LLM Agent for Phishing URL Detection</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Phishing%20Detection-red" alt="Phishing Detection">
            <img src="https://img.shields.io/badge/Episodic%20Memory-teal" alt="Episodic Memory">
            <img src="https://img.shields.io/badge/Multi--Modal-blue" alt="Multi-Modal">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.21394.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出 MPA 代理，利用过去推理轨迹的情节记忆来指导针对重复和新型钓鱼威胁的决策。<br>
            • 在公共数据集中回忆率较最先进基线提升了 13.6%，真实场景下提升高达 20%。<br>
            • 分析表明情节记忆贡献了约 27% 的回忆增益，且不会引入额外的计算开销。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-18</td>
        <td style="width: 55%;"><strong>MMA: Multimodal Memory Agent</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Multimodal-blue" alt="Multimodal">
            <img src="https://img.shields.io/badge/Reliability%20Score-orange" alt="Reliability Score">
            <img src="https://img.shields.io/badge/Visual%20Bias-red" alt="Visual Bias">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.16493.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 提出多模态记忆代理（MMA），通过为检索项分配动态可靠性评分（结合来源、衰减和冲突感应）来解决 RAG 中的过度自信错误。<br>
            • 引入 MMA-Bench 基准，用于控制说话者可靠性并评估文本-视觉矛盾下的信念动态。<br>
            • 揭示了“视觉安慰效应”，即代理容易继承基础模型中潜在的视觉偏见。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-02-07</td>
      <td style="width: 55%;"><strong>M2A: Multimodal Memory Agent with Dual-Layer Hybrid Memory for Long-Term Personalized Interactions</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Multimodal%20Memory-pink" alt="Multimodal Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-purple" alt="Memory Architecture">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.07624">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 该框架通过 ChatAgent（负责交互）和 MemoryManager（负责记忆操作）的协作，将静态的多模态个性化转变为能够随对话进程不断更新和演进的记忆机制。<br>
        • 系统由存储原始日志的底层和存储高层观察的语义层组成，利用证据 ID 链接两层记忆，并通过结合文本、关键词和图像的三路径检索实现精准的上下文召回。<br>
        • 论文开发了一套可扩展的流水线用于生成长程多模态对话数据集，实验证明 M2A 在处理复杂的个性化问题时显著优于现有的 RAG 和文本记忆基准。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-28</td>
      <td style="width: 55%;"><strong>Memory Retrieval in Transformers: Insights from The Encoding Specificity Principle</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Interpretability-pink" alt="Interpretability">
      <img src="https://img.shields.io/badge/Psycholinguistics-brown" alt="Psycholinguistics">
      <img src="https://img.shields.io/badge/Attention%20Mechanism-blue" alt="Attention Mechanism">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.20282">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
      • 借鉴心理学中的“编码特异性原则”（Encoding Specificity Principle），研究了 Transformer 注意力层中的记忆机制。<br>
      • 提出 Q 编码检索上下文，K 索引记忆痕迹，V 存储内容，并实证表明上下文线索被编码为关键词（Keywords）。<br>
      • 识别出了特定的注意力神经元，其激活有助于上下文定义关键词的检索，为机器遗忘等下游任务提供了理论基础和提取方法。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-28</td>
      <td style="width: 55%;"><strong>S3-Attention: Attention-Aligned Endogenous Retrieval for Memory-Bounded Long-Context Inference</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Efficient%20Inference-success" alt="Efficient Inference">
        <img src="https://img.shields.io/badge/Endogenous%20Retrieval-teal" alt="Endogenous Retrieval">
        <img src="https://img.shields.io/badge/Sparse%20Autoencoders-violet" alt="Sparse Autoencoders">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.17702">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 S3-Attention（Sparse & Semantic Streaming Attention），一种针对内存受限长上下文推理的框架，实现了 O(1) 的 GPU 内存占用。<br>
        • 利用稀疏自动编码器（SAE）将注意力状态解码为稀疏特征，在流式处理中构建 CPU 倒排索引并丢弃 KV 缓存。<br>
        • 通过特征共激活进行内源性检索，在 LongBench 上保持了接近全上下文的性能（例如在 Llama-3-8B 上保留了 99.4% 的性能）。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-19</td>
      <td style="width: 55%;"><strong>LLM-as-RNN: A Recurrent Language Model for Memory Updates and Sequence Prediction</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Recurrent%20Architecture-darkslategrey" alt="Recurrent Architecture">
        <img src="https://img.shields.io/badge/Inference--Only-orange" alt="Inference-Only">
        <img src="https://img.shields.io/badge/Time--Series-blue" alt="Time-Series">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.13352">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 LLM-as-RNN，一种仅推理的框架，将冻结的 LLM 转换为循环预测器，解决了标准 ICL 无法更新错误的问题。<br>
        • 将隐藏状态表示为自然语言记忆（结构化系统提示摘要），并通过基于反馈的文本重写在每一步更新该状态，实现了在线学习。<br>
        • 在医疗、气象和金融的时序预测任务中，LLM-as-RNN 在固定 Token 预算下显著优于 Zero-shot 和 MemPrompt 基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-14</td>
      <td style="width: 55%;"><strong>Continuum Memory Architectures for Long-Horizon LLM Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Architecture-purple" alt="Memory Architecture">
        <img src="https://img.shields.io/badge/Long--Horizon-red" alt="Long-Horizon">
        <img src="https://img.shields.io/badge/Continuum-success" alt="Continuum">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2601.09913">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 面向长时程智能体提出“连续体（continuum）”式记忆架构，解决长跨度任务中的稳定性与可持续回忆问题。<br>
        • 系统化讨论不同记忆层/库（如工作、情景、语义等）的分工与交互，以及随时间推进的管理策略。<br>
        • 通过长时程任务实验展示：架构化的记忆组织优于简单拼接/截断或朴素外检索。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-17</td>
      <td style="width: 55%;"><strong>Memory Bear AI: A Breakthrough from Memory to Cognition</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Human%20Brain%20Memory-darkcyan" alt="Human Brain Memory">
        <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2512.20651">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Memory Bear 构建了一种基于认知科学（ACT-R、艾宾浩斯）的类人记忆架构，通过区分显性与隐性记忆及引入智能语义剪枝，实现了从“记忆”到“认知”的跃迁。<br>
        • 该系统采用三层架构（存储、编排、应用），集成了自我反思引擎和多模态感知，在大幅降低 Token 消耗（约 90%）的同时，显著减少了幻觉并提升了长期交互的连贯性。<br>
        • 实验结果表明，Memory Bear 在准确率和响应延迟上均优于 Mem0 和 MemGPT，并已在医疗（慢性病管理）、企业（知识库）和教育（个性化学习）场景中验证了其有效性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-11</td>
      <td style="width: 55%;"><strong>O-Mem: Omni Memory System for Personalized, Long Horizon, Self-Evolving Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2511.13593">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • O-Mem 是一种基于主动用户画像的新型记忆框架，能够通过主动交互动态提取并更新用户特征和事件记录。<br>
        • 与依赖语义分组的系统不同，O-Mem 支持对角色属性和主题相关上下文进行层级检索，从而实现自适应且连贯的个性化响应。<br>
        • 该系统在 LoCoMo 和 PERSONAMEM 基准测试中达到了最先进的性能，同时与 LangMem 和 MemoryOS 等先前的框架相比，显著提高了 Token 效率和交互响应时间。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-11-21</td>
      <td style="width: 55%;"><strong>Episodic Memory in Agentic Frameworks: Suggesting Next Steps in Workflow Creation</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Workflow%20Memory-purple" alt="Workflow Memory">
        <img src="https://img.shields.io/badge/Next--Step-red" alt="Next-Step">
        <img src="https://img.shields.io/badge/Episodic-success" alt="Episodic">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2511.17775">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将“工作流轨迹/操作序列”作为情景记忆（episodic memory）存储，面向流程型 agent 的长期复用。<br>
        • 通过检索相似 workflow episode 为用户提供下一步建议（next-step suggestion），降低纯 LLM 规划带来的不确定性。<br>
        • 在 workflow 创建/编辑场景中评估建议质量与可用性，强调工具型、流程型 agent 的落地价值。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-11-11</td>
      <td style="width: 55%;"><strong>From Experience to Strategy: Empowering LLM Agents with Trainable Graph Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Graph%20Memory-purple" alt="Graph Memory">
        <img src="https://img.shields.io/badge/Trainable-red" alt="Trainable">
        <img src="https://img.shields.io/badge/Strategy-success" alt="Strategy">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2511.07800">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 引入可训练的图结构记忆，将经验以节点/边组织，支持跨回合复用与结构化推理。<br>
        • 重点在“从经验到策略”：通过学习记忆图上的选择/加权/路由，使 agent 能抽象出可迁移的决策模式。<br>
        • 在需要长期经验积累或多步策略形成的任务上，展示相对传统检索式记忆的优势。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-21</td>
      <td style="width: 55%;"><strong>LIGHTMEM: LIGHTWEIGHT AND EFFICIENT MEMORY-AUGMENTED GENERATION</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Human%20Memory-red" alt="Human Memory">
      <img src="https://img.shields.io/badge/Memory%20Compression-chocolate" alt="Memory Compression">
      <img src="https://img.shields.io/badge/Update%20Mechanisms-olive" alt="Update Mechanisms">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2510.18866">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • LightMem 是一种受 Atkinson-Shiffrin 人类记忆模型启发的轻量级记忆架构，旨在平衡 LLM 的性能与效率。<br>
        • 它具有三阶段流程：受认知启发的感官记忆用于过滤冗余，主题感知的短期记忆用于结构化访问，以及具有睡眠时间更新机制的长期记忆，以将维护与推理解耦。<br>
        • 在 LongMemEval 和 LoCoMo 上的实验结果表明，LightMem 在准确性上优于强大的基线模型，同时将 Token 使用量减少高达 100 倍，并显著降低了 API 调用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-10</td>
      <td style="width: 55%;"><strong>Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/System-darkblue" alt="System">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
      <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2508.09736">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 介绍了 M3-Agent，这是一种新型多模态智能体框架，通过处理连续的视觉和听觉输入来模拟人类记忆，以构建以实体为中心的情景和语义长期记忆。<br>
        • 提出了 M3-Bench，这是一个全面的长视频问答基准，包含来自机器人和网络视角的 1,020 个视频，旨在评估人物理解和跨模态推理等能力。<br>
        • 实验结果表明，通过强化学习训练的 M3-Agent 在记忆保持和推理任务中显著优于 Gemini-1.5-Pro 和 GPT-4o 等强大的基线模型。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-08</td>
      <td style="width: 55%;"><strong>A-MEM: Agentic Memory for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2502.12110">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • A-Mem 引入了一种受卢曼卡片盒笔记法（Zettelkasten）启发的动态记忆组织方式，赋予 LLM 智能体真正的长期记忆。<br>
        • 除了简单的存储，A-Mem 还支持自链接和自进化，使智能体在复杂的推理任务中获得显著优势。<br>
        • 实验结果表明，A-Mem 在性能、效率和可扩展性方面均优于现有方法，为构建更智能、更自主的 LLM 智能体奠定了坚实基础。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-10-01</td>
      <td style="width: 55%;"><strong>Improving Code Localization with Repository Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Repository%20Memory-purple" alt="Repository Memory">
        <img src="https://img.shields.io/badge/Code%20Localization-red" alt="Code Localization">
        <img src="https://img.shields.io/badge/SWE-success" alt="SWE">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2510.01003">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将仓库的 commit history/演化信息作为“长期 repository memory”，为软件工程 agent 提供可追溯的历史上下文。<br>
        • 通过检索与汇总历史变更、相关模块演进、issue/PR 线索，提升 bug/需求对应的代码定位（localization）。<br>
        • 结果表明：相较仅依赖当前代码快照，利用仓库记忆可显著提升定位准确性与定位效率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-08-12</td>
      <td style="width: 55%;"><strong>Livia: An Emotion-Aware AR Companion Powered by Modular AI Agents and Progressive Memory Compression</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/System-darkblue" alt="System">
        <img src="https://img.shields.io/badge/Memory%20Compression-chocolate" alt="Memory Compression">
        <img src="https://img.shields.io/badge/Human--AI%20Interaction-firebrick" alt="Human-AI Interaction">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2509.05298">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • Livia 是一款具有情感意识的 AR 伴侣，旨在通过模块化的多智能体架构和沉浸式增强现实交互来缓解孤独感。<br>
        • 它引入了两种新颖的记忆压缩算法——时间二进制压缩（TBC）和动态重要性记忆过滤器（DIMF）——以高效管理长期记忆，同时保留具有情感意义的上下文。<br>
        • 该系统集成了多模态情感识别（文本和语音）和自适应个性模型，展现出高准确性并能与用户建立更深层的情感纽带。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-08-05</td>
      <td style="width: 55%;"><strong>NEMORI: SELF-ORGANIZING AGENT MEMORY INSPIRED BY COGNITIVE SCIENCE</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
        <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
        <img src="https://img.shields.io/badge/Dynamic%20Memory%20Organization-darkviolet" alt="Dynamic Memory Organization">
        <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2508.03341">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • Nemori 是一种受认知科学启发的自组织记忆架构，旨在通过实现持久、自适应的记忆来解决大型语言模型在长期交互中的局限性。<br>
        • 它引入了用于自主情节分割的“两步对齐原则”和用于主动知识蒸馏的“预测-校准原则”，实现了从被动存储到主动学习的转变。<br>
        • 在 LoCoMo 和 LongMemEval 基准测试上的实验结果表明，Nemori 显著优于最先进的系统，且 Token 使用量比全上下文基线少 88%。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-07-23</td>
      <td style="width: 55%;"><strong>H-MEM: Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2507.22925">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 H-MEM，这是一种分层记忆架构，利用位置索引编码将记忆组织成四个语义层级，实现了高效的逐层检索，无需进行穷尽的相似度计算。<br>
        • 引入了一种动态记忆更新机制，根据用户反馈调整记忆权重，以反映用户不断变化的兴趣和心理状态。<br>
        • 在 LoCoMo 数据集上的实验结果表明，H-MEM 在长期对话任务中始终优于基线模型，同时显著降低了计算成本和检索延迟。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-07-10</td>
      <td style="width: 55%;"><strong>MIRIX: Multi-Agent Memory System for LLM-Based Agents</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-darkgreen" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Memory%20Modules-orange" alt="Memory Modules">
        <img src="https://img.shields.io/badge/Dataset-seagreen" alt="Dataset">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/abs/2507.07957">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • MIRIX 是一个模块化的多智能体记忆系统，通过集成由专用智能体管理的六个专门记忆组件（包括情景记忆、语义记忆和程序记忆），解决了扁平化记忆架构的局限性。<br>
        • 该框架引入了“主动检索”机制和元记忆管理器来动态协调记忆更新与检索，并在新引入的多模态基准 ScreenshotVQA（由高分辨率用户活动日志组成）上验证了这些能力。<br>
        • 实验结果表明，MIRIX 在 ScreenshotVQA 上的准确率比 RAG 基线高出 35%，存储空间减少了 99.9%，并在 LOCOMO 长对话基准上达到了最先进的性能。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-06-30</td>
      <td style="width: 55%;"><strong>Ella: Embodied Social Agents with Lifelong Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
        <img src="https://img.shields.io/badge/Episodic%20Memory-cadetblue" alt="Episodic Memory">
        <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
        <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2506.24019">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 介绍了 Ella，这是一个具身社交智能体，配备了结构化的终身多模态记忆系统，包含以名字为中心的语义记忆和时空情景记忆。<br>
        • 通过将这种终身记忆系统与基础模型集成，Ella 可以检索相关信息以进行决策、规划日常活动，并在 3D 开放世界中建立社会关系。<br>
        • 在动态环境中的实验结果证明了 Ella 影响、领导以及与其他智能体合作的能力，突显了结合结构化记忆与基础模型的潜力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-30</td>
      <td style="width: 55%;"><strong>Memory OS of AI Agent</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Operating%20System-midnightblue" alt="Memory Operating System">
      <img src="https://img.shields.io/badge/Human%20Brain%20Memory-darkcyan" alt="Human Brain Memory">
      <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      <img src="https://img.shields.io/badge/Personalized%20Memory-darkturquoise" alt="Personalized Memory">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2025.emnlp-main.1318.pdf">
      <img src="https://img.shields.io/badge/EMNLP-Paper-black?labelColor=green" alt="EMNLP Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemoryOS 旨在为 AI 智能体提供全面且高效的记忆管理。<br>
        • 受计算机操作系统内存管理原理和人类记忆分层结构的启发，MemoryOS 采用独特的段-页分层存储架构，包含四个核心功能模块：记忆存储、记忆更新、记忆检索和响应生成。<br>
        • 实验结果表明，MemoryOS 在主流基准测试的长对话中显著提高了上下文连贯性和个性化记忆保持能力；例如，在 LoCoMo 基准测试上，平均 F1 和 BLEU-1 分数分别提高了 49.11% 和 46.18%。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-28</td>
      <td style="width: 55%;"><strong>MemOS: A Memory OS for AI System</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/MemOS-darkorange" alt="MemOS">
        <img src="https://img.shields.io/badge/Memory%20Operating%20System-midnightblue" alt="Memory Operating System">
        <img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/abs/2507.03724">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • MemOS（记忆操作系统）是专为 AI 系统设计的记忆操作系统，它将记忆视为可管理的系统资源，统一了显式记忆、基于激活的记忆和参数级记忆的表示、调度和进化，以实现低成本的存储和检索。<br>
        • MemOS 采用三层架构，由接口层、操作层和基础设施层组成。接口层与用户或上游系统交互并提供标准化记忆 API；操作层组织和调度记忆资源；基础设施层处理记忆的存储、安全、迁移和数据流。<br>
        • MemOS 为跨任务适应、跨模态进化和跨平台迁移提供了操作系统级的支持。它的引入标志着大模型从“仅感知和生成”向“具有记忆和进化能力”智能的关键转变。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-04-28</td>
      <td style="width: 55%;"><strong>Mem0 Building production-ready AI agents with Scalable Long-Term memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Knowledge%20Graph-sepia" alt="Knowledge Graph">
      <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2504.19413">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • Mem0 是一种记忆架构，能从对话中动态提取并整合关键信息，使 AI 系统能够记住重要内容并维持跨会话对话。<br>
        • 作者进一步提出了 Mem0g，通过结合图结构记忆（即知识图谱）扩展了 Mem0，使 AI 系统能更有效地处理复杂的关系推理。<br>
        • NLI 任务增强了成分句法归纳能力，而 SMS 任务则降低了上层的这一能力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-02-22</td>
      <td style="width: 55%;"><strong>Echo: A Large Language Model with Temporal Episodic Memory</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Temporal%20Episodic-purple" alt="Temporal Episodic">
        <img src="https://img.shields.io/badge/LLM%20Model-red" alt="LLM Model">
        <img src="https://img.shields.io/badge/Recall-success" alt="Recall">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2502.16090">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出带“时间化情景记忆”的 LLM 形态，将事件按时间索引存储，面向时序依赖与经历回放式回忆。<br>
        • 强调 temporal episodic memory 对事件序列、时间关系、跨回合一致性推理的帮助。<br>
        • 通过相关基准/任务展示：相较无显式情景记忆的模型，在时序回忆与推理上更可靠。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-01-20</td>
      <td style="width: 55%;"><strong>ZEP: A TEMPORAL KNOWLEDGE GRAPH ARCHITECTURE FOR AGENT MEMORY</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Framework-darkslategrey" alt="Memory Framework">
      <img src="https://img.shields.io/badge/Knowledge%20Graph-sepia" alt="Knowledge Graph">
      <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2501.13956">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 介绍了 Zep，这是一种由动态且具有时间感知的知识图谱引擎 Graphiti 驱动的 AI 智能体记忆层服务。<br>
        • Zep 在保持历史关系的同时，综合了非结构化对话数据和结构化业务数据，使智能体能够处理复杂、演变的上下文。<br>
        • 实验结果表明，Zep 在深度记忆检索（DMR）基准测试中优于 MemGPT，并在更具挑战性的 LongMemEval 基准测试中显著提高了准确性和延迟表现。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-01-09</td>
      <td style="width: 55%;"><strong>Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Model%20Architecture-indigo" alt="Model Architecture">
      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      <img src="https://img.shields.io/badge/Dynamic%20Memory%20Management-mediumseagreen" alt="Dynamic Memory Management">
      <img src="https://img.shields.io/badge/Human--AI%20Interaction-firebrick" alt="Human-AI Interaction">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/abs/2501.00358">
      <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 Embodied VideoAgent，这是一种多模态智能体，通过融合第一视角视频与深度、姿态等具身感知输入来构建持久的场景记忆，以解决动态场景理解问题。<br>
        • 具有 VLM 驱动的记忆更新机制，可在动作过程中动态跟踪物体状态变化和关系，确保记忆在长形式交互中保持准确。<br>
        • 该智能体在 Ego4D-VQ3D 和 OpenEQA 等基准测试中达到了最先进的性能，并在生成合成具身用户-助手交互数据方面展示了实用价值。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-12-12</td>
      <td style="width: 55%;"><strong>Memory Layers at Scale</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Memory%20Layers-purple" alt="Memory Layers">
        <img src="https://img.shields.io/badge/KV%20Lookup-red" alt="KV Lookup">
        <img src="https://img.shields.io/badge/Scaling-success" alt="Scaling">
      </td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2412.09764">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 探索可训练的 key–value 记忆层（memory layers）作为“稀疏查表式容量扩展”，在不显著增加计算的情况下提升模型存储能力。<br>
        • 讨论大规模训练与工程实现：如何让超大记忆表可并行、可扩展并保持稳定训练。<br>
        • 在多个任务上展示：大容量记忆层可提升知识/事实类能力，并具备更好的容量-成本权衡。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-06-16</td>
      <td style="width: 55%;"><strong>Towards Lifelong Dialogue Agents via Timeline-based Memory Management</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Memory%20Management-darkorange" alt="Memory Management">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Graph--Structured%20Memory-seagreen" alt="Graph-Structured Memory">
      <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
      <img src="https://img.shields.io/badge/Benchmark-darkred" alt="Benchmark">
      </td>
      <td style="width: 15%;"><a href="https://aclanthology.org/2025.naacl-long.435.pdf">
      <img src="https://img.shields.io/badge/NAACL-Paper-black?labelColor=cyan" alt="NAACL Paper">
      </td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出了 THEANINE，这是一个用于终身对话智能体的框架，利用关系感知的记忆图谱来存储记忆而不删除，保留了时间与因果连接。<br>
        • 引入了一种时间轴增强的响应生成方法，检索并细化整个记忆时间轴，确保为长期交互保留丰富的上下文线索。<br>
        • 展示了 TeaFarm，这是一个反事实驱动的评估流程，旨在压力测试对话智能体正确引用过去对话的能力，THEANINE 在该流程中表现出优于现有基线的性能。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2024-05-04</td>
      <td style="width: 55%;"><strong>Memoro: Using Large Language Models to Realize a Concise Interface for Real-Time Memory Augmentation</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/System-darkblue" alt="System">
        <img src="https://img.shields.io/badge/Human--AI%20Interaction-firebrick" alt="Human-AI Interaction">
        <img src="https://img.shields.io/badge/Memory%20Retrieval-magenta" alt="Memory Retrieval">
        <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://dl.acm.org/doi/10.1145/3613904.3642450">
        <img src="https://img.shields.io/badge/ACM-Paper-black?labelColor=blue" alt="ACM Paper">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • Memoro 是一款可穿戴的音频记忆助手，旨在利用大型语言模型（LLM）进行简明的记忆检索，从而最大限度地减少社交互动中的干扰。<br>
          • 该系统引入了“无查询模式”，根据实时对话上下文主动推断用户的记忆需求，同时保留了用于明确自然语言请求的传统“查询模式”。<br>
          • 用户研究表明，Memoro 提高了回忆的信心并减少了设备交互时间，同时有效地保持了正在进行的对话质量。
        </td>
    </tr>
  </table>

</details>

## 🧰 仓库资源

### 📊 测试基准

|     任务类型      | 数据集和评估基准                                                  |
| :-----------------------: | ------------------------------------------------------------ |
| **个性化任务评估**  | [IMPLEXCONV](https://aclanthology.org/2025.emnlp-main.580.pdf), [PERSONAMEM](https://arxiv.org/pdf/2504.14225), [PERSONAMEM-v2](https://www.arxiv.org/pdf/2512.06688), [PersonaBench](https://aclanthology.org/2025.findings-acl.49.pdf), [PersonaFeedback](https://arxiv.org/pdf/2506.12915), [LaMP](https://aclanthology.org/2024.acl-long.399.pdf), [MemDaily](https://arxiv.org/pdf/2409.20163), [MPR](https://arxiv.org/pdf/2508.13250), [KnowMe-Bench](https://arxiv.org/abs/2601.04745)  |
|  **综合评价**   | [MemoryAgentBench](https://arxiv.org/pdf/2507.05257), [LifelongAgentBench](https://arxiv.org/pdf/2505.11942), [StreamBench](https://arxiv.org/pdf/2406.08747) |
|  **记忆机制评价**   | [MemBench](https://aclanthology.org/2025.findings-acl.989.pdf),  [Minerva](https://arxiv.org/pdf/2502.03358), [MemoryBench](https://arxiv.org/pdf/2510.17281) |
|  **长期记忆评估**   | [LOCCO](https://aclanthology.org/2025.findings-acl.1014.pdf), [LONGMEMEVAL](https://arxiv.org/pdf/2410.10813), [LOCOMO](https://aclanthology.org/2024.acl-long.747.pdf), [MADial-Bench](https://arxiv.org/abs/2409.15240), [StoryBench](https://arxiv.org/pdf/2506.13356), [DialSim](https://arxiv.org/pdf/2406.13144), [Mem-Gallery](https://arxiv.org/pdf/2601.03515), [RealMem](https://arxiv.org/pdf/2601.06966), [CloneMem](https://arxiv.org/pdf/2601.07023) |
|  **长对话推理**   | [PREFEVAL](https://arxiv.org/pdf/2502.09597),  [MiniLongBench](https://aclanthology.org/2025.acl-long.560.pdf)|
|  **长上下文理解**   | [LongBench V2](https://arxiv.org/pdf/2412.15204), [LongBench](https://arxiv.org/abs/2308.14508), [BABILong](https://arxiv.org/pdf/2406.10149), [HotpotQA](https://aclanthology.org/D18-1259.pdf) |
|  **长上下文评估** |[SCBENCH](https://arxiv.org/abs/2412.10319), [L-CiteEval](https://arxiv.org/pdf/2410.02115), [GLE](https://aclanthology.org/2024.acl-long.859/), [HOMER](https://arxiv.org/pdf/2404.10308), [RULER](https://arxiv.org/pdf/2404.06654), [MM-Needle](https://aclanthology.org/2025.naacl-long.166.pdf) |
|  **长文本生成**   | [LongGenBench](https://arxiv.org/pdf/2409.02076) |
|  **情景记忆评估**   | [PerLTQA](https://aclanthology.org/2024.sighan-1.18.pdf)|
|  **记忆幻觉评估**   | [HaluMem](https://arxiv.org/pdf/2511.03506) |
|  **Web交互与导航** | [WebChoreArena](https://arxiv.org/pdf/2506.01952), [MT-Mind2Web](https://arxiv.org/pdf/2402.15057), [WebShop](https://arxiv.org/pdf/2207.01206), [WebArena](https://arxiv.org/pdf/2307.13854) |


### 💻 开源系统
下面系统按照时间顺序排列:

| 系统      | 时间       | 关注数 | 开源网址和官方网站 |
|-------------|------------|-------|------------------|
| Zep         | 2023-05-19 | ![GitHub Repo stars](https://img.shields.io/github/stars/getzep/zep?style=social) | https://github.com/getzep/zep<br>https://www.getzep.com/ |
| Agentmemory | 2023-07-07 | ![GitHub Repo stars](https://img.shields.io/github/stars/elizaOS/agentmemory?style=social) | https://github.com/elizaOS/agentmemory<br>No official website |
| Cognee      | 2023-10-09 | ![GitHub Repo stars](https://img.shields.io/github/stars/topoteretes/cognee?style=social) | https://github.com/topoteretes/cognee<br>https://www.cognee.ai/ |
| Letta       | 2023-10-26 | ![GitHub Repo stars](https://img.shields.io/github/stars/letta-ai/letta?style=social) | https://github.com/letta-ai/letta<br>https://www.letta.com/ |
| Supermemory | 2024-02-22 | ![GitHub Repo stars](https://img.shields.io/github/stars/supermemoryai/supermemory?style=social) | https://github.com/supermemoryai/supermemory<br>https://supermemory.ai/ |
| Memary      | 2024-04-26 | ![GitHub Repo stars](https://img.shields.io/github/stars/kingjulio8238/Memary?style=social) | https://github.com/kingjulio8238/Memary <br>No official website |
| Second-Me   | 2024-06-26 | ![GitHub Repo stars](https://img.shields.io/github/stars/mindverse/Second-Me?style=social) | https://github.com/mindverse/Second-Me<br>https://home.second.me/ |
| Mem0        | 2024-07-11 | ![GitHub Repo stars](https://img.shields.io/github/stars/mem0ai/mem0?style=social) | https://github.com/mem0ai/mem0<br>https://mem0.ai/ |
| Memobase    | 2024-10-05 | ![GitHub Repo stars](https://img.shields.io/github/stars/memodb-io/memobase?style=social) | https://github.com/memodb-io/memobase<br>https://www.memobase.io/ |
| LangMem     | 2025-01-22 | ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langmem?style=social) | https://github.com/langchain-ai/langmem<br>https://langchain-ai.github.io/langmem/ |
| A-Mem       | 2025-02-17 | ![GitHub Repo stars](https://img.shields.io/github/stars/agiresearch/A-mem?style=social) | https://github.com/agiresearch/A-mem <br>No official website |
| Mirix       | 2025-04-16 | ![GitHub Repo stars](https://img.shields.io/github/stars/Mirix-AI/MIRIX?style=social) | https://github.com/Mirix-AI/MIRIX<br>https://mirix.io/ |
| MemEngine   | 2025-05-04 | ![GitHub Repo stars](https://img.shields.io/github/stars/nuster1128/MemEngine?style=social) | https://github.com/nuster1128/MemEngine<br>No official website |
| MemOS       | 2025-05-28 | ![GitHub Repo stars](https://img.shields.io/github/stars/MemTensor/MemOS?style=social) | https://github.com/MemTensor/MemOS<br>https://memos.openmem.net/ |
| MemoryOS    | 2025-05-30 | ![GitHub Repo stars](https://img.shields.io/github/stars/BAI-LAB/MemoryOS?style=social) | https://github.com/BAI-LAB/MemoryOS<br>https://baijia.online/memoryos/ |
| ReMe        | 2025-06-05 | ![GitHub Repo stars](https://img.shields.io/github/stars/agentscope-ai/ReMe?style=social) | https://github.com/agentscope-ai/ReMe<br>https://reme.agentscope.io/ |
| Nemori      | 2025-06-30 | ![GitHub Repo stars](https://img.shields.io/github/stars/nemori-ai/nemori?style=social) | https://github.com/nemori-ai/nemori <br>No official website |
| Memori      | 2025-07-24 | ![GitHub Repo stars](https://img.shields.io/github/stars/MemoriLabs/Memori?style=social) | https://github.com/MemoriLabs/Memori<br>https://memorilabs.ai/ |
| MemU        | 2025-08-09 | ![GitHub Repo stars](https://img.shields.io/github/stars/NevaMind-AI/memU?style=social) | https://github.com/NevaMind-AI/memU<br>https://memu.pro/ |
| MemMachine  | 2025-08-16 | ![GitHub Repo stars](https://img.shields.io/github/stars/MemMachine/MemMachine?style=social) | https://github.com/MemMachine/MemMachine<br>https://memmachine.ai/ |
| MineContext | 2025-09-30 | ![GitHub Repo stars](https://img.shields.io/github/stars/volcengine/MineContext?style=social) | https://github.com/volcengine/MineContext<br>No official website |
| TiMem | 2025-10-25 | ![GitHub Repo stars](https://img.shields.io/github/stars/TiMEM-AI/timem?style=social) | https://github.com/TiMEM-AI/timem<br>https://timem.cloud |
| EverMemOS   | 2025-10-29 | ![GitHub Repo stars](https://img.shields.io/github/stars/EverMind-AI/EverMemOS?style=social) | https://github.com/EverMind-AI/EverMemOS<br>https://evermind.ai/ |
| MemoryBear  | 2025-12-17 | ![GitHub Repo stars](https://img.shields.io/github/stars/SuanmoSuanyangTechnology/MemoryBear?style=social) | https://github.com/SuanmoSuanyangTechnology/MemoryBear<br>https://www.memorybear.ai/ |
| OMEGA  | 2025-12-17 | ![GitHub Repo stars](https://img.shields.io/github/stars/omega-memory/omega-memory?style=social) | https://github.com/omega-memory/omega-memory<br>https://omegamax.co/ |
| Autohand Code CLI | 2025-12-20 | ![GitHub Repo stars](https://img.shields.io/github/stars/autohandai/code-cli?style=social) | https://github.com/autohandai/code-cli<br>https://www.autohand.ai/code/ |
| Hindsight   | 2025-12-22 | ![GitHub Repo stars](https://img.shields.io/github/stars/vectorize-io/hindsight?style=social) | https://github.com/vectorize-io/hindsight<br>https://hindsight.vectorize.io/ |
| widemem-ai | 2026-02-23 | ![GitHub Repo stars](https://img.shields.io/github/stars/remete618/widemem-ai?style=social) | https://github.com/remete618/widemem-ai<br>https://widemem.ai |
| Riverse | 2026-02-25 | ![GitHub Repo stars](https://img.shields.io/github/stars/wangjiake/JKRiver?style=social) | https://github.com/wangjiake/JKRiver<br>https://wangjiake.github.io/riverse-docs/ |
| SuperLocalMemory | 2026-03-01 | ![GitHub Repo stars](https://img.shields.io/github/stars/qualixar/superlocalmemory?style=social) | https://github.com/qualixar/superlocalmemory<br>https://superlocalmemory.com/ |
| Cog | 2026-03-15 | ![GitHub Repo stars](https://img.shields.io/github/stars/marciopuga/cog?style=social) | https://github.com/marciopuga/cog<br>No official website |
| NeverOnce | 2026-03-18 | ![GitHub Repo stars](https://img.shields.io/github/stars/WeberG619/neveronce?style=social) | https://github.com/WeberG619/neveronce<br>https://pypi.org/project/neveronce/ |
| MHN AI Agent Memory | 2026-03-21 | ![GitHub Repo stars](https://img.shields.io/github/stars/shahzebqazi/mhn-ai-agent-memory?style=social) | https://github.com/shahzebqazi/mhn-ai-agent-memory<br>No official website |

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
      <td rowspan="6"><strong>记忆基本理论</strong></td>
      <td>https://www.youtube.com/watch?v=k3FUWWEwgfc</td>
      <td>基于LangGraph的短期记忆</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=WsGVXiWzTpI</td>
      <td>OpenAI: 智能体记忆设计模式</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=fsENEq4F55Q</td>
      <td>基于LangGraph的长期记忆</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=L-au0tvDJbI</td>
      <td>llm不具备类似人类的工作记忆</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=RkWor1BZOn0</td>
      <td> LLM进行长期记忆和个性化</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=CFih0_6tn2w</td>
      <td>将记忆作为大语言模型的一等任务</td>
    </tr>
    <tr>
      <td rowspan="4"><strong>记忆相关工具</strong></td>
      <td>https://www.bilibili.com/video/BV1hom8YAEhX</td>
      <td>记忆Agent</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1CU421o7DL</td>
      <td>基于Langchain的记忆agent</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1arJazVEaX</td>
      <td>开启记忆MCP</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV11HxXzuExk</td>
      <td>大模型Agent记忆</td>
    </tr>
    <tr>
      <td rowspan="10"><strong>记忆相关论文</strong></td>
      <td>https://www.bilibili.com/video/BV1XT8ez6E46</td>
      <td>AI agent记忆综述</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1f12wBpEXX</td>
      <td>为自进化智能体组织生成潜在记忆</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1deyFBKEFh</td>
      <td>大型语言模型的检索器预训练记忆</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV18FnVzpE6S</td>
      <td>记忆管理经验跟随行为的实证研究</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1mpbrzSEH9</td>
      <td>Agent记忆工作流</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1qEtozyEoh</td>
      <td>大型语言模型智能体记忆机制简介</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1FGrhYhEZK</td>
      <td>记忆层大规模扩展</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1aQ1xBkE45</td>
      <td>LLM agent记忆</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1Yz421f7uH</td>
      <td>评估LLM智能体的非常长期的会话记忆</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV19RWdzxEsR</td>
      <td>轻量级插件式记忆系统</td>
    </tr>
  </tbody>
</table>

### 🧠 Adam 框架

* **描述（Description）：** 基于 OpenClaw 构建的面向本地 AI 助手的五层持久化记忆与一致性架构。该框架旨在解决人工智能系统中的“记忆失效”（AI amnesia）问题，包括跨会话记忆丢失以及单次会话内部一致性逐渐退化的问题。
* **层级结构（Layers）：** 包括 Vault 注入机制、中期记忆检索（mid-session memory search）、神经图结构（包含 7219+ 个神经元）、基于 Gemini 每日核对（nightly reconciliation），以及带有 scratchpad dropout 检测功能的一致性监控模块。
* **验证情况（Validated）：** 已在真实业务环境中运行并验证，共计 353 个会话、6619 轮消息交互，持续生产环境运行 8 个月，由一名非开发人员完成部署与使用。
* **平台（Platform）：** 支持 Windows / macOS / Linux 平台，基于 OpenClaw 架构，采用本地优先（local-first）设计，并具有模型无关性（model-agnostic）。
* **相关链接（Links）：** [GitHub](https://github.com/strangeadvancedmarketing/Adam) | [Live Demo](https://strangeadvancedmarketing.github.io/Adam/) | [Interactive Proof](https://strangeadvancedmarketing.github.io/Adam/showcase/ai-amnesia-solved.html)

## 🤝  如何贡献
提交样式: 
```
Title: [paper's title]
Head: [head name1] (, [head name2] ...)
Published: [arXiv / ACL / ICLR / NIPS / ...]
Summary:
  - Innovation:
  - Tasks:
  - Significant Result: 
```

## 💬 社区和支持

加入我们的社区，提出问题，分享您的项目，并与其他开发人员联系.

- **GitHub Issues**: 在我们的 <a href="https://github.com/pm1255/Awesome-World-Model/issues" target="_blank">GitHub Issues</a> 中报告问题或提出功能需求。  
- **GitHub Pull Requests**: 通过 <a href="https://github.com/pm1255/Awesome-World-Model/pulls" target="_blank">Pull Requests</a> 提交代码改进。  
- **小红书**: 扫描下方二维码加入我们的讨论组，获取最新的World Model相关的研究信息，或推广您的相关研究成果。

<!-- <div style="text-align: center;">
  <img src="assets/rednote-qr-code.jpg" alt="QR Code" width="255">
</div> -->

<center>
  <img src="assets/rednote-qr-code.jpg" alt="QR Code" width="255">
</center>

## 🌟 仓库关注量

<a href="https://www.star-history.com/#IAAR-Shanghai/Awesome-AI-Memory&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=date&legend=top-left" />
 </picture>
</a>
