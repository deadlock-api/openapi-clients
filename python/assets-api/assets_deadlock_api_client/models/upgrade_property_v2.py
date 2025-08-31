from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.raw_ability_section_type_v2 import RawAbilitySectionTypeV2
from ..models.stats_usage_flag_v2 import StatsUsageFlagV2
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.raw_item_property_scale_function_subclass_v2 import RawItemPropertyScaleFunctionSubclassV2


T = TypeVar("T", bound="UpgradePropertyV2")


@_attrs_define
class UpgradePropertyV2:
    """
    Attributes:
        value (Union[None, Unset, float, str]):
        can_set_token_override (Union[None, Unset, bool]):
        provided_property_type (Union[None, Unset, str]):
        css_class (Union[None, Unset, str]):
        usage_flags (Union[None, Unset, list[StatsUsageFlagV2], str]):
        negative_attribute (Union[None, Unset, bool]):
        disable_value (Union[None, Unset, str]):
        loc_token_override (Union[None, Unset, str]):
        display_units (Union[None, Unset, str]):
        icon_path (Union[None, Unset, str]):
        scale_function (Union['RawItemPropertyScaleFunctionSubclassV2', None, Unset]):
        prefix (Union[None, Unset, str]):
        label (Union[None, Unset, str]):
        postfix (Union[None, Unset, str]):
        postvalue_label (Union[None, Unset, str]):
        conditional (Union[None, Unset, str]):
        icon (Union[None, Unset, str]):
        tooltip_section (Union[None, RawAbilitySectionTypeV2, Unset]):
        tooltip_is_elevated (Union[None, Unset, bool]):
        tooltip_is_important (Union[None, Unset, bool]):
    """

    value: Union[None, Unset, float, str] = UNSET
    can_set_token_override: Union[None, Unset, bool] = UNSET
    provided_property_type: Union[None, Unset, str] = UNSET
    css_class: Union[None, Unset, str] = UNSET
    usage_flags: Union[None, Unset, list[StatsUsageFlagV2], str] = UNSET
    negative_attribute: Union[None, Unset, bool] = UNSET
    disable_value: Union[None, Unset, str] = UNSET
    loc_token_override: Union[None, Unset, str] = UNSET
    display_units: Union[None, Unset, str] = UNSET
    icon_path: Union[None, Unset, str] = UNSET
    scale_function: Union["RawItemPropertyScaleFunctionSubclassV2", None, Unset] = UNSET
    prefix: Union[None, Unset, str] = UNSET
    label: Union[None, Unset, str] = UNSET
    postfix: Union[None, Unset, str] = UNSET
    postvalue_label: Union[None, Unset, str] = UNSET
    conditional: Union[None, Unset, str] = UNSET
    icon: Union[None, Unset, str] = UNSET
    tooltip_section: Union[None, RawAbilitySectionTypeV2, Unset] = UNSET
    tooltip_is_elevated: Union[None, Unset, bool] = UNSET
    tooltip_is_important: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.raw_item_property_scale_function_subclass_v2 import RawItemPropertyScaleFunctionSubclassV2

        value: Union[None, Unset, float, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        can_set_token_override: Union[None, Unset, bool]
        if isinstance(self.can_set_token_override, Unset):
            can_set_token_override = UNSET
        else:
            can_set_token_override = self.can_set_token_override

        provided_property_type: Union[None, Unset, str]
        if isinstance(self.provided_property_type, Unset):
            provided_property_type = UNSET
        else:
            provided_property_type = self.provided_property_type

        css_class: Union[None, Unset, str]
        if isinstance(self.css_class, Unset):
            css_class = UNSET
        else:
            css_class = self.css_class

        usage_flags: Union[None, Unset, list[str], str]
        if isinstance(self.usage_flags, Unset):
            usage_flags = UNSET
        elif isinstance(self.usage_flags, list):
            usage_flags = []
            for usage_flags_type_0_item_data in self.usage_flags:
                usage_flags_type_0_item = usage_flags_type_0_item_data.value
                usage_flags.append(usage_flags_type_0_item)

        else:
            usage_flags = self.usage_flags

        negative_attribute: Union[None, Unset, bool]
        if isinstance(self.negative_attribute, Unset):
            negative_attribute = UNSET
        else:
            negative_attribute = self.negative_attribute

        disable_value: Union[None, Unset, str]
        if isinstance(self.disable_value, Unset):
            disable_value = UNSET
        else:
            disable_value = self.disable_value

        loc_token_override: Union[None, Unset, str]
        if isinstance(self.loc_token_override, Unset):
            loc_token_override = UNSET
        else:
            loc_token_override = self.loc_token_override

        display_units: Union[None, Unset, str]
        if isinstance(self.display_units, Unset):
            display_units = UNSET
        else:
            display_units = self.display_units

        icon_path: Union[None, Unset, str]
        if isinstance(self.icon_path, Unset):
            icon_path = UNSET
        else:
            icon_path = self.icon_path

        scale_function: Union[None, Unset, dict[str, Any]]
        if isinstance(self.scale_function, Unset):
            scale_function = UNSET
        elif isinstance(self.scale_function, RawItemPropertyScaleFunctionSubclassV2):
            scale_function = self.scale_function.to_dict()
        else:
            scale_function = self.scale_function

        prefix: Union[None, Unset, str]
        if isinstance(self.prefix, Unset):
            prefix = UNSET
        else:
            prefix = self.prefix

        label: Union[None, Unset, str]
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        postfix: Union[None, Unset, str]
        if isinstance(self.postfix, Unset):
            postfix = UNSET
        else:
            postfix = self.postfix

        postvalue_label: Union[None, Unset, str]
        if isinstance(self.postvalue_label, Unset):
            postvalue_label = UNSET
        else:
            postvalue_label = self.postvalue_label

        conditional: Union[None, Unset, str]
        if isinstance(self.conditional, Unset):
            conditional = UNSET
        else:
            conditional = self.conditional

        icon: Union[None, Unset, str]
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        tooltip_section: Union[None, Unset, str]
        if isinstance(self.tooltip_section, Unset):
            tooltip_section = UNSET
        elif isinstance(self.tooltip_section, RawAbilitySectionTypeV2):
            tooltip_section = self.tooltip_section.value
        else:
            tooltip_section = self.tooltip_section

        tooltip_is_elevated: Union[None, Unset, bool]
        if isinstance(self.tooltip_is_elevated, Unset):
            tooltip_is_elevated = UNSET
        else:
            tooltip_is_elevated = self.tooltip_is_elevated

        tooltip_is_important: Union[None, Unset, bool]
        if isinstance(self.tooltip_is_important, Unset):
            tooltip_is_important = UNSET
        else:
            tooltip_is_important = self.tooltip_is_important

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if can_set_token_override is not UNSET:
            field_dict["can_set_token_override"] = can_set_token_override
        if provided_property_type is not UNSET:
            field_dict["provided_property_type"] = provided_property_type
        if css_class is not UNSET:
            field_dict["css_class"] = css_class
        if usage_flags is not UNSET:
            field_dict["usage_flags"] = usage_flags
        if negative_attribute is not UNSET:
            field_dict["negative_attribute"] = negative_attribute
        if disable_value is not UNSET:
            field_dict["disable_value"] = disable_value
        if loc_token_override is not UNSET:
            field_dict["loc_token_override"] = loc_token_override
        if display_units is not UNSET:
            field_dict["display_units"] = display_units
        if icon_path is not UNSET:
            field_dict["icon_path"] = icon_path
        if scale_function is not UNSET:
            field_dict["scale_function"] = scale_function
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if label is not UNSET:
            field_dict["label"] = label
        if postfix is not UNSET:
            field_dict["postfix"] = postfix
        if postvalue_label is not UNSET:
            field_dict["postvalue_label"] = postvalue_label
        if conditional is not UNSET:
            field_dict["conditional"] = conditional
        if icon is not UNSET:
            field_dict["icon"] = icon
        if tooltip_section is not UNSET:
            field_dict["tooltip_section"] = tooltip_section
        if tooltip_is_elevated is not UNSET:
            field_dict["tooltip_is_elevated"] = tooltip_is_elevated
        if tooltip_is_important is not UNSET:
            field_dict["tooltip_is_important"] = tooltip_is_important

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_item_property_scale_function_subclass_v2 import RawItemPropertyScaleFunctionSubclassV2

        d = dict(src_dict)

        def _parse_value(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_can_set_token_override(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        can_set_token_override = _parse_can_set_token_override(d.pop("can_set_token_override", UNSET))

        def _parse_provided_property_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provided_property_type = _parse_provided_property_type(d.pop("provided_property_type", UNSET))

        def _parse_css_class(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        css_class = _parse_css_class(d.pop("css_class", UNSET))

        def _parse_usage_flags(data: object) -> Union[None, Unset, list[StatsUsageFlagV2], str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                usage_flags_type_0 = []
                _usage_flags_type_0 = data
                for usage_flags_type_0_item_data in _usage_flags_type_0:
                    usage_flags_type_0_item = StatsUsageFlagV2(usage_flags_type_0_item_data)

                    usage_flags_type_0.append(usage_flags_type_0_item)

                return usage_flags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[StatsUsageFlagV2], str], data)

        usage_flags = _parse_usage_flags(d.pop("usage_flags", UNSET))

        def _parse_negative_attribute(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        negative_attribute = _parse_negative_attribute(d.pop("negative_attribute", UNSET))

        def _parse_disable_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        disable_value = _parse_disable_value(d.pop("disable_value", UNSET))

        def _parse_loc_token_override(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        loc_token_override = _parse_loc_token_override(d.pop("loc_token_override", UNSET))

        def _parse_display_units(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_units = _parse_display_units(d.pop("display_units", UNSET))

        def _parse_icon_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon_path = _parse_icon_path(d.pop("icon_path", UNSET))

        def _parse_scale_function(data: object) -> Union["RawItemPropertyScaleFunctionSubclassV2", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scale_function_type_0 = RawItemPropertyScaleFunctionSubclassV2.from_dict(data)

                return scale_function_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RawItemPropertyScaleFunctionSubclassV2", None, Unset], data)

        scale_function = _parse_scale_function(d.pop("scale_function", UNSET))

        def _parse_prefix(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        prefix = _parse_prefix(d.pop("prefix", UNSET))

        def _parse_label(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_postfix(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postfix = _parse_postfix(d.pop("postfix", UNSET))

        def _parse_postvalue_label(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postvalue_label = _parse_postvalue_label(d.pop("postvalue_label", UNSET))

        def _parse_conditional(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        conditional = _parse_conditional(d.pop("conditional", UNSET))

        def _parse_icon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_tooltip_section(data: object) -> Union[None, RawAbilitySectionTypeV2, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tooltip_section_type_0 = RawAbilitySectionTypeV2(data)

                return tooltip_section_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, RawAbilitySectionTypeV2, Unset], data)

        tooltip_section = _parse_tooltip_section(d.pop("tooltip_section", UNSET))

        def _parse_tooltip_is_elevated(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        tooltip_is_elevated = _parse_tooltip_is_elevated(d.pop("tooltip_is_elevated", UNSET))

        def _parse_tooltip_is_important(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        tooltip_is_important = _parse_tooltip_is_important(d.pop("tooltip_is_important", UNSET))

        upgrade_property_v2 = cls(
            value=value,
            can_set_token_override=can_set_token_override,
            provided_property_type=provided_property_type,
            css_class=css_class,
            usage_flags=usage_flags,
            negative_attribute=negative_attribute,
            disable_value=disable_value,
            loc_token_override=loc_token_override,
            display_units=display_units,
            icon_path=icon_path,
            scale_function=scale_function,
            prefix=prefix,
            label=label,
            postfix=postfix,
            postvalue_label=postvalue_label,
            conditional=conditional,
            icon=icon,
            tooltip_section=tooltip_section,
            tooltip_is_elevated=tooltip_is_elevated,
            tooltip_is_important=tooltip_is_important,
        )

        upgrade_property_v2.additional_properties = d
        return upgrade_property_v2

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
