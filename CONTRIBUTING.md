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

## Validation

Run:

```bash
python3 scripts/check_readme.py
```

Also open the paper and any new external resources manually. The automated check is offline and does not validate external availability, authorship, or scientific claims.

## Rights

By contributing original material, you agree to dedicate it under this repository's CC0 1.0 license. Do not submit copyrighted paper text or figures without appropriate permission.
