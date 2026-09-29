# Modifier

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **string** | Entry this one inherits from (&#x60;_base&#x60;). | [optional]
**class** | **string** | Engine class (&#x60;_class&#x60;), e.g. &#x60;citadel_neutral_laser_beam&#x60;. | [optional]
**class_name** | **string** |  |
**folder** | **string** | Editor folder (&#x60;_editor.folder_name&#x60;), e.g. &#x60;Neutral Ability&#x60;. | [optional]
**id** | **int** |  |
**properties** | **array<string,float>** | Numeric properties keyed by their source name. Nested properties use a dotted path (&#x60;m_GroundAuraModifier.m_modifierProvidedByAura.m_flDPS&#x60;, &#x60;subclass:&#x60; wrappers are skipped); &#x60;m_vecScriptValues&#x60; entries are keyed by their &#x60;m_eModifierValue&#x60; (&#x60;MODIFIER_VALUE_GRAVITY_SCALE&#x60;). |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
