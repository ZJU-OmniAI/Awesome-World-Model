# 论文索引

[世界模型](../README_cn.md) · [World Action Models](02-world-action-models.md) · [问题分类](03-problem-taxonomy.md)

- [基础研究](#foundations)
- [综述](#surveys)
- [视觉规划与动作解码](#wam-visual-planning)
- [几何与运动接口](#wam-geometry-motion)
- [预测表征与动作决策](#wam-representation)
- [世界与动作联合建模](#wam-joint)
- [价值、评价与决策反馈](#wam-feedback)
- [触觉与接触建模](#wam-tactile)
- [高效世界动作建模](#wam-efficiency)
- [状态、记忆与多阶段规划](#problem-memory)
- [动作与物理正确性](#problem-physics)
- [评测基准](#benchmarks)

<a id="foundations"></a>
## 基础研究

| 日期 | 论文 | 简介 |
|---|---|---|
| 2018-03-27 | <a id="paper-1803.10122"></a>**World Models** · [World Models](https://arxiv.org/abs/1803.10122) | 将视觉压缩、时序动态与控制结合，并研究在模型想象中学习策略。 |
| 2019-12-03 | <a id="paper-1912.01603"></a>**Dreamer** · [Dream to Control: Learning Behaviors by Latent Imagination](https://arxiv.org/abs/1912.01603) | 通过 latent 想象轨迹训练行为与价值模型。 |
| 2023-01-10 | <a id="paper-2301.04104"></a>**DreamerV3** · [Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104) | 用统一配置在多类任务中学习世界模型和控制策略。 |
| 2023-01-19 | <a id="paper-2301.08243"></a>**I-JEPA** · [Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2301.08243) | 通过预测图像区域的表征学习视觉特征。 |
| 2023-04-07 | <a id="paper-2304.03442"></a>**Generative Agents** · [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) | 用记忆、反思和规划构建交互式社会行为模拟。 |
| 2024-08-27 | <a id="paper-2408.14837"></a>**GameNGen** · [Diffusion Models Are Real-Time Game Engines](https://arxiv.org/abs/2408.14837) | 以动作条件视频生成模拟 DOOM 游戏的交互状态变化。 |
| 2024-11-10 | <a id="paper-2411.06559"></a>**WebDreamer** · [Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents](https://arxiv.org/abs/2411.06559) | 用语言模型模拟网页动作后果，支持网页智能体规划。 |
| 2025-06-11 | <a id="paper-2506.09985"></a>**V-JEPA 2** · [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) | 结合视频自监督与机器人交互数据，研究表征预测及规划。 |

<a id="surveys"></a>
## 综述

| 日期 | 论文 | 简介 |
|---|---|---|
| 2026-05-12 | <a id="paper-2605.12090"></a>**World Action Models survey** · [World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090) | 以世界预测与动作生成的结合梳理 WAM 研究路线。 |

<a id="wam-visual-planning"></a>
## 视觉规划与动作解码

| 日期 | 论文 | 简介 |
|---|---|---|
| 2023-01-31 | <a id="paper-2302.00111"></a>**UniPi** · [Learning Universal Policies via Text-Guided Video Generation](https://arxiv.org/abs/2302.00111) | 文本条件视频规划，再由逆动力学模型提取动作。 |
| 2023-10-16 | <a id="paper-2310.10625"></a>**Video Language Planning** · [Video Language Planning](https://arxiv.org/abs/2310.10625) | 以语言和视频展开树搜索，用价值判断选择视觉计划并交给控制策略。 |
| 2025-06-27 | <a id="paper-2506.22007"></a>**RoboEnvision** · [RoboEnvision: A Long-Horizon Video Generation Model for Multi-Task Robot Manipulation](https://arxiv.org/abs/2506.22007) | 以任务分解和关键帧生成连接长程视觉计划与执行。 |
| 2026-02-11 | <a id="paper-2602.10717"></a>**Say, Dream, and Act** · [Say, Dream, and Act: Learning Video World Models for Instruction-Driven Robot Manipulation](https://arxiv.org/abs/2602.10717) | 预测未来视频为动作模型提供上下文，并结合真实观测滚动控制。 |
| 2026-04-06 | <a id="paper-2604.04502"></a>**Veo-Act** · [Veo-Act: Enhancing VLA Policies with Frontier Video Models](https://arxiv.org/abs/2604.04502) | 用视频模型提供视觉计划，配合 VLA 执行机器人控制。 |
| 2026-07-21 | <a id="paper-2607.19343"></a>**MVA** · [Masked Visual Actions for Unified World Modeling](https://arxiv.org/abs/2607.19343) | 用部分可见的机器人或物体运动掩码统一前向预测与逆向推断。 |

<a id="wam-geometry-motion"></a>
## 几何与运动接口

| 日期 | 论文 | 简介 |
|---|---|---|
| 2023-10-12 | <a id="paper-2310.08576"></a>**AVDC** · [Learning to Act from Actionless Videos through Dense Correspondences](https://arxiv.org/abs/2310.08576) | 通过未来视频的稠密对应和深度估计几何控制量。 |
| 2024-07-21 | <a id="paper-2407.15208"></a>**Im2Flow2Act** · [Flow as the Cross-Domain Manipulation Interface](https://arxiv.org/abs/2407.15208) | 以对象 flow 连接人类视频和机器人策略；最终动作由学习式策略输出。 |
| 2025-06-06 | <a id="paper-2506.06199"></a>**3DFlowAction** · [3DFlowAction: Learning Cross-Embodiment Manipulation from 3D Flow World Model](https://arxiv.org/abs/2506.06199) | 预测物体三维运动，并结合抓取与轨迹优化转成机器人动作。 |
| 2025-12-31 | <a id="paper-2512.24766"></a>**Dream2Flow** · [Dream2Flow: Bridging Video Generation and Open-World Manipulation with 3D Object Flow](https://arxiv.org/abs/2512.24766) | 将生成视频恢复为三维对象流，以对象轨迹跟踪连接控制。 |
| 2026-05-17 | <a id="paper-2605.17522"></a>**RoboFlow4D** · [RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation](https://arxiv.org/abs/2605.17522) | 直接预测多帧三维 flow，为动作生成提供运动规划。 |
| 2026-06-12 | <a id="paper-2606.14048"></a>**WAM4D** · [WAM4D: Fast 4D World Action Model via Spatial Register Tokens](https://arxiv.org/abs/2606.14048) | 训练期用空间寄存 token 读取未来深度，推理期移除几何分支。 |
| 2026-06-15 | <a id="paper-2606.17046"></a>**Geometric Action Model** · [Geometric Action Model for Robot Policy Learning](https://arxiv.org/abs/2606.17046) | 将几何基础模型接入未来 latent 预测与动作解码。 |
| 2026-07-07 | <a id="paper-2607.06559"></a>**RynnWorld-4D** · [RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation](https://arxiv.org/abs/2607.06559) | 联合建模 RGB、深度和光流，再将内部四维动态表征用于策略。 |
| 2026-07-14 | <a id="paper-2607.13017"></a>**FlowWAM** · [FlowWAM: Optical Flow as a Unified Action Representation for World Action Models](https://arxiv.org/abs/2607.13017) | 将光流作为视频兼容的动作表征，连接策略与动作条件模拟。 |

<a id="wam-representation"></a>
## 预测表征与动作决策

| 日期 | 论文 | 简介 |
|---|---|---|
| 2024-06-19 | <a id="paper-2406.13301"></a>**ARDuP** · [ARDuP: Active Region Video Diffusion for Universal Policies](https://arxiv.org/abs/2406.13301) | 用活动区域约束视频 latent 预测，再在 latent 空间解码动作。 |
| 2024-12-19 | <a id="paper-2412.14803"></a>**VPP** · [Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations](https://arxiv.org/abs/2412.14803) | 提取视频模型的预测性中间特征，作为独立动作模型的条件。 |
| 2025-05-21 | <a id="paper-2505.15659"></a>**FLARE** · [FLARE: Robot Learning with Implicit World Modeling](https://arxiv.org/abs/2505.15659) | 用未来 latent 表征对齐增强动作策略，无需以 RGB 视频作为控制接口。 |
| 2025-12-17 | <a id="paper-2512.15692"></a>**mimic-video** · [mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs](https://arxiv.org/abs/2512.15692) | 使用视频动态表征支持连续机器人控制。 |
| 2026-04-30 | <a id="paper-2605.00078"></a>**Being-H0.7** · [Being-H0.7: A Latent World-Action Model from Egocentric Videos](https://arxiv.org/abs/2605.00078) | 对齐当前条件先验与训练期未来后验，推理只用当前上下文。 |
| 2026-05-07 | <a id="paper-2605.06481"></a>**OA-WAM** · [OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation](https://arxiv.org/abs/2605.06481) | 区分对象地址与动态内容，使动作解码能定位特定对象。 |
| 2026-06-02 | <a id="paper-2606.03188"></a>**GeoSem-WAM** · [GeoSem-WAM: Geometry- and Semantic-Aware World Action Models](https://arxiv.org/abs/2606.03188) | 增加未来几何和语义监督，部署时省去显式未来 rollout。 |
| 2026-06-10 | <a id="paper-2606.12217"></a>**AGRA** · [Making Foresight Actionable: Repurposing Representation Alignment in World Action Models](https://arxiv.org/abs/2606.12217) | 对齐世界模型与动作解码器的表征，使动作模型更关注任务相关区域。 |
| 2026-06-11 | <a id="paper-2606.13674"></a>**RepWAM** · [RepWAM: World Action Modeling with Representation Visual-Action Tokenizers](https://arxiv.org/abs/2606.13674) | 学习语义视觉动作 tokenizer，联合预测未来状态和 latent 动作。 |
| 2026-06-14 | <a id="paper-2606.15768"></a>**LaWAM** · [LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies](https://arxiv.org/abs/2606.15768) | 预测紧凑的潜空间视觉子目标，再据此生成动作。 |
| 2026-06-17 | <a id="paper-2606.19531"></a>**ImageWAM** · [ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?](https://arxiv.org/abs/2606.19531) | 用图像编辑去噪的 KV 特征连接目标变化与动作专家。 |
| 2026-07-02 | <a id="paper-2607.02195"></a>**Bridge-WA** · [Bridge-WA: Learning Action-Relevant World Dynamics for Robotic Manipulation](https://arxiv.org/abs/2607.02195) | 向动作模型注入未来状态、空间变化和局部运动等互补信息。 |
| 2026-08-02 | <a id="paper-2608.01397"></a>**SG-WAM** · [SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space](https://arxiv.org/abs/2608.01397) | 在几何感知的策略表征空间预测动作条件动态。 |

<a id="wam-joint"></a>
## 世界与动作联合建模

| 日期 | 论文 | 简介 |
|---|---|---|
| 2025-04-03 | <a id="paper-2504.02792"></a>**UWM** · [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](https://arxiv.org/abs/2504.02792) | 以不同视频和动作噪声时间步统一策略、视频预测及正逆动力学。 |
| 2025-06-26 | <a id="paper-2506.21539"></a>**WorldVLA** · [WorldVLA: Towards Autoregressive Action World Model](https://arxiv.org/abs/2506.21539) | 在统一自回归模型中结合动作生成与未来图像预测。 |
| 2025-11-21 | <a id="paper-2511.17502"></a>**RynnVLA-002** · [RynnVLA-002: A Unified Vision-Language-Action and World Model](https://arxiv.org/abs/2511.17502) | 共享视觉语言与世界建模能力，同时支持动作生成。 |
| 2025-12-15 | <a id="paper-2512.13030"></a>**Motus** · [Motus: A Unified Latent Action World Model](https://arxiv.org/abs/2512.13030) | 以理解、视频和动作专家及联合调度支持多种世界动作建模模式。 |
| 2026-01-29 | <a id="paper-2601.21998"></a>**LingBot-VA** · [Causal World Modeling for Robot Control](https://arxiv.org/abs/2601.21998) | 以自回归扩散耦合视频与动作专家，并持续引入真实观测反馈。 |
| 2026-02-17 | <a id="paper-2602.15922"></a>**DreamZero** · [World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922) | 联合视频和动作建模，按动作块生成并用真实观测更新闭环状态。 |
| 2026-04-30 | <a id="paper-2604.27792"></a>**MotuBrain** · [Motubrain: An Advanced World Action Model for Robot Control](https://arxiv.org/abs/2604.27792) | 三流 MoT 联合视频与动作，扩展语言、多视角和实时控制接口。 |
| 2026-06-04 | <a id="paper-2606.05979"></a>**WLA-0** · [World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis](https://arxiv.org/abs/2606.05979) | 在自回归主干中耦合语言子任务、未来状态和动作生成。 |
| 2026-07-09 | <a id="paper-2607.08639"></a>**LingBot-VA 2.0** · [Native Video-Action Pretraining for Generalizable Robot Control](https://arxiv.org/abs/2607.08639) | 采用因果结构进行视频动作联合预训练，结合语义 tokenizer、稀疏专家和异步控制。 |
| 2026-08-01 | <a id="paper-2608.00725"></a>**SelfWAM** · [SelfWAM: A Self-Grounded Unified World Action Model for Fast Robot Control](https://arxiv.org/abs/2608.00725) | 联合预测动作、动作条件未来帧与机器人自身掩码。 |

<a id="wam-feedback"></a>
## 价值、评价与决策反馈

| 日期 | 论文 | 简介 |
|---|---|---|
| 2026-01-22 | <a id="paper-2601.16163"></a>**Cosmos Policy** · [Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://arxiv.org/abs/2601.16163) | 将动作、状态及价值编码为视频 latent 帧，用统一视频模型训练控制与规划。 |
| 2026-05-31 | <a id="paper-2606.01027"></a>**τ₀-WM** · [$\tau_0$-WM: A Unified Video-Action World Model for Robotic Manipulation](https://arxiv.org/abs/2606.01027) | 统一视频动作生成、候选动作模拟与任务进度评价。 |
| 2026-06-19 | <a id="paper-2606.21088"></a>**MV-WAM** · [MV-WAM: Manifold-Aware World Action Model with Value Augmentation](https://arxiv.org/abs/2606.21088) | 联合视觉、动作与价值估计，利用进度价值进行偏差检测和恢复。 |

<a id="wam-tactile"></a>
## 触觉与接触建模

| 日期 | 论文 | 简介 |
|---|---|---|
| 2026-06-07 | <a id="paper-2606.08737"></a>**Dream-Tac** · [Dream-Tac: A Unified Tactile World Action Model for Contact-Rich Robot Manipulation](https://arxiv.org/abs/2606.08737) | 通过接触感知融合联合建模视觉、触觉和动作。 |
| 2026-07-26 | <a id="paper-2607.23783"></a>**N₀-TWAM** · [$N_0$-TWAM: Scaling Tactile-Native World-Action Model for Contact-Rich Manipulation](https://arxiv.org/abs/2607.23783) | 结合触觉信息，联合预测视觉、接触状态和动作。 |

<a id="wam-efficiency"></a>
## 高效世界动作建模

| 日期 | 论文 | 简介 |
|---|---|---|
| 2026-03-17 | <a id="paper-2603.16666"></a>**Fast-WAM** · [Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://arxiv.org/abs/2603.16666) | 训练期联合未来与动作预测，推理期使用当前帧世界特征生成动作。 |
| 2026-08-03 | <a id="paper-2608.02365"></a>**Faster-WAM** · [Faster-WAM: Do World Action Models Need Deep Action Modules?](https://arxiv.org/abs/2608.02365) | 保留世界模型能力，用轻量动作模块降低控制推理开销。 |
| 2026-08-04 | <a id="paper-2608.03701"></a>**LiLa-WAM** · [LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation](https://arxiv.org/abs/2608.03701) | 在紧凑 latent 空间进行未来推理，减少世界动作模型训练与推理成本。 |

<a id="problem-memory"></a>
## 状态、记忆与多阶段规划

| 日期 | 论文 | 简介 |
|---|---|---|
| 2025-06-05 | <a id="paper-2506.05284"></a>**Spatial Memory** · [Video World Models with Long-term Spatial Memory](https://arxiv.org/abs/2506.05284) | 以可检索的三维空间记忆与历史帧缓解回访遗忘。 |
| 2025-12-03 | <a id="paper-2512.04040"></a>**RELIC** · [RELIC: Interactive Video World Model with Long-Horizon Memory](https://arxiv.org/abs/2512.04040) | 把历史 latent 与相机信息压缩到 KV，并蒸馏为流式生成模型。 |
| 2026-04-13 | <a id="paper-2604.16484"></a>**DexWorldModel** · [DexWorldModel: Causal Latent World Modeling towards Automated Learning of Embodied Tasks](https://arxiv.org/abs/2604.16484) | 语义 latent、双状态 TTT 记忆和异步推理共同支撑机器人控制。 |
| 2026-06-07 | <a id="paper-2606.08775"></a>**WorldDP** · [Unifying Object-Centric World Models and Diffusion Policy: A Hierarchical Framework for Multi-Stage Robotic Tasks](https://arxiv.org/abs/2606.08775) | 对象中心世界模型规划子目标，低层扩散策略负责执行。 |

<a id="problem-physics"></a>
## 动作与物理正确性

| 日期 | 论文 | 简介 |
|---|---|---|
| 2025-10-11 | <a id="paper-2510.10125"></a>**Ctrl-World** · [Ctrl-World: A Controllable Generative World Model for Robot Manipulation](https://arxiv.org/abs/2510.10125) | 逐帧动作条件、多视角预测及位姿条件记忆支持策略模拟与评价。 |
| 2026-03-18 | <a id="paper-2603.17808"></a>**EVA** · [EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808) | 以逆动力学解码动作构造可执行性奖励，后训练视频世界模型。 |
| 2026-03-24 | <a id="paper-2603.23376"></a>**ABot-PhysWorld** · [ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment](https://arxiv.org/abs/2603.23376) | 物理标注数据与解耦偏好对齐改善物理合理性和动作跟随。 |
| 2026-06-26 | <a id="paper-2606.28128"></a>**PhysisForcing** · [PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation](https://arxiv.org/abs/2606.28128) | 以点轨迹和实体关系监督增强视频世界模型的物理一致性。 |

<a id="benchmarks"></a>
## 评测基准

| 日期 | 论文 | 简介 |
|---|---|---|
| 2024-06-12 | <a id="paper-2406.08407"></a>**MMWorld** · [MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos](https://arxiv.org/abs/2406.08407) | 面向跨学科视频理解与推理的多模态问答基准。 |
| 2024-10-23 | <a id="paper-2410.18072"></a>**WorldSimBench** · [WorldSimBench: Towards Video Generation Models as World Simulators](https://arxiv.org/abs/2410.18072) | 结合感知评价与操作评价，检验视频模拟器的视觉和行动能力。 |
| 2025-01-14 | <a id="paper-2501.09038"></a>**Physics-IQ** · [Do generative video models understand physical principles?](https://arxiv.org/abs/2501.09038) | 用真实物理现象的未来视频测试生成模型的物理预测能力。 |
| 2025-05-14 | <a id="paper-2505.09694"></a>**EWMBench** · [EWMBench: Evaluating Scene, Motion, and Semantic Quality in Embodied World Models](https://arxiv.org/abs/2505.09694) | 分别考察具身视频的场景一致性、运动正确性和语义对齐。 |
