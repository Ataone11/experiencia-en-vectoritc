const mysql = require('mysql');
//@hace la coneccion a la base de datos desde e local host
module.exports = () => {
  return mysql.createConnection({
    host:'localhost',
    user: 'root',
    password: '',
    database:'formulario_gg'
  });
}
