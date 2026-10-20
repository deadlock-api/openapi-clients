# HeroBanStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bans** | **int** | The number of matches in which this hero was banned. |
**bucket** | **int** | The bucket value (depends on the bucket query parameter). |
**hero_id** | **int** | The ID of the banned hero. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; |
**matches** | **int** | The number of matches with ban data in this bucket. A hero&#39;s ban rate is &#x60;bans / matches&#x60;; a ranked match has 3 bans and an unranked match 2, so the bans of all heroes do not divide into matches by a fixed count. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
