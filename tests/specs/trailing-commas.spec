function foo(
    $a = "hello",
    $b = "world",
) {
    // do something
}

$foo = function(
    $a = "hello",
    $b = "world",
) {
    // do something
}

~~~

function foo(
    $a = "hello",
    $b = "world") {
    // do something
}

$foo = function(
    $a = "hello",
    $b = "world") {
    // do something
}

---

foo(
    $a = "hello",
    $b = "world",
)

foo(
    "hello",
    "world",
)

$foo(
    "hello",
    "world",
)

~~~

foo(
    $a = "hello",
    $b = "world")

foo(
    "hello",
    "world")

$foo(
    "hello",
    "world")
