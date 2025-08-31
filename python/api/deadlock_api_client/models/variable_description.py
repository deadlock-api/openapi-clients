from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.variable_category import VariableCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="VariableDescription")


@_attrs_define
class VariableDescription:
    """
    Attributes:
        category (VariableCategory):
        description (str): The description of the variable.
        extra_args (list[str]): Extra arguments that can be passed to the variable.
        name (str): The name of the variable.
        default_label (Union[None, Unset, str]): The default label for the variable.
    """

    category: VariableCategory
    description: str
    extra_args: list[str]
    name: str
    default_label: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        description = self.description

        extra_args = self.extra_args

        name = self.name

        default_label: Union[None, Unset, str]
        if isinstance(self.default_label, Unset):
            default_label = UNSET
        else:
            default_label = self.default_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "description": description,
                "extra_args": extra_args,
                "name": name,
            }
        )
        if default_label is not UNSET:
            field_dict["default_label"] = default_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = VariableCategory(d.pop("category"))

        description = d.pop("description")

        extra_args = cast(list[str], d.pop("extra_args"))

        name = d.pop("name")

        def _parse_default_label(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_label = _parse_default_label(d.pop("default_label", UNSET))

        variable_description = cls(
            category=category,
            description=description,
            extra_args=extra_args,
            name=name,
            default_label=default_label,
        )

        variable_description.additional_properties = d
        return variable_description

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
