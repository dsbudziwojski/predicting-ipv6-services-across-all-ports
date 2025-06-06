CREATE OR REPLACE TABLE `<YOUR SELECTED TABLE NAME>` AS 
SELECT
  p AS port_number,
  COUNT(*) AS freq
FROM `my-table` -- IPv6 or IPv4 table created from LZR
GROUP BY p;