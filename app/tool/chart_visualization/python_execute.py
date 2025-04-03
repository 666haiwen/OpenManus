from app.config import config
from app.tool.python_execute import PythonExecute


class NormalPythonExecute(PythonExecute):
    """A tool for executing Python code with timeout and safety restrictions."""

    name: str = "python_execute"
    description: str = (
        "Execute Python code for in-depth data analysis, data reporting, or other tasks without direct visualization.\n"
        "Note:\n"
        "1. Provide your Python code as a plain text JSON string. DO NOT wrap your code with any markdown formatting, such as triple backticks (``` or ```python).\n"
        '2. IMPORTANT: Your code must be formatted as a valid JSON string. This means that all newline characters must be represented by the escape sequence "\\n" (a backslash followed by n), and no literal newline characters should be present. Also, ensure that your code retains its intended indentation via these escape sequences.\n'
        "3. The code should generate a comprehensive text-based report that includes at least a dataset overview, column details, basic statistics, derived metrics, time series comparisons, outlier analysis, and key insights.\n"
        "4. All outputs must be printed using print(), and any reports or processed files should be saved in the workspace directory: {directory}.\n"
        "5. Verify that any file paths referenced in your code are correct and that all required files exist at those locations.\n"
        "6. You can invoke this tool step-by-step to perform a complete analysis from summary to detailed exploration.".format(
            directory=config.workspace_root
        )
    )
    parameters: dict = {
        "type": "object",
        "properties": {
            "code_type": {
                "description": "Code type: e.g., data process, data report, or others.",
                "type": "string",
                "default": "process",
                "enum": ["process", "report", "others"],
            },
            "code": {
                "type": "string",
                "description": (
                    "Plain text Python code to execute. DO NOT include markdown formatting such as triple backticks. "
                    "Ensure the code retains its proper newline characters and indentation."
                ),
            },
        },
        "required": ["code"],
    }

    async def execute(self, code: str, code_type: str | None = None, timeout=5):
        if code.startswith("```"):
            lines = code.splitlines()
            if lines and lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].startswith("```"):
                lines = lines[:-1]
            code = "\n".join(lines)
        code = code.replace("```", "")
        return await super().execute(code, timeout)
