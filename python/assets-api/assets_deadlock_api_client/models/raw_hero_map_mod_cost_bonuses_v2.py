from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RawHeroMapModCostBonusesV2")


@_attrs_define
class RawHeroMapModCostBonusesV2:
    """
    Attributes:
        gold_threshold (int):
        bonus (float):
        percent_on_graph (float):
    """

    gold_threshold: int
    bonus: float
    percent_on_graph: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gold_threshold = self.gold_threshold

        bonus = self.bonus

        percent_on_graph = self.percent_on_graph

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gold_threshold": gold_threshold,
                "bonus": bonus,
                "percent_on_graph": percent_on_graph,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gold_threshold = d.pop("gold_threshold")

        bonus = d.pop("bonus")

        percent_on_graph = d.pop("percent_on_graph")

        raw_hero_map_mod_cost_bonuses_v2 = cls(
            gold_threshold=gold_threshold,
            bonus=bonus,
            percent_on_graph=percent_on_graph,
        )

        raw_hero_map_mod_cost_bonuses_v2.additional_properties = d
        return raw_hero_map_mod_cost_bonuses_v2

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
