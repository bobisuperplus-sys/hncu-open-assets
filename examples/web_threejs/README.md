# Web 3D 校园全景浏览示例 (Three.js)

本示例演示如何使用纯原生前端技术与 [Three.js](https://threejs.org/) 引擎加载并交互式渲染本项目提供的通用 glTF 2.0 格式校园全景模型（`models/campus/school.glb`）。

---

## 🚀 运行方法

受现代浏览器本地 `file://` 协议对外部二进制模型加载的安全限制（CORS），建议在项目根目录下通过轻量静态服务器运行：

```bash
# 1. 进入 hncu_assets 仓库根目录
cd hncu_assets

# 2. 启动 Python 自带简易 HTTP 服务器
python3 -m http.server 8080

# 3. 在浏览器打开示例页面
# http://localhost:8080/examples/web_threejs/
```

---

## 🎮 控制指南

- **鼠标左键拖拽**：360° 旋转观察视角
- **鼠标右键拖拽**：平移视角画布
- **滚轮滚动**：拉近 / 推远观察整个校园建筑体块
