# Generated API Service Reference

> Snapshot generated from the RelicPrison 1.0.0 API before the implementation repository was made private. Threading guidance on the hand-written developer pages still takes precedence over guesswork.

## BackupService

_Public API signature snapshot from RelicPrison 1.0.0._

```java
CompletableFuture<BackupView> create(String type);
Collection<BackupView> backups();
```

## BoosterService

_Public API signature snapshot from RelicPrison 1.0.0._

```java
Collection<BoosterView> activeFor(UUID playerId);
Collection<BoosterView> activeServerBoosters();
```

## DiagnosticService

_Public API signature snapshot from RelicPrison 1.0.0._

```java
DiagnosticSnapshot snapshot();
```

## MineAccessService

_Public API signature snapshot from RelicPrison 1.0.0._

```java
boolean canEnter(UUID playerId, String mineId);
boolean canMine(UUID playerId, String mineId);
```

## MineResetService

_Public API signature snapshot from RelicPrison 1.0.0._

```java
Optional<MineResetState> state(String mineId);
boolean isResetting(String mineId);
boolean requestReset(String mineId, String reason, boolean warnings);
boolean cancelPendingReset(String mineId);
long remainingBlocks(String mineId);
long resetCount(String mineId);
long nextReset(String mineId);
double minedPercentage(String mineId);
```

## MineService

_Public API signature snapshot from RelicPrison 1.0.0._

```java
Optional<? extends MineView> findMine(String id);
Collection<? extends MineView> mines();
Optional<? extends MineView> mineAt(String worldName, int x, int y, int z);
Optional<? extends MineView> mineAt(UUID worldId, int x, int y, int z);
```

## MiningService

_Public API signature snapshot from RelicPrison 1.0.0._

```java
long processedBlocks();
long activeOperations();
```

## MultiplierService

_Public API signature snapshot from RelicPrison 1.0.0._

```java
BigDecimal multiplier(UUID playerId);
```

## NumberFormatService

_Public API signature snapshot from RelicPrison 1.0.0._

```java
String full(double value);
String plain(double value);
String full(BigDecimal value);
String plain(BigDecimal value);
String currency(double value);
String currency(BigDecimal value);
String abbreviatedCurrency(double value);
String abbreviatedCurrency(BigDecimal value);
String abbreviated(double value);
String progress(double fraction);
```

## PlayerDataService

_Public API signature snapshot from RelicPrison 1.0.0._

```java
Optional<PlayerProfileView> cached(UUID playerId);
CompletableFuture<PlayerProfileView> load(UUID playerId, String playerName);
```

## PrestigeService

_Public API signature snapshot from RelicPrison 1.0.0._

```java
Optional<PrestigeView> prestige(String id);
Collection<PrestigeView> prestiges();
```

## ProgressionService

_Public API signature snapshot from RelicPrison 1.0.0._

```java
Optional<String> currentRank(UUID playerId);
Optional<String> currentPrestige(UUID playerId);
CompletableFuture<ProgressionResult> rankUp(UUID playerId, boolean maximum);
CompletableFuture<ProgressionResult> prestige(UUID playerId);
CompletableFuture<Void> repair(UUID playerId);
```

## RankService

_Public API signature snapshot from RelicPrison 1.0.0._

```java
Optional<RankView> rank(String id);
Collection<RankView> ranks();
```

## RelicPrisonApi

_Public API signature snapshot from RelicPrison 1.0.0._

```java
MineService mines();
MineResetService resets();
MineAccessService mineAccess();
RankService ranks();
PrestigeService prestiges();
ProgressionService progression();
PlayerDataService players();
SellService selling();
MultiplierService multipliers();
BoosterService boosters();
MiningService mining();
StatisticsService statistics();
BackupService backups();
DiagnosticService diagnostics();
NumberFormatService numbers();
String version();
```

## SellService

_Public API signature snapshot from RelicPrison 1.0.0._

```java
CompletableFuture<BigDecimal> sellInventory(UUID playerId);
CompletableFuture<SellResult> sellInventoryDetailed(UUID playerId);
BigDecimal estimatedInventoryValue(UUID playerId);
BigDecimal estimatedHeldValue(UUID playerId);
```

## StatisticsService

_Public API signature snapshot from RelicPrison 1.0.0._

```java
long lifetimeBlocks(UUID playerId);
long mineBlocks(String mineId);
long itemsSold(UUID playerId);
long rankups(UUID playerId);
long prestiges(UUID playerId);
long boostersUsed(UUID playerId);
long playtimeSeconds(UUID playerId);
CompletableFuture<List<LeaderboardEntry>> leaderboard(String metric, String period, int limit);
```

