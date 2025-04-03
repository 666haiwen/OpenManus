import asyncio

from app.agent.data_analysis import DataAnalysis

# from app.agent.manus import Manus


async def main():
    agent = DataAnalysis()
    # agent = Manus()
    await agent.run(
        """Requriment:
1. 分析以下数据并生成一个图文数据报告，格式为html.最终生成的产物是一个data report
2. 图表中需要有insights
Data:月份	团队A	团队B	团队C
1月	1200小时	1350小时	1100小时
2月	1250小时	1400小时	1150小时
3月	1180小时	1300小时	1300小时
4月	1220小时	1280小时	1400小时
5月	1230小时	1320小时 	1450小时
6月	1200小时	1250小时 	1500小时"""
    )


if __name__ == "__main__":
    asyncio.run(main())
