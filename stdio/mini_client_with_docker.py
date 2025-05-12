import asyncio
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp import ClientSession
import subprocess
async def main():
    # MCPサーバをサブプロセスとして起動(MCPサーバーを起動するコードを実行)
    # StdioServerParametersクラスのコンストラクタによりStdioServerParametersオブジェクトを取得
    server_params = StdioServerParameters(command="docker", args=["run", "--name", "mini_mcp_server", "--rm", "-i", "ghcr.io/mochizuki875/mini_mcp_server:latest"])

    # MCPクライアントを起動
    async with stdio_client(server_params) as (read_stream, write_stream): # 非同期で受信用Stream(stdout)と送信用Stream(stdin)を取得

        async with ClientSession(read_stream, write_stream) as session: # 非同期でStreamからセッションを作成
            await session.initialize()  # セッションの初期化を待機(awaitは非同期処理の完了を待機)

            print("tools:", await session.list_tools())  # MCPサーバーに含まれているツール一覧の取得を待機

            result = await session.call_tool("hello_world", {"name": "MCP"})  # セッションを使用してhello_worldというツールをMCPで実行(await完了を待機)
            print("Tool result:", result.content)

            # Enter入力待ち
            print("All done(Press Enter to exit)")
            input()

            # MCPサーバーを修了(もっと良いやり方あるはず...)
            subprocess.run(["docker", "rm", "-f", "mini_mcp_server"])

if __name__ == "__main__":
    asyncio.run(main())