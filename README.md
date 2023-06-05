# text_indexer
This script takes a path of a local directory, indexes all markdown files, and dumps the resulting dictionary as a json file.
- Does not import directory recursively
- Does not ignore "stop-words"
- Does not employ language-specific stemming
- Not concurrent (Slow for very large files)
