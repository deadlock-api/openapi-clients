from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player_card_slot_hero import PlayerCardSlotHero
    from ..models.player_card_slot_stat import PlayerCardSlotStat


T = TypeVar("T", bound="PlayerCardSlot")


@_attrs_define
class PlayerCardSlot:
    """
    Attributes:
        hero (Union['PlayerCardSlotHero', None, Unset]):
        slot_id (Union[None, Unset, int]):
        stat (Union['PlayerCardSlotStat', None, Unset]):
    """

    hero: Union["PlayerCardSlotHero", None, Unset] = UNSET
    slot_id: Union[None, Unset, int] = UNSET
    stat: Union["PlayerCardSlotStat", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.player_card_slot_hero import PlayerCardSlotHero
        from ..models.player_card_slot_stat import PlayerCardSlotStat

        hero: Union[None, Unset, dict[str, Any]]
        if isinstance(self.hero, Unset):
            hero = UNSET
        elif isinstance(self.hero, PlayerCardSlotHero):
            hero = self.hero.to_dict()
        else:
            hero = self.hero

        slot_id: Union[None, Unset, int]
        if isinstance(self.slot_id, Unset):
            slot_id = UNSET
        else:
            slot_id = self.slot_id

        stat: Union[None, Unset, dict[str, Any]]
        if isinstance(self.stat, Unset):
            stat = UNSET
        elif isinstance(self.stat, PlayerCardSlotStat):
            stat = self.stat.to_dict()
        else:
            stat = self.stat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hero is not UNSET:
            field_dict["hero"] = hero
        if slot_id is not UNSET:
            field_dict["slot_id"] = slot_id
        if stat is not UNSET:
            field_dict["stat"] = stat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.player_card_slot_hero import PlayerCardSlotHero
        from ..models.player_card_slot_stat import PlayerCardSlotStat

        d = dict(src_dict)

        def _parse_hero(data: object) -> Union["PlayerCardSlotHero", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hero_type_1 = PlayerCardSlotHero.from_dict(data)

                return hero_type_1
            except:  # noqa: E722
                pass
            return cast(Union["PlayerCardSlotHero", None, Unset], data)

        hero = _parse_hero(d.pop("hero", UNSET))

        def _parse_slot_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        slot_id = _parse_slot_id(d.pop("slot_id", UNSET))

        def _parse_stat(data: object) -> Union["PlayerCardSlotStat", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stat_type_1 = PlayerCardSlotStat.from_dict(data)

                return stat_type_1
            except:  # noqa: E722
                pass
            return cast(Union["PlayerCardSlotStat", None, Unset], data)

        stat = _parse_stat(d.pop("stat", UNSET))

        player_card_slot = cls(
            hero=hero,
            slot_id=slot_id,
            stat=stat,
        )

        player_card_slot.additional_properties = d
        return player_card_slot

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
