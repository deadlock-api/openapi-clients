from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_images_v1 import MapImagesV1
    from ..models.objective_positions_v1 import ObjectivePositionsV1
    from ..models.ziplane_path_v1 import ZiplanePathV1


T = TypeVar("T", bound="MapV1")


@_attrs_define
class MapV1:
    """
    Attributes:
        images (MapImagesV1):
        objective_positions (ObjectivePositionsV1):
        zipline_paths (list['ZiplanePathV1']): The ziplane paths of the map. Each path is a list of P0, P1, and P2
            points, describing the cubic spline.
        radius (Union[Unset, int]): The radius of the map. Default: 10752.
    """

    images: "MapImagesV1"
    objective_positions: "ObjectivePositionsV1"
    zipline_paths: list["ZiplanePathV1"]
    radius: Union[Unset, int] = 10752
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        images = self.images.to_dict()

        objective_positions = self.objective_positions.to_dict()

        zipline_paths = []
        for zipline_paths_item_data in self.zipline_paths:
            zipline_paths_item = zipline_paths_item_data.to_dict()
            zipline_paths.append(zipline_paths_item)

        radius = self.radius

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "images": images,
                "objective_positions": objective_positions,
                "zipline_paths": zipline_paths,
            }
        )
        if radius is not UNSET:
            field_dict["radius"] = radius

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_images_v1 import MapImagesV1
        from ..models.objective_positions_v1 import ObjectivePositionsV1
        from ..models.ziplane_path_v1 import ZiplanePathV1

        d = dict(src_dict)
        images = MapImagesV1.from_dict(d.pop("images"))

        objective_positions = ObjectivePositionsV1.from_dict(d.pop("objective_positions"))

        zipline_paths = []
        _zipline_paths = d.pop("zipline_paths")
        for zipline_paths_item_data in _zipline_paths:
            zipline_paths_item = ZiplanePathV1.from_dict(zipline_paths_item_data)

            zipline_paths.append(zipline_paths_item)

        radius = d.pop("radius", UNSET)

        map_v1 = cls(
            images=images,
            objective_positions=objective_positions,
            zipline_paths=zipline_paths,
            radius=radius,
        )

        map_v1.additional_properties = d
        return map_v1

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
