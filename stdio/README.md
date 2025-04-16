# MCP stdio Transport
## 概要
- MCPサーバーをサブプロセスとして起動(サーバーを起動するプログラム`mini_server.py`をクライアントを動かす前に実行)
- MCPクライアントを非同期プロセスとして起動し、`stdio`を使って通信する
- MPCクライアントは`stdin`に書き込みを行い、MPCサーバーは`stdout`に結果を返す(https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#stdio)
- メッセージフォーマットは[JSON-RPC](https://www.jsonrpc.org/)に準拠

### MCPサーバー
- `FastMCP`で`hello`というMCPサーバーを起動する
  - MCPサーバーには`hello_world`および`goodbye`というツールが含まれている(`@mcp.tool()`というデコレーターを設定)
    - ツールの機能はメッセージを生成して返すだけのシンプルなもの
- `stdio`を使用するために、起動時の`run()`メソッドの引数に`stdio`を指定

### MCPクライアント
- MCPクライアントを起動する
  - MPCサーバーとのやり取りは非同期で実行
- 起動時にMCPサーバーの`stdio`(`stdin`/`stdout`)を取得しセッションを取得する
- MCPサーバーで定義されているツール一覧を取得する
- `call_tool()`メソッドを用いてMCPサーバーにリクエスト(使用したいツールと引数)を送信

## 実行

```bash
$ python mini_client.py
Processing request of type ListToolsRequest
tools: meta=None nextCursor=None tools=[Tool(name='hello_world', description='Say hello to someone', inputSchema={'properties': {'name': {'title': 'Name', 'type': 'string'}}, 'required': ['name'], 'title': 'hello_worldArguments', 'type': 'object'}), Tool(name='goodbye', description='Say goodbye to someone', inputSchema={'properties': {'name': {'title': 'Name', 'type': 'string'}}, 'required': ['name'], 'title': 'goodbyeArguments', 'type': 'object'})]
Processing request of type CallToolRequest
Tool result: [TextContent(type='text', text='Hello, MCP!', annotations=None)]
```