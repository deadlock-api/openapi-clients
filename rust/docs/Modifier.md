# Modifier

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | Option<**String**> | Entry this one inherits from (`_base`). | [optional]
**class** | Option<**String**> | Engine class (`_class`), e.g. `citadel_neutral_laser_beam`. | [optional]
**class_name** | **String** |  | 
**folder** | Option<**String**> | Editor folder (`_editor.folder_name`), e.g. `Neutral Ability`. | [optional]
**id** | **u32** |  | 
**properties** | **std::collections::HashMap<String, f64>** | Numeric properties keyed by their source name. Nested properties use a dotted path (`m_GroundAuraModifier.m_modifierProvidedByAura.m_flDPS`, `subclass:` wrappers are skipped); `m_vecScriptValues` entries are keyed by their `m_eModifierValue` (`MODIFIER_VALUE_GRAVITY_SCALE`). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


