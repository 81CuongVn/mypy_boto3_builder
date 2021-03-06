# ImportString

> Auto-generated documentation for [mypy_boto3_builder.import_helpers.import_string](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py) module.

Wrapper for Python import strings.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](index.md#import-helpers) / ImportString
    - [ImportString](#importstring)
        - [ImportString.empty](#importstringempty)
        - [ImportString.from_str](#importstringfrom_str)
        - [ImportString().master_name](#importstringmaster_name)
        - [ImportString.parent](#importstringparent)
        - [ImportString().render](#importstringrender)
        - [ImportString().startswith](#importstringstartswith)

## ImportString

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L9)

```python
class ImportString():
    def __init__(master_name: str, *parts: str) -> None:
```

Wrapper for Python import strings.

#### Arguments

- `master` - Master module name
- `parts` - Other import parts

#### Examples

```python
import_string = ImportString("my", "name")

str(import_string)
'my.name'

import_string.render()
'my.name'

import_string.parts.append('test')
import_string.render()
'my.name.test'
```

### ImportString.empty

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L47)

```python
@classmethod
def empty() -> _R:
```

Create an empty ImportString.

### ImportString.from_str

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L40)

```python
@classmethod
def from_str(import_string: str) -> 'ImportString':
```

Create from string.

### ImportString().master_name

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L126)

```python
@property
def master_name() -> str:
```

Get first import string part or `builtins`.

### ImportString.parent

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L56)

```python
@classmethod
def parent() -> _R:
```

Get parent ImportString.

### ImportString().render

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L117)

```python
def render() -> str:
```

Render to string.

#### Returns

Ready to use import string.

### ImportString().startswith

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L85)

```python
def startswith(other: _R) -> bool:
```

Check if import string starts with `other`.

#### Examples

```python
ImportString('my', 'name').startswith(ImportString('my'))
True

ImportString('my_module', 'name').startswith(ImportString('my'))
False

ImportString('my', 'name').startswith(ImportString('my, 'name'))
True

ImportString('my', 'name').startswith(ImportString.empty())
True
```

#### Arguments

- `other` - Other import string.
