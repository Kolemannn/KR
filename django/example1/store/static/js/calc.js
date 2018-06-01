function calc()
{
    
    
    
    
    // // Выполняем вычисления
    // 1. Считываем данные с формы
    var N = parseInt($("#remInputN").val());
   
    var j  = parseInt($("#remInputC").val());// 2. Среднее время дообработки рабочей станции
    var tno  = parseInt($("#remInputtno").val()); // 3. Среднее время формирования запроса
    var to = parseInt($("#remInputto").val());// 4. Ср. время передачи по каналу в прямом напрвлении
    
   
    // 2. Инициализируем вспомогательные переменные
    
    

    // 3. Производим вычисления
    // 1й пункт
    var mno = 1/tno;
    var mo = 1/to;
    var Nfact = fact(N);
    var Cfact = fact(j);
    var f = mno/mo;


    for (var C = 1; C <= j; C++) {
        
        var Pk1 = 0;
        var Sum = 0;
        var P0 = 0 ;
        var Q = 0;
        var U = 0;
        var p = 0;
        var W = 0;

        for (var i = 0; i <=N ; i++) {

            if (i<=C)
            {
                Pk1=(Nfact*Math.pow(f,i))/(fact(i)*fact(N-i))
                
                if (i>=1)
                {
                    Sum+=i*Pk1;
                }
            
                if (i==0)
                {
                    P0+=(Math.pow(f,i)*Nfact/fact(N-i));
                }
                else
                {
                    P0+=Pk1;
                }
                 
            }
            else
            {
                Pk1=(Nfact*Math.pow(f,i))/(Math.pow(C,i-C)*Cfact*fact(N-i))

                Sum+=i*Pk1;
                       
                if ( i == 0)
                {
                    P0+=(Math.pow(f,i)*Nfact/fact(N-i));
                }
                else
                {
                    P0+=Pk1;
                }
            }
        }
       
        P0=1/P0;
 

        for (var i=C; i<=N; i++){
        Q+=(P0*(i-C)*Nfact*Math.pow(f,i))/(Math.pow(C,i-C)*Cfact*fact(N-i))
        }

        L = Sum * P0
        U = L- Q
        po = U/C
        Tp = (L*tno)/(N-L)
        W = Tp-to

        var Tc = 0;
        Tc=Tp+tno

        var pe = 0;
        pe=tno/Tc

        var n = 0;
        n = N-L
        
        var a = 0;
        a = (C*tno)/(N*to)
        var Y = 0;
        var Si = 200
        var S = 350
        Y = C*Si + L*S
            
    }
     
    


    function fact(x) {
        fac = 1
        if(x!=0){
            for (var i = 2 ; i <= x; i++) {
                fac*=i
            }
        }
        return fac
    }


       
    //    // 4. Выводи результаты
    $("#P0").html(P0.toFixed(6).toString());
    $("#Q").html((Q).toFixed(5).toString());
    $("#L").html((L).toFixed(5).toString());
    $("#U").html(U.toFixed(5).toString());
    $("#po").html(po.toFixed(5).toString());
    $("#n").html(n.toFixed(5).toString());
    $("#pe").html(pe.toFixed(5).toString());
    $("#W").html(W.toFixed(5).toString());
    $("#Tp").html(Tp.toFixed(5).toString());
    $("#Tc").html(Tc.toFixed(5).toString());
    $("#a").html(a.toFixed(5).toString());
    $("#Y").html(Y.toFixed(5).toString());
    
    $("#resform").show();
   
   
}

function back()
{
    $("#resform").hide();
   
}

