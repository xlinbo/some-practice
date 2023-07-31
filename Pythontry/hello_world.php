<?php
// 定义一个常量
define('GREETING', 'Hello, World!');

// 定义一个函数
function sayHello($name) {
    echo "Hello, " . $name . "!";
}

// 使用条件语句
if (strlen(GREETING) > 5) {
    echo GREETING;
} else {
    echo "Greeting is too short.";
}

// 使用循环语句
for ($i = 1; $i <= 5; $i++) {
    echo $i;
}

// 调用函数
sayHello("John");
?>
