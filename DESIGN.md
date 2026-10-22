# Engineering Rules

## 1. Product Principles
- Build for users first, not for demos.
- Keep the experience fast and mobile-friendly.
- Prefer clear and useful interactions over overly complex ones.
- Maintain a premium, consistent visual identity.

## 2. Development Rules
1. Every feature must be connected to a user need.
2. Keep logic modular and reusable.
3. Favor readability over cleverness.
4. Never hardcode secrets or production credentials.
5. Validate all external input before processing.
6. Keep error states visible and understandable.
7. Write tests for critical flows and agent orchestration.
8. Keep UI responsive even under weak network conditions.

## 3. Code Standards
- Use descriptive naming for classes, methods, and variables
- Keep files focused on a single responsibility
- Prefer small functions and clear abstractions
- Document important assumptions and decisions
- Avoid duplicated business logic

## 4. AI and Agent Rules
- Agent selection should be explicit and transparent
- Always provide context before invoking LLM tasks
- Ensure prompt instructions are safe and bounded
- Respect user privacy and consent for voice and memory features
- Keep prompt output structured and easy to parse

## 5. UI Rules
- Maintain the black-red holographic visual language consistently
- Respect accessibility contrast and readability
- Optimize layouts for Android touch interactions
- Support low-vision and high-contrast alternatives

## 6. Performance Rules
- Avoid unnecessary API calls
- Cache repeated data where helpful
- Minimize blocking operations on the main UI thread
- Use asynchronous patterns for long-running operations

## 7. Security Rules
- Store secrets in secure storage
- Encrypt sensitive local data when appropriate
- Protect APIs against misuse and abuse
- Log safely without exposing private information

## 8. Review Rules
- Every pull request should be reviewed for behavior, usability, and architecture impact
- Do not merge features with no testing coverage
- Keep documentation updated when behavior changes

## 9. Quality Gates
Before release, verify:
- Core flows work on real Android devices
- Voice input and output are functional
- Agent routing behaves correctly
- UI remains stable and visually consistent
- Errors are handled gracefully

## 10. Decision Framework
When making design or architecture decisions, prefer:
- Simplicity
- Maintainability
- Mobile usability
- Extensibility
- Clear user value
