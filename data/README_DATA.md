# Data Provenance and Download Steps

## Two Datasets (origins of the data used to compute "raw data")
IPv6 Data: LZRv6 scans over 55 ports from Georgia Tech Servers

IPv4 Data: LZR scans over 42 ports using Georgia Tech Servers

## Current Dataset
- ports-unique-lzr*.csv data was simply filtered using unique ports
- v*-deduped.csv data was simply deduping on all features provided by lzr except for ip, p, service (and asn since that was added)
- v6-conditional-probability.csv & port_only_v4.csv are computed using layer-4-conditional-probabilities.sql

## More Info
- BigQuery was used to do the initial filtering and compute the conditional probabilities
- Any postprocessing is done in the scripts found in the '/scripts' directory (not here)

## Download
- Not quite public data