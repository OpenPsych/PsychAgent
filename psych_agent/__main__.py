"""
Endpoint

Usage:
```shell
python psych_agent <topic>
```
"""

import typer

from psych_agent.agent import PsychAgent


app = typer.Typer()


@app.command()
def consult(topic: str):
    """
    Request a consultation with the psych-agent.

    :param topic: The topic of the consultation.
    """
    # 创建心理咨询智能体实例
    psych_agent = PsychAgent()
    # 调用智能体的 consult 方法
    result = psych_agent.consult(topic)
    # 输出结果
    typer.echo(result)


# 运行 Typer 应用
if __name__ == "__main__":
    app()
