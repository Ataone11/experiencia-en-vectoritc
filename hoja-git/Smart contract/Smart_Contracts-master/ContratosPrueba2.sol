pragma solidity ^0.4.10;

contract SalesContract {
    struct compra{
    string comprador;
    string vendedor;
    string lote;
    string resivido;
    
    }
   struct Producto{
      string nombre;
      string lote;
      uint cantidad;
      uint precio;
      bool disponible;
      uint256 updatedTime;
      
   }
    address public buyer;
    address public owner;
    bool public sold = false;
    string salesDescription = 'bienestarina';
    uint price = 2 ether;
    uint public cantidad = 0;
    uint public disponible = 15;
    uint fee=5 ether;
    uint loss = 80;
    
    mapping (address=>Producto) public productos;

    
    function Registra_producto(string _nombre,string _lote,uint _cantidad,uint256 _precio) payable {
        if(msg.value== fee)
        {
            productos[msg.sender]=Producto({
                
                  nombre: _nombre,
                  lote: _lote,
                  cantidad: _cantidad,
                  precio: _precio,
                  disponible: true,
                  updatedTime: block.timestamp
                  
                
            });
             owner.transfer(this.balance);
        }else {
            throw;
        }
    }
   // function Costo_del_registo(uint256 _fee){
        
     //   fee= _fee;
    //}
    function Canselar_registro(){
        productos[msg.sender].disponible=false;
        //owner.transfer(());
        msg.sender.transfer((fee*loss)/100);
    }
    function SalesContract() payable {
       owner = msg.sender;
        if(msg.value!=0){
            
            throw;
        }
    }
    
    function Cantidades (uint newcantidad) returns(uint){
        cantidad = newcantidad;
        return cantidad;
    }
    
    function comprar() payable {
         buyer = msg.sender;
        if(msg.value == (price*cantidad)) {
            owner.transfer(this.balance);
        } else {
            revert();
        }
        if(disponible == 0)
        {
            sold = true;
        }
        if(disponible > 0){
            disponible = disponible - cantidad;
        }
    }
    
    
}