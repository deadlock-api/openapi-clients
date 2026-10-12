
# HeroSwapStats

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **bucket** | **kotlin.Int** | The bucket value (depends on the bucket query parameter). |  |
| **heroId** | **kotlin.Int** | The ID of the hero. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; |  |
| **matches** | **kotlin.Long** | The number of players who played this hero, counting only players whose pre-game hero is known. |  |
| **pregamePicks** | **kotlin.Long** | The number of players who had this hero locked before the pre-game swap window. |  |
| **swappedAway** | **kotlin.Long** | The number of &#x60;pregame_picks&#x60; players who swapped away from this hero. |  |
| **swappedIn** | **kotlin.Long** | The number of players who played this hero after swapping to it from another pre-game hero. |  |
| **swappedInWins** | **kotlin.Long** | The number of &#x60;swapped_in&#x60; players who won the match. |  |



