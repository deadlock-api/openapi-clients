# PlayerEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  |
**badge** | **int** | &#x60;rank&#x60; and &#x60;peak_rank&#x60; sorts only: the rank badge the progress in &#x60;value&#x60; falls in, &#x60;0&#x60; when the player has no ranked match in range. Omitted for every other sort. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional]
**badge_progress** | **int** | &#x60;rank&#x60; and &#x60;peak_rank&#x60; sorts only: progress points into &#x60;badge&#x60;. A subrank spans 1000 points, the sixth of a tier 2000. &#x60;null&#x60; in Eternus, whose subranks are percentile cuts rather than point spans, and when the player has no ranked match in range. | [optional]
**matches** | **int** |  |
**rank** | **int** |  |
**value** | **float** |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
