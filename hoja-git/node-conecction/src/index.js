const app = require('./config/server');

require('./app/routes/formulario') (app);
require('./app/routes/login') (app);

//iniciar servidor jeje
app.listen(app.get('puerto'),() =>{
  console.log('puerto activo', app.get('puerto'));
});
