import json
import logging
from typing import Dict, Iterable, Tuple

SYMBOLS_SHSZ: Dict[str, Tuple[str, int, int]] = {}

logger = logging.getLogger("qtf_mcp")


def load_markets(fname: str):
  try:
    with open(fname) as fp:
      m = json.load(fp)
      for o in m["items"]:
        SYMBOLS_SHSZ[o["code"]] = (o["name"], 2, 2)
  except:
    logger.warning("load markets failed", exc_info=True)


def load_symbols():
  """
  load symbols from confs/markets.json
  """
  load_markets("confs/markets.json")


def symbol_with_name(symbols: Iterable[str]) -> Iterable[Tuple[str, str]]:
  """
  return symbol with name
  """
  for s in symbols:
    if s in SYMBOLS_SHSZ:
      yield (s, SYMBOLS_SHSZ[s][0])
    else:
      yield (s, "")


def get_symbol_name(symbol: str) -> str:
  """
  get symbol name
  """
  if symbol in SYMBOLS_SHSZ:
    return SYMBOLS_SHSZ[symbol][0]
  else:
    return ""


def search_symbols(query: str) -> list:
  """
  Search for symbols by name or code
  """
  query = query.upper()
  results = []
  
  for code, (name, _, _) in SYMBOLS_SHSZ.items():
    # Match by code or name
    if query in code or query in name:
      results.append({
        "symbol": code,
        "name": name
      })
    # Also match if query is part of the name (pinyin or Chinese)
    elif name and (query.lower() in name.lower()):
      results.append({
        "symbol": code,
        "name": name
      })
  
  return results
