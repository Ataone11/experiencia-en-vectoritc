const dbConnection = require('../../config/dbConnection');
module.exports = (app) => {
  const connection = dbConnection();
  const controller = {};


//@recibe=/ metodo=get
//@ retorna un redireccionamiento a la view formulario
  app.get('/',(req, res) => {
    connection.query('SELECT * FROM formulario', (err, result) => {
    console.log(result);
    res.render('formulario/formulario',{
          formulario: result
        });
     });
  });


//@recibe parametro=/i metodo get
//@ retorna un redireccionamiento a la view inicio
  app.get('/i',(req, res) => {
    connection.query('SELECT * FROM producto', (err, result) => {
    console.log(result);
    res.render('formulario/inicio',{
          formulario: result
        });
     });
  });


//@recibe parametro=/edit y recibe un ide de un producto con e metodo post
//@ devuelve los datos del ide recivido
  app.post('/edit/:id_producto',(req, res) => {
    const { id_producto } = req.params;
    console.log(id_producto);
      connection.query('SELECT * FROM producto WHERE id_producto = ?', [id_producto], (err, rows) => {

        console.log(rows);
        res.render('formulario/vender', {
          data: rows[0]
        })
      });

  });


  //@recibe parametro=/update con un ide de un producto y la nueva cantidad a actualizar y conecta los input metodo post
//@ actualiza la cantidad de la tabla producto en la base de datos

  app.post('/update/:id_producto&:Cantidad',(req, res) => {
    const  id_producto   = req.params.id_producto;
    const Cantidad=req.params.Cantidad;
    console.log(id_producto + ' '+Cantidad );

      connection.query('UPDATE producto SET Cantidad = ? WHERE id_producto = ? ', [Cantidad,id_producto], (err, rows) => {

        console.log(rows);
        res.redirect('/i');
      });

  });


//@recibe parametro=/formulario y conecta los input metodo post
//@ inserta un usuiaro a la base de datos
  app.post('/formulario', (req,res) => {
    //console.log(req.body);
  const {Cedula, Nombre, Apellido, Usuario,Pasword,Administrador} = req.body;
    connection.query('INSERT INTO formulario SET?', {
      Cedula: Cedula,
      Nombre: Nombre,
      Apellido: Apellido,
      Administrador:Administrador,
      Usuario: Usuario,
      Pasword: Pasword
    }, (err, result) => {
      res.redirect('/');
    });
  });


//@recibe parametro=/login  metodo post
//@ retorna un la vista de inicio y lista la tabla prductos
  app.post('/login', (req,res) => {
    //console.log(req.body);
    const {Pasword, Usuario} = req.body;
    connection.query('SELECT * FROM formulario WHERE Pasword =? and Usuario =?' , [
       Pasword,
       Usuario
    ], (err, result) => {

      if(result.length>0){

        connection.query('SELECT * FROM producto', (err, result) => {
          console.log(result);
          res.render('formulario/inicio',{
                formulario: result
              });
           });;
      } else{
        res.redirect('/login');
      }
    });
 });




 app.post('/buscar', (req,res) => {
  //console.log(req.body);
  const {Codigo,} = req.params;
  connection.query('SELECT * FROM Producto WHERE Codigo =? ' , [Codigo], (err, result) => {
    if(result.length>0){

     console.log(result);
      //res.redirect('/product');
      res.render('formulario/inicio');
    } else{
      res.redirect('/login');
    }
  });
});


//@recibe parametro=/producto metodo post
//@ inserta un producto a la tabla producto
  app.post('/producto', (req,res) => {
    //console.log(req.body);
  const {Codigo} = req.body;
  const {Producto} = req.body;
  const {Tipo} = req.body;
  //const {Cargo} = req.body;
  const {Cantidad} = req.body;
  const {Valor} = req.body;
    connection.query('INSERT INTO producto SET?', {
      codigo: Codigo,
      producto:Producto,
      tipo:Tipo,
      //cargo:Cargo,
      cantidad:Cantidad,
      valor:Valor,
        }, (err, result) => {
      res.redirect('/i');
    });
  });


//@recibe parametro=/reg metodo post
//@ direciona a la view formulario
  app.post('/reg',(req,res)=>
  {
    res.render('formulario/formulario');
  },(err, result)=>{
    //res.redirect('/');
  });


  //@recibe parametro=/product metodo post
//@ retorna un redireccionamiento a la view product
  app.post('/product',(req,res)=>
  {
    res.render('formulario/product');
  },(err, result)=>{
    //res.redirect('/');
  });


  //@recibe parametro=/login1 metodo post
//@ retorna un redireccionamiento a la view login
  app.post('/login1',(req,res)=>
  {
    res.render('formulario/login');
  },(err, result)=>{
    //res.redirect('/');
  });


  //@recibe parametro=/login metodo get
//@ retorna un redireccionamiento a la view login
  app.get('/login', function(req, res){
    res.render('formulario/login');
  });


//@recibe parametro=/inicio metodo post
//@ redirecta a la funcion /i
  app.post('/inicio', function(req, res){
    res.redirect('/i');
  });


//@recibe parametro=/i metodo get
//@ retorna un redireccionamiento a la view formulari
  app.post('/vender', function(req, res){
    res.render('formulario/vender');
  });
}
