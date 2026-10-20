
# HeroBanStats

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **bans** | **kotlin.Long** | The number of matches in which this hero was banned. |  |
| **bucket** | **kotlin.Int** | The bucket value (depends on the bucket query parameter). |  |
| **heroId** | **kotlin.Int** | The ID of the banned hero. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; |  |
| **matches** | **kotlin.Long** | The number of matches with ban data in this bucket. A hero&#39;s ban rate is &#x60;bans / matches&#x60;; a ranked match has 3 bans and an unranked match 2, so the bans of all heroes do not divide into matches by a fixed count. |  |



