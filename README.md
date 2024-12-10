# IIIF Viewer Demo

这是一个使用 IIIF（国际图像互操作框架）查看器的演示项目。该项目展示了如何使用 IIIF 标准来展示和注释图像。

## 项目结构

```
docs/
├── images/         # 图像文件
├── resources/      # 资源文件
├── index.html      # 主页面
├── manifest-referenced.json    # IIIF manifest 文件（定义图像展示结构）
└── annotation1.json           # 图像注释文件（包含文本注释）
```

## 功能特点

- 支持图像查看和缩放
- 支持多语言显示（日语和英语）
- 支持图像注释和标注
- 完全兼容 IIIF Presentation API 3.0
- 支持分页视图模式（paged behavior）
- 支持文本注释的精确定位（使用 FragmentSelector）

## 在线访问

访问以下地址查看演示：
https://oushiei120.github.io/iiif_test/docs/

## 技术规格

### IIIF 实现细节
- IIIF Presentation API 版本：3.0
- Manifest URL: `https://oushiei120.github.io/iiif_test/docs/manifest-referenced.json`
- 支持的查看器：任何兼容 IIIF 3.0 的查看器

### 图像规格
- 图像格式：PNG
- 基础图像尺寸：1850x1298 像素
- 支持动态缩放和平移

### 注释功能
- 支持多个独立注释
- 使用 FragmentSelector 进行精确定位
- 支持多语言文本注释
- 注释动机（motivation）：commenting

## 本地开发

1. 克隆仓库：
```bash
git clone https://github.com/oushiei120/iiif_test.git
```

2. 启动本地服务器：
```bash
# 使用 Python（推荐）
python -m http.server 8000

# 或使用 Node.js
npx http-server
```

3. 在浏览器中访问：
   - Python: `http://localhost:8000/docs/`
   - Node.js: `http://localhost:8080/docs/`

## 注意事项

- 确保使用支持 HTTPS 的服务器来托管项目
- 所有的 IIIF 资源都应该通过 HTTPS 访问
- 图像和注释的坐标系统使用像素单位
- 建议使用现代浏览器以获得最佳体验

## 相关链接

- [IIIF 规范文档](https://iiif.io/api/presentation/3.0/)
- [IIIF 验证服务](https://iiif.io/api/presentation/validator/service/)
