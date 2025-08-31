from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ZiplanePathV1")


@_attrs_define
class ZiplanePathV1:
    """
    Attributes:
        origin (list[float]): The origin of the path.
        color (str): The color of the path.
        p0_points (list[list[float]]): The P0 points of the path.
        p1_points (list[list[float]]): The P1 points of the path.
        p2_points (list[list[float]]): The P2 points of the path.
    """

    origin: list[float]
    color: str
    p0_points: list[list[float]]
    p1_points: list[list[float]]
    p2_points: list[list[float]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        origin = []
        for origin_item_data in self.origin:
            origin_item: float
            origin_item = origin_item_data
            origin.append(origin_item)

        color = self.color

        p0_points = []
        for p0_points_item_data in self.p0_points:
            p0_points_item = []
            for p0_points_item_item_data in p0_points_item_data:
                p0_points_item_item: float
                p0_points_item_item = p0_points_item_item_data
                p0_points_item.append(p0_points_item_item)

            p0_points.append(p0_points_item)

        p1_points = []
        for p1_points_item_data in self.p1_points:
            p1_points_item = []
            for p1_points_item_item_data in p1_points_item_data:
                p1_points_item_item: float
                p1_points_item_item = p1_points_item_item_data
                p1_points_item.append(p1_points_item_item)

            p1_points.append(p1_points_item)

        p2_points = []
        for p2_points_item_data in self.p2_points:
            p2_points_item = []
            for p2_points_item_item_data in p2_points_item_data:
                p2_points_item_item: float
                p2_points_item_item = p2_points_item_item_data
                p2_points_item.append(p2_points_item_item)

            p2_points.append(p2_points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "origin": origin,
                "color": color,
                "P0_points": p0_points,
                "P1_points": p1_points,
                "P2_points": p2_points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        origin = []
        _origin = d.pop("origin")
        for origin_item_data in _origin:

            def _parse_origin_item(data: object) -> float:
                return cast(float, data)

            origin_item = _parse_origin_item(origin_item_data)

            origin.append(origin_item)

        color = d.pop("color")

        p0_points = []
        _p0_points = d.pop("P0_points")
        for p0_points_item_data in _p0_points:
            p0_points_item = []
            _p0_points_item = p0_points_item_data
            for p0_points_item_item_data in _p0_points_item:

                def _parse_p0_points_item_item(data: object) -> float:
                    return cast(float, data)

                p0_points_item_item = _parse_p0_points_item_item(p0_points_item_item_data)

                p0_points_item.append(p0_points_item_item)

            p0_points.append(p0_points_item)

        p1_points = []
        _p1_points = d.pop("P1_points")
        for p1_points_item_data in _p1_points:
            p1_points_item = []
            _p1_points_item = p1_points_item_data
            for p1_points_item_item_data in _p1_points_item:

                def _parse_p1_points_item_item(data: object) -> float:
                    return cast(float, data)

                p1_points_item_item = _parse_p1_points_item_item(p1_points_item_item_data)

                p1_points_item.append(p1_points_item_item)

            p1_points.append(p1_points_item)

        p2_points = []
        _p2_points = d.pop("P2_points")
        for p2_points_item_data in _p2_points:
            p2_points_item = []
            _p2_points_item = p2_points_item_data
            for p2_points_item_item_data in _p2_points_item:

                def _parse_p2_points_item_item(data: object) -> float:
                    return cast(float, data)

                p2_points_item_item = _parse_p2_points_item_item(p2_points_item_item_data)

                p2_points_item.append(p2_points_item_item)

            p2_points.append(p2_points_item)

        ziplane_path_v1 = cls(
            origin=origin,
            color=color,
            p0_points=p0_points,
            p1_points=p1_points,
            p2_points=p2_points,
        )

        ziplane_path_v1.additional_properties = d
        return ziplane_path_v1

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
