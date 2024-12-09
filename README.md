# IIIF Viewer Demo

这是一个使用 IIIF（国际图像互操作框架）查看器的演示项目。该项目展示了如何使用 IIIF 标准来展示和注释图像。

## 项目结构

```
docs/
├── images/         # 图像文件
├── index.html      # 主页面
├── manifest-referenced.json    # IIIF manifest 文件
└── annotation1.json    # 图像注释文件
```

## 功能特点

- 支持图像查看和缩放
- 支持多语言（日语和英语）
- 支持图像注释
- 使用 IIIF Presentation API 3.0

## 在线访问

访问以下地址查看演示：
https://oushiei120.github.io/iiif_test/docs/

## 技术细节

- 使用 IIIF Presentation API 3.0
- Manifest URL: `https://oushiei120.github.io/iiif_test/docs/manifest-referenced.json`
- 图像格式：PNG
- 图像尺寸：1850x1298 像素

## 本地开发

1. 克隆仓库：
```bash
git clone https://github.com/oushiei120/iiif_test.git
```

2. 使用本地服务器运行项目，例如：
```bash
python -m http.server
```

3. 在浏览器中访问 `http://localhost:8000/docs/`
