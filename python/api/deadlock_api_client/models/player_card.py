from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player_card_slot import PlayerCardSlot


T = TypeVar("T", bound="PlayerCard")


@_attrs_define
class PlayerCard:
    """
    Attributes:
        account_id (int):
        slots (list['PlayerCardSlot']):
        ranked_badge_level (Union[None, Unset, int]): See more: <https://assets.deadlock-api.com/v2/ranks>
        ranked_rank (Union[None, Unset, int]): See more: <https://assets.deadlock-api.com/v2/ranks>
        ranked_subrank (Union[None, Unset, int]): See more: <https://assets.deadlock-api.com/v2/ranks>
    """

    account_id: int
    slots: list["PlayerCardSlot"]
    ranked_badge_level: Union[None, Unset, int] = UNSET
    ranked_rank: Union[None, Unset, int] = UNSET
    ranked_subrank: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        slots = []
        for slots_item_data in self.slots:
            slots_item = slots_item_data.to_dict()
            slots.append(slots_item)

        ranked_badge_level: Union[None, Unset, int]
        if isinstance(self.ranked_badge_level, Unset):
            ranked_badge_level = UNSET
        else:
            ranked_badge_level = self.ranked_badge_level

        ranked_rank: Union[None, Unset, int]
        if isinstance(self.ranked_rank, Unset):
            ranked_rank = UNSET
        else:
            ranked_rank = self.ranked_rank

        ranked_subrank: Union[None, Unset, int]
        if isinstance(self.ranked_subrank, Unset):
            ranked_subrank = UNSET
        else:
            ranked_subrank = self.ranked_subrank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "slots": slots,
            }
        )
        if ranked_badge_level is not UNSET:
            field_dict["ranked_badge_level"] = ranked_badge_level
        if ranked_rank is not UNSET:
            field_dict["ranked_rank"] = ranked_rank
        if ranked_subrank is not UNSET:
            field_dict["ranked_subrank"] = ranked_subrank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.player_card_slot import PlayerCardSlot

        d = dict(src_dict)
        account_id = d.pop("account_id")

        slots = []
        _slots = d.pop("slots")
        for slots_item_data in _slots:
            slots_item = PlayerCardSlot.from_dict(slots_item_data)

            slots.append(slots_item)

        def _parse_ranked_badge_level(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        ranked_badge_level = _parse_ranked_badge_level(d.pop("ranked_badge_level", UNSET))

        def _parse_ranked_rank(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        ranked_rank = _parse_ranked_rank(d.pop("ranked_rank", UNSET))

        def _parse_ranked_subrank(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        ranked_subrank = _parse_ranked_subrank(d.pop("ranked_subrank", UNSET))

        player_card = cls(
            account_id=account_id,
            slots=slots,
            ranked_badge_level=ranked_badge_level,
            ranked_rank=ranked_rank,
            ranked_subrank=ranked_subrank,
        )

        player_card.additional_properties = d
        return player_card

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
