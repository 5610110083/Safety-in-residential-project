<?php
<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Safety in residential system</title>

    <!-- Bootstrap Core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
    <link href='https://fonts.googleapis.com/css?family=Kaushan+Script' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700' rel='stylesheet' type='text/css'>

    <!-- Theme CSS -->
    <!-- <link href="css/agency.min.css" rel="stylesheet"> -->
    <link href="css/agency.css" rel="stylesheet">
    <link href="css/siczones.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body id="page-top" class="index">

    <!-- Navigation -->
    <nav id="mainNav" class="navbar navbar-default navbar-custom navbar-fixed-top">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header page-scroll">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span> Menu <i class="fa fa-bars"></i>
                </button>
                <a class="navbar-brand page-scroll" href="#page-top">Safety in residential system</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav navbar-right">
                    <li class="hidden">
                        <a href="#page-top"></a>
                    </li>
                    <li>
                        <a class="page-scroll" href="#login">Login</a>
                    </li>
                    <li>
                        <a class="page-scroll" href="#about">About</a>
                    </li>
                    <li>
                        <a class="page-scroll" href="#team">Team</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container-fluid -->
    </nav>

    <!-- Header -->
    <header>
        <div class="container">
            <div class="intro-text">
                <div class="intro-lead-in">Welcome to Safety project!</div>
                <div class="intro-heading">It's Nice To Meet You</div>
                <a href="#login" class="page-scroll btn btn-xl" onmouseover="style.color='black'" onmouseout="style.color='white'">
                Go to RPi server!</a>
            </div>
        </div>
    </header>

    <!-- login Section -->
    <!-- <section id="login" class="bg-light-gray"> -->
    <section id="login" class="bg-login">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 text-center">
                    <h2 class="section-heading">Login to server!</h2>
                    <h3 class="section-subheading text-muted">Please input RPi account to login</h3>
                </div>
            </div>
            <div class="wrapper">
                <form action="cgi-bin/index.py" method="post" name="Login_Form">
                    <!-- <hr class="colorgraph"> -->
                    <input type="text" class="form-control" name="Username" placeholder="Username" required="">
                    <input type="password" class="form-control" name="Password" placeholder="Password" required="">
                    <div>
                            <a href="#" data-toggle="modal" data-target="#login-modal" class="forgot-password">Forgot the password?</a>
                            <div class="modal fade" id="login-modal" tabindex="-1" role="dialog" aria-hidden="true" style="display: none;">
                                <div class="modal-dialog">
                                    <div class="loginmodal-container">
                                        <h4>Who are you? Roles?</h4>
                                        <br>
                                        <button type="button" class="close" data-dismiss="modal">close[&times;]</button>
                                    </div>
                                </div>
                            </div>
                     </div>
                    <br>
                    <button class="btn btn-lg btn-success btn-block" name="Submit" value="Login" type="Submit" onmouseover="style.color='yellow'" onmouseout="style.color='white'">
                        Login
                    </button>
                    <button class="btn btn-lg btn-danger btn-block" name="Reset" value="Reset" type="Reset" onmouseover="style.color='yellow'" onmouseout="style.color='white'">
                         Reset
                    </button>
                </form>

            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 text-center">
                    <h2 class="section-heading">About</h2>
                    <h3 class="section-subheading text-muted">RPi web server design for support setting configuration mode,view status report,history log and systems testing.</h3>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-12">
                    <ul class="timeline">
                        <li>
                            <div class="timeline-image">
                                <img class="img-circle img-responsive" src="img/about/1.jpg" alt="Beginnings">
                            </div>
                            <div class="timeline-panel">
                                <div class="timeline-heading">
                                    <h4>FEB 2016</h4>
                                    <h4 class="subheading">Our Beginnings project</h4>
                                </div>
                                <div class="timeline-body">
                                    <p class="text-muted">Since 1 february 2016 started this project.</p>
                                </div>
                            </div>
                        </li>
                        <li class="timeline-inverted">
                            <div class="timeline-image">
                                <img class="img-circle img-responsive" src="img/about/2.jpg" alt="">
                            </div>
                            <div class="timeline-panel">
                                <div class="timeline-heading">
                                    <h4>AUG 2016</h4>
                                    <h4 class="subheading">Develop and design</h4>
                                </div>
                                <div class="timeline-body">
                                    <p class="text-muted">Select sensore device, design circuit and coding alert with LINE application.</p>
                                </div>
                            </div>
                        </li>
                        <li>
                            <div class="timeline-image">
                                <img class="img-circle img-responsive" src="img/about/3.jpg" alt="Integrate Systems">
                            </div>
                            <div class="timeline-panel">
                                <div class="timeline-heading">
                                    <h4>SEP 2016 - OCT 2016</h4>
                                    <h4 class="subheading">Hardware Design and Integrate Systems</h4>
                                </div>
                                <div class="timeline-body">
                                    <p class="text-muted">Create detecting system with sensores device and test alert with LINE application.</p>
                                </div>
                            </div>
                        </li>
                        <li class="timeline-inverted">
                            <div class="timeline-image">
                                <img class="img-circle img-responsive" src="img/about/4.jpg" alt="new sites">
                            </div>
                            <div class="timeline-panel">
                                <div class="timeline-heading">
                                    <h4>NOV 2016</h4>
                                    <h4 class="subheading">Release all new sites</h4>
                                </div>
                                <div class="timeline-body">
                                    <p class="text-muted">Add new software features for systems on sites and design clean site.</p>
                                </div>
                            </div>
                        </li>
                        <li class="timeline-inverted">
                            <div class="timeline-image">
                                <h4>Be Part
                                    <br>Of Our
                                    <br>Story!</h4>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Team Section -->
    <section id="team" class="bg-team">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 text-center">
                    <h2 class="section-heading">Our Amazing Team</h2>
                    <h3 class="section-subheading text-muted">Safety in residential system.</h3>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <div class="team-member">
                        <img src="img/team/1.jpg" class="img-responsive img-circle" alt="">
                        <h4>Ranee Adam</h4>
                        <p class="text-muted">Voice Activity Detection</p>
                        <ul class="list-inline social-buttons">
                            <li><a href="#"><i class="fa fa-twitter"></i></a></li>
                            <li><a href="https://www.facebook.com/ranee.mahamad.3" target="blank"><i class="fa fa-facebook"></i></a></li>
                            <li><a href="https://www.instagram.com/" target="blank"><i class="fa fa-instagram"></i></a></li>
                        </ul>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="team-member">
                        <img src="img/team/2.jpg" class="img-responsive img-circle" alt="">
                        <h4>Jirapan Jitrak</h4>
                        <p class="text-muted">Creative systems</p>
                        <ul class="list-inline social-buttons">
                            <li><a href="#"><i class="fa fa-twitter"></i></a></li>
                            <li><a href="https://www.facebook.com/sic.story" target="blank"><i class="fa fa-facebook"></i></a></li>
                            <li><a href="https://www.instagram.com/siczones/" target="blank"><i class="fa fa-instagram"></i></a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-8 col-lg-offset-2 text-center">
                    <p class="large text-muted">Consultation by Assoc. Prof. Dr. Montri Karnjanadecha</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Clients Aside -->
    <aside class="clients">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <a href="#">
                        <img src="img/logos/coe.jpg" class="img-responsive img-centered" alt="">
                    </a>
                </div>
                <div class="col-md-6">
                    <br>
                    <br>
                    <p class="large text-muted">
                        Department of Computer Engineering Faculty of Engineering, Prince of Songkla University P.O. Box 2 Kohong, Hatyai, Songkhla 90112 THAILAND Tel: +66 (0)74 287075, Fax: +66 (0)74 287076
                    </p>
                </div>
            </div>
        </div>
    </aside>

    <footer>
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <span class="copyright">Copyright &copy; Siczones 2016</span>
                </div>
                <div class="col-md-6">
                    <ul class="list-inline quicklinks">
                        <li><a href="#">Privacy Policy</a>
                        </li>
                        <li><a href="#">Terms of Use</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>

    <!-- jQuery -->
    <script src="vendor/jquery/jquery.min.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="vendor/bootstrap/js/bootstrap.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>

    <!-- Contact Form JavaScript -->
    <script src="js/jqBootstrapValidation.js"></script>
    <script src="js/contact_me.js"></script>

    <!-- Theme JavaScript -->
    <script src="js/agency.min.js"></script>

</body>
