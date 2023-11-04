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
                    if($parameter == ""){
                        echo"<script>alert('Insert a parameter')</script>";
                        echo "<span id = 'NotFound'>Insert a parameter</span>";
                    }
                    $filename = "output/{$parameter}.txt";
                    $filename2 = "output/{$parameter}.Dk";
                }
                else if(isset($_POST["IMAGE"])){
                    $parameter = $_POST["input"];
                    if($parameter == ""){
                        echo"<script>alert('Insert a parameter')</script>";
                        echo "<span id = 'NotFound'>Insert a parameter</span>";
                    }
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
                document.getElementById("Img").style.backgroundColor="Green";
                document.getElementById("Img").style.borderRadius="20px";
                document.getElementById("Img").style.width="60px";
                document.getElementById("web").style.width="none";
                document.getElementById("web").style.backgroundColor="transparent";
                //document.getElementsByClassName("choice_bar")[0].style.marginLeft="-25px";
            }
            function Web_Search(){
                document.getElementById("Web").style.display="block";
                document.getElementById("image").style.display="none";
                document.getElementById("web").style.backgroundColor="Green";
                document.getElementById("web").style.borderRadius="20px";
                document.getElementById("web").style.width="50px";
                document.getElementById("Img").style.width="none";
                document.getElementById("Img").style.backgroundColor="transparent";
            }
        </script>
        <title>Darkus</title>
        <link rel = "stylesheet" href ="Css/Style.css">
    </head>
    <body onload = "Web_Search()">
        <center>
            <h1>DARKUS</h1>
            <p>A Onion Link Searcher</p>
            <div class = "choice_bar">
                <p onclick="Image_Search()" id = "Img">Images</p>
                <p onclick="Web_Search()" id = "web">Web</p>
            </div>
            <div class = "searchbar">
                <div id ="Web">
                    <form action = "" method = "POST">
                        <input type = "text" placeholder = "Insert the parameter to search in the DB" name = "input" id = "search">
                        <button type = "submit" name = "WEB">Search</button>
                    </form>
                </div>
                <div id ="image">
                    <form action = "" method = "POST">
                        <input type = "text" placeholder = "Insert the image parameter to search in the DB" name = "input" id = "search">
                        <button type = "submit" name = "IMAGE">Search</button>
                    </form>
                </div>
                <?php
                    get_res();
                ?>
            </div>
        </center>
        </div>
    </body>
</html>
