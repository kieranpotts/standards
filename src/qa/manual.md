# Manual testing

While [automated testing](./automated.md) SHOULD be prioritized, a comprehensive test strategy REQUIRES a balance of automated and manual testing. Both test strategies provide different insights into the evolving _quality_ of a software system.

Automated tests can tell you whether a system behaves in accordance with a written specification, either expressed as code or some other test grammar that can be parsed into executable tests. But automated tests can't tell you if the system is _right_ for the user in the way that the customer had intended. That can only be evaluated by the users themselves experiencing the software and providing feedback. Now, manual testing is no substitute for customer feedback, but it does provide valuable early feedback on the user experience – before the software is evaluated by the customer.

Manual testing shortens the feedback loop.

Manual testing also allows the QA team to ask questions of the software that were no asked earlier in the delivery pipeline. It is an opportunity to explore the software (known as exploratory testing or chaos testing). An outcome may be, for example, the discovery of code paths and use case scenarios that are not covered by the requirements or the automated tests.
