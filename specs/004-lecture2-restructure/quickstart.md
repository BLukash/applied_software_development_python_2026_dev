# Quickstart Guide: Lecture 2 Restructuring

**Branch**: `004-lecture2-restructure` | **Date**: 2026-02-06

## Overview

This guide provides step-by-step instructions for implementing the Lecture 2 restructuring.

## Prerequisites

- [ ] Read [spec.md](spec.md) to understand requirements
- [ ] Read [research.md](research.md) for context decisions
- [ ] Read [data-model.md](data-model.md) for section structure
- [ ] Read [contracts/sections.md](contracts/sections.md) for exact content

## Implementation Steps

### Phase 1: Preparation

1. **Backup current notebook**
   ```bash
   cp lectures/02-core-mechanics/lecture-02.ipynb lectures/02-core-mechanics/lecture-02.backup.ipynb
   ```

2. **Verify all code cells run successfully**
   - Open notebook in Jupyter
   - Run all cells (Kernel → Restart & Run All)
   - Fix any errors before proceeding

### Phase 2: Section Restructuring

Execute in this order to minimize conflicts:

#### Step 1: Create Section 4 (Complex Data Types)

1. Insert 4 new cells after current Section 3 (Identity/Equality):
   - Markdown: Section header + intro
   - Code: List and tuple examples
   - Code: Dict and set examples
   - Markdown: Conclusion

2. Use exact content from `contracts/sections.md` - Section 4

#### Step 2: Move Memory Representation (Section 2)

1. Cut cells 18-21 (Memory Representation)
2. Paste after Names & Objects section (after cell 10)
3. Add transition text at section start:
   > "Тепер, коли ми розуміємо, що імена — це посилання на об'єкти, подивимося, як ці об'єкти зберігаються в пам'яті."

#### Step 3: Split Identity vs Equality

1. **Simple Types section (Section 3):**
   - Keep cells 22-25 (concept, integer caching)
   - Keep cell 27 (None checking)
   - Keep cells 28-29 (string interning, warning)
   - Update section header to add "(Прості Типи)"
   - Add transition text

2. **Lists section (Section 6):**
   - Move cell 26 (list comparison) to new section after Mutability
   - Add transition text
   - Add new copy example cell

#### Step 4: Modify Names & Objects (Section 1)

1. Replace list aliasing example (cells 9-10) with integer rebinding
2. Use content from `contracts/sections.md` - Section 1

#### Step 5: Move Mutability (Section 5)

1. Cut cells 11-17 (Mutability)
2. Paste after Complex Data Types section
3. Update transition text at section start
4. Add note: "Деталі роботи з цими типами — у Лекції 3"

#### Step 6: Create Identity (Lists) Section (Section 6)

1. Create new section after Mutability
2. Add transition text
3. Add cells from `contracts/sections.md` - Section 6:
   - Aliasing example (from old Names section)
   - is vs == comparison (from old Identity section)
   - New copy example

#### Step 7: Renumber Remaining Sections

Update section numbers:
- Truthiness: 5 → 7
- Control Flow: 6 → 8
- Practical Patterns: 7 → 9
- Timing: 8 → 10

#### Step 8: Update Summary

Replace summary bullet points with new order from `contracts/sections.md` - Summary Section

### Phase 3: Validation

1. **Run all cells**
   - Verify no errors
   - Check all outputs are correct

2. **Check transitions**
   - Each section has connecting text
   - Flow feels natural

3. **Verify duration**
   - Estimate reading/presenting time
   - Should fit ~90 minutes (±10 min acceptable)

4. **Constitution compliance**
   - [ ] Learning objectives match new structure
   - [ ] 2 memes present (mutability-bug, timing-meme)
   - [ ] Ukrainian text with English terms in parentheses
   - [ ] Cross-references to Lecture 1 preserved
   - [ ] "Details in Lecture 3" note present

5. **Test exercises**
   - Verify exercises still make sense
   - All required concepts taught before exercises

### Phase 4: Final Review

1. **Learning objectives update**
   - May need minor wording update to match new flow
   - Ensure objectives still accurate

2. **What's Next section**
   - Verify Lecture 3 preview still accurate
   - Should mention "detailed complex types coverage"

## Rollback Plan

If restructuring causes issues:
```bash
cp lectures/02-core-mechanics/lecture-02.backup.ipynb lectures/02-core-mechanics/lecture-02.ipynb
```

## Success Criteria

- [ ] All 10 sections in correct order
- [ ] All transitions include connecting text
- [ ] Memory Representation immediately follows Names & Objects
- [ ] Complex Data Types introduced before Mutability
- [ ] Identity vs Equality split into Simple Types and Lists
- [ ] No content duplication with Lecture 1 or 3
- [ ] All code cells execute without errors
- [ ] Duration within 1.5 hours

## Files Modified

| File | Changes |
|------|---------|
| `lectures/02-core-mechanics/lecture-02.ipynb` | Full restructure |

## Timeline Estimate

| Phase | Tasks | Estimate |
|-------|-------|----------|
| Preparation | Backup, verify | 10 min |
| Restructuring | Steps 1-8 | 45 min |
| Validation | Testing, compliance | 20 min |
| Final review | Polish, commits | 15 min |
| **Total** | | ~90 min |
