var btn = document.get
    contenido = document.getElementById('informacion-tramite'),
    contador=0;
 function cambio(){
     if(contador==0){
        contenido.classList.add('mostrar');
        contador=1;
     }
     else{
        contenido.classList.remove('mostrar');
         contador=0;
     }
 }


btn.addEventListener('click',cambio,true)