# Awesome-AI-Memory

<p align="center">
    【English | <a href="README_cn.md">中文</a></a>】
</p>

<div align="center">
    <img src="assets/Gemini_Generated_Image_awesome_world_model.png" alt="Survey Framework" width="82%">
</div>

[![Awesome](https://awesome.re/badge.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![](https://img.shields.io/badge/PRs-Welcome-red)


## 👋 Introduction
Current Artificial Intelligence, especially in Reinforcement Learning (RL) and Autonomous Agents, still faces immense challenges when planning and decision-making in complex, dynamic, and unpredictable real-world environments. Traditional "Model-Free" approaches often rely heavily on extensive trial-and-error, resulting in extremely low data efficiency and poor generalization to unseen scenarios. Even Large Language Models (LLMs), which excel in other domains, often exhibit brittle reasoning and unrealistic planning due to a fundamental lack of understanding of physical laws (i.e., lacking "common sense").

To overcome these bottlenecks, World Models have emerged as a critical research direction for advancing AI towards higher-level intelligence. The core idea is to endow an AI system with an internal mental model of the external world—one that understands physical laws, causal relationships, and environmental dynamics. Through this model, an agent can perform internal simulations ("dreaming") in its "mind." It cannot only perceive the current state accurately but also use imagination to predict the future and evaluate the consequences of different actions, thereby achieving highly efficient planning, reflection, and reasoning without incurring the cost of real-world trial-and-error.

Awesome-World-Model is a curated list of resources focused on AI World Models and their applications across various domains, including Reinforcement Learning, Embodied AI, Autonomous Driving, and Multimodal Perception. It systematically compiles relevant research papers, open-source frameworks, benchmarks, and cutting-edge practices. This repository is dedicated to organizing and presenting the rapidly evolving landscape of World Model research, connecting multiple fields such as Deep Learning, Generative Models (especially Video Generation), Control Theory, Computer Vision, and Cognitive Science.


---

## 🎯 Goal of Repository
Our mission is to establish a centralized, continuously evolving knowledge base that serves as a valuable reference for researchers and practitioners, ultimately accelerating the development of intelligent systems capable of long-term memory retention, sustained reasoning, and adaptive evolution over time.

---

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

## 🔔 Recent hot research and news
+ 2026-4-4 – 🎉 Initial Repo

---

🗺️ Table of Contents
- [Introduction](#-introduction)
- [Goal of Repository](#-goal-of-repository)
- [Project Scope](#-project-scope)
- [Recent hot research and news](#-Recent-hot-research-and-news)
- [Core Concepts](#-core-concepts)
- [Paper List](#-paper-list)
  - [Survey](#Survey)
  - [Framework & Methods](#Framework-Methods)
  - [Benchmark & Datasets](#Benchmark-Datasets)
  - [System & model](#System-model)
- [Resource](#-resource)
  - [Benchmarks and tasks](#Benchmarks-and-tasks)
  - [Systems and open sources](#Systems-and-open-sources)
  - [Multi-media resource](#Multi-media-resource)
- [Make a Contribution](#-Make-a-Contribution)
- [Star Trends](#-star-trends)

---

## 🧠 Core Concepts

- LLM Memory: A fusion of implicit knowledge encoded within parameters (acquired during training) and explicit storage outside parameters (retrieved at runtime), enabling models to transcend token limitations and possess human-like abilities to "remember the past, understand the present, and predict the future."

- Memory System: The complete technical stack implementing memory functionality for large language models, comprising four core components:
  - Memory Storage Layer: Vector databases (e.g., Chroma, Weaviate), graph databases, or hybrid storage solutions
  - Memory Processing Layer: Embedding models, summarization generators, and memory segmenters
  - Memory Retrieval Layer: Multi-stage retrievers, reranking modules, and context injectors
  - Memory Control Layer: Memory prioritization managers, forgetting controllers, and consistency coordinators

- Memory Operations: Atomic memory operations executed through tool calling in memory systems:
  - Writing: Converting dialogue content into vectors for storage, often combined with summarization to reduce noise
  - Retrieval: Generating queries based on current context to obtain Top-K relevant memories
  - Updating: Finding relevant memories via vector similarity and replacing or enhancing them
  - Deletion: Removing specific memories based on user instructions or automatic policies (e.g., privacy expiration)
  - Compression: Merging multiple related memories into summaries to free storage space

- Memory Management: The methodology for managing memories within memory systems, including:
  - Memory Lifecycle: End-to-end management from creation, active usage, infrequent access, to archiving/deletion
  - Conflict Resolution: Arbitration mechanisms for contradictory information (e.g., timestamp priority, source credibility weighting)
  - Resource Budgeting: Allocating memory quotas to different users/tasks to prevent resource abuse
  - Security Governance: Automatic detection and de-identification of PII (Personally Identifiable Information)

- Memory Classification: A multi-dimensional classification system unique to memory systems:
  - By Access Frequency: Working memory (current tasks), frequent memory (personal preferences), archived memory (historical records)
  - By Structured Degree: Structured memory (database records), semi-structured memory (dialogue summaries), unstructured memory (raw conversations)
  - By Sharing Scope: Personal memory (single user), team memory (collaborative spaces), public memory (shared knowledge bases)
  - By Temporal Validity: Permanent memory (core facts), temporary memory (conversation context), time-sensitive memory (e.g., "user is in a bad mood today")

- Memory Mechanisms: Core technical components enabling memory system functionality:
  - Retrieval-Augmented Generation (RAG): Enhancing generation by retrieving relevant information from knowledge bases
  - Memory Reflection Loop: Models periodically "review" conversation history to generate high-level summaries
  - Memory Routing: Automatically selecting retrieval sources based on query type (personal memory/public knowledge base)

- Explicit Memory: Memory stored as raw text outside the model, implemented through vector databases with hybrid indexing strategies:
  - Dense Vector Indexing: Handling semantic similarity queries
  - Sparse Keyword Indexing: Processing exact match queries
  - Multi-vector Indexing: Segmenting long documents into multiple parts, each independently indexed

- Parametric Memory: Knowledge and capabilities stored within the fixed weights of a language model's architecture, characterized by:
  - Serving as the model's core long-term semantic memory carrier
  - Being activatable without external retrieval or explicit contextual support
  - Providing the foundational capability for zero-shot reasoning, general responses, and language generation

- Long-Term Memory: Key information designed for persistent storage, typically implemented as external knowledge bases with capabilities including:
  - Automatic Summarization: Distilling multi-turn dialogues into structured memory
  - Context Binding: Recording memory context to prevent erroneous generalization
  - Multimodal Storage: Simultaneously preserving text, images, audio, and other multimodal memories

- Short-Term Memory: Active information within the LLM's context window, constrained by attention mechanisms. Key techniques include:
  - KV Cache Management: Reusing key-value caches to reduce redundant computation
  - Context Compression: Using summaries instead of detailed history (e.g., "the previous 5 dialogue rounds discussed project budget")
  - Sliding Window Attention: Focusing only on the most recent N tokens while preserving special markers
  - Memory Summary Injection: Dynamically inserting summaries of long-term memory into short-term context

- Episodic Memory: Memory type recording specific user interaction history, fundamental to personalized AI:
  - User Identity Recognition: Identifying the same user across sessions
  - Interaction Trajectory Recording: Preserving user decision paths and feedback
  - Emotional State Tracking: Recording patterns of user mood changes
  - Preference Evolution Modeling: Capturing long-term changes in user interests

- Memory Forgetting: Deliberately designed forgetting mechanisms in large models, including:
  - Selective Forgetting (Machine Unlearning): Removing the influence of specific information from training data, such as covering specific knowledge with forgetting layers
  - Privacy-Driven Forgetting: Automatically identifying and deleting PII information, or setting automatic expiration
  - Memory Decay: Automatically lowering the priority of infrequently accessed memories based on usage frequency
  - Conflict-Driven Forgetting: Strategically updating or discarding old memories when new evidence conflicts with them

- Memory Retrieval: The complex process of precisely locating relevant information from massive memory repositories:
  - Semantic Pre-filtering: Vector similarity matching to obtain Top-100 candidates
  - Contextual Reranking: Reordering results based on current query context
  - Temporal Filtering: Prioritizing the most recent relevant information

- Memory Compression: A collection of techniques maximizing memory utility under limited resources:
  - Content-level Compression: Extracting core information while discarding redundant details
  - Representation-level Compression: Vector quantization (e.g., PQ coding), dimensionality reduction
  - Organization-level Compression: Clustering similar memories, building hierarchical memory structures
  - Knowledge Distillation: Transferring key patterns from external memory into parametric memory

---

## 📚 Paper List
Papers below are ordered by **publication date**:

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
        <td style="width: 55%;"><strong>Beyond the Context Window: A Cost-Performance Analysis of Fact-Based Memory vs. Long-Context LLMs for Persistent Agents</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Long%20Context-blue" alt="Long Context">
            <img src="https://img.shields.io/badge/Cost%20Analysis-brightgreen" alt="Cost Analysis">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.04814">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
  </table>
</details>





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
        <td style="width: 55%;"><strong>Governing Evolving Memory in LLM Agents: Risks, Mechanisms, and the Stability and Safety Governed Memory (SSGM) Framework</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/safety-red" alt="safety">
          <img src="https://img.shields.io/badge/Evolution-brightgreen" alt="Evolution">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.11768v1">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
  </table>
</details>








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
        <td style="width: 55%;"><strong>Towards Realistic Personalization: Evaluating Long-Horizon Preference Following in Personalized User-LLM Interactions</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Personalized-yellow" alt="Personalized">
            <img src="https://img.shields.io/badge/Interaction-blue" alt="Interaction">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.04191">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
  </table>
</details>





<details>
  <summary><strong>Systems & Models</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>Date</strong></td>
      <td><strong>Paper & Summary</strong></td>
      <td><strong>Tags</strong></td>
      <td><strong>Links</strong></td>
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
    <!-- <tr>
      <td rowspan="2" style="width: 15%;">2024-09-21</td>
      <td style="width: 55%;"><strong>Memory3: Language modeling with explict memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Base%20Model-darkred" alt="Base Model">
      <img src="https://img.shields.io/badge/Explicit%20Memory-darkgreen" alt="Explicit Memory">
      <img src="https://img.shields.io/badge/Memory%20Circuit-slateblue" alt="Memory Circuit">
      <img src="https://img.shields.io/badge/Long--Context%20Models-royalblue" alt="Long-Context Models">
      </td>
      <td style="width: 15%;"><a href="https://doi.org/10.4208/jml.240708">
      <img src="https://img.shields.io/badge/Journal%20of%20ML-Paper-black?labelColor=blueviolet" alt="Journal of ML Paper">
      </a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Memory3 is a novel large language model that introduces explicit memory to reduce training and inference costs.<br>
        • The study proposes a memory circuit theory that describes the process of memory externalization, clarifies the definition of knowledge, and highlights the model’s advantages in handling long contexts.<br>
        • Memory3 effectively manages the costs of knowledge writing and reading, and employs compression techniques to significantly reduce the storage requirements of explicit memory.
      </td>
    </tr> -->

  </table>

</details>

## 🧰 Resources

### 📊 Benchmarks and Tasks

|     Task Type      | Benchmarks \& Datasets                                                  |
| :-----------------------: | ------------------------------------------------------------ |
| **Personalized Task Evaluation**  | [IMPLEXCONV](https://aclanthology.org/2025.emnlp-main.580.pdf), [PERSONAMEM](https://arxiv.org/pdf/2504.14225), [PERSONAMEM-v2](https://www.arxiv.org/pdf/2512.06688), [PersonaBench](https://aclanthology.org/2025.findings-acl.49.pdf), [PersonaFeedback](https://arxiv.org/pdf/2506.12915), [LaMP](https://aclanthology.org/2024.acl-long.399.pdf), [MemDaily](https://arxiv.org/pdf/2409.20163), [MPR](https://arxiv.org/pdf/2508.13250), [KnowMe-Bench](https://arxiv.org/abs/2601.04745)  |


### 💻 Systems and Open Sources
Systems below are ordered by **publication date**:

| System      | Time       | Stars | GitHub & Website |
|-------------|------------|-------|------------------|
| Zep         | 2023-05-19 | ![GitHub Repo stars](https://img.shields.io/github/stars/getzep/zep?style=social) | https://github.com/getzep/zep<br>https://www.getzep.com/ |

### 🎥 Multi-media resource

<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>Website Link</th>
      <th>Video Introduction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="1"><strong>Basic Theory of Memory</strong></td>
      <td>https://www.youtube.com/watch?v=k3FUWWEwgfc</td>
      <td>Short-Term Memory with LangGraph</td>
    </tr>
    <tr>
      <td rowspan="1"><strong>Memory-Related Tools</strong></td>
      <td>https://www.bilibili.com/video/BV1hom8YAEhX</td>
      <td>LLMs as Operating Systems: Agent Memory</td>
    </tr>
    <tr>
      <td rowspan="1"><strong>Memory-Related Papers</strong></td>
      <td>https://www.bilibili.com/video/BV1XT8ez6E46</td>
      <td>AI agent Survey Memory</td>
    </tr>
  </tbody>
</table>


## 🤝  Make a Contribution
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

## 💬 Community & Support

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

## 🌟 Star Trends

<a href="https://www.star-history.com/#IAAR-Shanghai/Awesome-AI-Memory&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=IAAR-Shanghai/Awesome-AI-Memory&type=date&legend=top-left" />
 </picture>
</a>

