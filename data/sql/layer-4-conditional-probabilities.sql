CREATE OR REPLACE TABLE `<YOUR SELECTED TABLE NAME>` AS
WITH
  base AS (
    SELECT DISTINCT ip, p
    FROM `< LZR DATA >` -- Either IPv4 or IPv6
  ),
  pairs AS (
    SELECT
      b1.p AS port_b,
      b2.p AS port_a
    FROM base b1
    JOIN base b2
      ON b1.ip = b2.ip
     AND b1.p <> b2.p
  ),
  counts_pairs AS (
    SELECT port_b, port_a, COUNT(*) AS count_joint
    FROM pairs
    GROUP BY port_b, port_a
  ),
  counts_b AS (
    SELECT p AS port_b, COUNT(*) AS count_condition
    FROM base
    GROUP BY p
  )
SELECT
  cp.port_b,
  cp.port_a,
  cb.count_condition,
  cp.count_joint,
  SAFE_DIVIDE(cp.count_joint, cb.count_condition) AS probability
FROM counts_pairs AS cp
JOIN counts_b       AS cb
  ON cp.port_b = cb.port_b
ORDER BY port_b, probability DESC;