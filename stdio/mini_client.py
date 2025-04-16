import asyncio
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp import ClientSession

async def main():
    # MCPサーバをサブプロセスとして起動(MCPサーバーを起動するコードを実行)
    # StdioServerParametersクラスのコンストラクタによりStdioServerParametersオブジェクトを取得
    server_params = StdioServerParameters(command="python", args=["./mini_server.py"])

    # MCPクライアントを起動
    # StdioServerParametersオブジェクトから受信用Stream(stdout)と送信用Stream(stdin)を取得
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session: # 使用するStreamを使ってセッションを生成
            await session.initialize()  # セッションの初期化

            print("tools:", await session.list_tools())  # MCPサーバーに含まれているツール一覧を取得

            # セッションを使用してhello_worldというツールをMCPで実行
            result = await session.call_tool("hello_world", {"name": "MCP"})
            print("Tool result:", result.content)

if __name__ == "__main__":
    asyncio.run(main())