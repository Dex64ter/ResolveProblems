def FindTheIndexOfTheFirstOccurrenceInAString(haystack: str, needle: str) -> int:
  try:
    return haystack.index(needle)
  except:
    return -1
    