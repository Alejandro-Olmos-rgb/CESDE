//DECLARACION VARIABLES
let tiempo, hr, mn, sg;

//INGRESO DE DATOS
tiempo = prompt ("Digite la hora (hh:mm:ss)");

//PROCESO
partes = tiempo.split(":");
hr = parseInt(partes[0]);
mn = parseInt(partes[1]);
sg = parseInt(partes[2]);

//RESULTADO
if(hr==23 && mn ==59 && sg==59){
    hr = 0; mn = 0; sg = 0;
}
else{
    if(mn==59 && sg==59){
        hr+=1; mn=0; sg=0;
    }
    else{
        if(sg=59){
            m++; sg=0;
        }
        else{
            sg = sg + 1;
        }
    }
}


//SALIDA INFORMACION
document.writeln("La hora, un segundo despues, es " + hr, ":" + mn, ":", + sg);
