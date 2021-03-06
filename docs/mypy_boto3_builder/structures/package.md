# Package

> Auto-generated documentation for [mypy_boto3_builder.structures.package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py) module.

Parent class for all package structures.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Package
    - [Package](#package)
        - [Package().directory_name](#packagedirectory_name)
        - [Package().get_local_doc_link](#packageget_local_doc_link)
        - [Package().get_module_name](#packageget_module_name)
        - [Package().get_service_pypi_link](#packageget_service_pypi_link)
        - [Package().get_service_pypi_name](#packageget_service_pypi_name)
        - [Package().max_library_version](#packagemax_library_version)
        - [Package().min_library_version](#packagemin_library_version)

## Package

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L12)

```python
class Package():
    def __init__(
        data: type[BasePackageData],
        service_names: Iterable[ServiceName] = tuple(),
    ) -> None:
```

Parent class for all package structures.

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [ServiceName](../service_name.md#servicename)

### Package().directory_name

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L31)

```python
@property
def directory_name() -> str:
```

Directory name to store generated package.

### Package().get_local_doc_link

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L42)

```python
def get_local_doc_link(service_name: ServiceName | None = None) -> str:
```

Get link to local docs.

### Package().get_module_name

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L51)

```python
def get_module_name(service_name: ServiceName) -> str:
```

Get service module name.

#### See also

- [ServiceName](../service_name.md#servicename)

### Package().get_service_pypi_link

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L63)

```python
def get_service_pypi_link(service_name: ServiceName) -> str:
```

Get link to PyPI.

#### See also

- [ServiceName](../service_name.md#servicename)

### Package().get_service_pypi_name

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L57)

```python
def get_service_pypi_name(service_name: ServiceName) -> str:
```

Get PyPI package name for a service package.

#### See also

- [ServiceName](../service_name.md#servicename)

### Package().max_library_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L76)

```python
@property
def max_library_version() -> str:
```

Minimum required library version.

### Package().min_library_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L69)

```python
@property
def min_library_version() -> str:
```

Minimum required library version.
