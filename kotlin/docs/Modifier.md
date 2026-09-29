
# Modifier

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **className** | **kotlin.String** |  |  |
| **id** | **kotlin.Int** |  |  |
| **properties** | **kotlin.collections.Map&lt;kotlin.String, kotlin.Double&gt;** | Numeric properties keyed by their source name. Nested properties use a dotted path (&#x60;m_GroundAuraModifier.m_modifierProvidedByAura.m_flDPS&#x60;, &#x60;subclass:&#x60; wrappers are skipped); &#x60;m_vecScriptValues&#x60; entries are keyed by their &#x60;m_eModifierValue&#x60; (&#x60;MODIFIER_VALUE_GRAVITY_SCALE&#x60;). |  |
| **base** | **kotlin.String** | Entry this one inherits from (&#x60;_base&#x60;). |  [optional] |
| **propertyClass** | **kotlin.String** | Engine class (&#x60;_class&#x60;), e.g. &#x60;citadel_neutral_laser_beam&#x60;. |  [optional] |
| **folder** | **kotlin.String** | Editor folder (&#x60;_editor.folder_name&#x60;), e.g. &#x60;Neutral Ability&#x60;. |  [optional] |



