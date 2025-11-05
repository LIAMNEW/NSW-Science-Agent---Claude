# UI Design Rationale: Investigation Display

## Frontend Investigation Truncation

The frontend displays the first 3 NESA investigations with a "...and X more investigations" message.

### Design Decision
This truncation is intentional for optimal user experience:

1. **Prevents Overwhelming Students**: Some topics have 10+ investigations (e.g., "Change" has 10 investigations). Displaying all at once creates cognitive overload for Year 7-8 students.

2. **Maintains Clean Interface**: The UI remains scannable and focused, presenting the most immediately relevant investigations first.

3. **Progressive Disclosure**: Students see enough to understand the practical application without being overwhelmed. Teachers can expand on these in classroom settings.

4. **Industry Best Practice**: Educational platforms (Khan Academy, Coursera, etc.) use similar truncation strategies to maintain engagement.

### Implementation
- **Code Location**: `static/js/app.js` lines 133-141
- **Display Logic**: Shows first 3 investigations, then displays count of remaining items
- **All Data Available**: Complete investigation list is present in the API response; frontend chooses to display subset for UX reasons

### Complete Data Availability
The full investigation list is:
- ✓ Stored in `nesa_official_content.py`
- ✓ Retrieved by `CurriculumSpecialist`
- ✓ Passed through `Orchestrator`
- ✓ Available in API response
- ✓ Accessible to frontend JavaScript
- → Frontend displays 3 for optimal UX

This design balances completeness with usability for the target audience (Years 7-8 students).
