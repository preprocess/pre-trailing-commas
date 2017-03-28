--DESCRIPTION--

Test trailing commas

--GIVEN--

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

--EXPECT--

function foo($a = "hello", $b = "world") {
    // do something
}

$foo = function($a = "hello", $b = "world") {
    // do something
}

foo($a = "hello", $b = "world")
foo("hello", "world")

$foo("hello", "world")
