# TS-<N> deep dive

Findings from a deep review of TS-<N>: <Title>

~<NNN> lines across <N> files.

Assessed against the repository
[style guide](../../../../../docs/style-guide.md),
[TS-26: Technical Writing Style Guide](../../pages/026.adoc),
[TS-27: Markdown](../../pages/027.adoc),
[TS-28: AsciiDoc](../../pages/028.adoc),
and the [template](../../../../../template/).

**Assessment.** Two or three sentences. Lead with what is sound. Then state
the shape of the problems: their number, their concentration, and which category
dominates.

**Status:** Which tiers are applied, which are open. Update this line at the
end of every tier — it is the first thing a resuming agent reads.

## Priority order

1. **Correctness.** Contradictions and factual errors. A reader cannot comply
   with a standard that says two incompatible things.

2. **Coherence.** Structural problems. Structure must settle before content is
   added to it.

3. **Completeness.** Coverage gaps. Filled into a structure that has stopped
   moving.

4. **Conventions.** Style-guide conformance. Last, because content edits
   invalidate cosmetic fixes made too early.

## 1. Contradictions

- [ ] <file>:<line> says "..." but <file>:<line> says "..." instead.

- [ ] <file>:<line> says "..." but <file>:<line> says "..." instead.

## 2. Factual errors

- [ ] <file>:<line> claims "...", but what is true is "..." (citations).

- [ ] <file>:<line> claims "...", but what is true is "..." (citations).

## 3. Structural problems

- [ ] <file>:<line> ...

- [ ] <file>:<line> ...

## 4. Coverage gaps

- [ ] A description of something that is missing, and why it matters to the
      user. Recommend placing at <file>:<line>.

- [ ] A description of something that is missing, and why it matters to the
      user. Recommend placing at <file>:<line>.

## 5. Convention conformance

- [ ] <file>:<line> has diverged from <style guide or convention>.

- [ ] <file>:<line> has diverged from <style guide or convention>.

## 6. Prose defects

- [ ] <file>:<line> "<quoted text>" → <correction>

- [ ] <file>:<line> "<quoted text>" → <correction>
