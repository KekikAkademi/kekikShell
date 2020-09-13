<?php

file_put_contents("target_dir.txt", " "  . $_GET['cat'] . "\n", FILE_APPEND);

exit();

