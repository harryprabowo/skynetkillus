<!DOCTYPE html>
<html lang="en">
<head>
  <title>SkyNetKillUs | ChatBot</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="elemen/css/bootstrap.css">
  <link href="elemen/css/chat.css" rel="stylesheet" id="chat-css">
</head>
<!------ Include the above in your HEAD tag ---------->

<body>
<h1>
<?php
    if(isset($_REQUEST['input'])) {
        $command = escapeshellcmd('api\backendmodif.py ' . $_REQUEST['input']);
        echo($command);
        $output = shell_exec($command);
        echo($output);
    }
?>
</h1>
<div class="container-fluid">
    <div class="row">
        <div class="row-xs-3">
            <img src="elemen/img/kartunix-create-free-avatar.png" style="margin-top:30px; max-width:100%;" id="avatar1" >
        </div>
        <div class="col-sm-7">
            <div class="panel panel-primary">
                <div class="panel-heading rounded-top">
                    <strong class="primary-font">SkyNetKillUs Bot</strong>
                </div>
                <div class="panel-body">
                    <ul class="chat">
                            <li class="left clearfix">
                                    <div class="row">
                                    <div class="chat-body clearfix pull-right col-sm-7">
                                        <p>
                                            <!-- <?php 

                                            // $command = escapeshellcmd('api/backendmofif.py ' . );
                                            // $output = shell_exec($command);
                                            // echo $output;

                                            ?> -->
                                        </p>
                                    </div>
                                </div>                                
                            </li>
                        <li class="right clearfix">
                            <div class="row">
                                <div class="chat-body pull-right clearfix col-sm-7">
                                    <p>
                                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur bibendum ornare
                                        dolor, quis ullamcorper ligula sodales.
                                    </p>
                                </div> 
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="panel-footer">
                    <div class="input-group">
                       <form id="send-message-area">
                            <input id="sendie" name="sendie" type="text" class="form-control input-sm" placeholder="Type your message here...">
                            <span class="input-group-btn">
                                <button class="btn btn-warning btn-sm" id="btn-chat" >
                                    Send</button>
                                    
                            </span>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <p id="demo"></p>
</div>
 
</body>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="elemen/js/bootstrap.js"></script>
    <script>
        $(document).ready(function(){
            $("#btn-chat").click(function(){
                // $mystring = system('python backendmodif.py myargs', $retval);
                    
                })

                if (document.getElementById("avatar1").src == "elemen/img/kartunix-create-free-avatar-2.png") 
                {
                    document.getElementById("avatar1").src = "elemen/img/kartunix-create-free-avatar.png";
                    document.getElementById("demo").innerHTML = Date();
                }
                else 
                {
                    document.getElementById("avatar1").src = "elemen/img/kartunix-create-free-avatar.png";
                    document.getElementById("demo").innerHTML = "lalal";
                }

                
            })  
        // window.location = window.location.href  + "?input=asdf";         
    </script>
</html>



