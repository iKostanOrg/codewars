# Pointless Farmer

You've harvested a fruit. But the Internal Raisin Service (IRS) doesn't
allow you to eat your own produce, you have to launder it on the market first.
When you visit the market, you are given three conversion offers, and for
each conversion offer you must decide which direction to trade. A conversion
offer is a pair of fruits, and to buy the second fruit for the first fruit, 
the action is "buy". The opposite direction is "sell".

Given the offer `("apple", "orange")`, if you have an `apple`, then you may `buy
an orange`, or, if you have an `orange`, you may `sell` it for the apple.

## Example

```bash
pairs: [("apple", "orange"), ("orange", "pear"), ("apple", "pear")]
harvested fruit: "apple"

currently holding: apple
("apple", "orange")
buy
currently holding: orange
("orange", "pear")
buy
currently holding: pear
("apple", "pear")
sell
currently holding: apple (successfully ended up with the same fruit again)
```

As input you receive three conversion offers together with your harvested fruit,
and your output is a list of three actions of buy/sell, for the above example the
output is: `["buy", "buy", "sell"]`.

If it is not possible to end up with the original kind of fruit again after the
three conversions, return `"ERROR"` instead of the list of actions.

[Source](https://www.codewars.com/kata/597ab747d1ba5b843f0000ca)