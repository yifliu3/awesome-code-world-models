# Sources and curation record

## Snapshot

- Search and verification date: **2026-09-18**.
- Initial collection: **27 distinct papers**.
- Maintainer account: **yifliu3**.
- Discovery seed: [Awesome-World-Models](https://github.com/knightnemo/Awesome-World-Models).
- Metadata source: each entry's linked arXiv abstract page.
- Official resource provenance: links on paper abstract/full-text pages or the authors' project pages.

## Discovery

The initial search combined the seed list with arXiv search and the arXiv API, including these queries:

```text
"world model" code
"world models" "program synthesis"
"world models" executable
WorldCoder
Code2World
world AND symbolic
```

The broad code query and executable query were inspected newest-first, including September 2026 results. Targeted searches and the seed list supplied earlier work. Some API requests were rate-limited; successful arXiv website searches and individual paper pages were used instead.

The collection is selective. The search queries and inspected result windows do not establish exhaustive coverage, and unrelated results were excluded after examining their titles and abstracts.

## What was checked

For every paper:

- The title, first-submission date, and abstract on the arXiv abstract page.
- Whether the work fits the main topic or needs a related-work label.
- Whether the summary is supported by the source abstract.

For linked official resources:

- The destination was supplied by the paper or an author-controlled project page.
- Repository/project labels describe the resource type, not release completeness.
- No experiments, model weights, or third-party repository code were run as part of curation.
- All 51 distinct external paper, project, and repository URLs selected from the README returned HTTP 200 during the initial link check. This excludes badge-image services and this new repository's own links; a successful response does not establish scientific validity or release completeness.

Examples of the provenance chain:

| Paper/resource | Source of additional links |
| :--- | :--- |
| Code World Model | [Author project page](https://buaacyw.github.io/cwm/) links the repository. |
| Code as Worlds | [Author project page](https://mirros-lab.github.io/code-as-world/) links the repository. |
| PoE-World | [Author project page](https://topwasu.github.io/poe-world) links the repository. |
| OneLife | [Author project page](https://onelife-worldmodel.github.io/) links OneLife and Crafter-OO. |
| Text2World | [Author project page](https://text-to-world.github.io/) links the repository. |
| Symbolic world models via test-time scaling | [Author project page](https://vmlpddl.github.io/) links VML_PDDL. |
| TheoryCoder-2 | [Paper HTML](https://arxiv.org/html/2602.00929) links the TheoryCoder repository. |

## Date caveat

[World-Time Compute with Verified Code World Models](https://arxiv.org/abs/2609.09163) reports **July 7, 2026** in its v1 submission history and citation metadata even though its identifier begins with `2609`. This list preserves the reported submission date and flags the discrepancy rather than silently changing it.

Similarly, TheoryCoder-2 reports January 31, 2026 despite a `2602` identifier. Identifiers should not be used as exact publication dates.

## Limitations

This is primarily an abstract-level literature map, not a full-paper reproducibility review. Inclusion does not certify peer review, benchmark validity, code completeness, licensing suitability for downstream use, or claimed performance. Availability and source contents may change after the snapshot date.
