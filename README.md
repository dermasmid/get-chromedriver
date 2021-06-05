# Installation

```bash
pip3 install get_chromedriver
```

# Usage

From python:

```python
import get_chromedriver
get_chromedriver.download_chromedriver()
```
From the shell:
```bash
python3 -m get_chromedriver
```



The download_chromedriver() function takes a optional arg for the google chrome version, if not provided, we run `google-chrome --version`.
