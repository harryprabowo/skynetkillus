<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap 4 Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="elemen/css/bootstrap.css">
</head>
<body>
<!------ Include the above in your HEAD tag ---------->


<link href="elemen/css/chat.css" rel="stylesheet" id="chat-css">
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
                                    <div class="chat-body clearfix pull-left col-sm-7">
                                        <p>
                                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur bibendum ornare
                                            dolor, quis ullamcorper ligula sodales.
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
                        <input id="btn-input" type="text" class="form-control input-sm" placeholder="Type your message here..." />
                        <span class="input-group-btn">
                            <button onclick= "changeImage()" class="btn btn-warning btn-sm" id="btn-chat" >
                                Send</button>
                                <script lang="JavaScript">
                                        function changeImage() {
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
                                        }
                                </script>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <p id="demo"></p>
</div>
 <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="elemen/js/bootstrap.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>



