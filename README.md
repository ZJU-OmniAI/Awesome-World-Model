# Awesome-AI-Memory

<p align="center">
    【English | <a href="README_cn.md">中文</a>】
</p>

<div align="center">
    <img src="assets/Gemini_Generated_Image_awesome_world_model.png" alt="Survey Framework" width="82%">
</div>

[![Awesome](https://awesome.re/badge.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![](https://img.shields.io/badge/PRs-Welcome-red)

<a id="introduction"></a>
## 👋 Introduction
Current Artificial Intelligence, especially in Reinforcement Learning (RL) and Autonomous Agents, still faces immense challenges when planning and decision-making in complex, dynamic, and unpredictable real-world environments. Traditional "Model-Free" approaches often rely heavily on extensive trial-and-error, resulting in extremely low data efficiency and poor generalization to unseen scenarios. Even Large Language Models (LLMs), which excel in other domains, often exhibit brittle reasoning and unrealistic planning due to a fundamental lack of understanding of physical laws (i.e., lacking "common sense").

To overcome these bottlenecks, World Models have emerged as a critical research direction for advancing AI towards higher-level intelligence. The core idea is to endow an AI system with an internal mental model of the external world—one that understands physical laws, causal relationships, and environmental dynamics. Through this model, an agent can perform internal simulations ("dreaming") in its "mind." It cannot only perceive the current state accurately but also use imagination to predict the future and evaluate the consequences of different actions, thereby achieving highly efficient planning, reflection, and reasoning without incurring the cost of real-world trial-and-error.

Awesome-World-Model is a curated list of resources focused on AI World Models and their applications across various domains, including Reinforcement Learning, Embodied AI, Autonomous Driving, and Multimodal Perception. It systematically compiles relevant research papers, open-source frameworks, benchmarks, and cutting-edge practices. This repository is dedicated to organizing and presenting the rapidly evolving landscape of World Model research, connecting multiple fields such as Deep Learning, Generative Models (especially Video Generation), Control Theory, Computer Vision, and Cognitive Science.

---

<a id="goal-of-repository"></a>
## 🎯 Goal of Repository
Our mission is to establish a centralized, continuously evolving knowledge base that serves as a valuable reference for researchers and practitioners, ultimately accelerating the development of intelligent systems capable of long-term memory retention, sustained reasoning, and adaptive evolution over time.

---

<a id="project-scope"></a>
## 📏 Project Scope
This repository focuses on mechanisms, architectures, and applications that enable AI systems to build internal mental models of the external world (encompassing physical, causal, and social laws), rather than general generative models (unless specifically related to video/image generation as a world simulator). The content spans from foundational theoretical research (e.g., representation learning) to concrete engineering practices (e.g., simulators and deployment).

🌀 Included Content (In Scope)
- World Model Architectural Design: Latent Space Models specifically designed for learning Environment Dynamics, Predictive Coding architectures, and recurrent networks (RNNs/Transformers) serving as Transition Models.
- Representation Learning for World Models: Learning representations that are causal, physically meaningful, or Object-Centric, and the application of Self-Supervised Learning (SSL) in constructing world models.
- Simulation and Imagination Mechanisms: Using generative video/image models (e.g., Diffusion Models, GANs) as interactive World Simulators, and agent "Dreaming" or "Simulation-in-the-head" within internal models.
- Model-Based Planning and Control (MPC): Decision-making methods that combine World Models with Trajectory Planning, Tree Search (e.g., MCTS), or Gradient Descent optimization.
- Model-Based Reinforcement Learning (MBRL): Using learned World Models to accelerate Policy Optimization; offline or online RL via "imagination."
- Domain-Specific Applications: World Models for Autonomous Driving, Embodied Robotic manipulation, navigation, and scientific simulations.
- Cognitive Science and Biological Inspiration: Neuroscience models of how the Hippocampus or Neocortex builds environmental maps, and their implications for AI World Models.
- Evaluation and Benchmarking: Benchmarks and Datasets specifically for measuring World Model prediction accuracy, planning efficiency, data efficiency, and generalization.
- Open-Source Frameworks and Tools: Repositories and Simulation Environments dedicated to building and testing World Models.

🌀 Excluded Content (Out of Scope)
- General Video or Image Generation Research: If the purpose is not serving as a world model to support agent planning or understanding (e.g., general art generation, unconditional video interpolation).
- General Model-Free Reinforcement Learning: Unless it demonstrates a combination with World Models (e.g., as a baseline in Actor-Critic, but the focus isn't the world model itself).
- Pure Large Language Model (LLM) Reasoning: Unless the research specifically focuses on LLMs as a logical or common-sense model of the world applied to physical entities.
- Traditional Deterministic Physics Simulators: Unless focused on learning (Leaning from Data) physical laws, or used as a tool for building data-driven world models.
- Generic Machine Learning or Computer Vision Methods: Lacking a direct World Model application scenario.

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

<a id="recent-hot-research-and-news"></a>
## 🔔 Recent hot research and news
+ 2026-4-4 – 🎉 Initial Repo

---

## 🗺️ Table of Contents
- [Introduction](#introduction)
- [Goal of Repository](#goal-of-repository)
- [Project Scope](#project-scope)
- [Recent hot research and news](#recent-hot-research-and-news)
- [Core Concepts](#core-concepts)
- [Paper List](#paper-list)
  - [Survey](#survey)
  - [Framework & Methods](#framework-methods)
  - [Datasets & Benchmark](#datasets-benchmark)
- [Resources](#resources)
  - [Benchmarks and Tasks](#benchmarks-and-tasks)
  - [Multi-media Resource](#multi-media-resource)
- [Make a Contribution](#make-a-contribution)
- [Community and Support](#community-and-support)

---

<a id="core-concepts"></a>
## 🧠 Core Concepts

- **World Model**: An internal mental model of an AI system designed to understand the laws of physics, causal relationships, and the dynamic changes of the environment. It endows an agent with "imagination," enabling it to simulate future states internally and evaluate the consequences of actions, thereby achieving efficient planning and decision-making without resorting to expensive trial-and-error in the real environment.

- **State Representation Learning**: The process of transforming high-dimensional, redundant raw observational data (e.g., images, video) into low-dimensional, compact latent vectors that contain crucial semantic information. Ideal representations should possess the Markov property and be able to disentangle different entities and their attributes within the environment.

- **Transition Model / Dynamics Model**: A core component of the world model responsible for predicting how the environment will evolve to the next state after executing a specific action in the current state ($S_t, A_t \rightarrow S_{t+1}$). It captures the physical laws and causal logic of the environment.

- **Latent Space Simulation**: Performing future prediction and inference within a low-dimensional latent space rather than the raw pixel space. This greatly improves computational efficiency and allows the model to focus on high-level semantic changes while ignoring irrelevant details.

- **Model-Based Planning**: The process where an agent utilizes the world model to search for an optimal sequence of actions during lookahead or "dreaming." Common algorithms include Model Predictive Control (MPC) and Monte Carlo Tree Search (MCTS).

- **Model-Based Reinforcement Learning (MBRL)**: A reinforcement learning paradigm where the agent first learns a world model and then utilizes this model to generate simulated experience to train a policy or value function, thereby significantly improving data efficiency.

- **Differentiable Physics Engine**: A physics simulator capable of computing the gradients of outputs with respect to inputs. When integrated into a world model, it allows for direct optimization of control policies via gradient descent, enabling highly efficient learning.

- **Object-Centric Representation**: A way of representing the environment as a set of discrete objects and their interactions. This approach aligns with human cognition, helping to improve the model's generalization to unseen scenarios and its causal reasoning capabilities.

- **Multimodal World Model**: A world model capable of processing and integrating multiple perceptual modalities (e.g., vision, language, tactile, action). It leverages complementary information from different modalities to build a more comprehensive and robust understanding of the environment.

- **Causal Discovery & Reasoning**: The ability to distinguish between correlation and causation within a world model. This enables the agent to understand "what would happen if I did this" (Intervention) and to perform counterfactual reasoning.

- **Cognitive Map**: A specific form of a world model that focuses on the internal representation of the environment's spatial structure, topological relationships, and key landmarks, often used for navigation and long-term planning tasks.

- **General / Foundation World Model**: A world model pre-trained on massive, diverse datasets (e.g., internet-scale video) possessing strong generalization capabilities. It can serve as a universal physical common-sense knowledge base for downstream embodied AI tasks like robotic manipulation and autonomous driving.

---

<a id="paper-list"></a>
## 📚 Paper List
Papers below are ordered by **publication date**:

<a id="survey"></a>
<details>
  <summary><strong>Survey</strong></summary>

  <table style="width: 100%;">
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
      <td colspan="3">
            • Addresses the ongoing industry debate over the performance and cost trade-offs between long-context models and external memory systems for building persistent agents.<br>
            • Conducts a systematic cross-benchmark evaluation of long-context approaches and fact-based external memory solutions across three major memory benchmarks, assessing both accuracy and cumulative API inference cost.<br>
            • Long-context models demonstrate advantages in factual recall, but their costs increase with each interaction turn; at a 100k context length, memory systems surpass them in cost efficiency after approximately 10 turns, providing a quantitative basis for real-world engineering decisions.
        </td>
    <\tr>
  </table>
</details>

<a id="framework-methods"></a>
<details>
  <summary><strong>Framework & Methods</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>Date</strong></td>
      <td><strong>Paper & Summary</strong></td>
      <td><strong>Tags</strong></td>
      <td><strong>Links</strong></td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-03-11</td>
      <td style="width: 55%;"><strong>EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/RL Training-red" alt="safety">
        <img src="https://img.shields.io/badge/Physical Consistency-yellow" alt="Evolution">
      </td>
      <td style="width: 15%;"><a href="[https://arxiv.org/abs/2406.08407">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
      </a></td>
    </tr>
      </tr>
      <td colspan="3">
            • Addresses the ongoing industry debate over the performance and cost trade-offs between long-context models and external memory systems for building persistent agents.<br>
            • Conducts a systematic cross-benchmark evaluation of long-context approaches and fact-based external memory solutions across three major memory benchmarks, assessing both accuracy and cumulative API inference cost.<br>
            • Long-context models demonstrate advantages in factual recall, but their costs increase with each interaction turn; at a 100k context length, memory systems surpass them in cost efficiency after approximately 10 turns, providing a quantitative basis for real-world engineering decisions.
        </td>
    <\tr>
  </table>
</details>

<a id="datasets-benchmark"></a>
<details>
  <summary><strong>Datasets & Benchmark</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>Date</strong></td>
      <td><strong>Paper & Summary</strong></td>
      <td><strong>Tags</strong></td>
      <td><strong>Links</strong></td>
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
      </tr>
      <td colspan="3">
            • Addresses the ongoing industry debate over the performance and cost trade-offs between long-context models and external memory systems for building persistent agents.<br>
            • Conducts a systematic cross-benchmark evaluation of long-context approaches and fact-based external memory solutions across three major memory benchmarks, assessing both accuracy and cumulative API inference cost.<br>
            • Long-context models demonstrate advantages in factual recall, but their costs increase with each interaction turn; at a 100k context length, memory systems surpass them in cost efficiency after approximately 10 turns, providing a quantitative basis for real-world engineering decisions.
        </td>
    <\tr>
  </table>
</details>

<a id="resources"></a>
## 🧰 Resources

<a id="benchmarks-and-tasks"></a>
### 📊 Benchmarks and Tasks

| Task Type | Benchmarks & Datasets |
| :--: | -- |
| **Physical Consistency** | [MMWorld](https://arxiv.org/abs/2406.08407) |

<a id="multi-media-resource"></a>
### 🎥 Multi-media Resource

<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>Website Link</th>
      <th>Introduction</th>
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

<a id="make-a-contribution"></a>
## 🤝 Make a Contribution
Issue Template:
```
Title: [paper's title]
Head: [head name1] (, [head name2] ...)
Published: [arXiv / ACL / ICLR / NIPS / ...]
Summary:
  - Innovation:
  - Tasks:
  - Significant Result:
```

<a id="community-and-support"></a>
## 💬 Community and Support

Join our community to ask questions, share your projects, and connect with other developers.

- **GitHub Issues**: Report bugs or request features in our <a href="https://github.com/pm1255/Awesome-World-Model/issues" target="_blank">GitHub Issues</a>.
- **GitHub Pull Requests**: Contribute code improvements via <a href="https://github.com/pm1255/Awesome-World-Model/pulls" target="_blank">Pull Requests</a>.
- **Rednote**: Scan the QR code below to join our discussion group, get the latest research information related to World Model, or promote your related research results.

<!-- <div style="text-align: center;">
  <img src="assets/rednote-qr-code.jpg" alt="QR Code" width="255">
</div> -->

<!-- <center>
  <img src="assets/rednote-qr-code.jpg" alt="QR Code" width="255">
</center> -->

<table style="width:100%">
  <tr>
    <td align="center">
      <img src="assets/rednote-qr-code.jpg" alt="QR Code" width="255">
    </td>
  </tr>
</table>
