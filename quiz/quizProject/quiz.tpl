%#The page where quizzes are made
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
        <h2>{{topic[0]}}</h2>

        %countx = 1
        %for x in range (0,numQ):
                %if countx%2 == 0:
                    %bckg = "bg-light"
                %else:
                    %bckg = None
                %end
            <form class="{{bckg}}">
                <h4 style="margin:auto;text:center;">{{result[questions[x]][0]}}</h4>
              <fieldset class="form-group">
                <div class="row">
                  <div class="col-sm-10">
                    %ans = random.sample(range(0, len(result)-1), 3)
                    %ans.append(x)
                    %random.shuffle(ans)
                    %county = 1
                    %for y in ans:
                      %if county == 1:
                        %chck = checked
                      %else:
                        %chck = None
                      %end
                      <div class="form-check">
                        <input class="form-check-input" type="radio" name="Radios" id="gridRadios{{countx}}{{county}}" value="Radio{{x}}" {{chck}}>
                        <label class="form-check-label" for="gridRadios{{countx}}{{county}}">
                          {{result[questions[y]][1]}}
                        </label>
                      </div>
                      %county = county +1
                    %end
                  </div>
                </div>
              </fieldset>

            </form>
        %countx = countx + 1
        %end
    </div>


</body>