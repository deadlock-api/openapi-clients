# assets-deadlock-api-client.model.MapV1

## Load the model package
```dart
import 'package:assets-deadlock-api-client/api.dart';
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**radius** | **int** | The radius of the map. | [optional] [default to 10752]
**images** | [**MapImagesV1**](MapImagesV1.md) | The images of the map. | 
**objectivePositions** | [**ObjectivePositionsV1**](ObjectivePositionsV1.md) |  | [readonly] 
**ziplinePaths** | [**List<ZiplanePathV1>**](ZiplanePathV1.md) | The ziplane paths of the map. Each path is a list of P0, P1, and P2 points, describing the cubic spline. | [default to const []]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


