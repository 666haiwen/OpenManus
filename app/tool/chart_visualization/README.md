

# Chart Visualization Tool

The chart visualization tool generates data processing code through Python and ultimately invokes [@visactor/vmind](https://github.com/VisActor/VMind) to obtain chart specifications. Chart rendering is implemented using [@visactor/vchart](https://github.com/VisActor/VChart).

## Installation

1. Install Node.js >= 18

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
# After installation, restart the terminal and install the latest Node.js LTS version:
nvm install --lts
```

2. Install dependencies

```bash
cd app/tool/chart_visualization
npm install
```

## Tool Parameters
```typescript
{
  // Generates Python code for data processing to produce a CSV file
  code: string;
  // Parses user intent to generate chart description
  chart_description: string;
  // Final output type (png/html). HTML supports VChart rendering and interaction
  output_type: 'png' | 'html'
}
```

## Output
The final results will be saved locally in `png` or `html` format for subsequent use by agents.

## VMind Configuration

### LLM

VMind requires LLM invocation for intelligent chart generation. By default, it uses the `config.llm["default"]` configuration.

### Generation Settings

Main configurations include chart dimensions, theme, and generation method:
### Generation Method
Default: png. Currently supports automatic selection of `output_type` by LLM based on context.

### Dimensions
Default dimensions are unspecified. For HTML output, charts fill the entire page by default. For PNG output, defaults to `1000*1000`.

### Theme
Default theme: `'light'`. VChart supports multiple themes. See [Themes](https://www.visactor.io/vchart/guide/tutorial_docs/Theme/Theme_Extension).

## Testing

Two test tasks with different difficulty levels are provided:

### Basic Chart Generation Task

Generates charts from given data and specific requirements. Execute with:
```bash
python -m app.tool.chart_visualization.test.simple_chart
```
Results will be saved in `./data`, containing 9 different chart types.

### Simple Data Report Task

Processes raw data with basic analysis requirements. Execute with:
```bash
python -m app.tool.chart_visualization.test.simple_report
```
Results will also be saved in `./data`.
