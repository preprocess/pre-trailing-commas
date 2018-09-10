<?php

namespace Pre\TrailingCommas;

use Yay\Parser;
use function Yay\layer;

const LAYER_DELIMITERS_WITH_TRAILING_COMMA = [
    "{" => 1,
    T_CURLY_OPEN => 1,
    T_DOLLAR_OPEN_CURLY_BRACES => 1,
    "}" => -1,
    "[" => 2,
    "]" => -2,
    "(" => 3,
    "," => -3,
];

function layerWithTrailingComma(array $delimiters = LAYER_DELIMITERS_WITH_TRAILING_COMMA) : Parser
{
    return layer($delimiters);
}
