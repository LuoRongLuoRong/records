# 正则表达式实用实例——以 Python 为例

Python3 正则表达式 https://docs.python.org/zh-cn/3/library/re.html

### 匹配最短字符串

需求：将类似句子 `[[0]] is [[zero]]` 中的主语或者宾语置换成其它实体，比如改成 `[[1]] is [[zero]]`，或者 `[[0]] is [[one]]`。

在匹配的过程中发现，Python 会自动匹配最长字符串。因此，将 `.*` 改为 `(.*?)` 即可匹配最短字符串。

```python
def replace_entity(sentence, replaced_entity_content, head_flag=True):
    pattern = re.compile(r'\[\[(.*?)\]\]')   
    head = pattern.search(sentence)
    head_start_idx = head.span()[0]
    head_end_idx = head.span()[1]

    if head_flag: 
        return sentence[0:head_start_idx + 2] + replaced_entity_content + sentence[head_end_idx - 2:]
    else:
        tail = pattern.search(sentence, head_end_idx)
        tail_start_idx = tail.span()[0]
        tail_end_idx = tail.span()[1]
        return sentence[0:tail_start_idx + 2] + replaced_entity_content + sentence[tail_end_idx - 2:]
```

### 全字符匹配

需求：匹配全字符

```python
import re

text1 = 'ph1'
text2 = 'p'
pattern = re.compile('^(p|h1|h2|h3|h4|h5)$')
print(pattern.match(text1))
print(pattern.match(text2))
```

打印结果

```
None
<_sre.SRE_Match object; span=(0, 1), match='p'>
```

### 匹配数字和字母

需求：匹配数字、字母、下划线。

```python
import re

text1 = 'ph1-'
text2 = 'p'
pattern = re.compile('^([a-zA-Z_0-9]*)$')
print(pattern.match(text1))
print(pattern.match(text2))
```

### 匹配字符串中的字符串

使用 `re.findall()`。

```python
import re

text = 'MD5 has been found to suffer from extensive vulnerabilities.'
pattern_fun = 'has been found to'
res = re.findall(pattern_fun, text)

print(res)
```

输出：

```python
['has been found to']
```

