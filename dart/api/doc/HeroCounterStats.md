# deadlock-api-client.model.HeroCounterStats

## Load the model package
```dart
import 'package:deadlock-api-client/api.dart';
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists** | **int** | The number of assists by `hero_id` when facing `enemy_hero_id`. | 
**creeps** | **int** | The number of creeps killed by `hero_id` when facing `enemy_hero_id`. | 
**deaths** | **int** | The number of deaths by `hero_id` when facing `enemy_hero_id`. | 
**denies** | **int** | The number of denies by `hero_id` when facing `enemy_hero_id`. | 
**enemyAssists** | **int** | The number of assists by `enemy_hero_id` when facing `hero_id`. | 
**enemyCreeps** | **int** | The number of creeps killed by `enemy_hero_id` when facing `hero_id`. | 
**enemyDeaths** | **int** | The number of deaths by `enemy_hero_id` when facing `hero_id`. | 
**enemyDenies** | **int** | The number of denies by `enemy_hero_id` when facing `hero_id`. | 
**enemyHeroId** | **int** | The ID of the opposing hero. See more: <https://assets.deadlock-api.com/v2/heroes> | 
**enemyKills** | **int** | The number of kills by `enemy_hero_id` when facing `hero_id`. | 
**enemyLastHits** | **int** | The number of last hits by `enemy_hero_id` when facing `hero_id`. | 
**enemyNetworth** | **int** | The net worth of `enemy_hero_id` when facing `hero_id`. | 
**enemyObjDamage** | **int** | The amount of objective damage dealt by `enemy_hero_id` when facing `hero_id`. | 
**heroId** | **int** | The ID of the hero. See more: <https://assets.deadlock-api.com/v2/heroes> | 
**kills** | **int** | The number of kills by `hero_id` when facing `enemy_hero_id`. | 
**lastHits** | **int** | The number of last hits by `hero_id` when facing `enemy_hero_id`. | 
**matchesPlayed** | **int** | The total number of matches played between `hero_id` and `enemy_hero_id` that meet the filter criteria. | 
**networth** | **int** | The net worth of `hero_id` when facing `enemy_hero_id`. | 
**objDamage** | **int** | The amount of objective damage dealt by `hero_id` when facing `enemy_hero_id`. | 
**wins** | **int** | The number of times `hero_id` won the match when facing `enemy_hero_id`. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


