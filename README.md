# hncu-open-assets: 湖南城市学院开放数字资产库

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Format: glTF 2.0](https://img.shields.io/badge/3D_Format-glTF_2.0-blue.svg)](https://www.khronos.org/gltf/)
[![Format: GeoJSON/JSON](https://img.shields.io/badge/Dataset-JSON%2FMarkdown-green.svg)](https://json.org/)

`hncu-open-assets` 是面向**湖南城市学院（HNCU）**校园开发者、数字孪生研究人员及开源社区的**跨平台通用数字化校园资产库**。

本项目彻底摒弃了特定客户端框架（如 Qt/QML/Android）的私有格式绑定，全量采用**工业级开放标准（glTF 2.0 / GLB、JSON、Markdown、矢量/高清位图、TTF）**进行分类重构与规范化整理，旨在为全校开发者在 **Web 前端三维可视化、Unity/UE/Godot 游戏与虚拟仿真、移动端/小程序、大模型 RAG 校园知识库** 等开发场景中提供一站式、开箱即用的标准素材底座。

---

## 📂 资产全景架构 (Repository Layout)

```text
hncu-open-assets/
├── models/                        # 【3D 空间与建筑资产】(开放标准 glTF 2.0 / GLB)
│   ├── campus/                    # 校园全景大场景
│   │   ├── school.glb             # 湖南城市学院全景 3D 模型 (含建筑物、道路、东阳湖水系)
│   │   ├── buildings_index.json   # 55 栋建筑物中英文名称、分类与 Mesh ID 索引表
│   │   └── buildings_index.md     # 易读版建筑清单文档
│   ├── interior/                  # 室内空间与构件
│   │   └── dormitory.glb          # 学生标准公寓室内 3D 模型 (上床下桌家具布局)
│   └── compatibility/             # (可选) 引擎预编译网格归档
│       └── qt_quick3d_meshes/     # 针对 Qt 6 Quick 3D 渲染管线优化的 .mesh 资产
│
├── datasets/                      # 【校园数据与知识资产】(通用 JSON / Markdown，开箱支持 AI RAG)
│   ├── faq/                       # 校园生活高频常见问题与官方权威解答
│   │   ├── campus_faq.json        # 结构化问答对 (可直接用于智能客服与知识库检索)
│   │   └── campus_faq.md          # Markdown 问答速查表
│   ├── regulations/               # 官方在校规章制度与办事指引 Markdown 全集
│   │   ├── 湖南城市学院学生管理规定.md
│   │   ├── 信电院综合测评与综合素质评价细则(2025试行).md
│   │   ├── 新生报到流程指引.md
│   │   ├── 新生入校常见事项须知.md
│   │   ├── 学生医保与意外险报账流程.md
│   │   ├── 学生银行卡号信息完善指南.md
│   │   └── 校卫生所门诊就医与医保报销提示.md
│   └── knowledge/                 # 校园知识图谱与结构化综合数据
│       └── hncu_knowledge.json    # 4MB 全校综合实体知识库
│
├── branding/                      # 【品牌视觉与多媒体素材】
│   ├── logos/                     # 官方校徽高清透明底
│   │   └── hncu_logo.png
│   ├── photos/                    # 校园实景摄影与横幅背景
│   │   └── campus_scenery.jpg
│   └── ui/                        # 校园通用人像/形象卡片背景
│       └── avatar_background.png
│
├── typography/                    # 【字体与排版资产】
│   ├── fonts/
│   │   └── 方正北魏楷书简体.ttf   # 经典北魏楷书字库 (适用于大标题、证书及抬头)
│   └── README.md                  # WebFont 转换与前端使用指引
│
└── examples/                      # 【跨技术栈通用开箱即用示例】
    ├── web_threejs/               # Web 纯原生 Three.js 3D 校园全景浏览交互页面
    │   ├── index.html             # 双击即开的浏览器 3D 交互页面
    │   └── README.md
    └── python_knowledge/          # Python 3 行代码加载校园知识库检索演示
        ├── search_faq.py
        └── README.md
```

---

## 🏛️ 核心资产详细介绍

### 1. 3D 校园空间模型 (`models/`)
* **格式规范**：Khronos 官方推荐的通用开放二进制格式 **glTF 2.0 (`.glb`)**。
* **兼容平台**：
  * **Web**：Three.js、Babylon.js、Cesium、Google `<model-viewer>`。
  * **游戏/仿真引擎**：Unity 3D、Unreal Engine 5、Godot Engine、Blender。
  * **原生系统**：Windows 3D 查看器、macOS QuickLook。
* **主要场景**：
  * `school.glb`：基于 OpenStreetMap 真实地理空间高程构建的城院主校区模型，包含 57 个 Mesh 与 65 个 Node，完整覆盖**逸夫图书馆、1-3号教学楼、一/二工训楼、电信楼、土木楼、管理楼、音乐厅、主体育场、东阳湖水系与 1~26 栋学生公寓群**。
  * `buildings_index.json`：清晰整理了全校 55 栋核心建筑与公共设施的 ID、中英文名称及功能属性分类（行政、教学、住宿、生活、基础设施），极大方便了 3D 室内外联动、地标打点（POI）与路径导航开发。

---

### 2. 校园生活知识与规章数据集 (`datasets/`)
* **高频问答 (`campus_faq.json`)**：
  * 涵盖一卡通补卡（服务大厅窗口与夏冬作息）、宿舍门禁（23:30）、四人寝宿舍楼栋（18-26栋）、奖助学金、学分规定、旷课处分等级、转专业要求等官方标准问答对。
* **制度规章 (`regulations/`)**：
  * Markdown 纯文本轻量存储，结构化小节清晰，便于直接导入向量数据库（Chroma / Milvus / FAISS）作为学校智能问答 Agent 的知识库底层语料。

---

### 3. 视觉与字体资产 (`branding/` & `typography/`)
* 包含了标准分辨率的透明底校徽矢量/PNG、校园实景大图，以及经典的北魏楷书字库。

---

## 💻 快速开箱即用指南 (Quick Start)

### 场景 A：在 Web 网页中渲染 3D 校园 (Three.js)

无需任何复杂依赖，前端加载 `school.glb` 仅需几行核心代码：

```javascript
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';

const scene = new THREE.Scene();
const loader = new GLTFLoader();

// 异步加载湖南城市学院全景模型
loader.load('models/campus/school.glb', (gltf) => {
  scene.add(gltf.scene);
  console.log("湖南城市学院 3D 校园全景模型加载成功！");
});
```
> 💡 完整可交互的 360° 漫游演示页面见 [`examples/web_threejs/index.html`](examples/web_threejs/index.html)。

---

### 场景 B：在 Python / AI Agent 中使用校园知识库

```python
import json

# 1. 加载校园生活高频常见问答
with open('datasets/faq/campus_faq.json', 'r', encoding='utf-8') as f:
    faq_data = json.load(f)

# 2. 快速匹配问答
user_query = "饭卡掉了"
for item in faq_data['items']:
    if user_query in item['question']:
        print(f"Q: {item['question']}\nA: {item['answer']}")
```
> 💡 完整示例脚本见 [`examples/python_knowledge/search_faq.py`](examples/python_knowledge/search_faq.py)。

---

### 场景 C：在 Unity 游戏引擎中使用

1. 将 `models/campus/school.glb` 直接拖入 Unity 工程的 `Assets/Models/` 目录下；
2. 安装 Unity 官方扩展包 `glTFast` 或直接提取材质；
3. 将 Prefab 拖入 Scene 视口，添加网格碰撞体（Mesh Collider）即可实现第一人称校园漫游。

---

## 🤝 开源协议与贡献指南 (License & Contributing)

1. **代码与通用格式资产**：基于 [MIT License](LICENSE) 许可协议开放给广大开发者免费使用。
2. **知识产权与校名标识说明**：
   - 湖南城市学院校徽、校名文字等品牌标识所有权归属于**湖南城市学院**官方所有，仅供学术科研、校园开发与非营利性公益展示使用；
   - 商业用途请联系学校官方有关部门授权。
3. **欢迎贡献**：
   - 欢迎广大城院校友与在校师生提交 Pull Request 补充更高精度的建筑模型、精美贴图、校园全景摄影或最新政策问答！
