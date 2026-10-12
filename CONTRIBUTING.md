# Contributing

Please keep this list focused, verifiable, and useful for readers.

## Propose a paper

Open an issue or pull request with:

1. Exact paper title and a primary-source paper link.
2. First-submission date from the paper's source page.
3. The most appropriate category from the README taxonomy.
4. A one-sentence explanation of what code represents or executes.
5. Official project, repository, or dataset links, if verified from author-controlled sources.

Use this format:

```markdown
- **[YYYY-MM-DD] Exact Paper Title** — `Core`
  A concise, factual description of the representation, method, or evaluation.
  [Paper](https://arxiv.org/abs/XXXX.XXXXX) · [Project](https://example.org/)
```

## Curation rules

- Use one primary entry per paper, newest-first within its category.
- Official project releases may be listed without a paper; keep them in the separate project-release section rather than inventing a paper title, arXiv link, or submission date.
- Do not treat paper revisions or renamed versions as separate papers.
- Distinguish executable dynamics from static scene construction and existing-engine use.
- Generic coding agents and generic video world models are outside the default scope.
- Keep summaries original; do not paste paper abstracts.
- Avoid unqualified “first,” “best,” “solved,” or leaderboard claims.
- Do not infer publication dates from arXiv identifiers.
- Do not label a project page as code or imply a placeholder repository is a runnable release.
- Do not add unofficial reproductions as official code.
- If a source is ambiguous, document the ambiguity instead of guessing.
- Update the paper count and search date only when the corresponding work has actually been done.

## Propose a project release

Provide the exact project name and an official release, GitHub repository, or project-page URL. A paper and a technical summary are optional. Record the date you checked the resources, not an inferred publication date, and briefly distinguish an announcement or placeholder from an available code release.

Use the project-release table in the README:

```markdown
| **Project Name** | Organization | YYYY-MM-DD | [Project](https://example.org/) | Project page available; no paper destination verified. |
```

Include the primary-source provenance in `SOURCES.md`, check for duplicate projects, and update the separate project-release count. Rendering infrastructure belongs here when its official documentation explicitly connects it to upstream code-defined worlds; generic video generation remains outside the default scope.

## Validation

Run:

```bash
python3 scripts/check_readme.py
```

Also open the paper, if applicable, and any new external resources manually. The automated check is offline and does not validate external availability, authorship, scientific claims, or project-release table counts.

## Rights

By contributing original material, you agree to dedicate it under this repository's CC0 1.0 license. Do not submit copyrighted paper text or figures without appropriate permission.
