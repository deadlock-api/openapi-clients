from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.objective_position_v1 import ObjectivePositionV1


T = TypeVar("T", bound="ObjectivePositionsV1")


@_attrs_define
class ObjectivePositionsV1:
    """
    Attributes:
        team0_core (ObjectivePositionV1):
        team1_core (ObjectivePositionV1):
        team0_titan (ObjectivePositionV1):
        team1_titan (ObjectivePositionV1):
        team0_tier2_1 (ObjectivePositionV1):
        team0_tier2_3 (ObjectivePositionV1):
        team0_tier2_4 (ObjectivePositionV1):
        team1_tier2_1 (ObjectivePositionV1):
        team1_tier2_3 (ObjectivePositionV1):
        team1_tier2_4 (ObjectivePositionV1):
        team0_tier1_1 (ObjectivePositionV1):
        team0_tier1_3 (ObjectivePositionV1):
        team0_tier1_4 (ObjectivePositionV1):
        team1_tier1_1 (ObjectivePositionV1):
        team1_tier1_3 (ObjectivePositionV1):
        team1_tier1_4 (ObjectivePositionV1):
        team0_tier2_2 (Union['ObjectivePositionV1', None, Unset]):
        team1_tier2_2 (Union['ObjectivePositionV1', None, Unset]):
        team0_tier1_2 (Union['ObjectivePositionV1', None, Unset]):
        team1_tier1_2 (Union['ObjectivePositionV1', None, Unset]):
    """

    team0_core: "ObjectivePositionV1"
    team1_core: "ObjectivePositionV1"
    team0_titan: "ObjectivePositionV1"
    team1_titan: "ObjectivePositionV1"
    team0_tier2_1: "ObjectivePositionV1"
    team0_tier2_3: "ObjectivePositionV1"
    team0_tier2_4: "ObjectivePositionV1"
    team1_tier2_1: "ObjectivePositionV1"
    team1_tier2_3: "ObjectivePositionV1"
    team1_tier2_4: "ObjectivePositionV1"
    team0_tier1_1: "ObjectivePositionV1"
    team0_tier1_3: "ObjectivePositionV1"
    team0_tier1_4: "ObjectivePositionV1"
    team1_tier1_1: "ObjectivePositionV1"
    team1_tier1_3: "ObjectivePositionV1"
    team1_tier1_4: "ObjectivePositionV1"
    team0_tier2_2: Union["ObjectivePositionV1", None, Unset] = UNSET
    team1_tier2_2: Union["ObjectivePositionV1", None, Unset] = UNSET
    team0_tier1_2: Union["ObjectivePositionV1", None, Unset] = UNSET
    team1_tier1_2: Union["ObjectivePositionV1", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.objective_position_v1 import ObjectivePositionV1

        team0_core = self.team0_core.to_dict()

        team1_core = self.team1_core.to_dict()

        team0_titan = self.team0_titan.to_dict()

        team1_titan = self.team1_titan.to_dict()

        team0_tier2_1 = self.team0_tier2_1.to_dict()

        team0_tier2_3 = self.team0_tier2_3.to_dict()

        team0_tier2_4 = self.team0_tier2_4.to_dict()

        team1_tier2_1 = self.team1_tier2_1.to_dict()

        team1_tier2_3 = self.team1_tier2_3.to_dict()

        team1_tier2_4 = self.team1_tier2_4.to_dict()

        team0_tier1_1 = self.team0_tier1_1.to_dict()

        team0_tier1_3 = self.team0_tier1_3.to_dict()

        team0_tier1_4 = self.team0_tier1_4.to_dict()

        team1_tier1_1 = self.team1_tier1_1.to_dict()

        team1_tier1_3 = self.team1_tier1_3.to_dict()

        team1_tier1_4 = self.team1_tier1_4.to_dict()

        team0_tier2_2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.team0_tier2_2, Unset):
            team0_tier2_2 = UNSET
        elif isinstance(self.team0_tier2_2, ObjectivePositionV1):
            team0_tier2_2 = self.team0_tier2_2.to_dict()
        else:
            team0_tier2_2 = self.team0_tier2_2

        team1_tier2_2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.team1_tier2_2, Unset):
            team1_tier2_2 = UNSET
        elif isinstance(self.team1_tier2_2, ObjectivePositionV1):
            team1_tier2_2 = self.team1_tier2_2.to_dict()
        else:
            team1_tier2_2 = self.team1_tier2_2

        team0_tier1_2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.team0_tier1_2, Unset):
            team0_tier1_2 = UNSET
        elif isinstance(self.team0_tier1_2, ObjectivePositionV1):
            team0_tier1_2 = self.team0_tier1_2.to_dict()
        else:
            team0_tier1_2 = self.team0_tier1_2

        team1_tier1_2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.team1_tier1_2, Unset):
            team1_tier1_2 = UNSET
        elif isinstance(self.team1_tier1_2, ObjectivePositionV1):
            team1_tier1_2 = self.team1_tier1_2.to_dict()
        else:
            team1_tier1_2 = self.team1_tier1_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team0_core": team0_core,
                "team1_core": team1_core,
                "team0_titan": team0_titan,
                "team1_titan": team1_titan,
                "team0_tier2_1": team0_tier2_1,
                "team0_tier2_3": team0_tier2_3,
                "team0_tier2_4": team0_tier2_4,
                "team1_tier2_1": team1_tier2_1,
                "team1_tier2_3": team1_tier2_3,
                "team1_tier2_4": team1_tier2_4,
                "team0_tier1_1": team0_tier1_1,
                "team0_tier1_3": team0_tier1_3,
                "team0_tier1_4": team0_tier1_4,
                "team1_tier1_1": team1_tier1_1,
                "team1_tier1_3": team1_tier1_3,
                "team1_tier1_4": team1_tier1_4,
            }
        )
        if team0_tier2_2 is not UNSET:
            field_dict["team0_tier2_2"] = team0_tier2_2
        if team1_tier2_2 is not UNSET:
            field_dict["team1_tier2_2"] = team1_tier2_2
        if team0_tier1_2 is not UNSET:
            field_dict["team0_tier1_2"] = team0_tier1_2
        if team1_tier1_2 is not UNSET:
            field_dict["team1_tier1_2"] = team1_tier1_2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.objective_position_v1 import ObjectivePositionV1

        d = dict(src_dict)
        team0_core = ObjectivePositionV1.from_dict(d.pop("team0_core"))

        team1_core = ObjectivePositionV1.from_dict(d.pop("team1_core"))

        team0_titan = ObjectivePositionV1.from_dict(d.pop("team0_titan"))

        team1_titan = ObjectivePositionV1.from_dict(d.pop("team1_titan"))

        team0_tier2_1 = ObjectivePositionV1.from_dict(d.pop("team0_tier2_1"))

        team0_tier2_3 = ObjectivePositionV1.from_dict(d.pop("team0_tier2_3"))

        team0_tier2_4 = ObjectivePositionV1.from_dict(d.pop("team0_tier2_4"))

        team1_tier2_1 = ObjectivePositionV1.from_dict(d.pop("team1_tier2_1"))

        team1_tier2_3 = ObjectivePositionV1.from_dict(d.pop("team1_tier2_3"))

        team1_tier2_4 = ObjectivePositionV1.from_dict(d.pop("team1_tier2_4"))

        team0_tier1_1 = ObjectivePositionV1.from_dict(d.pop("team0_tier1_1"))

        team0_tier1_3 = ObjectivePositionV1.from_dict(d.pop("team0_tier1_3"))

        team0_tier1_4 = ObjectivePositionV1.from_dict(d.pop("team0_tier1_4"))

        team1_tier1_1 = ObjectivePositionV1.from_dict(d.pop("team1_tier1_1"))

        team1_tier1_3 = ObjectivePositionV1.from_dict(d.pop("team1_tier1_3"))

        team1_tier1_4 = ObjectivePositionV1.from_dict(d.pop("team1_tier1_4"))

        def _parse_team0_tier2_2(data: object) -> Union["ObjectivePositionV1", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                team0_tier2_2_type_0 = ObjectivePositionV1.from_dict(data)

                return team0_tier2_2_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ObjectivePositionV1", None, Unset], data)

        team0_tier2_2 = _parse_team0_tier2_2(d.pop("team0_tier2_2", UNSET))

        def _parse_team1_tier2_2(data: object) -> Union["ObjectivePositionV1", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                team1_tier2_2_type_0 = ObjectivePositionV1.from_dict(data)

                return team1_tier2_2_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ObjectivePositionV1", None, Unset], data)

        team1_tier2_2 = _parse_team1_tier2_2(d.pop("team1_tier2_2", UNSET))

        def _parse_team0_tier1_2(data: object) -> Union["ObjectivePositionV1", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                team0_tier1_2_type_0 = ObjectivePositionV1.from_dict(data)

                return team0_tier1_2_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ObjectivePositionV1", None, Unset], data)

        team0_tier1_2 = _parse_team0_tier1_2(d.pop("team0_tier1_2", UNSET))

        def _parse_team1_tier1_2(data: object) -> Union["ObjectivePositionV1", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                team1_tier1_2_type_0 = ObjectivePositionV1.from_dict(data)

                return team1_tier1_2_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ObjectivePositionV1", None, Unset], data)

        team1_tier1_2 = _parse_team1_tier1_2(d.pop("team1_tier1_2", UNSET))

        objective_positions_v1 = cls(
            team0_core=team0_core,
            team1_core=team1_core,
            team0_titan=team0_titan,
            team1_titan=team1_titan,
            team0_tier2_1=team0_tier2_1,
            team0_tier2_3=team0_tier2_3,
            team0_tier2_4=team0_tier2_4,
            team1_tier2_1=team1_tier2_1,
            team1_tier2_3=team1_tier2_3,
            team1_tier2_4=team1_tier2_4,
            team0_tier1_1=team0_tier1_1,
            team0_tier1_3=team0_tier1_3,
            team0_tier1_4=team0_tier1_4,
            team1_tier1_1=team1_tier1_1,
            team1_tier1_3=team1_tier1_3,
            team1_tier1_4=team1_tier1_4,
            team0_tier2_2=team0_tier2_2,
            team1_tier2_2=team1_tier2_2,
            team0_tier1_2=team0_tier1_2,
            team1_tier1_2=team1_tier1_2,
        )

        objective_positions_v1.additional_properties = d
        return objective_positions_v1

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
