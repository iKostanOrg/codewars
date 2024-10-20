# Is your period late

In this kata, we will make a function to test whether a period is late.

Our function will take three parameters:

```text
1. **last** - The Date object with the date of the last period

2. **today** - The Date object with the date of the check

3. **cycleLength** - Integer representing the length of the cycle in days
```

If the today is later from last than the cycleLength, the function should
return **true**.

We consider it to be late if the number of passed days is larger than the
cycleLength. Otherwise return **false**.

[Source](https://www.codewars.com/kata/578a8a01e9fd1549e50001f1)
