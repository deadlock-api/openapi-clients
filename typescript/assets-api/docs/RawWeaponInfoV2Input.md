# RawWeaponInfoV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_bCanZoom** | **boolean** |  | [optional] [default to undefined]
**m_flBulletDamage** | **number** |  | [optional] [default to undefined]
**m_flBulletGravityScale** | **number** |  | [optional] [default to undefined]
**m_flBulletInheritShooterVelocityScale** | **number** |  | [optional] [default to undefined]
**m_flBulletLifetime** | **number** |  | [optional] [default to undefined]
**m_flBulletRadius** | **number** |  | [optional] [default to undefined]
**m_flBulletRadiusVsWorld** | **number** |  | [optional] [default to undefined]
**m_flBulletReflectAmount** | **number** |  | [optional] [default to undefined]
**m_flBulletReflectScale** | **number** |  | [optional] [default to undefined]
**m_flBulletWhizDistance** | **number** |  | [optional] [default to undefined]
**m_flBurstShotCooldown** | **number** |  | [optional] [default to undefined]
**m_flCritBonusAgainstNpcs** | **number** |  | [optional] [default to undefined]
**m_flCritBonusEnd** | **number** |  | [optional] [default to undefined]
**m_flCritBonusEndRange** | **number** |  | [optional] [default to undefined]
**m_flCritBonusStart** | **number** |  | [optional] [default to undefined]
**m_flCritBonusStartRange** | **number** |  | [optional] [default to undefined]
**m_flCycleTime** | **number** |  | [optional] [default to undefined]
**m_flIntraBurstCycleTime** | **number** |  | [optional] [default to undefined]
**m_flMaxSpinCycleTime** | **number** |  | [optional] [default to undefined]
**m_flDamageFalloffBias** | **number** |  | [optional] [default to undefined]
**m_flDamageFalloffEndRange** | **number** |  | [optional] [default to undefined]
**m_flDamageFalloffEndScale** | **number** |  | [optional] [default to undefined]
**m_flDamageFalloffStartRange** | **number** |  | [optional] [default to undefined]
**m_flDamageFalloffStartScale** | **number** |  | [optional] [default to undefined]
**m_flHorizontalPunch** | **number** |  | [optional] [default to undefined]
**m_flRange** | **number** |  | [optional] [default to undefined]
**m_flRecoilRecoveryDelayFactor** | **number** |  | [optional] [default to undefined]
**m_flRecoilRecoverySpeed** | **number** |  | [optional] [default to undefined]
**m_flRecoilShotIndexRecoveryTimeFactor** | **number** |  | [optional] [default to undefined]
**m_flRecoilSpeed** | **number** |  | [optional] [default to undefined]
**m_flReloadMoveSpeed** | **number** |  | [optional] [default to undefined]
**m_flScatterYawScale** | **number** |  | [optional] [default to undefined]
**m_AimingShootSpreadPenalty** | [**MAimingshootspreadpenalty**](MAimingshootspreadpenalty.md) |  | [optional] [default to undefined]
**m_StandingShootSpreadPenalty** | [**MStandingshootspreadpenalty**](MStandingshootspreadpenalty.md) |  | [optional] [default to undefined]
**m_flShootMoveSpeedPercent** | **number** |  | [optional] [default to undefined]
**m_flShootSpreadPenaltyDecay** | **number** |  | [optional] [default to undefined]
**m_flShootSpreadPenaltyDecayDelay** | **number** |  | [optional] [default to undefined]
**m_flShootSpreadPenaltyPerShot** | **number** |  | [optional] [default to undefined]
**m_flShootingUpSpreadPenalty** | **number** |  | [optional] [default to undefined]
**m_flVerticalPunch** | **number** |  | [optional] [default to undefined]
**m_flZoomFov** | **number** |  | [optional] [default to undefined]
**m_flZoomMoveSpeedPercent** | **number** |  | [optional] [default to undefined]
**m_iBullets** | **number** |  | [optional] [default to undefined]
**m_iBurstShotCount** | **number** |  | [optional] [default to undefined]
**m_iClipSize** | **number** |  | [optional] [default to undefined]
**m_flSpread** | **number** |  | [optional] [default to undefined]
**m_flStandingSpread** | **number** |  | [optional] [default to undefined]
**m_flLowAmmoIndicatorThreshold** | **number** |  | [optional] [default to undefined]
**m_flRecoilSeed** | **number** |  | [optional] [default to undefined]
**m_flReloadDuration** | **number** |  | [optional] [default to undefined]
**m_BulletSpeedCurve** | [**RawItemWeaponInfoBulletSpeedCurveV2Input**](RawItemWeaponInfoBulletSpeedCurveV2Input.md) |  | [optional] [default to undefined]
**m_HorizontalRecoil** | [**RawWeaponInfoHorizontalRecoilV2Input**](RawWeaponInfoHorizontalRecoilV2Input.md) |  | [optional] [default to undefined]
**m_VerticalRecoil** | [**RawWeaponInfoVerticalRecoilV2Input**](RawWeaponInfoVerticalRecoilV2Input.md) |  | [optional] [default to undefined]

## Example

```typescript
import { RawWeaponInfoV2Input } from 'assets-deadlock-api-client';

const instance: RawWeaponInfoV2Input = {
    m_bCanZoom,
    m_flBulletDamage,
    m_flBulletGravityScale,
    m_flBulletInheritShooterVelocityScale,
    m_flBulletLifetime,
    m_flBulletRadius,
    m_flBulletRadiusVsWorld,
    m_flBulletReflectAmount,
    m_flBulletReflectScale,
    m_flBulletWhizDistance,
    m_flBurstShotCooldown,
    m_flCritBonusAgainstNpcs,
    m_flCritBonusEnd,
    m_flCritBonusEndRange,
    m_flCritBonusStart,
    m_flCritBonusStartRange,
    m_flCycleTime,
    m_flIntraBurstCycleTime,
    m_flMaxSpinCycleTime,
    m_flDamageFalloffBias,
    m_flDamageFalloffEndRange,
    m_flDamageFalloffEndScale,
    m_flDamageFalloffStartRange,
    m_flDamageFalloffStartScale,
    m_flHorizontalPunch,
    m_flRange,
    m_flRecoilRecoveryDelayFactor,
    m_flRecoilRecoverySpeed,
    m_flRecoilShotIndexRecoveryTimeFactor,
    m_flRecoilSpeed,
    m_flReloadMoveSpeed,
    m_flScatterYawScale,
    m_AimingShootSpreadPenalty,
    m_StandingShootSpreadPenalty,
    m_flShootMoveSpeedPercent,
    m_flShootSpreadPenaltyDecay,
    m_flShootSpreadPenaltyDecayDelay,
    m_flShootSpreadPenaltyPerShot,
    m_flShootingUpSpreadPenalty,
    m_flVerticalPunch,
    m_flZoomFov,
    m_flZoomMoveSpeedPercent,
    m_iBullets,
    m_iBurstShotCount,
    m_iClipSize,
    m_flSpread,
    m_flStandingSpread,
    m_flLowAmmoIndicatorThreshold,
    m_flRecoilSeed,
    m_flReloadDuration,
    m_BulletSpeedCurve,
    m_HorizontalRecoil,
    m_VerticalRecoil,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
