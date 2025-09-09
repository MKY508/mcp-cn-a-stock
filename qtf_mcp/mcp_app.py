from io import StringIO

from mcp.server.fastmcp import Context, FastMCP

from . import research

# Create an MCP server
mcp_app = FastMCP(
  "CnStock",
  sse_path="/cnstock/sse",
  message_path="/cnstock/messages/",
  streamable_http_path="/cnstock/mcp",
)


@mcp_app.tool()
async def search(query: str, ctx: Context) -> str:
  """Search for stock symbols by name or code
  Args:
    query (str): Search query (stock name or code)
  Returns:
    str: JSON array of matching stock IDs
  """
  from .symbols import search_symbols
  import json
  
  # Search for matching symbols
  results = search_symbols(query)
  
  # Return IDs in format ChatGPT expects
  ids = [{"id": r["symbol"], "name": r["name"], "type": "stock"} for r in results[:10]]
  return json.dumps(ids, ensure_ascii=False)


@mcp_app.tool()
async def fetch(resource_id: str, ctx: Context) -> str:
  """Fetch detailed information for a specific stock
  Args:
    resource_id (str): Stock symbol ID (e.g., "SH600000")
  Returns:
    str: Full stock information
  """
  # Use the existing medium function for fetching
  return await medium(resource_id, ctx)


@mcp_app.tool()
async def brief(symbol: str, ctx: Context) -> str:
  """Get brief information for a given stock symbol, including
  - basic data
  - trading data
  Args:
    symbol (str): Stock symbol, must be in the format of "SH000001" or "SZ000001", you should infer user inputs like stock name to stock symbol
  """
  who = ctx.request_context.request.client.host  # type: ignore
  raw_data = await research.load_raw_data(symbol, None, who)
  buf = StringIO()
  if len(raw_data) == 0:
    return "No data found for symbol: " + symbol
  research.build_basic_data(buf, symbol, raw_data)
  research.build_trading_data(buf, symbol, raw_data)
  """Get brief information for a given stock symbol"""
  return buf.getvalue()


@mcp_app.tool()
async def medium(symbol: str, ctx: Context) -> str:
  """Get medium information for a given stock symbol, including
  - basic data
  - trading data
  - financial data
  Args:
    symbol (str): Stock symbol, must be in the format of "SH000001" or "SZ000001", you infer convert user inputs like stock name to stock symbol
  """
  who = ctx.request_context.request.client.host  # type: ignore
  raw_data = await research.load_raw_data(symbol, None, who)
  buf = StringIO()
  if len(raw_data) == 0:
    return "No data found for symbol: " + symbol
  research.build_basic_data(buf, symbol, raw_data)
  research.build_trading_data(buf, symbol, raw_data)
  research.build_financial_data(buf, symbol, raw_data)
  return buf.getvalue()


@mcp_app.tool()
async def full(symbol: str, ctx: Context) -> str:
  """Get full information for a given stock symbol, including
  - basic data
  - trading data
  - financial data
  - technical analysis data
  Args:
    symbol (str): Stock symbol, must be in the format of "SH000001" or "SZ000001", you should infer user inputs like stock name to stock symbol
  """
  who = ctx.request_context.request.client.host  # type: ignore
  raw_data = await research.load_raw_data(symbol, None, who)
  buf = StringIO()
  if len(raw_data) == 0:
    return "No data found for symbol: " + symbol
  research.build_basic_data(buf, symbol, raw_data)
  research.build_trading_data(buf, symbol, raw_data)
  research.build_financial_data(buf, symbol, raw_data)
  research.build_technical_data(buf, symbol, raw_data)
  return buf.getvalue()
