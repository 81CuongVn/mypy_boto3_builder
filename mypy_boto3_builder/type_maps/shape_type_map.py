"""
String to type annotation map to replace overriden botocore shapes.
"""
from collections.abc import Iterable

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict

# FIXME: a hack to avoid cicular TypedDict in dynamodb package
TableAttributeValueType: TypeSubscript = TypeSubscript(
    Type.Union,
    [
        Type.bytes,
        Type.bytearray,
        Type.str,
        Type.int,
        Type.Decimal,
        Type.bool,
        TypeSubscript(Type.Set, [Type.int]),
        TypeSubscript(Type.Set, [Type.Decimal]),
        TypeSubscript(Type.Set, [Type.str]),
        TypeSubscript(Type.Set, [Type.bytes]),
        TypeSubscript(Type.Set, [Type.bytearray]),
        Type.SequenceAny,
        Type.MappingStrAny,
        Type.none,
    ],
)

AttributeValueTypeDef: TypeTypedDict = TypeTypedDict(
    "AttributeValueTypeDef",
    [
        TypedDictAttribute("S", Type.str, False),
        TypedDictAttribute("N", Type.str, False),
        TypedDictAttribute("B", Type.bytes, False),
        TypedDictAttribute("SS", TypeSubscript(Type.Sequence, [Type.str]), False),
        TypedDictAttribute("NS", TypeSubscript(Type.Sequence, [Type.str]), False),
        TypedDictAttribute("BS", TypeSubscript(Type.Sequence, [Type.bytes]), False),
        TypedDictAttribute("M", Type.MappingStrAny, False),
        TypedDictAttribute("L", Type.SequenceAny, False),
        TypedDictAttribute("NULL", Type.bool, False),
        TypedDictAttribute("BOOL", Type.bool, False),
    ],
)

# FIXME: a hack to avoid cicular TypedDict in lambda package
InvocationResponseTypeDef: TypeTypedDict = TypeTypedDict(
    "InvocationResponseTypeDef",
    [
        TypedDictAttribute("StatusCode", Type.int, False),
        TypedDictAttribute("FunctionError", Type.str, False),
        TypedDictAttribute("LogResult", Type.str, False),
        TypedDictAttribute("Payload", Type.IOBytes, False),
        TypedDictAttribute("ExecutedVersion", Type.str, False),
    ],
)

StreamingBodyType = ExternalImport(ImportString("botocore", "response"), "StreamingBody")
ShapeTypeMap = dict[ServiceName, dict[str, FakeAnnotation]]

SHAPE_TYPE_MAP: ShapeTypeMap = {
    ServiceNameCatalog.all: {
        "integer": Type.int,
        "long": Type.int,
        "boolean": Type.bool,
        "double": Type.float,
        "float": Type.float,
        "timestamp": TypeSubscript(Type.Union, [Type.datetime, Type.str]),
        "blob": TypeSubscript(Type.Union, [Type.str, Type.bytes, Type.IOAny, StreamingBodyType]),
        "blob_streaming": TypeSubscript(
            Type.Union, [Type.str, Type.bytes, Type.IOAny, StreamingBodyType]
        ),
    },
    ServiceNameCatalog.lambda_: {
        "InvocationResponseTypeDef": InvocationResponseTypeDef,
    },
    ServiceNameCatalog.dynamodb: {
        "AttributeValueTypeDef": AttributeValueTypeDef,
        "AttributeValueTableTypeDef": TableAttributeValueType,
    },
}

OUTPUT_SHAPE_TYPE_MAP: ShapeTypeMap = {
    ServiceNameCatalog.all: {
        "timestamp": Type.datetime,
        "blob": Type.bytes,
        "blob_streaming": StreamingBodyType,
    },
}


def get_shape_type_stub(
    shape_type_maps: Iterable[ShapeTypeMap],
    service_name: ServiceName,
    shape_name: str,
) -> FakeAnnotation | None:
    """
    Get stub type for input botocore shape.

    Arguments:
        shape_type_map -- Map to lookup
        service_name -- Service name
        shape_name -- Target TypedDict name

    Returns:
        Type annotation or None.
    """
    service_names = (service_name, ServiceNameCatalog.all)
    for shape_type_map in shape_type_maps:
        for current_service_name in service_names:
            service_shape_type_map = shape_type_map.get(current_service_name, {})
            if shape_name in service_shape_type_map:
                return service_shape_type_map[shape_name]

    return None
