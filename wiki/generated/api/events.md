# Generated Event Reference

> Snapshot generated from the RelicPrison 1.0.0 public event API before the implementation repository was made private.

## RelicAutoSellEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicAutoSellEvent(UUID playerId, BigDecimal baseValue, BigDecimal finalValue)
```

## RelicBoosterActivateEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicBoosterActivateEvent(String boosterId, UUID owner, BigDecimal multiplier, long expiresAt)
```

## RelicBoosterExpireEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicBoosterExpireEvent(String boosterId, UUID owner)
```

## RelicMineBlockProcessEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicMineBlockProcessEvent(UUID playerId, String mineId, BlockPosition position, String source)
```

## RelicMineCreatedEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicMineCreatedEvent(MineView mine)
```

## RelicMineCreateEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicMineCreateEvent(MineView mine)
```

## RelicMineDeletedEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicMineDeletedEvent(MineView mine)
```

## RelicMineDeleteEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicMineDeleteEvent(MineView mine)
```

## RelicMineResetCompleteEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicMineResetCompleteEvent(String mineId, String reason, long totalBlocks, long durationMillis)
```

## RelicMineResetFailEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicMineResetFailEvent(String mineId, String reason, String error)
```

## RelicMineResetPrepareEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicMineResetPrepareEvent(String mineId, String reason)
```

## RelicMineResetStartEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicMineResetStartEvent(String mineId, String reason, long totalBlocks)
```

## RelicMineUpdatedEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicMineUpdatedEvent(MineView previous, MineView current)
```

## RelicMineUpdateEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicMineUpdateEvent(MineView previous, MineView proposed)
```

## RelicPlayerDataLoadEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicPlayerDataLoadEvent(PlayerProfileView profile)
```

## RelicPlayerPrestigeEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicPlayerPrestigeEvent(UUID playerId, String oldPrestige, String newPrestige, BigDecimal cost)
```

## RelicPlayerProgressionRepairEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicPlayerProgressionRepairEvent(UUID playerId, String lastKnownPlayerName, Set<String> previousDirectRankGroups, Set<String> previousDirectPrestigeGroups, String expectedRank, String expectedPrestige, List<String> repairsPerformed, String repairReason, boolean automatic)
```

## RelicPlayerRankUpEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicPlayerRankUpEvent(UUID playerId, String oldRank, String newRank, BigDecimal cost)
```

## RelicSellEvent

_Public API signature snapshot from RelicPrison 1.0.0._

```java
public RelicSellEvent(UUID playerId, BigDecimal baseValue, BigDecimal finalValue)
```

