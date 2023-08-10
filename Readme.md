# Description

A template for Python programming language project using the Broken Framework

Don't forget to change the License.md

Name everything "PackageName" and

- `PackageName/__main__.py:main()`: Entry function, should be the command `packagename` on `pyproject.toml`
- `PackageName/__init__.py`: Package initialization

Add `from Broken import *` on `__init__.py` and `from . import *` on `__main__.py`

# Usage

```bash
broken pythontemplate # "packagename"
broken release pythontemplate linux-amd64
broken date
...
```

