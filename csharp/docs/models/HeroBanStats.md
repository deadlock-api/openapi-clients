# DeadlockApiClient.Model.HeroBanStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Bans** | **long** | The number of matches in which this hero was banned. | 
**Bucket** | **int** | The bucket value (depends on the bucket query parameter). | 
**HeroId** | **int** | The ID of the banned hero. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**Matches** | **long** | The number of matches with ban data in this bucket. A hero&#39;s ban rate is &#x60;bans / matches&#x60;; a ranked match has 3 bans and an unranked match 2, so the bans of all heroes do not divide into matches by a fixed count. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

