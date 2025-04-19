import asyncio
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp import ClientSession

async def main():
    # MCPサーバをサブプロセスとして起動(MCPサーバーを起動するコードを実行)
    # StdioServerParametersクラスのコンストラクタによりStdioServerParametersオブジェクトを取得
    server_params = StdioServerParameters(command="python", args=["./mini_server.py"])

    # MCPクライアントを起動
    async with stdio_client(server_params) as (read_stream, write_stream): # 非同期で受信用Stream(stdout)と送信用Stream(stdin)を取得
        async with ClientSession(read_stream, write_stream) as session: # 非同期でStreamからセッションを作成
            await session.initialize()  # セッションの初期化を待機(awaitは非同期処理の完了を待機)

            print("tools:", await session.list_tools())  # MCPサーバーに含まれているツール一覧の取得を待機

            result = await session.call_tool("hello_world", {"name": "MCP"})  # セッションを使用してhello_worldというツールをMCPで実行(await完了を待機)
            print("Tool result:", result.content)

if __name__ == "__main__":
    asyncio.run(main())