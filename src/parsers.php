<?php

namespace Yay;

const LAYER_DELIMITERS_WITH_TRAILING_COMMA = [
    ',' => -3,
] + LAYER_DELIMITERS;

function layer_with_trailing_comma(array $delimiters = LAYER_DELIMITERS_WITH_TRAILING_COMMA) : Parser
{
    return layer($delimiters);
}
