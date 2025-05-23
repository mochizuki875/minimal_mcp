from mcp.server.fastmcp import FastMCP

# helloというMCPサーバーを起動
mcp = FastMCP("hello")

# hello_worldというツールを定義
@mcp.tool(name="hello_world", description="Say hello to someone")
async def hello_world(name: str) -> str:
    return f"Hello, {name}!"

# goodbyeというツールを定義
@mcp.tool(name="goodbye", description="Say goodbye to someone")
async def goodbye(name: str) -> str:
    return f"Goodbye, {name}!"

if __name__ == "__main__":

    # MCPサーバーのホストとポートを設定
    mcp.settings.host = "0.0.0.0"
    mcp.settings.port = 8080
    
    # 通信にSSEを使用する
    # uvicornでMCPサーバーが実行される
    mcp.run(transport="sse")