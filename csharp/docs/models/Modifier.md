# DeadlockApiClient.Model.Modifier

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClassName** | **string** |  | 
**Id** | **int** |  | 
**Properties** | **Dictionary&lt;string, double&gt;** | Numeric properties keyed by their source name. Nested properties use a dotted path (&#x60;m_GroundAuraModifier.m_modifierProvidedByAura.m_flDPS&#x60;, &#x60;subclass:&#x60; wrappers are skipped); &#x60;m_vecScriptValues&#x60; entries are keyed by their &#x60;m_eModifierValue&#x60; (&#x60;MODIFIER_VALUE_GRAVITY_SCALE&#x60;). | 
**Base** | **string** | Entry this one inherits from (&#x60;_base&#x60;). | [optional] 
**Class** | **string** | Engine class (&#x60;_class&#x60;), e.g. &#x60;citadel_neutral_laser_beam&#x60;. | [optional] 
**Folder** | **string** | Editor folder (&#x60;_editor.folder_name&#x60;), e.g. &#x60;Neutral Ability&#x60;. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

