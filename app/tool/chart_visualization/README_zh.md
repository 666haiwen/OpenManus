# 图表可视化工具

图表可视化工具，通过python生成数据处理代码，最终调用[@visactor/vmind](https://github.com/VisActor/VMind)得到图表的spec结果，图表渲染使用[@visactor/vchart](https://github.com/VisActor/VChart)

## 安装

1. 安装node >= 18

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
# 安装完成后重启终端，然后安装 Node 最新 LTS 版本：
nvm install --lts
```

2. 安装依赖

```bash
cd app/tool/chart_visualization
npm install
```

## 工具参数
```typescript
{
  // 用于生产数据处理的python代码，最终得到csv文件
  code: string;
  // 解析用户意图，得到图表描述
  chart_description: string;
  // 最终产物png或者html;html下支持vchart渲染和交互
  output_type: 'png' | 'html'
}
```

## 输出
最终以'png'或者'html'的形式保存在本地，供后续agent使用

## VMind配置

### LLM

VMind本身也需要通过调用大模型得到智能图表生成结果，目前默认会使用`config.llm["default"]`配置

### 生成配置

主要生成配置包括图表的宽高、主题以及生成方式；
### 生成方式
默认为png，目前支持大模型根据上下文自己选择`output_type`

### 宽高
目前默认不指定宽高，`html`下默认占满整个页面，'png'下默认为`1000 * 1000`

### 主题
目前默认主题为`'light'`，VChart图表支持多种主题，详见[主题](https://www.visactor.io/vchart/guide/tutorial_docs/Theme/Theme_Extension)


## 测试

当前设置了两种不能难度的任务用于测试

### 简单图表生成任务

给予数据和具体的图表生成需求，测试结果，执行命令：
```bash
python -m app.tool.chart_visualization.test.simple_chart
```
结果应位于`./data`下，涉及到9种不同的图表结果

### 简单数据报表任务

给予简单原始数据可分析需求，需要对数据进行简单加工处理，执行命令：
```bash
python -m app.tool.chart_visualization.test.simple_report
```
结果同样位于`./data`下
