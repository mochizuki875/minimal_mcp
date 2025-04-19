import asyncio
from mcp.client.sse import sse_client
from mcp import ClientSession

async def main():
    # MCPクライアントを起動
    # URLを指定してStream(MemoryObjectReceiveStream)を取得
    async with sse_client(url="http://localhost:8080/sse") as stream:
        async with ClientSession(read_stream=stream[0], write_stream=stream[1]) as session: # 使用するStreamを使ってセッションを生成
            await session.initialize()  # セッションの初期化

            print("tools:", await session.list_tools())  # MCPサーバーに含まれているツール一覧を取得

            # セッションを使用してhello_worldというツールをMCPで実行
            result = await session.call_tool("hello_world", {"name": "MCP"})
            print("Tool result:", result.content)

if __name__ == "__main__":
    asyncio.run(main())