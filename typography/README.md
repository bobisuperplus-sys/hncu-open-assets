# 字体与排版资产 (Typography & Fonts)

本目录归档了湖南城市学院数字化产品中使用的特色书法字体与排版资产。

---

## 📁 字体清单

| 字体文件 | 格式 | 说明 | 适用场景 |
| :--- | :--- | :--- | :--- |
| `方正北魏楷书简体.ttf` | TrueType (.ttf) | 经典北魏楷书字形，笔力雄健、结构古朴 | 系统大标题、荣誉证书、官方封面抬头、校园文创 |

---

## 🌐 Web 端使用与格式优化建议

为了在 Web 网页或 H5 小程序中实现最佳的加载速度与体积压缩，建议使用 `woff2` 格式或进行字蛛（Font-Spider）字符集子集化裁剪：

```css
@font-face {
  font-family: 'HNCU-BeiWeiKai';
  src: url('./fonts/方正北魏楷书简体.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
  font-display: swap;
}

.school-title {
  font-family: 'HNCU-BeiWeiKai', serif;
}
```
