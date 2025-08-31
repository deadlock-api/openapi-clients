from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RankImagesV2")


@_attrs_define
class RankImagesV2:
    """
    Attributes:
        large (Union[None, Unset, str]):
        large_webp (Union[None, Unset, str]):
        large_subrank1 (Union[None, Unset, str]):
        large_subrank1_webp (Union[None, Unset, str]):
        large_subrank2 (Union[None, Unset, str]):
        large_subrank2_webp (Union[None, Unset, str]):
        large_subrank3 (Union[None, Unset, str]):
        large_subrank3_webp (Union[None, Unset, str]):
        large_subrank4 (Union[None, Unset, str]):
        large_subrank4_webp (Union[None, Unset, str]):
        large_subrank5 (Union[None, Unset, str]):
        large_subrank5_webp (Union[None, Unset, str]):
        large_subrank6 (Union[None, Unset, str]):
        large_subrank6_webp (Union[None, Unset, str]):
        small (Union[None, Unset, str]):
        small_webp (Union[None, Unset, str]):
        small_subrank1 (Union[None, Unset, str]):
        small_subrank1_webp (Union[None, Unset, str]):
        small_subrank2 (Union[None, Unset, str]):
        small_subrank2_webp (Union[None, Unset, str]):
        small_subrank3 (Union[None, Unset, str]):
        small_subrank3_webp (Union[None, Unset, str]):
        small_subrank4 (Union[None, Unset, str]):
        small_subrank4_webp (Union[None, Unset, str]):
        small_subrank5 (Union[None, Unset, str]):
        small_subrank5_webp (Union[None, Unset, str]):
        small_subrank6 (Union[None, Unset, str]):
        small_subrank6_webp (Union[None, Unset, str]):
    """

    large: Union[None, Unset, str] = UNSET
    large_webp: Union[None, Unset, str] = UNSET
    large_subrank1: Union[None, Unset, str] = UNSET
    large_subrank1_webp: Union[None, Unset, str] = UNSET
    large_subrank2: Union[None, Unset, str] = UNSET
    large_subrank2_webp: Union[None, Unset, str] = UNSET
    large_subrank3: Union[None, Unset, str] = UNSET
    large_subrank3_webp: Union[None, Unset, str] = UNSET
    large_subrank4: Union[None, Unset, str] = UNSET
    large_subrank4_webp: Union[None, Unset, str] = UNSET
    large_subrank5: Union[None, Unset, str] = UNSET
    large_subrank5_webp: Union[None, Unset, str] = UNSET
    large_subrank6: Union[None, Unset, str] = UNSET
    large_subrank6_webp: Union[None, Unset, str] = UNSET
    small: Union[None, Unset, str] = UNSET
    small_webp: Union[None, Unset, str] = UNSET
    small_subrank1: Union[None, Unset, str] = UNSET
    small_subrank1_webp: Union[None, Unset, str] = UNSET
    small_subrank2: Union[None, Unset, str] = UNSET
    small_subrank2_webp: Union[None, Unset, str] = UNSET
    small_subrank3: Union[None, Unset, str] = UNSET
    small_subrank3_webp: Union[None, Unset, str] = UNSET
    small_subrank4: Union[None, Unset, str] = UNSET
    small_subrank4_webp: Union[None, Unset, str] = UNSET
    small_subrank5: Union[None, Unset, str] = UNSET
    small_subrank5_webp: Union[None, Unset, str] = UNSET
    small_subrank6: Union[None, Unset, str] = UNSET
    small_subrank6_webp: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        large: Union[None, Unset, str]
        if isinstance(self.large, Unset):
            large = UNSET
        else:
            large = self.large

        large_webp: Union[None, Unset, str]
        if isinstance(self.large_webp, Unset):
            large_webp = UNSET
        else:
            large_webp = self.large_webp

        large_subrank1: Union[None, Unset, str]
        if isinstance(self.large_subrank1, Unset):
            large_subrank1 = UNSET
        else:
            large_subrank1 = self.large_subrank1

        large_subrank1_webp: Union[None, Unset, str]
        if isinstance(self.large_subrank1_webp, Unset):
            large_subrank1_webp = UNSET
        else:
            large_subrank1_webp = self.large_subrank1_webp

        large_subrank2: Union[None, Unset, str]
        if isinstance(self.large_subrank2, Unset):
            large_subrank2 = UNSET
        else:
            large_subrank2 = self.large_subrank2

        large_subrank2_webp: Union[None, Unset, str]
        if isinstance(self.large_subrank2_webp, Unset):
            large_subrank2_webp = UNSET
        else:
            large_subrank2_webp = self.large_subrank2_webp

        large_subrank3: Union[None, Unset, str]
        if isinstance(self.large_subrank3, Unset):
            large_subrank3 = UNSET
        else:
            large_subrank3 = self.large_subrank3

        large_subrank3_webp: Union[None, Unset, str]
        if isinstance(self.large_subrank3_webp, Unset):
            large_subrank3_webp = UNSET
        else:
            large_subrank3_webp = self.large_subrank3_webp

        large_subrank4: Union[None, Unset, str]
        if isinstance(self.large_subrank4, Unset):
            large_subrank4 = UNSET
        else:
            large_subrank4 = self.large_subrank4

        large_subrank4_webp: Union[None, Unset, str]
        if isinstance(self.large_subrank4_webp, Unset):
            large_subrank4_webp = UNSET
        else:
            large_subrank4_webp = self.large_subrank4_webp

        large_subrank5: Union[None, Unset, str]
        if isinstance(self.large_subrank5, Unset):
            large_subrank5 = UNSET
        else:
            large_subrank5 = self.large_subrank5

        large_subrank5_webp: Union[None, Unset, str]
        if isinstance(self.large_subrank5_webp, Unset):
            large_subrank5_webp = UNSET
        else:
            large_subrank5_webp = self.large_subrank5_webp

        large_subrank6: Union[None, Unset, str]
        if isinstance(self.large_subrank6, Unset):
            large_subrank6 = UNSET
        else:
            large_subrank6 = self.large_subrank6

        large_subrank6_webp: Union[None, Unset, str]
        if isinstance(self.large_subrank6_webp, Unset):
            large_subrank6_webp = UNSET
        else:
            large_subrank6_webp = self.large_subrank6_webp

        small: Union[None, Unset, str]
        if isinstance(self.small, Unset):
            small = UNSET
        else:
            small = self.small

        small_webp: Union[None, Unset, str]
        if isinstance(self.small_webp, Unset):
            small_webp = UNSET
        else:
            small_webp = self.small_webp

        small_subrank1: Union[None, Unset, str]
        if isinstance(self.small_subrank1, Unset):
            small_subrank1 = UNSET
        else:
            small_subrank1 = self.small_subrank1

        small_subrank1_webp: Union[None, Unset, str]
        if isinstance(self.small_subrank1_webp, Unset):
            small_subrank1_webp = UNSET
        else:
            small_subrank1_webp = self.small_subrank1_webp

        small_subrank2: Union[None, Unset, str]
        if isinstance(self.small_subrank2, Unset):
            small_subrank2 = UNSET
        else:
            small_subrank2 = self.small_subrank2

        small_subrank2_webp: Union[None, Unset, str]
        if isinstance(self.small_subrank2_webp, Unset):
            small_subrank2_webp = UNSET
        else:
            small_subrank2_webp = self.small_subrank2_webp

        small_subrank3: Union[None, Unset, str]
        if isinstance(self.small_subrank3, Unset):
            small_subrank3 = UNSET
        else:
            small_subrank3 = self.small_subrank3

        small_subrank3_webp: Union[None, Unset, str]
        if isinstance(self.small_subrank3_webp, Unset):
            small_subrank3_webp = UNSET
        else:
            small_subrank3_webp = self.small_subrank3_webp

        small_subrank4: Union[None, Unset, str]
        if isinstance(self.small_subrank4, Unset):
            small_subrank4 = UNSET
        else:
            small_subrank4 = self.small_subrank4

        small_subrank4_webp: Union[None, Unset, str]
        if isinstance(self.small_subrank4_webp, Unset):
            small_subrank4_webp = UNSET
        else:
            small_subrank4_webp = self.small_subrank4_webp

        small_subrank5: Union[None, Unset, str]
        if isinstance(self.small_subrank5, Unset):
            small_subrank5 = UNSET
        else:
            small_subrank5 = self.small_subrank5

        small_subrank5_webp: Union[None, Unset, str]
        if isinstance(self.small_subrank5_webp, Unset):
            small_subrank5_webp = UNSET
        else:
            small_subrank5_webp = self.small_subrank5_webp

        small_subrank6: Union[None, Unset, str]
        if isinstance(self.small_subrank6, Unset):
            small_subrank6 = UNSET
        else:
            small_subrank6 = self.small_subrank6

        small_subrank6_webp: Union[None, Unset, str]
        if isinstance(self.small_subrank6_webp, Unset):
            small_subrank6_webp = UNSET
        else:
            small_subrank6_webp = self.small_subrank6_webp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if large is not UNSET:
            field_dict["large"] = large
        if large_webp is not UNSET:
            field_dict["large_webp"] = large_webp
        if large_subrank1 is not UNSET:
            field_dict["large_subrank1"] = large_subrank1
        if large_subrank1_webp is not UNSET:
            field_dict["large_subrank1_webp"] = large_subrank1_webp
        if large_subrank2 is not UNSET:
            field_dict["large_subrank2"] = large_subrank2
        if large_subrank2_webp is not UNSET:
            field_dict["large_subrank2_webp"] = large_subrank2_webp
        if large_subrank3 is not UNSET:
            field_dict["large_subrank3"] = large_subrank3
        if large_subrank3_webp is not UNSET:
            field_dict["large_subrank3_webp"] = large_subrank3_webp
        if large_subrank4 is not UNSET:
            field_dict["large_subrank4"] = large_subrank4
        if large_subrank4_webp is not UNSET:
            field_dict["large_subrank4_webp"] = large_subrank4_webp
        if large_subrank5 is not UNSET:
            field_dict["large_subrank5"] = large_subrank5
        if large_subrank5_webp is not UNSET:
            field_dict["large_subrank5_webp"] = large_subrank5_webp
        if large_subrank6 is not UNSET:
            field_dict["large_subrank6"] = large_subrank6
        if large_subrank6_webp is not UNSET:
            field_dict["large_subrank6_webp"] = large_subrank6_webp
        if small is not UNSET:
            field_dict["small"] = small
        if small_webp is not UNSET:
            field_dict["small_webp"] = small_webp
        if small_subrank1 is not UNSET:
            field_dict["small_subrank1"] = small_subrank1
        if small_subrank1_webp is not UNSET:
            field_dict["small_subrank1_webp"] = small_subrank1_webp
        if small_subrank2 is not UNSET:
            field_dict["small_subrank2"] = small_subrank2
        if small_subrank2_webp is not UNSET:
            field_dict["small_subrank2_webp"] = small_subrank2_webp
        if small_subrank3 is not UNSET:
            field_dict["small_subrank3"] = small_subrank3
        if small_subrank3_webp is not UNSET:
            field_dict["small_subrank3_webp"] = small_subrank3_webp
        if small_subrank4 is not UNSET:
            field_dict["small_subrank4"] = small_subrank4
        if small_subrank4_webp is not UNSET:
            field_dict["small_subrank4_webp"] = small_subrank4_webp
        if small_subrank5 is not UNSET:
            field_dict["small_subrank5"] = small_subrank5
        if small_subrank5_webp is not UNSET:
            field_dict["small_subrank5_webp"] = small_subrank5_webp
        if small_subrank6 is not UNSET:
            field_dict["small_subrank6"] = small_subrank6
        if small_subrank6_webp is not UNSET:
            field_dict["small_subrank6_webp"] = small_subrank6_webp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_large(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        large = _parse_large(d.pop("large", UNSET))

        def _parse_large_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        large_webp = _parse_large_webp(d.pop("large_webp", UNSET))

        def _parse_large_subrank1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        large_subrank1 = _parse_large_subrank1(d.pop("large_subrank1", UNSET))

        def _parse_large_subrank1_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        large_subrank1_webp = _parse_large_subrank1_webp(d.pop("large_subrank1_webp", UNSET))

        def _parse_large_subrank2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        large_subrank2 = _parse_large_subrank2(d.pop("large_subrank2", UNSET))

        def _parse_large_subrank2_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        large_subrank2_webp = _parse_large_subrank2_webp(d.pop("large_subrank2_webp", UNSET))

        def _parse_large_subrank3(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        large_subrank3 = _parse_large_subrank3(d.pop("large_subrank3", UNSET))

        def _parse_large_subrank3_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        large_subrank3_webp = _parse_large_subrank3_webp(d.pop("large_subrank3_webp", UNSET))

        def _parse_large_subrank4(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        large_subrank4 = _parse_large_subrank4(d.pop("large_subrank4", UNSET))

        def _parse_large_subrank4_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        large_subrank4_webp = _parse_large_subrank4_webp(d.pop("large_subrank4_webp", UNSET))

        def _parse_large_subrank5(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        large_subrank5 = _parse_large_subrank5(d.pop("large_subrank5", UNSET))

        def _parse_large_subrank5_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        large_subrank5_webp = _parse_large_subrank5_webp(d.pop("large_subrank5_webp", UNSET))

        def _parse_large_subrank6(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        large_subrank6 = _parse_large_subrank6(d.pop("large_subrank6", UNSET))

        def _parse_large_subrank6_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        large_subrank6_webp = _parse_large_subrank6_webp(d.pop("large_subrank6_webp", UNSET))

        def _parse_small(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small = _parse_small(d.pop("small", UNSET))

        def _parse_small_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small_webp = _parse_small_webp(d.pop("small_webp", UNSET))

        def _parse_small_subrank1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small_subrank1 = _parse_small_subrank1(d.pop("small_subrank1", UNSET))

        def _parse_small_subrank1_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small_subrank1_webp = _parse_small_subrank1_webp(d.pop("small_subrank1_webp", UNSET))

        def _parse_small_subrank2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small_subrank2 = _parse_small_subrank2(d.pop("small_subrank2", UNSET))

        def _parse_small_subrank2_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small_subrank2_webp = _parse_small_subrank2_webp(d.pop("small_subrank2_webp", UNSET))

        def _parse_small_subrank3(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small_subrank3 = _parse_small_subrank3(d.pop("small_subrank3", UNSET))

        def _parse_small_subrank3_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small_subrank3_webp = _parse_small_subrank3_webp(d.pop("small_subrank3_webp", UNSET))

        def _parse_small_subrank4(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small_subrank4 = _parse_small_subrank4(d.pop("small_subrank4", UNSET))

        def _parse_small_subrank4_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small_subrank4_webp = _parse_small_subrank4_webp(d.pop("small_subrank4_webp", UNSET))

        def _parse_small_subrank5(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small_subrank5 = _parse_small_subrank5(d.pop("small_subrank5", UNSET))

        def _parse_small_subrank5_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small_subrank5_webp = _parse_small_subrank5_webp(d.pop("small_subrank5_webp", UNSET))

        def _parse_small_subrank6(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small_subrank6 = _parse_small_subrank6(d.pop("small_subrank6", UNSET))

        def _parse_small_subrank6_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small_subrank6_webp = _parse_small_subrank6_webp(d.pop("small_subrank6_webp", UNSET))

        rank_images_v2 = cls(
            large=large,
            large_webp=large_webp,
            large_subrank1=large_subrank1,
            large_subrank1_webp=large_subrank1_webp,
            large_subrank2=large_subrank2,
            large_subrank2_webp=large_subrank2_webp,
            large_subrank3=large_subrank3,
            large_subrank3_webp=large_subrank3_webp,
            large_subrank4=large_subrank4,
            large_subrank4_webp=large_subrank4_webp,
            large_subrank5=large_subrank5,
            large_subrank5_webp=large_subrank5_webp,
            large_subrank6=large_subrank6,
            large_subrank6_webp=large_subrank6_webp,
            small=small,
            small_webp=small_webp,
            small_subrank1=small_subrank1,
            small_subrank1_webp=small_subrank1_webp,
            small_subrank2=small_subrank2,
            small_subrank2_webp=small_subrank2_webp,
            small_subrank3=small_subrank3,
            small_subrank3_webp=small_subrank3_webp,
            small_subrank4=small_subrank4,
            small_subrank4_webp=small_subrank4_webp,
            small_subrank5=small_subrank5,
            small_subrank5_webp=small_subrank5_webp,
            small_subrank6=small_subrank6,
            small_subrank6_webp=small_subrank6_webp,
        )

        rank_images_v2.additional_properties = d
        return rank_images_v2

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
