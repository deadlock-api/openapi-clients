# DeadlockApiClient.Model.RankInfo
One `m_vecRankInfo` entry of the game file (build 6857+), as listed there.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BadgeShields** | **int** | Losses a player at a badge&#39;s first subrank with 0 rank points can take before dropping a badge (rank loss protection shields). | [optional] 
**RankEnd** | **int** | Rank badge (tier * 10 + subrank) the entry stops at: it covers the ranks below it. In Beta Season 2, 91 (Phantom I) gives every rank below Phantom shields and Phantom and up none. | [optional] 
**SubRankShields** | **int** | Losses a player can take before dropping a subrank (rank loss protection shields). | [optional] 
**SubRankXp** | **List&lt;int&gt;** | Rank points needed per subrank step, the last one being the step to the next badge (Beta Season 2: 1000 between subranks, 1500 from the final subrank). | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

