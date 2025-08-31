from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RawItemPropertyScaleFunctionSubclassV2")


@_attrs_define
class RawItemPropertyScaleFunctionSubclassV2:
    """
    Attributes:
        class_name (Union[None, Unset, str]):
        subclass_name (Union[None, Unset, str]):
        specific_stat_scale_type (Union[None, Unset, str]):
        scaling_stats (Union[None, Unset, list[str]]):
        stat_scale (Union[None, Unset, float]):
    """

    class_name: Union[None, Unset, str] = UNSET
    subclass_name: Union[None, Unset, str] = UNSET
    specific_stat_scale_type: Union[None, Unset, str] = UNSET
    scaling_stats: Union[None, Unset, list[str]] = UNSET
    stat_scale: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_name: Union[None, Unset, str]
        if isinstance(self.class_name, Unset):
            class_name = UNSET
        else:
            class_name = self.class_name

        subclass_name: Union[None, Unset, str]
        if isinstance(self.subclass_name, Unset):
            subclass_name = UNSET
        else:
            subclass_name = self.subclass_name

        specific_stat_scale_type: Union[None, Unset, str]
        if isinstance(self.specific_stat_scale_type, Unset):
            specific_stat_scale_type = UNSET
        else:
            specific_stat_scale_type = self.specific_stat_scale_type

        scaling_stats: Union[None, Unset, list[str]]
        if isinstance(self.scaling_stats, Unset):
            scaling_stats = UNSET
        elif isinstance(self.scaling_stats, list):
            scaling_stats = self.scaling_stats

        else:
            scaling_stats = self.scaling_stats

        stat_scale: Union[None, Unset, float]
        if isinstance(self.stat_scale, Unset):
            stat_scale = UNSET
        else:
            stat_scale = self.stat_scale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if class_name is not UNSET:
            field_dict["class_name"] = class_name
        if subclass_name is not UNSET:
            field_dict["subclass_name"] = subclass_name
        if specific_stat_scale_type is not UNSET:
            field_dict["specific_stat_scale_type"] = specific_stat_scale_type
        if scaling_stats is not UNSET:
            field_dict["scaling_stats"] = scaling_stats
        if stat_scale is not UNSET:
            field_dict["stat_scale"] = stat_scale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_class_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        class_name = _parse_class_name(d.pop("class_name", UNSET))

        def _parse_subclass_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subclass_name = _parse_subclass_name(d.pop("subclass_name", UNSET))

        def _parse_specific_stat_scale_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        specific_stat_scale_type = _parse_specific_stat_scale_type(d.pop("specific_stat_scale_type", UNSET))

        def _parse_scaling_stats(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scaling_stats_type_0 = cast(list[str], data)

                return scaling_stats_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        scaling_stats = _parse_scaling_stats(d.pop("scaling_stats", UNSET))

        def _parse_stat_scale(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        stat_scale = _parse_stat_scale(d.pop("stat_scale", UNSET))

        raw_item_property_scale_function_subclass_v2 = cls(
            class_name=class_name,
            subclass_name=subclass_name,
            specific_stat_scale_type=specific_stat_scale_type,
            scaling_stats=scaling_stats,
            stat_scale=stat_scale,
        )

        raw_item_property_scale_function_subclass_v2.additional_properties = d
        return raw_item_property_scale_function_subclass_v2

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
