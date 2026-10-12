# DeadlockApiClient.Model.HeroSwapStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Bucket** | **int** | The bucket value (depends on the bucket query parameter). | 
**HeroId** | **int** | The ID of the hero. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**Matches** | **long** | The number of players who played this hero, counting only players whose pre-game hero is known. | 
**PregamePicks** | **long** | The number of players who had this hero locked before the pre-game swap window. | 
**SwappedAway** | **long** | The number of &#x60;pregame_picks&#x60; players who swapped away from this hero. | 
**SwappedIn** | **long** | The number of players who played this hero after swapping to it from another pre-game hero. | 
**SwappedInWins** | **long** | The number of &#x60;swapped_in&#x60; players who won the match. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

