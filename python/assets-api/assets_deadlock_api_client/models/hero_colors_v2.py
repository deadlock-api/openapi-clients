from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HeroColorsV2")


@_attrs_define
class HeroColorsV2:
    """
    Attributes:
        glow_enemy (list[int]):
        glow_friendly (list[int]):
        glow_team1 (list[int]):
        glow_team2 (list[int]):
        ui (list[int]):
    """

    glow_enemy: list[int]
    glow_friendly: list[int]
    glow_team1: list[int]
    glow_team2: list[int]
    ui: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        glow_enemy = []
        for glow_enemy_item_data in self.glow_enemy:
            glow_enemy_item: int
            glow_enemy_item = glow_enemy_item_data
            glow_enemy.append(glow_enemy_item)

        glow_friendly = []
        for glow_friendly_item_data in self.glow_friendly:
            glow_friendly_item: int
            glow_friendly_item = glow_friendly_item_data
            glow_friendly.append(glow_friendly_item)

        glow_team1 = []
        for glow_team1_item_data in self.glow_team1:
            glow_team1_item: int
            glow_team1_item = glow_team1_item_data
            glow_team1.append(glow_team1_item)

        glow_team2 = []
        for glow_team2_item_data in self.glow_team2:
            glow_team2_item: int
            glow_team2_item = glow_team2_item_data
            glow_team2.append(glow_team2_item)

        ui = []
        for ui_item_data in self.ui:
            ui_item: int
            ui_item = ui_item_data
            ui.append(ui_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "glow_enemy": glow_enemy,
                "glow_friendly": glow_friendly,
                "glow_team1": glow_team1,
                "glow_team2": glow_team2,
                "ui": ui,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        glow_enemy = []
        _glow_enemy = d.pop("glow_enemy")
        for glow_enemy_item_data in _glow_enemy:

            def _parse_glow_enemy_item(data: object) -> int:
                return cast(int, data)

            glow_enemy_item = _parse_glow_enemy_item(glow_enemy_item_data)

            glow_enemy.append(glow_enemy_item)

        glow_friendly = []
        _glow_friendly = d.pop("glow_friendly")
        for glow_friendly_item_data in _glow_friendly:

            def _parse_glow_friendly_item(data: object) -> int:
                return cast(int, data)

            glow_friendly_item = _parse_glow_friendly_item(glow_friendly_item_data)

            glow_friendly.append(glow_friendly_item)

        glow_team1 = []
        _glow_team1 = d.pop("glow_team1")
        for glow_team1_item_data in _glow_team1:

            def _parse_glow_team1_item(data: object) -> int:
                return cast(int, data)

            glow_team1_item = _parse_glow_team1_item(glow_team1_item_data)

            glow_team1.append(glow_team1_item)

        glow_team2 = []
        _glow_team2 = d.pop("glow_team2")
        for glow_team2_item_data in _glow_team2:

            def _parse_glow_team2_item(data: object) -> int:
                return cast(int, data)

            glow_team2_item = _parse_glow_team2_item(glow_team2_item_data)

            glow_team2.append(glow_team2_item)

        ui = []
        _ui = d.pop("ui")
        for ui_item_data in _ui:

            def _parse_ui_item(data: object) -> int:
                return cast(int, data)

            ui_item = _parse_ui_item(ui_item_data)

            ui.append(ui_item)

        hero_colors_v2 = cls(
            glow_enemy=glow_enemy,
            glow_friendly=glow_friendly,
            glow_team1=glow_team1,
            glow_team2=glow_team2,
            ui=ui,
        )

        hero_colors_v2.additional_properties = d
        return hero_colors_v2

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
