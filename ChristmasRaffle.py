import random, ssl, smtplib, Constants
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def ParseInput():
    names = []
    mails = []
    with open("Input.txt" , "r", encoding="utf-8") as f:
        for person in f.readlines():
            names += [person.split(" - ")[0]]
            mails += [person.split(" - ")[1].replace("\n", "")]
    return [names, mails]

def GetChristmasRaffle(input):
    inputNames = input[0].copy()
    while True:
        random.shuffle(inputNames)
        control = True
        for i in range(len(inputNames)):
            if input[0][i] == inputNames[i]:
                control = False
                break
        if control:
            break
    permutations = []
    for i in range(len(inputNames)):
        permutations += [[input[0][i], input[1][i], inputNames[i]]]
    return permutations

def CreateHtmlBody(name1, name2):
    return """
    <html lang="en">
<head>
  <style>
    .center {
      width: auto;
    }
    .tree {
      padding-top: 20px;
      padding-bottom: 10px;
      width: 500px; 
      line-height: 0.2; 
      margin: 0 auto;
    }
    .text {
      width: 80%;
      margin-left: 10%;
      margin-right: 10%; 
      margin: 0 auto; 
      font-size: 20px;
      text-align: center;
      padding-bottom: 20px;
    }
    .line {
      text-align:center;
    }
    .r {
      color: red;
    }
    .b {
      color: blue;
    }
    .y {
      color: yellow;
    }
    .c {
      color: cyan;
    }
    .w {
      color: white;
    }
    .g {
      color: green;
    }
    .brown {
      color: brown;
    }
    .o {
        color: orange;
    }
  </style>
</head>
<body style="background-color:#110c0d; color: white; font-family: 'Roboto Mono', monospace;">
  <div>
    <div class="tree">
      <p class="line y">|</p>
      <p class="line y">\|/</p>
      <p class="line y">--*--</p>
      <p class="line g">><span class="o">o</span><</p>
      <p class="line g">>><span class="r">@</span><<</p>
      <p class="line g">>><span class="r">@</span>>><span class="b">O</span><</p>
      <p class="line g">>><span class="y">*</span>><span class="r">@</span><<<<</p>
      <p class="line g">><span class="r">@</span><<<span class="b">O</span>>>><span class="y">*</span><<</p>
      <p class="line g">><span class="o">o</span><<<<span class="y">*</span>><span class="r">@</span>><span class="b">O</span><<span class="r">@</span><</p>
      <p class="line g">><span class="y">*</span>>><span class="b">O</span><<<span class="b">O</span>>><span class="o">o</span>><span class="y">*</span><<</p>
      <p class="line g">>><span class="o">o</span>>>><span class="y">*</span><<<span class="y">*</span><<<span class="r">@</span><<span class="y">*</span><<</p>
      <p class="line g">><span class="o">o</span>><span class="r">@</span><<<<span class="o">o</span><<span class="y">*</span>>><span class="o">o</span><<<span class="b">O</span><<<</p>
      <p class="line g">>><span class="y">*</span><<<<span class="y">*</span><<<span class="y">*</span>>><span class="y">*</span><<<span class="b">O</span>><span class="r">@</span><<span class="r">@</span><</p>
      <p class="line g">>><span class="r">@</span><<span class="y">*</span><<<span class="o">o</span>><span class="o">o</span>>>><span class="r">@</span>><span class="b">O</span>>>><span class="r">@</span><<span class="r">@</span><</p>
      <p class="line g">>><span class="y">*</span><<span class="r">@</span><<span class="b">O</span><<<span class="o">o</span>>>><span class="y">*</span><<<span class="r">@</span><<span class="o">o</span><<<<span class="o">o</span><<</p>
      <p class="line g">>><span class="r">@</span><<<span class="o">o</span>>>><span class="y">*</span>>>><span class="r">@</span><<span class="b">O</span><<<<span class="o">o</span><<<<span class="o">o</span>><span class="b">O</span><</p>
      <p class="line g">><span class="b">O</span><<span class="r">@</span><<<span class="y">*</span><<span class="o">o</span>>><span class="r">@</span><<<span class="b">O</span><<<span class="b">O</span>>>><span class="o">o</span>>><span class="o">o</span>><span class="y">*</span><<</p>
      <p class="line g">>><span class="r">@</span>><span class="r">@</span><<<<span class="o">o</span>>>><span class="o">o</span><<<<span class="o">o</span><<<<span class="o">o</span>><span class="r">@</span>>>><span class="o">o</span>>><span class="b">O</span><</p>
      <p class="line g">>><span class="b">O</span><<<<span class="y">*</span>><span class="r">@</span><<<<span class="b">O</span><<<span class="o">o</span><<<<span class="r">@</span><<span class="o">o</span><<<span class="y">*</span><<span class="y">*</span>><span class="b">O</span><<<<</p>
      <p class="line g">><span class="o">o</span><<<<span class="o">o</span><<span class="y">*</span><<<<span class="o">o</span><<<span class="r">@</span><<<<span class="y">*</span>>>><span class="o">o</span><<<<span class="o">o</span><<span class="y">*</span><<<<span class="b">O</span><<</p>
      <p class="line g">>><span class="b">O</span>><span class="y">*</span><<span class="b">O</span>>>><span class="o">o</span><<<<span class="b">O</span><<<<span class="y">*</span>>><span class="y">*</span>>><span class="b">O</span>>><span class="b">O</span>>><span class="r">@</span><<span class="b">O</span><<<span class="y">*</span><</p>
      <p class="line g">><span class="r">@</span>>>><span class="b">O</span>><span class="r">@</span><<<<span class="r">@</span>><span class="b">O</span><<<span class="y">*</span>><span class="b">O</span><<<span class="b">O</span>>>><span class="o">o</span><<span class="o">o</span>>><span class="y">*</span><<<span class="o">o</span><<<span class="y">*</span><<</p>
      <p class="line brown">|_____|</p>
    </div>
    <div class="text">
        <!--Who.Name is name of the recipient-->
       <span class="r">Merry Christmas </span><span class="c">&nbsp;""" + name1 + """</span><br>
        <!--Whom.Name is the name of the person to whom the gift will be given-->
       <span class="w">Gift recipient from you </span> <span class="y">&nbsp;""" + name2 + """</span>
    </div>
  </div>
</body>
</html>
    """

def SendEmails(raffles):
    for person in raffles:
        mail = MIMEMultipart("alternative")
        mail["From"] = Constants.MAIL_SENDER
        mail["Subject"] = "Yılbaşı Çekilişi Sonucu"
        mail["To"] = person[1]
        mail.attach(MIMEText(CreateHtmlBody(person[0], person[2]), "html"))
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(Constants.MAIL_SENDER, Constants.MAIL_PWD)
            smtp.sendmail(Constants.MAIL_SENDER, person[1], mail.as_string())

SendEmails(GetChristmasRaffle(ParseInput()))