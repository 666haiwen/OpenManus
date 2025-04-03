import asyncio
from app.tool.chart_visualization import DataVisualization


async def mock_request(delay, value):
    await asyncio.sleep(delay)  # 模拟异步IO操作（如网络请求）
    return value


async def main():
    # 创建多个异步任务
    tasks = [
        mock_request(1, "结果1"),
        mock_request(2, "结果2"),
        mock_request(3, "结果3"),
    ]

    # 并发执行所有任务，等待全部完成
    results = await asyncio.gather(*tasks)
    print(results)  # 输出: ['结果1', '结果2', '结果3']


async def test_chart():
    chartTool = DataVisualization()
    print(
        await chartTool.execute(
            "workspace/insight_metadata.json", "html", "insight", "en"
        )
    )


if __name__ == "__main__":
    asyncio.run(test_chart())
    # 运行主协程
    # asyncio.run(main())
