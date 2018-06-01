function calc_an()
{
    
    var minimum;
    var Tchan ;// Среднее время пребывания запроса в канале
    var Tproc ;// Среднее время пребывания запроса в процессоре
    var Tdisk ;// Среднее время пребывания запроса в диске
    var Lf ; // Интеснивность фонового потока после очередной итерации
    var delta1 ;// Вспомогательное значение (5й пункт)
    var L;// Лямбда
    // Загрузка узлов системы
    var roChan;
    var  roProc ;
    var  roDisk;
    var roDisk;
    var roPC ;
    var roPolz;
    
    // // Выполняем вычисления
    // 1. Считываем данные с формы
    var NPC = parseInt($("#inputN").val());// 1. Количество рабочих станций
   
    var T0  = parseInt($("#inputT0").val());// 2. Среднее время дообработки рабочей станции
    var Tp  = parseInt($("#inputTp").val()); // 3. Среднее время формирования запроса
    var tk1 = parseFloat($("#inputtk1").val());// 4. Ср. время передачи по каналу в прямом напрвлении
    var tk2 = parseFloat($("#inputtk2").val());// 5. Ср. время передачи по каналу в обратном напрвлении

    var C = parseInt($("#inputC").val());// 6. Количество процессоров
    var tpr = parseInt($("#inputtpr").val());// 7. Среднее время обработки запроса в процессоре
    var Ndisk = parseInt($("#inputkoldisk").val());// 8. Количество дисков
    var tdi = parseFloat($("#inputtdi").val());// 9. Среднее время обработки запроса в дискe
    var P = parseFloat($("#inputPi").val());// 10. Верояность обращения к диску после обработки запроса в процессоре
    var Pi = parseFloat($("#inputPid").val());// 11. Верояность обращения к процессору после обработки запроса в диске
    var K1 = parseFloat($("#inputK1").val());// 12. Коэффициент К1
    var K2 = parseFloat($("#inputK2").val());// 13. Коэффициент К2
    var prec = parseFloat($("#inputprec").val()); // 14. Точность
   
    // 2. Инициализируем вспомогательные переменные
    var beta = 1 / (1 - P);
    var tk = 0.5 * (tk1 + tk2);
    

    // 3. Производим вычисления
    // 1й пункт
    //    if (Pi == 0 || tdi==0 || tpr == 0) 
    if (Pi == 0) 
    {
        if ( (1/(2*tk)) < (C / (beta*tpr))  )
            minimum = 1/(2*tk) ;
        else 
            minimum = C / (beta*tpr);
    }
    else
    {
        if ( (1/(2*tk)) < (C / (beta*tpr))  ) 
        {
            if ((1/(2*tk)) < (1 / (beta*Pi*tdi)))
                minimum = 1/(2*tk);
            else minimum = 1 / (beta*Pi*tdi);
        }
        else
        { 
            if ((C / (beta*tpr)) < (1 / (beta*Pi*tdi)))
                minimum = C / (beta*tpr)
            else minimum = 1 / (beta*Pi*tdi);
        }
    }
    var   Lf1 = K1 * minimum * ( (NPC - 1)/NPC );
   
    var flag =true;
    while (flag) 
    {
   
        // 2й пункт
        Tchan = (2*tk) / (1 - 2*Lf1*tk);
        Tproc = (beta*tpr) / (1 - Math.pow(beta*Lf1*tpr/C, C));
        Tdisk = (beta*tdi) / (1 - beta*Pi*Lf1*tdi);
       
        // 3й пункт
        Lf = (NPC - 1) / (T0 + Tp + Tchan + Tproc + Tdisk);
    
        
        if ( (Math.abs(Lf1 - Lf) / Lf) < prec )  flag = false;
        // 5й пункт
        delta1 = (Lf1 - Lf) / K2;
        Lf1 = Lf1 - delta1;
      
    }
    
    // 6й пункт
    Tchan = (2*tk) / (1 - 2*Lf1*tk);
    Tproc = (beta*tpr) / (1 - Math.pow(beta*Lf1*tpr/C, C));
    Tdisk = (beta*tdi) / (1 - beta*Pi*Lf1*tdi);
    
    Tcycle = T0 + Tp + Tchan + Tproc + Tdisk;
    roPC = (T0 + Tp) / Tcycle;
    roPolz = Tp / Tcycle;
    
    L = NPC / Tcycle;
    roChan = 2*L*tk;
    roProc = beta*L*tpr/C;
    roDisk = beta*L*Pi*tdi;
    var roDisk2;
    (Ndisk == 1)? roDisk2 = 0 : roDisk2 = roDisk;
       
    //    // 4. Выводи результаты
    $("#resroPC").html(roPC.toFixed(2).toString());
    $("#rest0Tcycle").html((T0/Tcycle).toFixed(2).toString());
    $("#resroPCNPC").html((roPC * NPC).toFixed(1).toString());
    $("#resTTNPC").html(((T0/Tcycle) * NPC).toFixed(1).toString());
    $("#kanal").html((roChan).toFixed(2).toString());
    $("#cpu").html((roProc).toFixed(2).toString());
    $("#d1").html((roDisk).toFixed(2).toString());
    $("#d2").html((roDisk2).toFixed(2).toString());
    $("#syscycle").html((Tcycle).toFixed(2).toString());
    $("#sysreact").html((Tcycle - Tp).toFixed(2).toString());
    
    $("#resform_an").show();
    $("#inputform").hide();
   
}

function back_an()
{
    $("#resform").hide();
    $("#inputform").show();
}

function hide()
{
    $("#form").addClass('hideblock');
}