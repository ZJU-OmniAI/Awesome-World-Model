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
|  **Comprehensive Evaluation**   | [MemoryAgentBench](https://arxiv.org/pdf/2507.05257), [LifelongAgentBench](https://arxiv.org/pdf/2505.11942), [StreamBench](https://arxiv.org/pdf/2406.08747) |
|  **Memory Mechanism Evaluation**   | [MemBench](https://aclanthology.org/2025.findings-acl.989.pdf),  [Minerva](https://arxiv.org/pdf/2502.03358), [MemoryBench](https://arxiv.org/pdf/2510.17281) |
|  **Long-Term Memory Evaluation**   | [LOCCO](https://aclanthology.org/2025.findings-acl.1014.pdf), [LONGMEMEVAL](https://arxiv.org/pdf/2410.10813), [LOCOMO](https://aclanthology.org/2024.acl-long.747.pdf), [MADial-Bench](https://arxiv.org/abs/2409.15240), [StoryBench](https://arxiv.org/pdf/2506.13356), [DialSim](https://arxiv.org/pdf/2406.13144), [Mem-Gallery](https://arxiv.org/pdf/2601.03515), [RealMem](https://arxiv.org/pdf/2601.06966), [CloneMem](https://arxiv.org/pdf/2601.07023) |
|  **Long-Dialogue Reasoning**   | [PREFEVAL](https://arxiv.org/pdf/2502.09597),  [MiniLongBench](https://aclanthology.org/2025.acl-long.560.pdf)|
|  **Long-Context Understanding**   | [LongBench V2](https://arxiv.org/pdf/2412.15204), [LongBench](https://arxiv.org/abs/2308.14508), [BABILong](https://arxiv.org/pdf/2406.10149), [HotpotQA](https://aclanthology.org/D18-1259.pdf) |
|  **Long-Context Evaluation** |[SCBENCH](https://arxiv.org/abs/2412.10319), [L-CiteEval](https://arxiv.org/pdf/2410.02115), [GLE](https://aclanthology.org/2024.acl-long.859/), [HOMER](https://arxiv.org/pdf/2404.10308), [RULER](https://arxiv.org/pdf/2404.06654), [MM-Needle](https://aclanthology.org/2025.naacl-long.166.pdf) |
|  **Long-Form Text Generation**   | [LongGenBench](https://arxiv.org/pdf/2409.02076) |
|  **Episodic Memory Evaluation**   | [PerLTQA](https://aclanthology.org/2024.sighan-1.18.pdf)|
|  **Memory Hallucination Evaluation**   | [HaluMem](https://arxiv.org/pdf/2511.03506) |
|  **Web Interaction & Navigation** | [WebChoreArena](https://arxiv.org/pdf/2506.01952), [MT-Mind2Web](https://arxiv.org/pdf/2402.15057), [WebShop](https://arxiv.org/pdf/2207.01206), [WebArena](https://arxiv.org/pdf/2307.13854) |


### 💻 Systems and Open Sources
Systems below are ordered by **publication date**:

| System      | Time       | Stars | GitHub & Website |
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
| SuperLocalMemory | 2026-03-01 | ![GitHub Repo stars](https://img.shields.io/github/stars/qualixar/superlocalmemory?style=social) | https://github.com/qualixar/superlocalmemory<br>https://superlocalmemory.com/ |
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
      <td rowspan="6"><strong>Basic Theory of Memory</strong></td>
      <td>https://www.youtube.com/watch?v=k3FUWWEwgfc</td>
      <td>Short-Term Memory with LangGraph</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=WsGVXiWzTpI</td>
      <td>OpenAI: Agent Memory Patterns
</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=fsENEq4F55Q</td>
      <td>Long-Term Memory with LangGraph</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=L-au0tvDJbI</td>
      <td>LLMs Do Not Have Human-Like Working Memories</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=RkWor1BZOn0</td>
      <td> long-term memory and personalization for LLM applications</td>
    </tr>
    <tr>
      <td>https://www.youtube.com/watch?v=CFih0_6tn2w</td>
      <td>A Paradigm Shift to Memory as a First Class Citizen for LLMs</td>
    </tr>
    <tr>
      <td rowspan="4"><strong>Memory-Related Tools</strong></td>
      <td>https://www.bilibili.com/video/BV1hom8YAEhX</td>
      <td>LLMs as Operating Systems: Agent Memory</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1CU421o7DL</td>
      <td>Langchain Agent with memory</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1arJazVEaX</td>
      <td>Open Memory MCP</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV11HxXzuExk</td>
      <td> Agentic Memory for LLM Agents</td>
    </tr>
    <tr>
      <td rowspan="10"><strong>Memory-Related Papers</strong></td>
      <td>https://www.bilibili.com/video/BV1XT8ez6E46</td>
      <td>AI agent Survey Memory</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1f12wBpEXX</td>
      <td>MemGen: Weaving Generative Latent Memory for Self-Evolving Agents</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1deyFBKEFh</td>
      <td>MLP Memory: A Retriever-Pretrained Memory for Large Language Models</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV18FnVzpE6S</td>
      <td>How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1mpbrzSEH9</td>
      <td>Agent Workflow Memory</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1qEtozyEoh</td>
      <td>Introduction to the Memory Mechanism of Large Language Model Agents</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1FGrhYhEZK</td>
      <td>Memory Layers at Scale</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1aQ1xBkE45</td>
      <td>Agentic Memory for LLM Agents</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV1Yz421f7uH</td>
      <td>Evaluating Very Long-Term Conversational Memory of LLM Agents</td>
    </tr>
    <tr>
      <td>https://www.bilibili.com/video/BV19RWdzxEsR</td>
      <td>Lightweight plug-in memory system</td>
    </tr>
  </tbody>
</table>

### 🧠 Adam Framework

- **Description:** 5-layer persistent memory and coherence architecture for local AI assistants built on OpenClaw. Solves AI amnesia (cross-session) and within-session coherence degradation.
- **Layers:** Vault injection, mid-session memory search, neural graph (7219+ neurons), nightly Gemini reconciliation, coherence monitor with scratchpad dropout detection.
- **Validated:** 353 sessions, 6619 message turns, 8 months production use on a live business by a non-developer.
- **Platform:** Windows/macOS/Linux, OpenClaw, local-first, model-agnostic.
- **Links:** [GitHub](https://github.com/strangeadvancedmarketing/Adam) | [Live Demo](https://strangeadvancedmarketing.github.io/Adam/) | [Interactive Proof](https://strangeadvancedmarketing.github.io/Adam/showcase/ai-amnesia-solved.html)

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

