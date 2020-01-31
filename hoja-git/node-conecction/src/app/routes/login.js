const dbConnection = require('../../config/dbConnection');
module.exports = (app) => {
  const connection = dbConnection();


app.post('/login', (req,res) => {
    //console.log(req.body);
    const {Pasword, Usuario} = req.body;
    connection.query('SELECT * FROM formulario WHERE Pasword =? and Usuario =?' , [
       Pasword,
       Usuario
    ], (err, result) => {
      if(result.length>0){
        console.log(result);
        res.redirect('/');
      } else{
        res.redirect('/login');
      }


    });
  });
}