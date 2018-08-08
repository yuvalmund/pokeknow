const express = require('express')
const app = express()
var path = require('path');
const spawn = require("child_process").spawn;

app.use(express.static(path.join(__dirname + '/')));

app.get('/', function (req, res) {
    res.sendFile(__dirname +"/index.html")
  })

  app.post('/user', function (req, res) {
    const pythonProcess = spawn('python',["igal_model/integ.py", "EAACysRWXxoUBABv6FC7OtN57tLwwZChXFWJ98OwqaMu2BJY5dRSHQ6iXmTZBmCCjGuocL0KtyhXJAKyLIoGnUwS6OYQrtlZAwgwK6hbyd1f2Y8cQPTsxjx2zVqBBWRrpmbexVqz26dqkn18hyMgPrQQ0V33IwVSjwM474zmWb1k535ZClOq9pU1AxUvfZBOQZD"]);
  })

app.listen(3000, () => console.log('Example app listening on port 3000!'))