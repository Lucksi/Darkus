<!--ORIGINAL CREATOR: Luca Garofalo (Lucksi)
AUTHOR: Luca Garofalo (Lucksi)
Copyright (C) 2023 Lucksi <lukege287@gmail.com>
License: GNU General Public License v3.0-->

<!DOCTYPE HTML>
<html>
    <head>
        <?php
            function get_res(){
                if (isset($_POST["WEB"])){
                    $parameter = $_POST["input"];
                    $filename = "output/{$parameter}.txt";
                    $filename2 = "output/{$parameter}.Dk";
                }
                else{
                    $parameter = $_POST["input"];
                    $filename = "output/{$parameter}_image.txt";
                    $filename2 = "output/{$parameter}_image.Dk";
                }
                if($parameter != ""){
                    if(file_exists($filename)){
                        $f = fopen($filename,"r")or die("\n\nError");
                        echo "<h3>{$parameter}-Results:</h3>";
                        echo "<div class = 'results'>";
                        while (!feof($f)){
                            $content = fgets($f);
                            echo "\t\t\t<p>".$content."</p>";
                        }
                        echo "</div>";
                    }
                    else if(file_exists($filename2)){
                        $f = fopen($filename2,"r")or die("\n\nError");
                        echo "<h3>{$parameter}-Results:</h3>";
                        echo "<div class = 'results'>";
                        while (!feof($f)){
                            $content = fgets($f);
                            $converted = base64_decode($content);
                            echo "\t\t\t<pre><p>".$converted."</pre>";
                        }
                        echo "</div>";
                    }

                    else{
                        echo "<span id = 'NotFound'>{$parameter} Not Found</span>";
                    }
                }
            }
        ?>
        <script>
            function Image_Search(){
                document.getElementById("image").style.display="block";
                document.getElementById("Web").style.display="none";
            }
            function Web_Search(){
                document.getElementById("image").style.display="none";
                document.getElementById("Web").style.display="block";
            }   
        </script>
        <title>Darkus</title>
        <link rel = "stylesheet" href ="Css/Style.css">
    </head>
    <body>
        <center>
            <h1>DARKUS</h1>
            <p>A Onion Link Searcher</p>
            <div class = "choice_bar">
                <h5 onclick="Image_Search()">Images</h5>
                <h5 onclick="Web_Search()">Web</h5>   
            </div>         
            <div class = "searchbar">
                <div id ="Web">
                    <form action = "" method = "Post">
                        <input type = "text" placeholder = "Insert the term to search in the DB" name = "input" id = "search">
                        <button type = "submit" name = "WEB">Search</button>
                    </form>
                </div>
                <div id ="image">
                    <form action = "" method = "Post">
                        <input type = "text" placeholder = "Insert the image to search in the DB" name = "input" id = "search">
                        <button type = "submit" name = "IMAGE">Search</button>
                </div>     
                </form>
                <?php
                    get_res();
                ?>   
            </div>
        <!--</center>-->
        </center>
        </div>
    </body>
</html>

<?php
