# # MMRHistory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  |
**division** | **int** | Extracted from the rank the division (rank // 10) |
**division_tier** | **int** | Extracted from the rank the division tier (rank % 10) |
**match_id** | **int** |  |
**player_score** | **float** | Player Score is the index for the rank array (internally used for the rank regression) |
**rank** | **int** | The Player Rank (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; |
**start_time** | **int** | Start time of the match |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
