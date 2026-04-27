---
type: meta
title: "Dashboard"
created: 2026-04-27
updated: 2026-04-27
tags: [meta, dashboard]
---

# Wiki Dashboard

## Recent Activity
```dataview
TABLE type, status, updated FROM "wiki" SORT updated DESC LIMIT 15
```

## Seed Pages (Need Development)
```dataview
LIST FROM "wiki" WHERE status = "seed" SORT updated ASC
```

## Sources by Year
```dataview
TABLE author, venue, year FROM "wiki/sources" SORT year DESC
```

## Entities Missing Sources
```dataview
LIST FROM "wiki/entities" WHERE !sources OR length(sources) = 0
```

## Open Questions / Gaps
```dataview
LIST FROM "wiki/gaps" WHERE status = "open" SORT created DESC
```

## Synthesis Pages
```dataview
TABLE status FROM "wiki/questions" SORT updated DESC
```
