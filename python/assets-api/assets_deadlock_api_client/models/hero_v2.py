from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hero_type_v2 import HeroTypeV2
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hero_colors_v2 import HeroColorsV2
    from ..models.hero_description_v2 import HeroDescriptionV2
    from ..models.hero_images_v2 import HeroImagesV2
    from ..models.hero_physics_v2 import HeroPhysicsV2
    from ..models.hero_shop_stat_display_v2 import HeroShopStatDisplayV2
    from ..models.hero_starting_stats_v2 import HeroStartingStatsV2
    from ..models.hero_v2_cost_bonuses_type_0 import HeroV2CostBonusesType0
    from ..models.hero_v2_item_slot_info import HeroV2ItemSlotInfo
    from ..models.hero_v2_items import HeroV2Items
    from ..models.hero_v2_level_info import HeroV2LevelInfo
    from ..models.hero_v2_purchase_bonuses import HeroV2PurchaseBonuses
    from ..models.hero_v2_scaling_stats import HeroV2ScalingStats
    from ..models.hero_v2_standard_level_up_upgrades import HeroV2StandardLevelUpUpgrades
    from ..models.raw_hero_stats_display_v2 import RawHeroStatsDisplayV2
    from ..models.raw_hero_stats_uiv2 import RawHeroStatsUIV2


T = TypeVar("T", bound="HeroV2")


@_attrs_define
class HeroV2:
    """
    Attributes:
        id (int):
        class_name (str):
        name (str):
        description (HeroDescriptionV2):
        player_selectable (bool):
        disabled (bool):
        in_development (bool):
        needs_testing (bool):
        assigned_players_only (bool):
        limited_testing (bool):
        complexity (int):
        skin (int):
        images (HeroImagesV2):
        items (HeroV2Items):
        starting_stats (HeroStartingStatsV2):
        item_slot_info (HeroV2ItemSlotInfo):
        physics (HeroPhysicsV2):
        colors (HeroColorsV2):
        shop_stat_display (HeroShopStatDisplayV2):
        stats_display (RawHeroStatsDisplayV2):
        hero_stats_ui (RawHeroStatsUIV2):
        level_info (HeroV2LevelInfo):
        scaling_stats (HeroV2ScalingStats):
        purchase_bonuses (HeroV2PurchaseBonuses):
        standard_level_up_upgrades (HeroV2StandardLevelUpUpgrades):
        recommended_upgrades (Union[None, Unset, list[str]]):
        recommended_ability_order (Union[None, Unset, list[str]]):
        tags (Union[None, Unset, list[str]]):
        gun_tag (Union[None, Unset, str]):
        hideout_rich_presence (Union[None, Unset, str]):
        hero_type (Union[HeroTypeV2, None, Unset]):
        prerelease_only (Union[None, Unset, bool]):
        cost_bonuses (Union['HeroV2CostBonusesType0', None, Unset]):
    """

    id: int
    class_name: str
    name: str
    description: "HeroDescriptionV2"
    player_selectable: bool
    disabled: bool
    in_development: bool
    needs_testing: bool
    assigned_players_only: bool
    limited_testing: bool
    complexity: int
    skin: int
    images: "HeroImagesV2"
    items: "HeroV2Items"
    starting_stats: "HeroStartingStatsV2"
    item_slot_info: "HeroV2ItemSlotInfo"
    physics: "HeroPhysicsV2"
    colors: "HeroColorsV2"
    shop_stat_display: "HeroShopStatDisplayV2"
    stats_display: "RawHeroStatsDisplayV2"
    hero_stats_ui: "RawHeroStatsUIV2"
    level_info: "HeroV2LevelInfo"
    scaling_stats: "HeroV2ScalingStats"
    purchase_bonuses: "HeroV2PurchaseBonuses"
    standard_level_up_upgrades: "HeroV2StandardLevelUpUpgrades"
    recommended_upgrades: Union[None, Unset, list[str]] = UNSET
    recommended_ability_order: Union[None, Unset, list[str]] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    gun_tag: Union[None, Unset, str] = UNSET
    hideout_rich_presence: Union[None, Unset, str] = UNSET
    hero_type: Union[HeroTypeV2, None, Unset] = UNSET
    prerelease_only: Union[None, Unset, bool] = UNSET
    cost_bonuses: Union["HeroV2CostBonusesType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hero_v2_cost_bonuses_type_0 import HeroV2CostBonusesType0

        id = self.id

        class_name = self.class_name

        name = self.name

        description = self.description.to_dict()

        player_selectable = self.player_selectable

        disabled = self.disabled

        in_development = self.in_development

        needs_testing = self.needs_testing

        assigned_players_only = self.assigned_players_only

        limited_testing = self.limited_testing

        complexity = self.complexity

        skin = self.skin

        images = self.images.to_dict()

        items = self.items.to_dict()

        starting_stats = self.starting_stats.to_dict()

        item_slot_info = self.item_slot_info.to_dict()

        physics = self.physics.to_dict()

        colors = self.colors.to_dict()

        shop_stat_display = self.shop_stat_display.to_dict()

        stats_display = self.stats_display.to_dict()

        hero_stats_ui = self.hero_stats_ui.to_dict()

        level_info = self.level_info.to_dict()

        scaling_stats = self.scaling_stats.to_dict()

        purchase_bonuses = self.purchase_bonuses.to_dict()

        standard_level_up_upgrades = self.standard_level_up_upgrades.to_dict()

        recommended_upgrades: Union[None, Unset, list[str]]
        if isinstance(self.recommended_upgrades, Unset):
            recommended_upgrades = UNSET
        elif isinstance(self.recommended_upgrades, list):
            recommended_upgrades = self.recommended_upgrades

        else:
            recommended_upgrades = self.recommended_upgrades

        recommended_ability_order: Union[None, Unset, list[str]]
        if isinstance(self.recommended_ability_order, Unset):
            recommended_ability_order = UNSET
        elif isinstance(self.recommended_ability_order, list):
            recommended_ability_order = self.recommended_ability_order

        else:
            recommended_ability_order = self.recommended_ability_order

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        gun_tag: Union[None, Unset, str]
        if isinstance(self.gun_tag, Unset):
            gun_tag = UNSET
        else:
            gun_tag = self.gun_tag

        hideout_rich_presence: Union[None, Unset, str]
        if isinstance(self.hideout_rich_presence, Unset):
            hideout_rich_presence = UNSET
        else:
            hideout_rich_presence = self.hideout_rich_presence

        hero_type: Union[None, Unset, str]
        if isinstance(self.hero_type, Unset):
            hero_type = UNSET
        elif isinstance(self.hero_type, HeroTypeV2):
            hero_type = self.hero_type.value
        else:
            hero_type = self.hero_type

        prerelease_only: Union[None, Unset, bool]
        if isinstance(self.prerelease_only, Unset):
            prerelease_only = UNSET
        else:
            prerelease_only = self.prerelease_only

        cost_bonuses: Union[None, Unset, dict[str, Any]]
        if isinstance(self.cost_bonuses, Unset):
            cost_bonuses = UNSET
        elif isinstance(self.cost_bonuses, HeroV2CostBonusesType0):
            cost_bonuses = self.cost_bonuses.to_dict()
        else:
            cost_bonuses = self.cost_bonuses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "class_name": class_name,
                "name": name,
                "description": description,
                "player_selectable": player_selectable,
                "disabled": disabled,
                "in_development": in_development,
                "needs_testing": needs_testing,
                "assigned_players_only": assigned_players_only,
                "limited_testing": limited_testing,
                "complexity": complexity,
                "skin": skin,
                "images": images,
                "items": items,
                "starting_stats": starting_stats,
                "item_slot_info": item_slot_info,
                "physics": physics,
                "colors": colors,
                "shop_stat_display": shop_stat_display,
                "stats_display": stats_display,
                "hero_stats_ui": hero_stats_ui,
                "level_info": level_info,
                "scaling_stats": scaling_stats,
                "purchase_bonuses": purchase_bonuses,
                "standard_level_up_upgrades": standard_level_up_upgrades,
            }
        )
        if recommended_upgrades is not UNSET:
            field_dict["recommended_upgrades"] = recommended_upgrades
        if recommended_ability_order is not UNSET:
            field_dict["recommended_ability_order"] = recommended_ability_order
        if tags is not UNSET:
            field_dict["tags"] = tags
        if gun_tag is not UNSET:
            field_dict["gun_tag"] = gun_tag
        if hideout_rich_presence is not UNSET:
            field_dict["hideout_rich_presence"] = hideout_rich_presence
        if hero_type is not UNSET:
            field_dict["hero_type"] = hero_type
        if prerelease_only is not UNSET:
            field_dict["prerelease_only"] = prerelease_only
        if cost_bonuses is not UNSET:
            field_dict["cost_bonuses"] = cost_bonuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hero_colors_v2 import HeroColorsV2
        from ..models.hero_description_v2 import HeroDescriptionV2
        from ..models.hero_images_v2 import HeroImagesV2
        from ..models.hero_physics_v2 import HeroPhysicsV2
        from ..models.hero_shop_stat_display_v2 import HeroShopStatDisplayV2
        from ..models.hero_starting_stats_v2 import HeroStartingStatsV2
        from ..models.hero_v2_cost_bonuses_type_0 import HeroV2CostBonusesType0
        from ..models.hero_v2_item_slot_info import HeroV2ItemSlotInfo
        from ..models.hero_v2_items import HeroV2Items
        from ..models.hero_v2_level_info import HeroV2LevelInfo
        from ..models.hero_v2_purchase_bonuses import HeroV2PurchaseBonuses
        from ..models.hero_v2_scaling_stats import HeroV2ScalingStats
        from ..models.hero_v2_standard_level_up_upgrades import HeroV2StandardLevelUpUpgrades
        from ..models.raw_hero_stats_display_v2 import RawHeroStatsDisplayV2
        from ..models.raw_hero_stats_uiv2 import RawHeroStatsUIV2

        d = dict(src_dict)
        id = d.pop("id")

        class_name = d.pop("class_name")

        name = d.pop("name")

        description = HeroDescriptionV2.from_dict(d.pop("description"))

        player_selectable = d.pop("player_selectable")

        disabled = d.pop("disabled")

        in_development = d.pop("in_development")

        needs_testing = d.pop("needs_testing")

        assigned_players_only = d.pop("assigned_players_only")

        limited_testing = d.pop("limited_testing")

        complexity = d.pop("complexity")

        skin = d.pop("skin")

        images = HeroImagesV2.from_dict(d.pop("images"))

        items = HeroV2Items.from_dict(d.pop("items"))

        starting_stats = HeroStartingStatsV2.from_dict(d.pop("starting_stats"))

        item_slot_info = HeroV2ItemSlotInfo.from_dict(d.pop("item_slot_info"))

        physics = HeroPhysicsV2.from_dict(d.pop("physics"))

        colors = HeroColorsV2.from_dict(d.pop("colors"))

        shop_stat_display = HeroShopStatDisplayV2.from_dict(d.pop("shop_stat_display"))

        stats_display = RawHeroStatsDisplayV2.from_dict(d.pop("stats_display"))

        hero_stats_ui = RawHeroStatsUIV2.from_dict(d.pop("hero_stats_ui"))

        level_info = HeroV2LevelInfo.from_dict(d.pop("level_info"))

        scaling_stats = HeroV2ScalingStats.from_dict(d.pop("scaling_stats"))

        purchase_bonuses = HeroV2PurchaseBonuses.from_dict(d.pop("purchase_bonuses"))

        standard_level_up_upgrades = HeroV2StandardLevelUpUpgrades.from_dict(d.pop("standard_level_up_upgrades"))

        def _parse_recommended_upgrades(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recommended_upgrades_type_0 = cast(list[str], data)

                return recommended_upgrades_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        recommended_upgrades = _parse_recommended_upgrades(d.pop("recommended_upgrades", UNSET))

        def _parse_recommended_ability_order(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recommended_ability_order_type_0 = cast(list[str], data)

                return recommended_ability_order_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        recommended_ability_order = _parse_recommended_ability_order(d.pop("recommended_ability_order", UNSET))

        def _parse_tags(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_gun_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        gun_tag = _parse_gun_tag(d.pop("gun_tag", UNSET))

        def _parse_hideout_rich_presence(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hideout_rich_presence = _parse_hideout_rich_presence(d.pop("hideout_rich_presence", UNSET))

        def _parse_hero_type(data: object) -> Union[HeroTypeV2, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hero_type_type_0 = HeroTypeV2(data)

                return hero_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[HeroTypeV2, None, Unset], data)

        hero_type = _parse_hero_type(d.pop("hero_type", UNSET))

        def _parse_prerelease_only(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        prerelease_only = _parse_prerelease_only(d.pop("prerelease_only", UNSET))

        def _parse_cost_bonuses(data: object) -> Union["HeroV2CostBonusesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cost_bonuses_type_0 = HeroV2CostBonusesType0.from_dict(data)

                return cost_bonuses_type_0
            except:  # noqa: E722
                pass
            return cast(Union["HeroV2CostBonusesType0", None, Unset], data)

        cost_bonuses = _parse_cost_bonuses(d.pop("cost_bonuses", UNSET))

        hero_v2 = cls(
            id=id,
            class_name=class_name,
            name=name,
            description=description,
            player_selectable=player_selectable,
            disabled=disabled,
            in_development=in_development,
            needs_testing=needs_testing,
            assigned_players_only=assigned_players_only,
            limited_testing=limited_testing,
            complexity=complexity,
            skin=skin,
            images=images,
            items=items,
            starting_stats=starting_stats,
            item_slot_info=item_slot_info,
            physics=physics,
            colors=colors,
            shop_stat_display=shop_stat_display,
            stats_display=stats_display,
            hero_stats_ui=hero_stats_ui,
            level_info=level_info,
            scaling_stats=scaling_stats,
            purchase_bonuses=purchase_bonuses,
            standard_level_up_upgrades=standard_level_up_upgrades,
            recommended_upgrades=recommended_upgrades,
            recommended_ability_order=recommended_ability_order,
            tags=tags,
            gun_tag=gun_tag,
            hideout_rich_presence=hideout_rich_presence,
            hero_type=hero_type,
            prerelease_only=prerelease_only,
            cost_bonuses=cost_bonuses,
        )

        hero_v2.additional_properties = d
        return hero_v2

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
