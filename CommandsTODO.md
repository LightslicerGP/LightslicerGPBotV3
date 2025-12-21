## Rest In Peace, AOIJS.

`created 12/14/25`

### check .vscode/settings.json to unhide files if needed

# Commands to do

```llvm
[] = required
() = optional

 @ = user/role
 # = channel
 = = number
 > = listed option
 . = string
 : = default option
 | = logical OR
 * = user <@586225258269245538> only
```

## Economy

- bal `(@user)`
- - add `(@user) [=amount]` \*
- - gamble `[=amount]`
- - give `[@user] [=amount]`
- - remove `[@user] [=amount]` \*
- - reset `[@user]` \*
- - set `(@user) [=amount]` \*
- - top
- daily
- job `(@user)`
- - apply `[>job|=jobNumber]`
- - give `(@user) [>job|=jobNumber]` \*
- - raise reset `(@user) [>job|=jobNumber] [=amount]` \*
- - raise set `(@user) [>job|=jobNumber]` \*
- - remove `(@user) [>job|=jobNumber]` \*
- shop `[>item]`
- - shop buy `[>item]`
- - shop sell `[>item]`
- work
- - clock `[in|out]`

## Fun

- animal `[>animal]`
- chat `[.message]`
- comment `[.message]`
- coinflip
- diceroll
- random `(=min:1) (=max:100)`
- tweet `[.message]`

## General

- banned `(@user)`
- bot info
- bot restart
- bump
- - `(bump ping)`
- - bump channel set `(#channel:current)`
- - bump channel
- - bump role set `[@role]`
- - bump role
- calc `[.equation]`
- date
- embed
- eval `[.code]`
- test
- help `[>command]`
- invite
- ping
- profile `(@user)`
- - set `[>item] [.text]`
- - remove `[>item]`
- rawjson `[.json]`
- version
- whois `[@user]`

## Pet

- pet
- - pet shop
- - pet buy `[>pet]`
- pets

## Simulation

- travel `[>location]`
