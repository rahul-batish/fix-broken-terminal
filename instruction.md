Analyze the Apache-style access log at `/app/access.log` and write a JSON report to `/app/report.json`.

Success criteria:

1. `/app/report.json` exists and is a UTF-8 JSON object with exactly these three keys: `total_requests`, `unique_ips`, and `top_path`.
2. `total_requests` is `6`, the number of non-empty request entries in `/app/access.log`.
3. `unique_ips` is `3`, the number of distinct client IP addresses in the log.
4. `top_path` is `"/index.html"`, the URL path requested most often in the log.
