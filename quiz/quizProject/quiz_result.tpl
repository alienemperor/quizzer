%#The page where quizzes are answered
%import random
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</head>

<body>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="/">Quizzer</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/add">New Topic</a>
          </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </nav>

  <div class="container" style="margin:auto;width:80%;padding-top:20px;">
        <h3>Topics:</h3>
        <table class="table table-striped table-bordered" style="text:center">
            <tr>
                <th>Term</th>
                <th>Your Choice</th>
                <th>Correct answer</th>
            </tr>

        %for x in range(0, (len(success)-1)):
            %if success[x]:
                %y = "correct"
                %bckg = "bg-success text-white"
            %else:
                %y = "Incorrect"
                %bckg = "bg-danger text-white"
            %end
          <tr>
            <td>{{resultquest[x]}}</td>
            <td class="{{bckg}}">{{resultans[x]}}</td>
            <td>{{realans[x]}}</td>
          </tr>
        %end
        </table>
    </div>

</body>