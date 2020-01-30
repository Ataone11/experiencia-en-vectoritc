pragma solidity ^0.4.10;

contract SalesContract {

    struct Compra{
       address comprador;
       address vendedor;
       string Producto;
       uint cantidad;
       uint precio_total;
       bool resivido;
       uint256 updatedTime;

    }
   struct Producto{
      string nombre;
      string lote;
      uint cantidad;
      uint precio_por_unidad;
      bool disponible;
      uint256 updatedTime;

   }
    //address public buyer;
    //bool public sold = false;
    //string salesDescription = 'bienestarina';
    //uint price = 2 ether;
    //uint public cantidad = 0;
    //uint public disponible = 15;

    address public owner;
    uint fee = 5 ether;
    uint loss = 80;

    mapping (address=>Producto) public productos;
    mapping (address=>Compra) public compras;

    function SalesContract() payable {
       owner = msg.sender;
        if(msg.value!=0){

            throw;
        }
    }

    function Registra_producto(string _nombre,string _lote,uint _cantidad,uint256 _precio) payable {
        if(msg.value== fee)
        {
            productos[msg.sender]=Producto({

                  nombre: _nombre,
                  lote: _lote,
                  cantidad: _cantidad,
                  precio_por_unidad: _precio*1000000000000000000,
                  disponible: true,
                  updatedTime:block.timestamp

            });
             owner.transfer(this.balance);
        }else {
            throw;
        }
    }
//    function Costo_del_registo(uint256 _fee){

      //  fee= _fee;
    //}
    //function Canselar_registro(){
      //  productos[msg.sender].disponible=false;
        //owner.transfer(());
     //   msg.sender.transfer((fee*loss)/100);
    //}

    function comprar(address _vendedor, uint _cantidad) payable {
         if(msg.value== (productos[ _vendedor].precio_por_unidad*_cantidad)  )
         {
             compras[msg.sender]= Compra({
               comprador:msg.sender,
               vendedor:_vendedor,
               Producto:productos[ _vendedor].nombre,
               cantidad:_cantidad,
               precio_total:(productos[ _vendedor].precio_por_unidad*_cantidad),
               resivido: true,
               updatedTime:block.timestamp

             });
              _vendedor.transfer(this.balance);

         }else {
            throw;
        }
        if(productos[ _vendedor].cantidad > 0){

           productos[ _vendedor].cantidad=productos[ _vendedor].cantidad-_cantidad;
        }
    }



}
