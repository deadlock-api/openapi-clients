# IngestLiveUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broadcast_url** | **str** |  | 
**lobby_id** | **int** |  | [optional] 
**match_id** | **int** |  | 
**started_at** | **int** |  | [optional] 

## Example

```python
from deadlock_api_client.models.ingest_live_url import IngestLiveUrl

# TODO update the JSON string below
json = "{}"
# create an instance of IngestLiveUrl from a JSON string
ingest_live_url_instance = IngestLiveUrl.from_json(json)
# print the JSON string representation of the object
print(IngestLiveUrl.to_json())

# convert the object into a dict
ingest_live_url_dict = ingest_live_url_instance.to_dict()
# create an instance of IngestLiveUrl from a dict
ingest_live_url_from_dict = IngestLiveUrl.from_dict(ingest_live_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


