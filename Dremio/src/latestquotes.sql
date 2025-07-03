  SELECT * 
  FROM(
    SELECT "_id",quotesNumber,Version,Row_Number() over(partition by quotesNumber order by Version DESC) as latestquoteVersion
    FROM(
        SELECT "_id", quotesNumber, nested_1.quotesVersion.version AS Version
        FROM (
          SELECT "_id", nested_0.quotes.quoteNumber AS quotesNumber, flatten(nested_0.quotes.quoteVersions) AS quotesVersion
          FROM (
            SELECT "_id", flatten(quotes) AS quotes
            FROM "@test"."Odin VDS ".Prospects AS Prospects
      ) nested_0
    ) nested_1
    ) nested_2
  )node3
  where LatestquoteVersion =1